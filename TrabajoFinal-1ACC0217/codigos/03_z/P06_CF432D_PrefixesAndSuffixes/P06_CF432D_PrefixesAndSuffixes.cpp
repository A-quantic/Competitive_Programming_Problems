/*
 * Problema 6 - Tema: Algoritmo Z
 * Codeforces 432D. Prefixes and Suffixes
 * https://codeforces.com/problemset/problem/432/D
 * (Enunciado resumido segun la descripcion usada en este informe: para cada longitud l tal
 *  que el prefijo de longitud l de s es tambien sufijo de s, imprimir l y el numero de
 *  apariciones de ese prefijo en s; las longitudes se imprimen en orden creciente.
 *  )
 *
 * Con el arreglo Z (z[0] = n):
 *   - l es borde  <=>  l = n  o  z[n-l] == l.
 *   - apariciones del prefijo de longitud l = #{ i : z[i] >= l }  (incluye i = 0).
 *     Se obtiene con un arreglo de frecuencias de z y sumas de sufijos en O(n).
 *
 * Compilar : g++ -std=c++17 -O2 -Wall -Wextra -o p06 P06_CF432D_PrefixesAndSuffixes.cpp
 * Entrada  : una linea con s.
 * Salida   : k, y luego k lineas "l c" (longitud y numero de apariciones).
 */
#include <algorithm>
#include <iostream>
#include <string>
#include <utility>
#include <vector>

using namespace std;

vector<int> construirZ(const string& s) {
    int n = static_cast<int>(s.size());
    vector<int> z(n, 0);
    z[0] = n;
    int l = 0, r = 0;  // ventana [l, r)
    for (int i = 1; i < n; ++i) {
        if (i < r) z[i] = min(r - i, z[i - l]);
        while (i + z[i] < n && s[z[i]] == s[i + z[i]]) ++z[i];
        if (i + z[i] > r) {
            l = i;
            r = i + z[i];
        }
    }
    return z;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string s;
    cin >> s;
    int n = static_cast<int>(s.size());
    vector<int> z = construirZ(s);

    vector<int> cnt(n + 2, 0);                    // cnt[v] = cuantos i tienen z[i] == v
    for (int i = 0; i < n; ++i) ++cnt[z[i]];
    for (int l = n - 1; l >= 1; --l) cnt[l] += cnt[l + 1];  // cnt[l] = #{i : z[i] >= l}

    vector<pair<int, int>> respuesta;
    for (int l = 1; l <= n; ++l)
        if (l == n || z[n - l] == l) respuesta.emplace_back(l, cnt[l]);

    cout << respuesta.size() << '\n';
    for (const auto& p : respuesta) cout << p.first << ' ' << p.second << '\n';
    return 0;
}
