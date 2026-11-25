/*
 * Problema 11 - Tema: Arboles ternarios (arbol de busqueda ternario, TST)
 * LeetCode 211. Design Add and Search Words Data Structure (Medium)
 * https://leetcode.com/problems/design-add-and-search-words-data-structure/
 *
 * Cada nodo guarda un caracter y tres hijos:
 *   lo  -> caracteres menores que c   (misma posicion de la palabra)
 *   eq  -> siguiente caracter cuando coincide c (avanza una posicion)
 *   hi  -> caracteres mayores que c   (misma posicion de la palabra)
 * addWord recorre/crea nodos; search sigue una sola rama por letra y, ante '.',
 * explora las tres ramas (lo y hi con la misma posicion, eq con la siguiente).
 *
 * Compilar : g++ -std=c++17 -O2 -Wall -Wextra -o p11 P11_LC211_TernarySearchTree.cpp
 * Formato local de E/S (en LeetCode solo se envia la clase WordDictionary):
 *   Linea 1 : q
 *   q lineas: "add palabra" o "search patron"
 *   Salida  : una linea "true"/"false" por cada search
 */
#include <iostream>
#include <string>
#include <vector>
using namespace std;

class WordDictionary {
    struct Nodo {
        char c;
        bool fin = false;
        int lo = -1, eq = -1, hi = -1;
        explicit Nodo(char ch) : c(ch) {}
    };
    vector<Nodo> t;   // nodos en un vector; la raiz es t[0] (si existe)

    int nuevo(char c) { t.emplace_back(c); return (int)t.size() - 1; }

    bool buscar(int nodo, const string& p, size_t i) const {
        if (nodo == -1) return false;
        const Nodo& x = t[nodo];
        char ch = p[i];
        if (ch == '.' || ch < x.c)
            if (buscar(x.lo, p, i)) return true;
        if (ch == '.' || ch > x.c)
            if (buscar(x.hi, p, i)) return true;
        if (ch == '.' || ch == x.c) {
            if (i + 1 == p.size()) return x.fin;
            return buscar(x.eq, p, i + 1);
        }
        return false;
    }

public:
    WordDictionary() { t.reserve(1 << 16); }

    void addWord(const string& w) {
        if (t.empty()) nuevo(w[0]);
        int nodo = 0;
        size_t i = 0;
        while (true) {
            char ch = w[i];
            if (ch < t[nodo].c) {
                if (t[nodo].lo == -1) { int k = nuevo(ch); t[nodo].lo = k; }
                nodo = t[nodo].lo;
            } else if (ch > t[nodo].c) {
                if (t[nodo].hi == -1) { int k = nuevo(ch); t[nodo].hi = k; }
                nodo = t[nodo].hi;
            } else if (i + 1 == w.size()) {
                t[nodo].fin = true;
                return;
            } else {
                ++i;
                if (t[nodo].eq == -1) { int k = nuevo(w[i]); t[nodo].eq = k; }
                nodo = t[nodo].eq;
            }
        }
    }

    bool search(const string& p) const { return !t.empty() && buscar(0, p, 0); }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int q;
    if (!(cin >> q)) return 0;
    WordDictionary d;
    while (q--) {
        string op, w;
        cin >> op >> w;
        if (op == "add") d.addWord(w);
        else cout << (d.search(w) ? "true" : "false") << '\n';
    }
    return 0;
}
