import sqlite3
import os
import sys
import random
import time

if 'foxbaja_telemetria.db' not in os.listdir():
    print("\nERRO: base de dados nao existe\n")
    sys.exit()


with sqlite3.connect('foxbaja_telemetria.db') as conn:
    c = conn.cursor()

    for i in range(600):
        velocidade = random.randint(20,30)
        temperatura = random.randint(60,90)
        rotacao = random.randint(2000,3000)
        freio = random.randint(50,100)
        combustivel = random.randint(1, 30)
        c.execute(f"""
        INSERT INTO telemetria 
        (rotacao, velocidade, freio, combustivel, temperatura)
        VALUES
        ({rotacao}, {velocidade}, {freio}, {combustivel}, {temperatura})
        """)

        conn.commit()
        print(f"Velocidade: {velocidade} - Temperatura: {temperatura} - Rotacao: {rotacao} - Freio: {freio} - Combustivel: {combustivel}\n")
        time.sleep(1)
