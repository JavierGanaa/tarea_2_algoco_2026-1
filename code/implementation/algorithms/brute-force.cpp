// idea: generar iterativamente todas las combinaciones posibles de capitulos a ver
// como si fuera el cuentakilometros de un auto (odometro).
// un vector guarda cuantos capitulos vemos de cada anime en el intento actual.
// probamos la combinacion, calculamos si es valida y cuanta satisfaccion da.
// luego le sumamos 1 al ultimo anime; si se pasa de su tope, vuelve a 0 y le suma 1 al anterior.
// es fuerza bruta pura, no usa recursion y evalua exhaustivamente el espacio de soluciones.

#include <bits/stdc++.h>
using namespace std;

// Estructuras basicas compartidas
struct Capitulo {
    long long t;
    long long c;
    long long v;
};

struct Anime {
    string nombre;
    int q;
    long long b;
    vector<Capitulo> capitulos;
};

long long fuerza_bruta(long long M, long long E, const vector<Anime>& animes) {
    int n = animes.size();
    if (n == 0) return 0;

    // Arreglo para guardar cuantos capitulos vemos de cada anime en la combinacion actual.
    // Inicia en [0, 0, 0, ..., 0]
    vector<int> seleccion(n, 0);
    long long mejor_satisfaccion = 0;

    bool terminado = false;

    while (!terminado) {
        // 1. EVALUAR LA COMBINACION ACTUAL
        long long tiempo_total = 0;
        long long energia_total = 0;
        long long satisfaccion_total = 0;
        bool combinacion_valida = true;

        for (int i = 0; i < n; ++i) {
            int caps_a_ver = seleccion[i];
            
            for (int j = 0; j < caps_a_ver; ++j) {
                tiempo_total += animes[i].capitulos[j].t;
                energia_total += animes[i].capitulos[j].c;
                satisfaccion_total += animes[i].capitulos[j].v;
            }

            // Si al evaluar esta combinacion vemos que supero los limites,
            // marcamos que no es valida y rompemos el ciclo de evaluacion temprano.
            if (tiempo_total > M || energia_total > E) {
                combinacion_valida = false;
                break;
            }

            // Si vimos todos los capitulos de este anime, cobramos el bono
            if (caps_a_ver == animes[i].q) {
                satisfaccion_total += animes[i].b;
            }
        }

        // Si sobrevivio a la verificacion de limites y es un nuevo record, lo guardamos
        if (combinacion_valida && satisfaccion_total > mejor_satisfaccion) {
            mejor_satisfaccion = satisfaccion_total;
        }

        // 2. GENERAR LA SIGUIENTE COMBINACION (Avanzar el "odometro")
        int pos = n - 1;
        while (pos >= 0) {
            seleccion[pos]++;
            
            // Si la cantidad de capitulos que quiero ver supera el total que tiene ese anime
            if (seleccion[pos] > animes[pos].q) {
                seleccion[pos] = 0; // Vuelve a 0
                pos--; // Pasa el "acarreo" al anime anterior
            } else {
                // Si no se paso del tope, la nueva combinacion esta lista para evaluarse
                break; 
            }
        }

        // Si el "acarreo" retrocedio mas alla del primer anime, significa que ya revisamos TODO el arbol
        if (pos < 0) {
            terminado = true;
        }
    }

    return mejor_satisfaccion;
}