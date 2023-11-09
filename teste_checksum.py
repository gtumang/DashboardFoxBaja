#Programa: Comunicacao Arduino e Raspberry Pi com LoRa
#Autor: Arduino e Cia
 
import time



#Configura a serial e a velocidade de transmissao


def checksum(data):
    filtered = data.split("/")
    print(f"edir {filtered[0]}")
    checksum = 0
    for i in range(0, len(filtered[0])):
        checksum += ord(filtered[0][i])
    return checksum
 
 
while(1):
    
    print ("Aguardando informacoes do LoRa...")
    msg = "0,0,-1,-1,-127/659;"
    #Aguarda a string na serial
    # x = ser.readline()
    # msg = x.decode('utf-8')
    #Mostra na tela a string recebida
    print ("Recebido: ", msg)
    print(checksum(msg))
    
    
    time.sleep(1)