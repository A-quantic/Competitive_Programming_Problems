/*
 * Problema 2 - Tema: Map
 * LeetCode 731. My Calendar II
 * https://leetcode.com/problems/my-calendar-ii/
 *
 * Estructura central: std::map<int,int> como "arreglo de diferencias disperso".
 * Reservar [s, e) suma +1 en la clave s y -1 en la clave e. Recorriendo el mapa en orden
 * de claves y acumulando, se obtiene el numero de reservas activas en cada instante;
 * si alguna supera 2 hay triple reserva y se revierte la insercion.
 *
 * Compilar : g++ -std=c++17 -O2 -Wall -Wextra -o p02 P02_LC731_MyCalendarII.cpp
 *
 * Formato local de E/S (en LeetCode se envia solo la clase MyCalendarTwo):
 *   Linea 1 : q
 *   q lineas: "<start> <end>"
 *   Salida  : "true" o "false" por cada llamada a book.
 */
#include <iostream>
#include <map>

using namespace std;

class MyCalendarTwo {
    map<int, int> delta;  // instante -> cambio en el numero de reservas activas

public:
    bool book(int start, int end) {
        ++delta[start];  // inserta/actualiza el contador en el instante de inicio
        --delta[end];    // y en el de fin (intervalo semiabierto [start, end))
        int activas = 0;
        for (const auto& par : delta) {  // recorrido en orden creciente de claves
            activas += par.second;
            if (activas > 2) {           // triple reserva: se revierte la operacion
                if (--delta[start] == 0) delta.erase(start);
                if (++delta[end] == 0) delta.erase(end);
                return false;
            }
        }
        return true;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int q;
    cin >> q;
    MyCalendarTwo cal;
    while (q--) {
        int s, e;
        cin >> s >> e;
        cout << (cal.book(s, e) ? "true" : "false") << '\n';
    }
    return 0;
}
