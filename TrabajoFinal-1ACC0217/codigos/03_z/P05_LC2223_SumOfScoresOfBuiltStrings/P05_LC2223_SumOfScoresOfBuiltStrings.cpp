/*
 * Problema 5 - Tema: Algoritmo Z
 * LeetCode 2223. Sum of Scores of Built Strings
 * https://leetcode.com/problems/sum-of-scores-of-built-strings/
 *
 * La cadena s_i (longitud i) es el sufijo de s que empieza en n-i. Su puntaje es el LCP
 * (prefijo comun mas largo) con s, que es exactamente Z[n-i]. Con Z[0] = n, la respuesta
 * es sum(Z). La suma puede llegar a n(n+1)/2 ~ 5*10^9, por eso se usa long long.
 *
 * Compilar : g++ -std=c++17 -O2 -Wall -Wextra -o p05 P05_LC2223_SumOfScoresOfBuiltStrings.cpp
 * Formato local: una linea con s.  Salida: la suma de puntajes.
 */
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

// z[i] = longitud del mayor prefijo comun entre s y s[i..]. Por convencion z[0] = n.
// Ventana [l, r): s[l..r) coincide con el prefijo s[0..r-l) (la ocurrencia mas a la derecha).
vector<int> construirZ(const string& s) {
    int n = static_cast<int>(s.size());
    vector<int> z(n, 0);
    z[0] = n;
    int l = 0, r = 0;
    for (int i = 1; i < n; ++i) {
        if (i < r) z[i] = min(r - i, z[i - l]);              // reutiliza lo ya comparado
        while (i + z[i] < n && s[z[i]] == s[i + z[i]]) ++z[i];  // extiende solo mas alla de r
        if (i + z[i] > r) {                                  // nueva ventana mas a la derecha
            l = i;
            r = i + z[i];
        }
    }
    return z;
}

long long sumScores(const string& s) {
    vector<int> z = construirZ(s);
    long long total = 0;
    for (int v : z) total += v;
    return total;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string s;
    cin >> s;
    cout << sumScores(s) << '\n';
    return 0;
}
