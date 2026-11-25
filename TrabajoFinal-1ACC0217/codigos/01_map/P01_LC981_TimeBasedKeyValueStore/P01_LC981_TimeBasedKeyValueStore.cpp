/*
 * Problema 1 - Tema: Map
 * LeetCode 981. Time Based Key-Value Store
 * https://leetcode.com/problems/time-based-key-value-store/
 *
 * Estructura central: std::map<int, std::string> por cada clave (arbol rojo-negro,
 * claves ordenadas por timestamp). get(key, t) debe devolver el valor con el MAYOR
 * timestamp <= t: se obtiene con upper_bound(t) y retrocediendo una posicion.
 *
 * Compilar : g++ -std=c++17 -O2 -Wall -Wextra -o p01 P01_LC981_TimeBasedKeyValueStore.cpp
 *
 * Formato local de E/S (arnes de prueba; en LeetCode solo se envia la clase TimeMap):
 *   Linea 1 : q  (numero de operaciones)
 *   q lineas: "set <key> <value> <timestamp>"  o  "get <key> <timestamp>"
 *   Salida  : una linea por cada "get" (linea vacia si no existe valor).
 */
#include <iostream>
#include <iterator>
#include <map>
#include <string>
#include <unordered_map>

using namespace std;

class TimeMap {
    // clave -> (timestamp -> valor). El map interno mantiene los timestamps ordenados.
    unordered_map<string, map<int, string>> db;

public:
    // Insercion/actualizacion: O(log m), m = numero de timestamps de esa clave.
    void set(const string& key, const string& value, int timestamp) {
        db[key][timestamp] = value;
    }

    // Busqueda del "piso" del timestamp: O(log m).
    string get(const string& key, int timestamp) const {
        auto it = db.find(key);
        if (it == db.end()) return "";
        const map<int, string>& tiempos = it->second;
        auto ub = tiempos.upper_bound(timestamp);  // primer timestamp estrictamente mayor
        if (ub == tiempos.begin()) return "";       // todos los timestamps son mayores
        return prev(ub)->second;                    // mayor timestamp <= timestamp
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int q;
    cin >> q;
    TimeMap tm;
    while (q--) {
        string op;
        cin >> op;
        if (op == "set") {
            string key, value;
            int ts;
            cin >> key >> value >> ts;
            tm.set(key, value, ts);
        } else {
            string key;
            int ts;
            cin >> key >> ts;
            cout << tm.get(key, ts) << '\n';
        }
    }
    return 0;
}
