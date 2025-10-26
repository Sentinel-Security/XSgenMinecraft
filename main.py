# please dont steal the code or give me credits, dont change the code if you dont know what are you doing.

import random

import string

import requests

from threading import Thread, Lock

import time


num_giftcards = 100000000  

code_length = 16     

part_length = 4      

num_parts = 4       


characters = string.ascii_uppercase + string.digits  

output_file = "giftcards_validos.txt"




lock = Lock()



def generar_codigo():

    parts = [

        ''.join(random.choice(characters) for _ in range(part_length)),

        ''.join(random.choice(characters) for _ in range(part_length)),

        ''.join(random.choice(characters) for _ in range(part_length)),

        ''.join(random.choice(characters) for _ in range(part_length))

    ]

    return '-'.join(parts)



def validar_codigo(codigo):

    url = f"https://api.mojang.com/validate/{codigo}"

    respuesta = requests.get(url)

    if respuesta.status_code == 200:

        return "[+]"  

    else:

        return "[-]"  



def validar_codigo_hilo(codigo):

    resultado = validar_codigo(codigo)

    print(f"{codigo} - {resultado}")


    if resultado == "[+]":

        with lock:

            with open(output_file, "a") as f:

                f.write(codigo + "\n")



def main():

    print(f"generating {num_giftcards} codes of Minecraft Premium...")

    

    with open(output_file, "w") as f:

        f.truncate(0)  


    hilos = []

    for _ in range(num_giftcards):

        codigo = generar_codigo()

        hilo = Thread(target=validar_codigo_hilo, args=(codigo,))

        hilos.append(hilo)

        hilo.start()


    for hilo in hilos:

        hilo.join()


    print(f"the codes valids is {num_giftcards} codes. the valids codes is getting in:'{output_file}'.")



if __name__ == "__main__":

    print("=========================================================================")
    print(" /$$   /$$        /$$$$$$         /$$$$$$  /$$        /$$$$$$  /$$   /$$")
    print("| $$  / $$       /$$__  $$       /$$__  $$| $$       /$$__  $$| $$$ | $$")
    print("|  $$/ $$/      | $$  \__/      | $$  \__/| $$      | $$  \ $$| $$$$| $$")
    print("\  $$$$/       |  $$$$$$       | $$      | $$      | $$$$$$$$| $$ $$ $$")
    print("  >$$  $$        \____  $$      | $$      | $$      | $$__  $$| $$  $$$$")
    print(" /$$/\  $$       /$$  \ $$      | $$    $$| $$      | $$  | $$| $$\  $$$")
    print("| $$  \ $$      |  $$$$$$/      |  $$$$$$/| $$$$$$$$| $$  | $$| $$ \  $$")
    print("|__/  |__/       \______/        \______/ |________/|__/  |__/|__/  \__/")
    print("==========================================================================")
    print("this gen is created by Sentinel-Security or XS CLAN:https://discord.gg/Frybs2bJvv")
    print("-------- Gen of Minecraft Premium --------")

    usuario_input = input("for continue print:XS.TOP ")


    if usuario_input == "XS.TOP":

        main()

    else:

        print("Entrada incorrecta. El programa se cerrará.")
