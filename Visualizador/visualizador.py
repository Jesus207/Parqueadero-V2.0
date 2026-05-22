import time
import os
import random

archivo = "../evento.txt"

# 12 celdas
celdas = {i: None for i in range(1, 13)}

# mapa placa -> celda (para poder liberar)
placa_a_celda = {}

def limpiar():
    os.system("clear")

def buscar_celda_libre():
    libres = [c for c, v in celdas.items() if v is None]
    return random.choice(libres) if libres else None


def mostrar_parqueadero():
    print("  " * 2, " - "*11,"  "*11, end="\n")
    print("       PARQUEADERO SIMULADO EN TIEMPO REAL", end="\n")
    print("  " * 2, " - "*11,"  "*11, end="\n")

    for i in range(1, 7):
        izq = f"{i}   {celdas[i] if celdas[i] else '--LIBRE--'}"
        der = f"{i+4}    {celdas[i+4] if celdas[i+4] else '--LIBRE--'}"

        print(f"{izq:<25} || {der}")

    print("\n" + "-" * 50)


def procesar_evento(linea):
    if "PLACA RECIBIDA" not in linea:
        return

    try:
        partes = linea.split("|")

        placa = partes[0].split("->")[1].strip()
        tiempo = partes[-1].strip()

        #  SI YA EXISTE → LIBERAR
        if placa in placa_a_celda:
            celda = placa_a_celda[placa]
            celdas[celda] = None
            del placa_a_celda[placa]

            print(f"🔴 LIBERADO -> {placa} | Celda {celda} | {tiempo}")

        else:
            #  ASIGNAR CELDA ALEATORIA
            celda = buscar_celda_libre()

            if celda is None:
                print(f"⚠️ Parqueadero lleno -> {placa}")
                return

            celdas[celda] = placa
            placa_a_celda[placa] = celda

            print(f"🟢 OCUPADO -> {placa} | Celda {celda} | {tiempo}")

    except Exception as e:
        print("Error procesando evento:", e)


while True:
    try:
        limpiar()

        print("📡 SISTEMA PARQUEADERO - VISUALIZADOR\n")

        try:
            with open(archivo, "r") as f:
                lineas = f.readlines()

            for linea in lineas[-10:]:
                print("⚪ " + linea.strip())
                procesar_evento(linea)

        except FileNotFoundError:
            print("⏳ Esperando eventos...")

        print("\n")
        mostrar_parqueadero()

        print("\n🔄 Actualizando cada 2 segundos...")

        time.sleep(2)

    except KeyboardInterrupt:
        print("\n🛑 Visualizador detenido")
        break