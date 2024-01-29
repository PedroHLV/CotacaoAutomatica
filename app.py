import yfinance
import pyautogui
import pyperclip
import time

# codigo = input("Digite o código da ação desejada: ")
# periodo = input("Digite o prazo para escolher o período ('d' para dias e 'mo' para meses): ")

# # Buscar os dados das ações
# dados = yfinance.Ticker(codigo).history(periodo)
# fechamento = dados.Close



# # Gerar analise de forma automática
# fechamento_max = fechamento.max()
# fechamento_min = fechamento.min()
# atual = fechamento.iloc[-1]
# print(atual)

email = input("Digite o email do destinatário: ")
assunto = input("Digite o assunto do email: ")
corpo_email = f"""
Prezado Gestor,
Seguem as análises diárias dos últimos {periodo} meses da ação {codigo}:

Cotação Máxima: R$ XXX
Cotação Minima: R$ XXX
Cotação Atual: R$ XXX

Qualquer dúvida, fico a disposição !
"""
# enviar e-mail
pyautogui.PAUSE = 2

# Blooc para abrir o email
pyautogui.press('winleft')
pyautogui.write('edge')
pyautogui.press('enter')
pyautogui.hotkey("ctrl", "t")
pyperclip.copy("www.outlook.com")
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey('enter')

# Bloco para achar o position do mouse onde vai ser clicado
# time.sleep(5)
# position = pyautogui.position()
# print(position)

# Abrir o campo de novo email
pyautogui.click(x=2056, y=175)

# Inserir destinatário
pyperclip.copy(email)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

# Inserir assunto
pyperclip.copy(assunto)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

# Corpo do email
pyperclip.copy(corpo_email)
pyautogui.hotkey("ctrl", "v")
