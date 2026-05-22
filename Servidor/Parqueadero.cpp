#include "Parqueadero.h"
#include <iostream>
#include <ctime>

using namespace std;
Parqueadero::Parqueadero(){}
string Parqueadero::procesarPlaca(string placa){
    if (ocupacion) return "OCUPADO | Celda X";
    else return "LIBRE | Celda X";
    return "OK: " + placa;
}