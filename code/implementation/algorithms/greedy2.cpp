// comenzar siempre con el anime con menor cantidad de capitulos, 
// ya que eso significa que se verá una gran cantidad de animes,
// maximizando así la cantidad de bonos de satisfacción recibidos



#include <bits/stdc++.h>
using namespace std;

// Estructuras basicas (las mismas que usaremos en general.cpp)
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

// Funcion auxiliar: el "arbitro" que le dice al sort que ordene de MENOR a MAYOR cantidad de capitulos
bool comparar_menos_capitulos(const Anime& a1, const Anime& a2) {
    return a1.q < a2.q; 
}

long long greedy_menos_capitulos(long long M, long long E, vector<Anime> animes) {
    // Ordenamos la lista de animes priorizando los que tienen menos capitulos
    sort(animes.begin(), animes.end(), comparar_menos_capitulos);

    long long satisfaccion_total = 0;
    long long minutos_restantes = M;
    long long energia_restante = E;

    for (int i = 0; i < animes.size(); ++i) {
        int capitulos_vistos = 0;
        
        for (int j = 0; j < animes[i].q; ++j) {
            long long tiempo_req = animes[i].capitulos[j].t;
            long long energia_req = animes[i].capitulos[j].c;
            long long satisfaccion_cap = animes[i].capitulos[j].v;

            // Verificamos si la mochila todavia aguanta este capitulo
            if (minutos_restantes >= tiempo_req && energia_restante >= energia_req) {
                
                minutos_restantes -= tiempo_req;
                energia_restante -= energia_req;
                satisfaccion_total += satisfaccion_cap;
                capitulos_vistos++;
                
            } else {
                // Ya no nos alcanza para seguir el orden de este anime, pasamos al siguiente
                break;
            }
        }

        // Si logramos ver todos los capitulos que tenia este anime, cobramos su bono
        if (capitulos_vistos == animes[i].q) {
            satisfaccion_total += animes[i].b;
        }
    }

    return satisfaccion_total;
}




