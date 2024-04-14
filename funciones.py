import numpy as np
from variables import *
import random

class Tablero():
    def __init__(self):
        pass

    def tablero(self):
        tablero = self.tablero = np.full(TABLERO, " ")
        return tablero

class Barco():
    def __init__(self):
        pass
    def colocar_barco(self,tablero, posiciones):
        for posiciones_barco_jugador in posiciones:
            for fila, columna in posiciones_barco_jugador:
                tablero[fila, columna] = "O"
        return tablero
    
        

class Disparo():
    def __init__(self):
        pass

    def coordenadas(self):
        x = input("Inserte el número de la fila para disparar: ")
        y = input("Inserte el número de la columna para disparar")
        try:
            x = int(x)
            y = int(y)
            if x in range(0,10) and y in range (0,10):
                return (x,y)
            else:
                return None
        except:
            print("Debes insertar números entre el 0 y el 9") #Si no lo cumplen vuelve a pedir datos
            self.coordenadas()
    
    def disparo_usuario(self, tablero_visible, tablero_invisible):
        comprueba_disparo = []
        tablero_invisible = tablero_invisible 
        tablero_visible = tablero_visible
        coordenadas = self.coordenadas()
        if coordenadas:
            if not coordenadas in comprueba_disparo:
                if tablero_invisible[coordenadas] == "O" and tablero_visible[coordenadas] == " ":
                    comprueba_disparo.append(coordenadas)  #Guardo las cordenadas
                    print(f"Disparaste a {coordenadas} y acertaste") #Si en el invisible hay barco en las coordenadas ingresadas
                    tablero_visible[coordenadas] = "X"
                    return True
                else:
                    print(f"Disparaste a {coordenadas} y fallaste") #Si en el invisible no hay barco en las coordenadas ingresadas, pone - en el visible
                    tablero_visible[coordenadas] = "-"
                    return False
            else:
                print(f"Ya disparaste a {coordenadas}")
                self.disparo_usuario(tablero_visible=tablero_visible, tablero_invisible=tablero_invisible)
        else:
            print("Debes insertar números entre el 0 y el 9")
            self.disparo_usuario(tablero_visible=tablero_visible, tablero_invisible=tablero_invisible)

    def disparo_maquina(self, tablero_visible, tablero_invisible):
        comprueba_disparo = []
        tablero_invisible = tablero_invisible
        tablero_visible = tablero_visible
        x = random.randint(0,9)
        y = random.randint(0,9)
        coordenadas = (x,y)
        if not coordenadas in comprueba_disparo:
            if tablero_invisible[coordenadas] == "O" and tablero_visible[coordenadas] == " ":
                print(f"La máquina disparó a {coordenadas} y acertó")
                tablero_visible[coordenadas] = "X"
                return True
            else:
                print(f"La máquina disparó a {coordenadas} y falló")
                tablero_visible[coordenadas] = "-"
                return False
        else:
            self.disparo_maquina(tablero_visible=tablero_visible, tablero_invisible=tablero_invisible)
