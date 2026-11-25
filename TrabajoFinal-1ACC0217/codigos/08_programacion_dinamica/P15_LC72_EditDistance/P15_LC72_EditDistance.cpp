/*
 * Problema 15 - Tema: Programacion Dinamica (DP sobre prefijos de dos cadenas)
 * LeetCode 72. Edit Distance
 * https://leetcode.com/problems/edit-distance/
 *
 * ESTADO     : D[i][j] = distancia de edicion minima entre los prefijos a[0..i) y b[0..j).
 * CASOS BASE : D[i][0] = i (borrar i caracteres), D[0][j] = j (insertar j caracteres).
 * RECURRENCIA: D[i][j] = D[i-1][j-1]                                   si a[i-1] == b[j-1]
 *              D[i][j] = 1 + min(D[i-1][j]      (borrar a[i-1]),
 *                                D[i][j-1]      (insertar b[j-1]),
 *                                D[i-1][j-1])   (reemplazar)           si a[i-1] != b[j-1]
 * RESPUESTA  : D[m][n].
 * Se incluye tambien la version con memoria O(min(m, n)) (dos filas), activable con --opt.
 *
 * Compilar : g++ -std=c++17 -O2 -Wall -Wextra -o p15 P15_LC72_EditDistance.cpp
 * Formato local: linea 1 = word1 (puede estar vacia), linea 2 = word2 (puede estar vacia).
 * Salida: la distancia de edicion.
 */
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

// Tabulacion completa: tiempo O(mn), espacio O(mn).
int minDistance(const string& a, const string& b) {
    int m = static_cast<int>(a.size()), n = static_cast<int>(b.size());
    vector<vector<int>> D(m + 1, vector<int>(n + 1, 0));
    for (int i = 0; i <= m; ++i) D[i][0] = i;
    for (int j = 0; j <= n; ++j) D[0][j] = j;
    for (int i = 1; i <= m; ++i) {
        for (int j = 1; j <= n; ++j) {
            if (a[i - 1] == b[j - 1]) D[i][j] = D[i - 1][j - 1];
            else D[i][j] = 1 + min({D[i - 1][j], D[i][j - 1], D[i - 1][j - 1]});
        }
    }
    return D[m][n];
}

// Misma recurrencia con dos filas: espacio O(min(m, n)).
int minDistanceOptimizado(const string& a, const string& b) {
    const string& corta = (a.size() <= b.size()) ? a : b;
    const string& larga = (a.size() <= b.size()) ? b : a;
    int c = static_cast<int>(corta.size()), l = static_cast<int>(larga.size());
    vector<int> previa(c + 1), actual(c + 1);
    for (int j = 0; j <= c; ++j) previa[j] = j;
    for (int i = 1; i <= l; ++i) {
        actual[0] = i;
        for (int j = 1; j <= c; ++j) {
            if (larga[i - 1] == corta[j - 1]) actual[j] = previa[j - 1];
            else actual[j] = 1 + min({previa[j], actual[j - 1], previa[j - 1]});
        }
        swap(previa, actual);
    }
    return previa[c];
}

int main(int argc, char** argv) {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    bool optimizado = (argc > 1 && string(argv[1]) == "--opt");
    string a, b;
    getline(cin, a);
    getline(cin, b);
    if (!a.empty() && a.back() == '\r') a.pop_back();
    if (!b.empty() && b.back() == '\r') b.pop_back();
    cout << (optimizado ? minDistanceOptimizado(a, b) : minDistance(a, b)) << '\n';
    return 0;
}
