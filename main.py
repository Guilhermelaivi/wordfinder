import pandas as pd

comentarios = pd.read_excel("./comentarios.xlsx")
listaComentarios = comentarios["comentarios"].tolist()


