/*
 * Problema 3 - Tema: KMP
 * LeetCode 214. Shortest Palindrome
 * https://leetcode.com/problems/shortest-palindrome/
 *
 * Idea: el prefijo palindromico mas largo P de s se obtiene con el arreglo LPS (funcion
 * prefijo de KMP) de la cadena t = s + '#' + reverse(s). El ultimo valor de LPS es la
 * longitud del mayor prefijo de s que tambien es sufijo de reverse(s), es decir, el
 * mayor prefijo palindromico. La respuesta es reverse(sufijo restante) + s.
 *
 * Compilar : g++ -std=c++17 -O2 -Wall -Wextra -o p03 P03_LC214_ShortestPalindrome.cpp
 *
 * Formato local de E/S (en LeetCode se envia solo Solution::shortestPalindrome):
 *   Entrada : una linea con s (puede estar vacia).   Salida: el palindromo mas corto.
 */
#include <iostream>
#include <string>
#include <vector>

using namespace std;

// lps[i] = longitud del mayor borde propio (prefijo que tambien es sufijo) de t[0..i].
vector<int> construirLPS(const string& t) {
    int m = static_cast<int>(t.size());
    vector<int> lps(m, 0);
    for (int i = 1; i < m; ++i) {
        int k = lps[i - 1];
        while (k > 0 && t[i] != t[k]) k = lps[k - 1];  // reutiliza bordes previos, sin retroceder i
        if (t[i] == t[k]) ++k;
        lps[i] = k;
    }
    return lps;
}

string shortestPalindrome(const string& s) {
    int n = static_cast<int>(s.size());
    if (n == 0) return s;
    string rev(s.rbegin(), s.rend());
    string t = s + '#' + rev;                // '#' evita bordes que crucen la frontera
    vector<int> lps = construirLPS(t);
    int longitudPalindromo = lps.back();     // mayor prefijo palindromico de s
    return rev.substr(0, n - longitudPalindromo) + s;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    string s;
    getline(cin, s);
    if (!s.empty() && s.back() == '\r') s.pop_back();
    cout << shortestPalindrome(s) << '\n';
    return 0;
}
