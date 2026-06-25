#include <bits/stdc++.h>
#include <sys/resource.h>


using namespace std;
using namespace std::chrono;
namespace fs = std::filesystem;

// Cabeceras simuladas para los algoritmos (asumiendo que estaran en los otros archivos cpp o se compilaran juntos)
// Se deben incluir las estructuras Anime y Capitulo que definimos en los archivos greedy
struct Capitulo {
    long long t;
    long long c;
    long long v;
};

struct Anime {
    std::string nombre;
    int q;
    long long b;
    std::vector<Capitulo> capitulos;
};

// Declaracion de las funciones Greedy que ya tenemos
long long greedy_mayor_bono(long long M, long long E, vector<Anime> animes);
long long greedy_menos_capitulos(long long M, long long E, vector<Anime> animes);
long long fuerza_bruta(long long M, long long E, const vector<Anime>& animes);


// Funcion para medir memoria (extraida de la referencia)
long get_mem_usage(){
    struct rusage myusage;
    getrusage(RUSAGE_SELF, &myusage);
    return myusage.ru_maxrss;
}

int main(){
    // Rutas actualizadas segun la especificacion de la Tarea 2
    string input_dir = "data/inputs"; // "code/implementation/data/inputs";
    string output_dir = "data/outputs";
    string measurement_dir = "data/measurements";

    // Recorrer todos los archivos generados
    for (const auto& entry : fs::directory_iterator(input_dir)){

        string input_file = entry.path().string();
        string filename = entry.path().filename().string();
        string input_name = filename.substr(0, filename.size()-4); // Quitar el .txt

        string output_file = output_dir + "/" + input_name + "_out.txt";
        string measurement_file = measurement_dir + "/" + input_name + "_mea.txt";

        ifstream in_f(input_file);
        if (!in_f.is_open()) {
            cerr << "No se pudo abrir " << input_file << "\n";
            continue;
        }

        // Lectura del nuevo formato (n, M, E)
        int n;
        long long M, E;
        in_f >> n >> M >> E;

        vector<Anime> lista_animes;
        for (int i = 0; i < n; ++i) {
            Anime anime_actual;
            in_f >> anime_actual.nombre >> anime_actual.q >> anime_actual.b;

            for (int j = 0; j < anime_actual.q; ++j) {
                Capitulo cap;
                in_f >> cap.t >> cap.c >> cap.v;
                anime_actual.capitulos.push_back(cap);
            }
            lista_animes.push_back(anime_actual);
        }
        in_f.close();

        ofstream out_f(output_file);
        ofstream meas_f(measurement_file); 

        // Ejecutar y medir los 2 algoritmos Greedy
        for(int i = 0; i < 3; i++){
            auto inicio = high_resolution_clock::now();
            long memoria_inicio = get_mem_usage();
            
            long long resultado = 0;
            string nombre_algoritmo = "";

            if(i == 0){
                resultado = greedy_mayor_bono(M, E, lista_animes);
                nombre_algoritmo = "Greedy_Mayor_Bono";
            } else if (i == 1) {
                resultado = greedy_menos_capitulos(M, E, lista_animes);
                nombre_algoritmo = "Greedy_Menos_Capitulos";
            } else if (i == 2) {
                if (n==3 || n==5 || n==8){
                    resultado = fuerza_bruta(M, E, lista_animes);
                    nombre_algoritmo = "Fuerza_Bruta";
                } else {
                    continue;
                }    
            }       

            long memoria_fin = get_mem_usage();
            auto fin = high_resolution_clock::now();

            auto duracion = duration_cast<nanoseconds>(fin - inicio);
            double tiempo = duracion.count() / 1000.0; // microsegundos
            long memoria_usada = memoria_fin - memoria_inicio;

            // Mostrar progreso en consola
            cout << nombre_algoritmo << " termino para " << input_name << "\n";

            // Guardar salida
            out_f << nombre_algoritmo << " -> MaxSatisfaccion: " << resultado << "\n";

            // Guardar mediciones
            meas_f << nombre_algoritmo << " -> \n";
            meas_f << "Tiempo (ms): " << tiempo << "\n";
            meas_f << "Memoria usada: " << memoria_usada << "\n";
        }
        
        out_f.close();
        meas_f.close();
    }

    return 0;
}