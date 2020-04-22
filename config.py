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
    'inspections':{
        'url':'https://yamaguchi-opendata.jp/ckan/dataset/f6e5cff9-ae43-4cd9-a398-085187277edf/resource/21b7caeb-05b2-401b-8245-28757de8f444/download/350001_yamaguchi_covid19_test_count.csv',
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
    "検査実施_件数",
]

#先にある順にデコードされます
CODECS = ['utf-8-sig','cp932','shift_jis','euc_jp',
          'euc_jis_2004','euc_jisx0213',
          'iso2022_jp','iso2022_jp_1','iso2022_jp_2','iso2022_jp_2004','iso2022_jp_3','iso2022_jp_ext',
          'shift_jis_2004','shift_jisx0213',
          'utf_16','utf_16_be','utf_16_le','utf_7','utf_8_sig']