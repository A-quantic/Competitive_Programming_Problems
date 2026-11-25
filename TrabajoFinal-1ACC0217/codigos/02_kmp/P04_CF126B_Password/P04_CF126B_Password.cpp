/*
 * Problema 4 - Tema: KMP
 * Codeforces 126B. Password
 * https://codeforces.com/problemset/problem/126/B
 * (Enunciado resumido segun la descripcion usada en este informe: encontrar la subcadena
 *  mas larga t que sea a la vez prefijo, sufijo y que ademas aparezca en el interior de s;
 *  si no existe, imprimir "Just a legend".)
 *
 * Idea con LPS:
 *  - Los bordes de s (prefijo = sufijo) forman la cadena n -> lps[n-1] -> lps[lps[n-1]-1] ...
 *  - Un borde de longitud k aparece en el interior si existe una posicion i en [1, n-2]
 *    con lps[i] >= k (un prefijo de s de longitud lps[i] termina en i, luego el prefijo de
 *    longitud k es sufijo de ese prefijo, y ocurre terminando en i <= n-2).
 *  - Se prueba cada borde de mayor a menor y se devuelve el primero que cumple.
 *
 * Compilar : g++ -std=c++17 -O2 -Wall -Wextra -o p04 P04_CF126B_Password.cpp
 * Entrada  : una linea con la cadena s.   Salida: la subcadena o "Just a legend".
 */
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

vector<int> construirLPS(const string& s) {
    int n = static_cast<int>(s.size());
    vector<int> lps(n, 0);
    for (int i = 1; i < n; ++i) {
        int k = lps[i - 1];
        while (k > 0 && s[i] != s[k]) k = lps[k - 1];
        if (s[i] == s[k]) ++k;
        lps[i] = k;
    }
    return lps;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string s;
    cin >> s;
    int n = static_cast<int>(s.size());
    vector<int> lps = construirLPS(s);

    // Mayor valor de lps en posiciones interiores 1..n-2.
    int maxInterior = 0;
    for (int i = 1; i + 1 < n; ++i) maxInterior = max(maxInterior, lps[i]);

    int k = lps[n - 1];  // mayor borde propio
    while (k > 0) {
        if (k <= maxInterior) {      // el borde de longitud k ocurre tambien en el interior
            cout << s.substr(0, k) << '\n';
            return 0;
        }
        k = lps[k - 1];              // siguiente borde mas corto (cadena de bordes)
    }
    cout << "Just a legend\n";
    return 0;
}
