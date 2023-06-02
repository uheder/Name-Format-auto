"""

Created by @uheder_macedo, 2023

"""

import os
from datetime import datetime, timedelta
import time

#main function
def get_data():

    """
    sets the path, get the inputs and rename the files

    """
    caminho = input("Digite o caminho da pasta dos arquivos a serem renomeados: ")
    #gets the path of the folder that the files are on
    mes = input("Digite o número do mês (MM): ") #get the month input
    ano = input("Digite o ano (AAAA): ") #get the year

    #verify if month and year are inputs of correct length for the program to actually run
    if len(ano) != 4 or len(mes) != 2:
        raise ValueError
    try:
        mes = int(mes)
        ano = int(ano)

    except ValueError: #handles the error and start the program again
        print("Formato inválido, reiniciando...")
        time.sleep(5)
        return get_data

    else:
        files = os.listdir(caminho)
        data = datetime(ano, mes, 1) #format used on the files

        for file in files:
            if file.endswith(".xlsx") or file.endswith(".xls"):
                novo_nome = data.strftime("%d-%m-%Y.xlsx") #sets the format

                caminho_antigo = os.path.join(caminho, file)
                caminho_novo = os.path.join(caminho, novo_nome)

                os.rename(caminho_antigo, caminho_novo) #rename the files as intended
                data += timedelta(days=1) #add 1 to day in the format

        print("Arquivos renomeados com sucesso!") #print messages for the user
        print("Fechando programa...")
        time.sleep(5) #wait before closing the program

get_data() #runs the program
