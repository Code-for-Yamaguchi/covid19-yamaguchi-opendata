#外部リソース定義
REMOTE_SOURCES = {
    'patients':{
        'url':'https://yamaguchi-opendata.jp/ckan/dataset/f6e5cff9-ae43-4cd9-a398-085187277edf/resource/f56e6552-4c5d-4ec6-91c0-090f553e0aea/download/350001_yamaguchi_covid19_patients.csv',
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
]

#先にある順にデコードされます
CODECS = ['utf-8-sig','cp932','shift_jis','euc_jp',
          'euc_jis_2004','euc_jisx0213',
          'iso2022_jp','iso2022_jp_1','iso2022_jp_2','iso2022_jp_2004','iso2022_jp_3','iso2022_jp_ext',
          'shift_jis_2004','shift_jisx0213',
          'utf_16','utf_16_be','utf_16_le','utf_7','utf_8_sig']