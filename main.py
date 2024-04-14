from funciones import Tablero, Barco, Disparo
from variables import *

class Game():
    def __init__(self):
        pass

    def partida(self):
        
        barco = Barco()
        usuario = Tablero().tablero()
        maquina = Tablero().tablero()

        usuario_visible = barco.colocar_barco(Tablero().tablero(), posiciones_barco_jugador)
        maquina_visible = Tablero().tablero()

        
        barco.colocar_barco(usuario, posiciones_barco_jugador)
        barco.colocar_barco(maquina, posiciones_barco_jugador)

        print("Usuario")
        print(usuario_visible)
        print("\t")
        print("Máquina")
        print(maquina_visible)

        #Forma de romper el bucle
        dic_usuario = {"X" : 0}
        dic_maquina = {"X" : 0}

        while True:
            while Disparo().disparo_usuario(tablero_invisible=maquina, tablero_visible=maquina_visible) == True:
                print(maquina_visible) #Disparo del usuario
                dic_maquina["X"] += 1 #Verificar los aciertos del usuario
            
            print("dic_maquina", dic_maquina["X"])

            if dic_maquina["X"] >= 20:
                print("Has ganado!")
                break

            while Disparo().disparo_maquina(tablero_invisible=usuario, tablero_visible=usuario_visible) == True:
                print(usuario_visible) #Disparo maquina
                dic_usuario["X"] += 1 #Verificar aciertos maquina

            print("dic_usuario", dic_usuario["X"])

            if dic_usuario["X"] >= 20:
                print("Ha ganado la máquina!")
                break
    
Game().partida()





