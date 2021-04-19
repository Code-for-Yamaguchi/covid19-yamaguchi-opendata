#外部リソース定義
REMOTE_SOURCES = {
    'patients':{
        'url':'https://yamaguchi-opendata.jp/ckan/dataset/f6e5cff9-ae43-4cd9-a398-085187277edf/resource/f56e6552-4c5d-4ec6-91c0-090f553e0aea/download/350001_yamaguchi_covid19_patients.csv',
        'type':'csv'
    },
    'inspections_people':{
        'url':'https://yamaguchi-opendata.jp/ckan/dataset/f6e5cff9-ae43-4cd9-a398-085187277edf/resource/2b48b14f-2221-4b42-9a7d-78ab89641d23/download/350001_yamaguchi_covid19_test_people.csv',
        'type':'csv'
    },
    'hospitalizations':{
        'url':'https://yamaguchi-opendata.jp/ckan/dataset/f6e5cff9-ae43-4cd9-a398-085187277edf/resource/1a5f9bca-3216-45df-8a99-5c591df8f628/download/350001_yamaguchi_covid19_hospitalization.csv',
        'type':'csv'
	},
    'querents':{
        'url':'https://yamaguchi-opendata.jp/ckan/dataset/f6e5cff9-ae43-4cd9-a398-085187277edf/resource/7f2f7b7c-48de-4c41-86ae-bef45da8aeaa/download/350001_yamaguchi_covid19_call_center.csv',
        'type':'csv'
	}
}

#ヘッダーにkeyがあればvalueに置き換えます
HEADER_TRANSLATIONS = {
}

#intにキャストすべきkey
#translation後のkeyを指定する必要があります
INT_CAST_KEYS = [
    "No",
    "検査実施_人数 ",
    "入院",
    "退院",
    "死亡",
    "相談件数"
]

#先にある順にデコードされます
CODECS = ['utf-8-sig','cp932','shift_jis','euc_jp',
          'euc_jis_2004','euc_jisx0213',
          'iso2022_jp','iso2022_jp_1','iso2022_jp_2','iso2022_jp_2004','iso2022_jp_3','iso2022_jp_ext',
          'shift_jis_2004','shift_jisx0213',
          'utf_16','utf_16_be','utf_16_le','utf_7','utf_8_sig']