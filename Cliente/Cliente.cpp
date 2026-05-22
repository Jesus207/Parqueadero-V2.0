#include <iostream>
#include <cstring>
#include <unistd.h>
#include <arpa/inet.h>

using namespace std;

string generarPlaca() {
    string letras = "ABCDEF";
    string numeros = "0123456789";

    string placa = "";
    placa += letras[rand() % 6];
    placa += letras[rand() % 6];
    placa += letras[rand() % 6];
    placa += numeros[rand() % 10];
    placa += numeros[rand() % 10];
    placa += numeros[rand() % 10];

    return placa;
}

int main() {

    srand(time(NULL));

    int sock = socket(AF_INET, SOCK_STREAM, 0);

    if (sock < 0) {
        cout << "Error creando socket cliente" << endl;
        return 1;
    }

    sockaddr_in servidor;
    servidor.sin_family = AF_INET;
    servidor.sin_port = htons(8080);

    // 🔥 IMPORTANTE: si estás en Codespaces usa IP del server
    servidor.sin_addr.s_addr = inet_addr("127.0.0.1");

    if (connect(sock, (sockaddr*)&servidor, sizeof(servidor)) < 0) {
        cout << "Error conectando al servidor" << endl;
        return 1;
    }

    cout << "Conectado al servidor" << endl;

    while (true) {
        cliente_fd = socket(AF_INET, SOCK_STREAM, 0);

        if (connect(cliente_fd, (sockaddr*)&direccion, sizeof(direccion)) == 0) {
            cout << "Conectado al servidor" << endl;
            break;
        }

        cout << "Reintentando conexión..." << endl;
        sleep(2);
    }

    return 0;
}