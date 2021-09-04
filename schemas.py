SCHEMAS = {
    "last_update":{
        "type": "string",
        "default": ""
    },
    "patients": {
        "type": "object",
        "required": [
            "last_update",
            "data"
        ],
        "properties": {
            "last_update": {
                "type": "string",
                "default": ""
            },
            "data": {
                "type": "array",
                "default": [],
                "items": {
                    "type": "object",
                    "default": {},
                    "required": [
                        "No",
                        "市区町村名",
                        "公表日",
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
                        "陽性確定日": {
                            "type": "string",
                            "default": ""
                        },
                        "公表日": {
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
            }
        }
    },
    "inspections_people": {
        "type": "object",
        "required": [
            "last_update",
            "data"
        ],
        "properties": {
            "last_update": {
                "type": "string",
                "default": ""
            },
            "data": {
                "type": "array",
                "default": [],
                "items": {
                    "type": "object",
                    "default": {},
                    "required": [
                        "実施_年月日",
                        "検査実施_人数 "
                    ],
                    "properties": {
                        "実施_年月日": {
                            "type": "string",
                            "default": ""
                        },
                        "全国地方公共団体コード": {
                            "type": "string",
                            "default": ""
                        },
                        "都道府県名 ": {
                            "type": "string",
                            "default": ""
                        },
                        "市区町村名 ": {
                            "type": "string",
                            "default": ""
                        },
                        "検査実施_人数 ": {
                            "type": "integer",
                            "default": ""
                        },
                        "備考": {
                            "type": "string",
                            "default": ""
                        }
                    }
                }
            }
        }
    },
    "inspections": {
        "type": "object",
        "required": [
            "last_update",
            "data"
        ],
        "properties": {
            "last_update": {
                "type": "string",
                "default": ""
            },
            "data": {
                "type": "array",
                "default": [],
                "items": {
                    "type": "object",
                    "default": {},
                    "required": [
                        "実施年月日",
                        "検査実施_件数"
                    ],
                    "properties": {
                        "実施年月日": {
                            "type": "string",
                            "default": ""
                        },
                        "全国地方公共団体コード": {
                            "type": "string",
                            "default": ""
                        },
                        "都道府県名 ": {
                            "type": "string",
                            "default": ""
                        },
                        "市区町村名": {
                            "type": "string",
                            "default": ""
                        },
                        "検査実施_件数": {
                            "type": "integer",
                            "default": ""
                        },
                        "備考": {
                            "type": "string",
                            "default": ""
                        }
                    }
                }
            }
        }
    },
    "hospitalizations": {
        "type": "object",
        "required": [
            "last_update",
            "data"
        ],
        "properties": {
            "last_update": {
                "type": "string",
                "default": ""
            },
            "data": {
                "type": "array",
                "default": [],
                "items": {
                    "type": "object",
                    "default": {},
                    "required": [
                        "受付_年月日",
                        "入院",
                        "退院",
                        "死亡"
                    ],
                    "properties": {
                        "受付_年月日": {
                            "type": "string",
                            "default": ""
                        },
                        "全国地方公共団体コード": {
                            "type": "string",
                            "default": ""
                        },
                        "都道府県名 ": {
                            "type": "string",
                            "default": ""
                        },
                        "市区町村名": {
                            "type": "string",
                            "default": ""
                        },
                        "入院": {
                            "type": "integer",
                            "default": ""
                        },
                        "退院": {
                            "type": "integer",
                            "default": ""
                        },
                        "死亡": {
                            "type": "integer",
                            "default": ""
                        },
                    }
                }
            }
        }
    },
    "querents": {
        "type": "object",
        "required": [
            "last_update",
            "data"
        ],
        "properties": {
            "last_update": {
                "type": "string",
                "default": ""
            },
            "data": {
                "type": "array",
                "default": [],
                "items": {
                    "type": "object",
                    "default": {},
                    "required": [
                        "受付_年月日",
                        "相談件数"
                    ],
                    "properties": {
                        "受付_年月日": {
                            "type": "string",
                            "default": ""
                        },
                        "全国地方公共団体コード": {
                            "type": "string",
                            "default": ""
                        },
                        "都道府県名 ": {
                            "type": "string",
                            "default": ""
                        },
                        "市区町村名": {
                            "type": "string",
                            "default": ""
                        },
                        "相談件数": {
                            "type": "integer",
                            "default": ""
                        },
                    }
                }
            }
        }
    }
}
