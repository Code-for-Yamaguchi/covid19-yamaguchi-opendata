import dataloader as dl

if __name__ == "__main__":
    dm = dl.CovidDataManager()
    print('###fetch data###')
    #REMOTE_SOUCESのすべてのソースにアクセス・データ取得しself.dataに保存
    dm.fetch_datas()
    #print(dm.data)
    print('###done###')
    #dict型であるself.dataの全要素がスキーマ定義に適合するかチェック
    dm.validate()
    #self.dataの全要素をjson形式で出力
    dm.export_jsons()
    print('---done---')

    gd = dl.GraphData()
    gd.main()
