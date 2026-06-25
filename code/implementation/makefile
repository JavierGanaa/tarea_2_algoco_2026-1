# Makefile para la Tarea 2 - AniMarathon

# Variables de compilacion
CXX = g++
CXXFLAGS = -Wall -std=c++17 -O3
TARGET = general

# Archivos de codigo fuente
SRCS = general.cpp algorithms/greedy1.cpp algorithms/greedy2.cpp algorithms/brute-force.cpp

# Variable para Python. 
# Como estas usando la terminal de WSL (Linux), el comando estandar es python3.
# Si en algun momento ejecutas esto desde PowerShell en Windows, cambialo a 'py' o 'python' segun tu configuracion.
PYTHON_CMD = python3
GENERATOR_SCRIPT = scripts/testcases_generator.py
PLOT_SCRIPT = scripts/plot_generator.py

# Regla por defecto: genera los casos, compila y luego ejecuta
all: generate compile run plot

# 1. Generar los casos de prueba con Python
generate:
	$(PYTHON_CMD) $(GENERATOR_SCRIPT)

# 2. Compilar los algoritmos C++
compile:
	$(CXX) $(CXXFLAGS) $(SRCS) -o $(TARGET)

# 3. Ejecutar el programa principal
run:
	./$(TARGET)

# 4. Generar los graficos justo despues de que C++ termine
plot:
	$(PYTHON_CMD) $(PLOT_SCRIPT)

# Limpiar el ejecutable (util para reiniciar el entorno)
clean:
	rm -f $(TARGET)