import pandas as pd

comentarios = pd.read_excel("./comentarios.xlsx")
listaComentarios = comentarios["comentarios"].tolist()

palavrasChaves = pd.read_excel("./baseDeDados.xlsx")
listaPalavras = palavrasChaves ["SUDIR"].tolist()

comentariosFinais = []

for comentario in listaComentarios:  
    for palavra in listaPalavras: 
        if str(palavra) in str(comentario):
            comentariosFinais.append(comentario) 
            
            break

tabelaFinal = pd.DataFrame({"Comentários": comentariosFinais})
tabelaFinal.to_excel("tabelaFinal.xlsx", index=False)
                

 