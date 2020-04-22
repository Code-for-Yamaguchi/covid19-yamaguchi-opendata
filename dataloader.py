import datetime
import csv
import numpy as np
import pandas as pd
import json
import glob
import os
import urllib.request
import jsonschema
import config
import schemas
import sys

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
        self.data = {
            "last_update":datetime.datetime.now(self.JST).isoformat(),
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
            'last_update': datetime.datetime.now(self.JST).isoformat(),
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

    def export_jsons(self, directory='data/'):
        for key in self.data:
            print(key + '.json')
            self.export_json_of(key, directory)

    def export_json_of(self, key, directory='data/'):
        if not os.path.exists(directory):
            os.makedirs(directory)
        with open(directory + key + '.json', 'w', encoding='utf-8') as f:
            json.dump(self.data[key], f, indent=4, ensure_ascii=False)