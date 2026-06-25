// idea :comenzar siempre con el anime con mayor bono de satisfaccion

#include <bits/stdc++.h>
using namespace std;

// Estructuras basicas para organizar la informacion leida del txt
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

// Funcion auxiliar para que std::sort ordene de mayor a menor bono
bool comparar_bono(const Anime& a1, const Anime& a2) {
    return a1.b > a2.b;
}

long long greedy_mayor_bono(long long M, long long E, vector<Anime> animes) {
    // Ordenamos la lista de animes segun el bono de mayor a menor
    // Nota: 'animes' se pasa por valor, asi que esta copia local se ordena 
    // sin afectar el arreglo original en el main
    sort(animes.begin(), animes.end(), comparar_bono);

    long long satisfaccion_total = 0;
    long long minutos_restantes = M;
    long long energia_restante = E;

    for (int i = 0; i < animes.size(); ++i) {
        int capitulos_vistos = 0;
        
        // Intentar ver los capitulos en orden (prefijo obligatorio)
        for (int j = 0; j < animes[i].q; ++j) {
            long long tiempo_req = animes[i].capitulos[j].t;
            long long energia_req = animes[i].capitulos[j].c;
            long long satisfaccion_cap = animes[i].capitulos[j].v;

            // Revisar si nos alcanzan los recursos para este capitulo especifico
            if (minutos_restantes >= tiempo_req && energia_restante >= energia_req) {
                
                minutos_restantes -= tiempo_req;
                energia_restante -= energia_req;
                satisfaccion_total += satisfaccion_cap;
                capitulos_vistos++;
                
            } else {
                // Si no me alcanza para este capitulo, la regla dice que no puedo ver los siguientes.
                // Asi que rompemos el ciclo de este anime y pasamos al siguiente.
                break;
            }
        }

        // Si el contador de capitulos vistos es igual al total de capitulos de este anime, cobramos el bono
        if (capitulos_vistos == animes[i].q) {
            satisfaccion_total += animes[i].b;
        }
    }

    return satisfaccion_total;
}








