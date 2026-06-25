"""
Este codigo debe generar casos de prueba para los algoritmos implementados en C++, en la carpeta code/implementation/data/intputs/
"""


import random
import os





'''
def generar(tope_capitulos):
    
    cantidad_capitulos = random.randint(1, tope_capitulos)

    bono_satisfaccion = random.randint(0, 1000000000)

    return # aun no sé







def main():

    # El enunciacio da anuncia que la cantidad total de capitulos entre todos los anime debe ser max 700
    # Q:
    cantidad_max_caps_restantes = 700 
    # si eventualmente esta variable llegara a ser por ejemplo 21,
    # entonces el siguiente anime puede tener a lo más 21 caps, en lugar de 30.
    # una opción: ¿¿ si la variable llega a 0, se deja de hacer capitulos y se deja de listar animes (pq tendrían 0 capitulos) ??


    # casos pequeños n = {3, 5, 8}
    n = [3, 5, 8]
    tope_capitulos = 10

    for i in n:
        generar(tope_capitulos)

    # casos medianos n = {20, 40, 80}
    n = [20, 40, 80]

    # casos grandes  n = {100, 150, 200}
    n = [100, 150, 200]

'''




import random
import os

def generar_datos_animes(n, tipo_caso):
    datos = []
    
    # El enunciado indica que la cantidad total de capitulos entre todos los anime debe ser max 700 
    cantidad_max_caps_restantes = 700 
    
    # Configurar topes segun el tipo de caso
    tope_capitulos = 30 
    if tipo_caso == "pequenio":
        tope_capitulos = 4 # Mantener pequeño para que Fuerza Bruta no tarde tanto
        
    tiempo_total_generado = 0
    energia_total_generada = 0
    lineas_animes = []

    for i in range(1, n + 1):
        # Asegurar al menos 1 capitulo por anime restante para que ninguno quede en 0
        capitulos_reservados = n - i 
        
        # Calcular el maximo real que le podemos dar a este anime sin romper el limite de 700
        max_q_real = min(tope_capitulos, cantidad_max_caps_restantes - capitulos_reservados)
        if max_q_real < 1:
            max_q_real = 1
            
        cantidad_capitulos = random.randint(1, max_q_real)
        cantidad_max_caps_restantes = cantidad_max_caps_restantes - cantidad_capitulos
        
        bono_satisfaccion = random.randint(0, 1000000000) 
        nombre_anime = "anime_" + str(i)
        
        # Guardar la linea del anime
        lineas_animes.append(nombre_anime + " " + str(cantidad_capitulos) + " " + str(bono_satisfaccion))
        
        # Generar los capitulos de este anime
        for j in range(cantidad_capitulos):
            t = random.randint(1, 300) 
            c = random.randint(1, 100) 
            v = random.randint(1, 1000000000) 
            
            tiempo_total_generado = tiempo_total_generado + t
            energia_total_generada = energia_total_generada + c
            
            lineas_animes.append(str(t) + " " + str(c) + " " + str(v))

    # Generar topes M y E proporcionales a lo que se genero, para que el algoritmo tenga que "elegir"
    M = random.randint(tiempo_total_generado // 4 + 1, tiempo_total_generado // 2 + 10)
    E = random.randint(energia_total_generada // 4 + 1, energia_total_generada // 2 + 10)
    
    # Respetar los topes maximos absolutos del enunciado
    if M > 3000:
        M = 3000 
    if E > 500:
        E = 500 

    # Armar el arreglo final sumando la primera linea requerida
    primera_linea = str(n) + " " + str(M) + " " + str(E) 
    datos.append(primera_linea)
    
    for linea in lineas_animes:
        datos.append(linea)
        
    return datos


def guardar_archivo(nombre_archivo, datos):
    ruta_script = os.path.abspath(__file__)
    carpeta_script = os.path.dirname(ruta_script)
    carpeta_implementation = os.path.dirname(carpeta_script)
    # Guardar en code/implementation/data/inputs/
    ruta_inputs = os.path.join(carpeta_implementation, "data", "inputs")
    
    if not os.path.exists(ruta_inputs):
        os.makedirs(ruta_inputs)
        
    ruta_archivo = os.path.join(ruta_inputs, nombre_archivo)
    
    archivo = open(ruta_archivo, "w")
    for linea in datos:
        archivo.write(linea + "\n")
    archivo.close()


def main():
    # Variables de casos recomendadas en el enunciado
    casos_pequenios = [3, 5, 8] 
    casos_medianos = [20, 40, 80] 
    casos_grandes = [100, 150, 200]  
    
    letras = ["a", "b", "c"]
    
    # Generar casos pequenos
    for n in casos_pequenios:
        for i in letras:
            nombre = "testcases_" + str(n) + "_" + i + ".txt" 
            datos = generar_datos_animes(n, "pequenio")
            guardar_archivo(nombre, datos)
            
    # Generar casos medianos
    for n in casos_medianos:
        for i in letras:
            nombre = "testcases_" + str(n) + "_" + i + ".txt"
            datos = generar_datos_animes(n, "mediano")
            guardar_archivo(nombre, datos)
            
    # Generar casos grandes
    for n in casos_grandes:
        for i in letras:
            nombre = "testcases_" + str(n) + "_" + i + ".txt"
            datos = generar_datos_animes(n, "grande")
            guardar_archivo(nombre, datos)

if __name__ == "__main__":
    main()














































