SCHEMAS = {
    "last_update":{
        "type": "string",
        "default": ""
    },
    "patients": {
        "type": "object",
        "required": [
            "data",
            "last_update"
        ],
        "properties": {
            "data": {
                "type": "array",
                "default": [],
                "items": {
                    "type": "object",
                    "default": {},
                    "required": [
                        "No",
                        "市区町村名",
                        "公表_年月日",
                        "患者_年代",
                        "患者_性別",
                        "備考"
                    ],
                    "properties": {
                        "No": {
                            "type": "integer",
                            "default": ""
                        },
                        "全国地方公共団体コード": {
                            "type": "string",
                            "default": ""
                        },
                        "都道府県名": {
                            "type": "string",
                            "default": ""
                        },
                        "市区町村名": {
                            "type": "string",
                            "default": ""
                        },
                        "公表_年月日": {
                            "type": "string",
                            "default": ""
                        },
                        "患者_年代": {
                            "type": "string",
                            "default": ""
                        },
                        "患者_性別": {
                            "type": "string",
                            "default": ""
                        },
                        "備考": {
                            "type": "string",
                            "default": ""
                        }
                    }
                }
            },
            "last_update": {
                "type": "string",
                "default": ""
            }
        }
    }
}