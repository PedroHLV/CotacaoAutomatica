import yfinance
import pyautogui
import pyperclip
import time

codigo = input("Digite o código da ação desejada: ")
periodo = input("Digite o prazo para escolher o período ('d' para dias e 'mo' para meses): ")

# Buscar os dados das ações
dados = yfinance.Ticker(codigo).history(periodo)
fechamento = dados.Close



# Gerar analise de forma automática
fechamento_max = fechamento.max()
fechamento_min = fechamento.min()
atual = fechamento.iloc[-1]
print(atual)

email = input("Digite o email do destinatário: ")
assunto = input("Digite o assunto do email: ")
corpo_email = f"""
Prezado Gestor,
Seguem as análises diárias dos últimos {periodo} meses da ação {codigo}:

Cotação Máxima: R$ {round(fechamento_max,2)}
Cotação Minima: R$ {round(fechamento_min,2)}
Cotação Atual: R$ {round(atual,2)}

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
time.sleep(2)

# Bloco para achar o position do mouse onde vai ser clicado
# time.sleep(5)
# position = pyautogui.position()
# print(position)

# Abrir o campo de novo email
pyautogui.click(x=152, y=261)

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

# Enviar email
time.sleep(3)
pyautogui.click(x=410, y=324)

