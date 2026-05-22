#!/bin/bash

echo "=================================="
echo "   INICIANDO SISTEMA PARQUEADERO "
echo "=================================="

# 1. Compilar servidor y cliente (por seguridad)
echo "Compilando servidor..."
g++ Servidor/Servidor.cpp Servidor/Parqueadero.cpp -IServidor -o servidor

echo "Compilando cliente..."
g++ Cliente/Cliente.cpp -o cliente


# 2. Ejecutar servidor (en background)
echo "Iniciando servidor..."
./servidor &
SERVER_PID=$!

sleep 2

# 3. Ejecutar cliente (en background)
echo "Iniciando cliente..."
./cliente &
CLIENT_PID=$!

sleep 2

# 4. Ejecutar visualizador Python
echo "Iniciando visualizador..."
python3 Visualizador/visualizador.py &
VISUAL_PID=$!

echo "=================================="
echo "Sistema corriendo:"
echo "Servidor PID: $SERVER_PID"
echo "Cliente PID: $CLIENT_PID"
echo "Visualizador PID: $VISUAL_PID"
echo "=================================="

wait