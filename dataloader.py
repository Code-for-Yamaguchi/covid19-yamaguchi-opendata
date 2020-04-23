import datetime
import csv
import json
import glob
import os
import urllib.request
import jsonschema
import config
import schemas
import sys
import collections

class CovidDataManager:
    #日本標準時
    JST = datetime.timezone(datetime.timedelta(hours=+9), "JST")

    #設定ファイル
    REMOTE_SOURCES = config.REMOTE_SOURCES #外部ファイルの参照設定
    HEADER_TRANSLATIONS = config.HEADER_TRANSLATIONS #headerの変換一覧
    INT_CAST_KEYS = config.INT_CAST_KEYS #intにキャストすべきkey
    CODECS = config.CODECS #ファイルエンコーディングリスト

    #バリデーション用のスキーマ定義
    SCHEMAS = schemas.SCHEMAS

    def __init__(self):
        now = datetime.datetime.now(self.JST)
        self.now_str = now.strftime("%Y/%m/%d %H:%M")

        self.data = {
            "last_update":self.now_str,
        }

    def fetch_datas(self):
        for key in self.REMOTE_SOURCES:
            print(key)
            datatype = self.REMOTE_SOURCES[key]['type']
            dataurl = self.REMOTE_SOURCES[key]['url']
            data = {}
            if datatype == 'csv':
                data = self.import_csv_from(dataurl)
            else:
                sys.exit("Unsupported file type")

            self.data[key] = data

    def import_csv_from(self, csvurl):
        request_file = urllib.request.urlopen(csvurl)
        if not request_file.getcode() == 200:
            sys.exit("HTTP status: " + str(request_file.getcode()))
        f = self.decode_csv(request_file.read())
        #filename = os.path.splitext(os.path.basename(csvurl))[0]
        datas = self.csvstr_to_dicts(f)

        return {
            'last_update': self.now_str,
            'data': datas
        }

    #デコード出来るまでCODECS内全コーデックでトライする
    def decode_csv(self, csv_data)->str:
        print('csv decoding')
        for codec in self.CODECS:
            try:
                csv_str = csv_data.decode(codec)
                print('ok:' + codec)
                return csv_str
            except:
                print('ng:' + codec)
                continue
        print('Appropriate codec is not found.')

    #CSV文字列を[dict]型に変換
    def csvstr_to_dicts(self, csvstr) -> list:
        datas = []
        rows = [row for row in csv.reader(csvstr.splitlines())]
        header = rows[0]
        header = self.translate_header(header)
        maindatas = rows[1:]
        for d in maindatas:
            #空行はスキップ
            if d == []:
                continue
            data = {}
            for i in range(len(header)):
                data[header[i]] = d[i]
                if header[i] in self.INT_CAST_KEYS:
                    data[header[i]] = int(d[i])
            datas.append(data)
        return datas

    #HEADER_TRANSLATIONSに基づきデータのヘッダ(key)を変換
    def translate_header(self, header:list)->list:
        for i in range(len(header)):
            for key in self.HEADER_TRANSLATIONS:
                if header[i] == key:
                    header[i] = self.HEADER_TRANSLATIONS[key]
        return header

    #生成されるjsonの正当性チェック
    def validate(self):
        for key in self.data:
            jsonschema.validate(self.data[key], self.SCHEMAS[key])

    def export_jsons(self, directory='origin_data/'):
        for key in self.data:
            print(key + '.json')
            self.export_json_of(key, directory)

    def export_json_of(self, key, directory='origin_data/'):
        if not os.path.exists(directory):
            os.makedirs(directory)
        with open(directory + key + '.json', 'w', encoding='utf-8') as f:
            json.dump(self.data[key], f, indent=4, ensure_ascii=False)

class GraphData:
    def __init__(self):
        self.outfile = [
            "patients_cnt.json",
            "patients.json",
            "inspections.json",
            "hosptitalizations.json",
            "querents.json"
        ]

        #origin_file_list = glob.glob("./origin_data/*.json")
        #print(origin_file_list)

    def main(self):
        self.generate_patients_cnt()
        self.generate_patients()
        self.generate_inspections()

    def generate_patients_cnt(self, origin_directory='origin_data/', out_directory='data/'):
        if not os.path.exists(out_directory):
            os.makedirs(out_directory)
        with open(origin_directory + "patients.json", encoding='utf-8') as f:
            data = json.load(f)
        with open("previous_data/patients_cnt.json", encoding='utf-8') as f:
            prev_data = json.load(f)
        prev_data["last_update"] = data["last_update"]

        prev_data = self.add_patiennts_data(prev_data, data)

        with open(out_directory+ self.outfile[0], 'w') as f:
            json.dump(prev_data, f, ensure_ascii=False, indent=4, separators=(',', ': '))

    def generate_patients(self, origin_directory='origin_data/', out_directory='data/'):
        with open(origin_directory + "patients.json", encoding='utf-8') as f:
            data = json.load(f)
        out = [{elem:dic[elem] for elem in dic if not (elem in ['都道府県名', '全国地方公共団体コード'])} for dic in data["data"]]
        data["data"] = out
        with open(out_directory+ self.outfile[1], 'w') as f:
            json.dump(data, f, ensure_ascii=False, indent=4, separators=(',', ': '))

    def generate_inspections(self, origin_directory='origin_data/', out_directory='data/'):
        with open(origin_directory + "inspections.json", encoding='utf-8') as f:
            data = json.load(f)
        with open("previous_data/inspections.json", encoding='utf-8') as f:
            prev_data = json.load(f)
        out = []
        for dic in data["data"]:
            dic["日付"] = dic.pop("実施年月日")
            dic["日付"] = self.format_date(dic["日付"])
            dic["日付"] += "T08:00:00.000Z"
            dic["小計"] = dic.pop("検査実施_件数")
            del_list = ['全国地方公共団体コード', '都道府県名', '市区町村名', '備考']
            [dic.pop(d) for d in del_list]
            out.append(dic)

        prev_data["data"].extend(out)
        # 昨日までのデータがない場合は暫定で最後のデータを入力
        # 土日だけ抜けてるとめんどくさい...月曜に土日のデータもいれてほしい
        prev_data = self.add_data(prev_data, data)
        prev_data["last_update"] = data["last_update"]
        with open(out_directory+ self.outfile[2], 'w') as f:
            json.dump(prev_data, f, ensure_ascii=False, indent=4, separators=(',', ': '))

    def format_date(self, date_str):
        #print(datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+9), "JST")).isoformat())
        date_dt = datetime.datetime.strptime(date_str, "%Y/%m/%d")

        return date_dt.strftime("%Y-%m-%d")

    def add_patiennts_data(self, prev_data, data):
        lastday = prev_data["data"][-1]["日付"][:10]
        lastday = datetime.date(int(lastday[:4]), int(lastday[5:7]), int(lastday[8:10]))
        today = datetime.date.today()	# timezoneはどうなるのか調査が必要
        period = today - lastday
        daily_cnt = self.daily_patients(data["data"])
        if period.days == 0:
            if today in daily_cnt.keys():
                prev_data["data"][-1]["小計"] = daily_cnt[today]
        for d in range(period.days):
            write_day = lastday + datetime.timedelta(days=d+1)
            if write_day not in daily_cnt.keys():
                print("この日の陽性患者はいません")
                pat_num = 0
            else:
                pat_num = daily_cnt[write_day]
            prev_data["data"].append(
				{
					"日付": write_day.strftime("%Y-%m-%d") + "T08:00:00.000Z",
					"小計": pat_num
				}
			)
            print(write_day)

        return prev_data

    def daily_patients(self, data):
        date_list = []
        for d in data:
            date_str = d.get("公表_年月日")
            dt = self.format_date(date_str)
            dt = datetime.date(int(dt[:4]), int(dt[5:7]), int(dt[8:10]))
            date_list.append(dt)
        #print(daylist[0])
        c = collections.Counter(date_list)
        #print(c)
        #print("="*30)
        #print(datetime.date(2020, 4, 5) in c.keys())
        #print(c.values())
        return c
    
    def add_data(self, prev_data, data):
        lastday = prev_data["data"][-1]["日付"][:10]
        lastday = datetime.date(int(lastday[:4]), int(lastday[5:7]), int(lastday[8:10]))
        today = datetime.date.today()	# timezoneはどうなるのか調査が必要
        period = today - lastday
        print(period.days)
        if period.days == 1: # こちらの場合はorigin_dataが対応してない土日だけ考えれば良い
            return prev_data
        for d in range(1, period.days):
            write_day = lastday + datetime.timedelta(days=d)
            prev_data["data"].append(
				{
					"日付": write_day.strftime("%Y-%m-%d") + "T08:00:00.000Z",
					"小計": prev_data["data"][-1]["小計"]
				}
			)
            print(write_day)

        return prev_data

if __name__ == "__main__":
    gd = GraphData()
    gd.main()