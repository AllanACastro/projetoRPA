import pyautogui as pag

pag.locateOnScreen('invoice.png')
localizacaoBotao = pag.locateOnScreen('invoice.png', confidence=0.45)
pag.moveTo(localizacaoBotao[0] + 50 ,localizacaoBotao[1]+ 22)
pag.click()



# pag.locateOnScreen('botaoAdc.png')
# localizacaoBotao = pag.locateOnScreen('botaoAdc.png')
# pag.moveTo(localizacaoBotao[0] + 5 ,localizacaoBotao[1]+ 10)
# pag.click()py