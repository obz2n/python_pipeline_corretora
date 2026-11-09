import os
import pandas as pd
import camelot
import matplotlib.pyplot as plt
import matplotlib as mpl
from config import FILE_NAME

# Teste com um arquivo PDF específico
path = os.path.abspath(f"{FILE_NAME}")

# leitura do PDF 
tables = camelot.read_pdf(
    path
    ,pages='1-end'
    ,flavor='stream'
    ,table_areas=['72,570,500,310']
    ,columns=['72,106,111,161,170,218,220,282,284,332,341,380,382,441,446,489']
)

print(tables[0].parsing_report)
# Plotando o contorno da tabela extraída
#camelot.plot(tables[0], kind='contour')
#plt.show()

# exibindo o conteúdo da tabela extraída
print(tables[0].df)