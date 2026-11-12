# FILE_NAME para teste reapido utilizando apenas um arquivo
FILE_NAME = "../workspace/python_pipeline_corretora/data/nota_corretagem_ficticia.pdf"
FILES_PATH = "../workspace/python_pipeline_corretora/data"
LOG_PATH = "../workspace/python_pipeline_corretora/logs"
CSV_PATH = "../workspace/python_pipeline_corretora/data/csv"

CONFIGS = {
    'pages':'1-end',
    'flavor':'stream',
    'table_areas':['27,603,571,425'],
    'columns':[
        '30,40',
        '42,112',
        '117,138',
        '140,204',
        '207,235',
        '238,322',
        '324,355',
        '357,403',
        '405,463',
        '468,548',
        '551,568'
    ],
    'strip_text':'\n',
    'password':''
}