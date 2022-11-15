import pyautogui
from python_imagesearch.imagesearch import imagesearch_loop, imagesearch
import time
import sys
from tkinter import*

acceptButtonImg = './sample.png'

def checkGameAvailableLoop():
    while True:
        pos = imagesearch(acceptButtonImg, 0.8)
        if not pos[0] == -1:
            pyautogui.click(pos[0], pos[1])
            print("Game accepted!")
            break
        
        time.sleep(1)



def fechar():
    exit()



menu_inicial = Tk()
menu_inicial.title("Auto Accept LoL")

#forma da janela
menu_inicial.geometry("200x100")   
menu_inicial.resizable(0, 0)

#botao iniciar
botao_iniciar = Button(menu_inicial, text = "ACTIVE THE AUTO ACCEPT", command=lambda: checkGameAvailableLoop() )
botao_iniciar.pack()
botao_iniciar.place(x=20, y=20)

#botao sair
botao_sair = Button(menu_inicial, text= "CLOSE THE AUTO ACCEPTER", command=lambda: fechar() )
botao_sair.pack()
botao_sair.place(x=20, y=50)



menu_inicial.mainloop()
