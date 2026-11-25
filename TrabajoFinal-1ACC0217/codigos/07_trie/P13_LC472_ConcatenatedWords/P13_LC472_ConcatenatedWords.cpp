/*
 * Problema 13 - Tema: Trie
 * LeetCode 472. Concatenated Words (Hard)
 * https://leetcode.com/problems/concatenated-words/
 *
 * Una palabra es "concatenada" si se forma con al menos dos palabras MAS CORTAS de la lista.
 * Se procesan las palabras por longitud creciente; el trie contiene solo palabras mas cortas
 * (o de igual longitud, que nunca coinciden con w porque no hay duplicados).
 * Para cada w: puede[i] = el prefijo w[0..i) se parte en palabras del trie.
 * Desde cada i alcanzable se recorre el trie con w[i..] y cada nodo "fin" en la posicion j
 * marca puede[j+1]. Si puede[|w|], w es concatenada (usa >= 2 piezas porque todas son mas
 * cortas que w). Todas las palabras se insertan despues de evaluarse.
 *
 * Compilar : g++ -std=c++17 -O2 -Wall -Wextra -o p13 P13_LC472_ConcatenatedWords.cpp
 * Formato local de E/S (en LeetCode solo se envia la clase Solution):
 *   Linea 1 : n         Siguientes n lineas: una palabra
 *   Salida  : k y luego las k palabras concatenadas, en el orden de la entrada
 */
#include <algorithm>
#include <array>
#include <iostream>
#include <numeric>
#include <string>
#include <vector>
using namespace std;

class Solution {
    struct Nodo {
        array<int, 26> hijo;
        bool fin = false;
        Nodo() { hijo.fill(-1); }
    };
    vector<Nodo> trie{Nodo()};

    void insertar(const string& w) {
        int nodo = 0;
        for (char ch : w) {
            int c = ch - 'a';
            if (trie[nodo].hijo[c] == -1) {
                trie[nodo].hijo[c] = (int)trie.size();
                trie.emplace_back();
            }
            nodo = trie[nodo].hijo[c];
        }
        trie[nodo].fin = true;
    }

    bool esConcatenada(const string& w) const {
        int L = (int)w.size();
        vector<char> puede(L + 1, 0);
        puede[0] = 1;
        for (int i = 0; i < L; ++i) {
            if (!puede[i]) continue;
            int nodo = 0;
            for (int j = i; j < L; ++j) {
                nodo = trie[nodo].hijo[w[j] - 'a'];
                if (nodo == -1) break;
                if (trie[nodo].fin) puede[j + 1] = 1;
            }
            if (puede[L]) return true;
        }
        return false;
    }

public:
    vector<string> findAllConcatenatedWordsInADict(vector<string>& words) {
        vector<int> orden(words.size());
        iota(orden.begin(), orden.end(), 0);
        stable_sort(orden.begin(), orden.end(),
                    [&](int a, int b) { return words[a].size() < words[b].size(); });
        size_t total = 0;
        for (auto& w : words) total += w.size();
        trie.reserve(total + 1);
        vector<char> marca(words.size(), 0);
        for (int id : orden) {
            const string& w = words[id];
            if (w.empty()) continue;
            if (esConcatenada(w)) marca[id] = 1;
            insertar(w);
        }
        vector<string> res;
        for (size_t i = 0; i < words.size(); ++i)
            if (marca[i]) res.push_back(words[i]);
        return res;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    vector<string> words(n);
    for (auto& w : words) cin >> w;
    Solution s;
    vector<string> res = s.findAllConcatenatedWordsInADict(words);
    cout << res.size() << '\n';
    for (auto& w : res) cout << w << '\n';
    return 0;
}
