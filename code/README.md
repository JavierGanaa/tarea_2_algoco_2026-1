# Documentación

scripts de python estuvieron basados en los de la tarea anterior

## Implementación

### Programa principal

El archivo `general.cpp` es el principal y se encarga de hacer todo el flujo:
- Lee automáticamente los casos de prueba desde la carpeta `inputs`.
- Ejecuta los algoritmos (los dos Greedy y el de Fuerza Bruta). Aunque el de Fuerza Bruta tiene una condición para que solo corra en los casos pequeños y así no se quede pegado el programa.
- Mide el tiempo y la memoria que usa cada uno.
- Guarda las satisfacciones finales en `outputs` y los datos de rendimiento en `measurements`.


### Scripts

Son solo dos scripts en Python:
- `testcases_generator.py`: Crea los `.txt` con los datos aleatorios de los animes para todos los tamaños probados.
- `plot_generator.py`: Lee los `.txt` que generó el código en C++ y usa `matplotlib` para armar y guardar los 4 gráficos de los resultados.
Se crearon 2 series de gráficos, los que consideran todos los tipos de casos, y los que consideran solo los casos pequeños, este segundo tipo de gráficos existe para poder hacer más visible la comparación de los Greedy con el Fuerza Bruta, ya que en casos grandes no existe el DP para comparar.
