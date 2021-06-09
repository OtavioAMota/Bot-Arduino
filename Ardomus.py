import serial
import pyautogui
import keyboard
import time

PortaSerial = "COM9" #porta para se comunicar com o arduino
VeloArdu = 9600 #velocidade de resposta

menosy = "001" #comando para o arduino mexer o mouse no eixo Y
maisy = "002" #comando para o arduino mexer o mouse no eixo Y
menosx = "003" #comando para o arduino mexer o mouse no eixo X
maisx = "004" #comando para o arduino mexer o mouse no eixo X
click = "005" #comando para o arduino clicar com o botão esquerdo
elena = "006" #keyboard

def criar_porta(): #Cria a porta de comunicação
    global portaUSB
    portaUSB = serial.Serial(PortaSerial, VeloArdu)
    
def send_command(cod): #envia os comandos para o arduino
    aux = str(cod)
    portaUSB.write(aux.encode())
    return cod

def GetMousePos():# pega a informação da posição do mouse
    x, y = pyautogui.position()
    #print(x,y)
    return x,y

def SeePixelColor():# Clica no pixel com uma determinada cor
    R = range(193,223) #208+-15
    G = range(44,74) #59+-15
    B =  range(27,57)#42+-15
    color = (R,G,B)
    screen = pyautogui.screenshot()
    for x in range(0,screen.width):
        for y in range(0,screen.height):
            if screen.getpixel((x,y)) == color:
                print(screen.getpixel((x,y)))
                return x,y

criar_porta()

while True:
    if keyboard.is_pressed('o'):
        send_command("006");
    '''
    mousex, mousey = GetMousePos()
    px,py = 1280,540
    if(mousey > py):
        send_command("001")
    if(mousey < py):
        send_command("002")
    if(mousex > px):
        send_command("004")
    if(mousex < px):
        send_command("003")
    time.sleep(0.002)
    '''