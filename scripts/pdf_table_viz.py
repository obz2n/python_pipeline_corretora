import os
import pandas as pd
import camelot
import matplotlib.pyplot as plt
import matplotlib as mpl


FILE_NAME = "../python_pipeline_corretora/data/nota_corretagem_ficticia.pdf"

# Teste com um arquivo PDF específico
path = os.path.abspath(f"{FILE_NAME}")

# leitura do PDF 
tables = camelot.read_pdf(
    path
    ,pages='1-end'
    ,flavor='stream'
    ,table_areas=['27,603,571,425']
    ,columns=[''
    '30,40'
    ',42,112'
    ',117,138'
    ',140,204'
    ',207,235'
    ',238,322'
    ',324,355'
    ',357,403'
    ',405,463'
    ',468,548'
    ',551,568']
)

print(tables[0].parsing_report)
# Plotando o contorno da tabela extraída
#camelot.plot(tables[0], kind='grid')
#plt.show()

# exibindo o conteúdo da tabela extraída
print(tables[0].df)