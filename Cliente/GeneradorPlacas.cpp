#include "GeneradorPlacas.h"
#include <cstdlib>
#include <ctime>

using namespace std;

string GeneradorPlacas::generar() {

    string placa = "";

    // letras
    for (int i = 0; i < 3; i++) {
        placa += char('A' + rand() % 26);
    }

    // números
    for (int i = 0; i < 3; i++) {
        placa += char('0' + rand() % 10);
    }

    return placa;
}