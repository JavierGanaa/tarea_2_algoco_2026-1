# Adaptado de la tarea anterior

import os
import re
import matplotlib.pyplot as plt

# Para obtener la ruta de la carpeta sin usar rutas absolutas que se rompen
# use la solucion de este post de stackoverflow:
# https://stackoverflow.com/questions/918154/relative-paths-in-python
directorio_actual = os.path.dirname(os.path.abspath(__file__))
ruta_mediciones = os.path.join(directorio_actual, '../data/measurements')
ruta_outputs = os.path.join(directorio_actual, '../data/outputs')
ruta_graficos = os.path.join(directorio_actual, '../data/plots')

# Diccionarios para guardar los datos de los txt
tiempos_g1 = {}
tiempos_g2 = {}
tiempos_fb = {}

for archivo in os.listdir(ruta_mediciones):
    if ".txt" not in archivo: 
        continue

    # sacar el tamanio del arreglo del inicio del nombre
    match_tamanio = re.match(r'^testcases_(\d+)', archivo)
    if match_tamanio == None: 
        continue
    n = int(match_tamanio.group(1))

    ruta_archivo = os.path.join(ruta_mediciones, archivo)
    with open(ruta_archivo, 'r', encoding='utf-8') as f:
        texto = f.read()
        
        # Regex sacado de stackoverflow para atrapar numeros con notacion cientifica (ej: 6.66e+06)
        # https://stackoverflow.com/questions/4703390/how-to-extract-a-floating-number-from-a-string
        regex_numeros = r'(\d+(?:\.\d+)?(?:[eE][+-]?\d+)?)' 
        
        # Regex modificado para buscar el salto de línea y la palabra "Tiempo (ms):"
        g1_m = re.search(r'^Greedy_Mayor_Bono.*?\n\s*Tiempo \(ms\):\s*' + regex_numeros, texto, re.IGNORECASE | re.MULTILINE)
        g2_m = re.search(r'^Greedy_Menos_Capitulos.*?\n\s*Tiempo \(ms\):\s*' + regex_numeros, texto, re.IGNORECASE | re.MULTILINE)
        fb_m = re.search(r'^Fuerza_Bruta.*?\n\s*Tiempo \(ms\):\s*' + regex_numeros, texto, re.IGNORECASE | re.MULTILINE)

        if g1_m:
            if n not in tiempos_g1:
                tiempos_g1[n] = []
            tiempos_g1[n].append(float(g1_m.group(1)))
            
        if g2_m:
            if n not in tiempos_g2:
                tiempos_g2[n] = []
            tiempos_g2[n].append(float(g2_m.group(1)))
            
        if fb_m:
            if n not in tiempos_fb:
                tiempos_fb[n] = []
            tiempos_fb[n].append(float(fb_m.group(1)))

# Promediar los tiempos para cada tamanio, 
x_g1 = sorted(tiempos_g1.keys())
y_g1 = []
for x in x_g1:
    promedio = sum(tiempos_g1[x]) / len(tiempos_g1[x])
    y_g1.append(promedio)

x_g2 = sorted(tiempos_g2.keys())
y_g2 = []
for x in x_g2:
    promedio = sum(tiempos_g2[x]) / len(tiempos_g2[x])
    y_g2.append(promedio)

x_fb = sorted(tiempos_fb.keys())
y_fb = []
for x in x_fb:
    promedio = sum(tiempos_fb[x]) / len(tiempos_fb[x])
    y_fb.append(promedio)

# GRAFICO DE TIEMPO (TODOS)
# https://www.geeksforgeeks.org/graph-plotting-in-python-set-1/
plt.figure(figsize=(10, 6)) 

plt.plot(x_g1, y_g1, marker='o', label="Greedy_Mayor_Bono")
plt.plot(x_g2, y_g2, marker='s', label="Greedy_Menos_Capitulos")
if len(x_fb) > 0:
    plt.plot(x_fb, y_fb, marker='^', label="Fuerza_Bruta")

plt.xlabel('Cantidad de animes (n)')
plt.ylabel('Tiempo promedio (ms)')
plt.title('Tiempo de Ejecucion Promedio')

# Escala logaritmica para que el gráfico sea entendible a simple vista
plt.xscale('log')
plt.yscale('log')

plt.legend()
plt.grid(True)

# Guardar el archivo en la carpeta de plots
if not os.path.exists(ruta_graficos):
    os.makedirs(ruta_graficos)

guardado_tiempo = os.path.join(ruta_graficos, 'tiempo_plot_promedio.png')
plt.savefig(guardado_tiempo)
print("El grafico se guardo bien en:", guardado_tiempo)


# GRAFICO DE TIEMPO (SOLO CASOS PEQUENIOS)
plt.clf() 
plt.figure(figsize=(10, 6)) 

casos_pequenios = [3, 5, 8]

x_g1_peq = []
y_g1_peq = []
for i in range(len(x_g1)):
    if x_g1[i] in casos_pequenios:
        x_g1_peq.append(x_g1[i])
        y_g1_peq.append(y_g1[i])

x_g2_peq = []
y_g2_peq = []
for i in range(len(x_g2)):
    if x_g2[i] in casos_pequenios:
        x_g2_peq.append(x_g2[i])
        y_g2_peq.append(y_g2[i])

x_fb_peq = []
y_fb_peq = []
for i in range(len(x_fb)):
    if x_fb[i] in casos_pequenios:
        x_fb_peq.append(x_fb[i])
        y_fb_peq.append(y_fb[i])

plt.plot(x_g1_peq, y_g1_peq, marker='o', label="Greedy_Mayor_Bono")
plt.plot(x_g2_peq, y_g2_peq, marker='s', label="Greedy_Menos_Capitulos")
plt.plot(x_fb_peq, y_fb_peq, marker='^', label="Fuerza_Bruta")

plt.xlabel('Cantidad de animes (n)')
plt.ylabel('Tiempo promedio (ms)')
plt.title('Tiempo de Ejecucion Promedio (Casos Pequenios)')

plt.legend()
plt.grid(True)

guardado_tiempo_peq = os.path.join(ruta_graficos, 'tiempo_pequenios_plot_promedio.png')
plt.savefig(guardado_tiempo_peq)
print("El grafico de tiempo pequenios se guardo bien en:", guardado_tiempo_peq)








# graficar outputs de satisfaccion, es similar al código para graficar el tiempo
satis_g1 = {}
satis_g2 = {}
satis_fb = {}

for archivo in os.listdir(ruta_outputs):
    if ".txt" not in archivo: 
        continue

    match_tamanio = re.match(r'^testcases_(\d+)', archivo)
    if match_tamanio == None: 
        continue
    n = int(match_tamanio.group(1))

    ruta_archivo = os.path.join(ruta_outputs, archivo)
    with open(ruta_archivo, 'r', encoding='utf-8') as f:
        texto = f.read()
        
        regex_numeros = r'(\d+(?:\.\d+)?(?:[eE][+-]?\d+)?)' 
        
        # Regex modificado para buscar en la carpeta de outputs
        g1_s = re.search(r'^Greedy_Mayor_Bono -> MaxSatisfaccion:\s*' + regex_numeros, texto, re.IGNORECASE | re.MULTILINE)
        g2_s = re.search(r'^Greedy_Menos_Capitulos -> MaxSatisfaccion:\s*' + regex_numeros, texto, re.IGNORECASE | re.MULTILINE)
        fb_s = re.search(r'^Fuerza_Bruta -> MaxSatisfaccion:\s*' + regex_numeros, texto, re.IGNORECASE | re.MULTILINE)

        if g1_s:
            if n not in satis_g1:
                satis_g1[n] = []
            satis_g1[n].append(float(g1_s.group(1)))
            
        if g2_s:
            if n not in satis_g2:
                satis_g2[n] = []
            satis_g2[n].append(float(g2_s.group(1)))
            
        if fb_s:
            if n not in satis_fb:
                satis_fb[n] = []
            satis_fb[n].append(float(fb_s.group(1)))

# Promediar la satisfaccion para cada tamanio
x_g1_s = sorted(satis_g1.keys())
y_g1_s = []
for x in x_g1_s:
    promedio = sum(satis_g1[x]) / len(satis_g1[x])
    y_g1_s.append(promedio)

x_g2_s = sorted(satis_g2.keys())
y_g2_s = []
for x in x_g2_s:
    promedio = sum(satis_g2[x]) / len(satis_g2[x])
    y_g2_s.append(promedio)

x_fb_s = sorted(satis_fb.keys())
y_fb_s = []
for x in x_fb_s:
    promedio = sum(satis_fb[x]) / len(satis_fb[x])
    y_fb_s.append(promedio)


# GRAFICO DE SATISFACCION (TODOS)
# Limpiamos la figura por si se dibujó el grafico de tiempo justo antes
plt.clf() 
plt.figure(figsize=(10, 6)) 

plt.plot(x_g1_s, y_g1_s, marker='o', label="Greedy_Mayor_Bono")
plt.plot(x_g2_s, y_g2_s, marker='s', label="Greedy_Menos_Capitulos")
if len(x_fb_s) > 0:
    plt.plot(x_fb_s, y_fb_s, marker='^', label="Fuerza_Bruta")

plt.xlabel('Cantidad de animes (n)')
plt.ylabel('Satisfaccion promedio')
plt.title('Satisfaccion Promedio de Algoritmos (Todos los animes)')

# Solo dejamos logaritmo en X. En Y está comentado porque el log(0) da error matemático
plt.xscale('log')
# plt.yscale('log')

plt.legend()
plt.grid(True)

guardado_satis = os.path.join(ruta_graficos, 'satisfaccion_plot_promedio.png')
plt.savefig(guardado_satis)
print("El grafico de satisfaccion se guardo bien en:", guardado_satis)


# GRAFICO DE SATISFACCION (SOLO CASOS PEQUENIOS)
plt.clf() 
plt.figure(figsize=(10, 6)) 

x_g1_s_peq = []
y_g1_s_peq = []
for i in range(len(x_g1_s)):
    if x_g1_s[i] in casos_pequenios:
        x_g1_s_peq.append(x_g1_s[i])
        y_g1_s_peq.append(y_g1_s[i])

x_g2_s_peq = []
y_g2_s_peq = []
for i in range(len(x_g2_s)):
    if x_g2_s[i] in casos_pequenios:
        x_g2_s_peq.append(x_g2_s[i])
        y_g2_s_peq.append(y_g2_s[i])

x_fb_s_peq = []
y_fb_s_peq = []
for i in range(len(x_fb_s)):
    if x_fb_s[i] in casos_pequenios:
        x_fb_s_peq.append(x_fb_s[i])
        y_fb_s_peq.append(y_fb_s[i])

plt.plot(x_g1_s_peq, y_g1_s_peq, marker='o', label="Greedy_Mayor_Bono")
plt.plot(x_g2_s_peq, y_g2_s_peq, marker='s', label="Greedy_Menos_Capitulos")
plt.plot(x_fb_s_peq, y_fb_s_peq, marker='^', label="Fuerza_Bruta")

plt.xlabel('Cantidad de animes (n)')
plt.ylabel('Satisfaccion promedio')
plt.title('Satisfaccion Promedio de Algoritmos (Casos Pequenios)')

plt.legend()
plt.grid(True)

guardado_satis_peq = os.path.join(ruta_graficos, 'satisfaccion_pequenios_plot_promedio.png')
plt.savefig(guardado_satis_peq)
print("El grafico de satisfaccion pequenios se guardo bien en:", guardado_satis_peq)