#                   ESCREVER O PASSO A PASSO DO PROJETO `AUTOMAÇÃO DE PROJETOS EM PYTHON´

# 1 Entrar no sistema da empresa
    # # https://dlp.hashtagtreinamentos.com/python/intensivao/login

    # # pip install pyautogui

    # # pip install pandas numpy openpyxl

import pyautogui
import time

# clicar - pyautogui.click
# escrever - pyautogui.write
# apertar uma tecla - pyautogui.presss
# apertar - pyautogui.hotkey("ctrl", "C")
# scroll - pyautogui.scroll

        # pyautogui.PAUSE = 1

# aperta a tecla do windonws
# digita o nome do programa
# aperta enter
# abrir o sistema da empresa
pyautogui.press("Win")
pyautogui.write("Chrome")
pyautogui.press("Enter")

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("Enter")

# esperar 1 segundos
time.sleep(1)





# 2 Fazer login
    # #

# clicar no campo de email
# escrever o email
# clicar no campo de senha
# escrever a senha
# clicar no botão de logar
pyautogui.click(x=1236, y=375)
pyautogui.write("chrisaraujo124@gmail.com")
# pyautogui.click(x=1239, y=471)
# pyautogui.write("12345")
# pyautogui.click(x=961, y=539)
# ou
pyautogui.press("Tab")
pyautogui.write("12345")
pyautogui.press("Tab")
pyautogui.press("Enter")

# esperar 1 segundos
time.sleep(1)





# 3 Importar a base de dados
    # #

import pandas

tabela = pandas.read_csv("produtos.csv")





for linha in tabela.index:
    
    # 4 Cadastrar um produto
        # #

    # CODIGO
    pyautogui.click(x=1212, y=257)
    pyautogui.write(tabela.loc[linha, "codigo"])
    pyautogui.press("Tab")

    # MARCA
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("Tab")

    # TIPO
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("Tab")

    # CATEGORIA
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("Tab")

    # PREÇO
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("Tab")

    # CUSTO
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("Tab")

    # OBS
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(obs)
        
    pyautogui.press("Tab")

    # Enviar o produto
    pyautogui.press("Enter")
    pyautogui.scroll(10000)






# 5 Repetir até acabar a base de dados
    # #

