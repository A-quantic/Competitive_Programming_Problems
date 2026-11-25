/*
 * Problema 12 - Tema: Trie (trie binario de 31 bits)
 * LeetCode 421. Maximum XOR of Two Numbers in an Array
 * https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/
 *
 * Cada numero (0 <= x < 2^31) se inserta como una cadena de 31 bits, del bit 30 al 0.
 * Para maximizar x XOR y se busca, bit a bit desde el mas significativo, el hijo con el
 * bit opuesto; si existe se suma ese bit al resultado y se avanza por el, si no se avanza
 * por el unico hijo disponible. Es una busqueda voraz correcta porque un bit alto vale mas
 * que todos los bits inferiores juntos.
 *
 * Compilar : g++ -std=c++17 -O2 -Wall -Wextra -o p12 P12_LC421_MaximumXOROfTwoNumbers.cpp
 * Formato local: n / n enteros.   Salida: el XOR maximo.
 */
#include <algorithm>
#include <array>
#include <iostream>
#include <vector>

using namespace std;

class TrieBinario {
    static const int BITS = 31;
    vector<array<int, 2>> hijo;  // hijo[nodo][bit]; el indice 0 es la raiz y significa "sin hijo" si es destino

public:
    explicit TrieBinario(size_t nodosEsperados = 1) {
        hijo.reserve(nodosEsperados * BITS + 1);
        hijo.push_back({0, 0});  // raiz
    }
    void insertar(int x) {                        // O(31)
        int nodo = 0;
        for (int b = BITS - 1; b >= 0; --b) {
            int bit = (x >> b) & 1;
            if (hijo[nodo][bit] == 0) {
                hijo[nodo][bit] = static_cast<int>(hijo.size());
                hijo.push_back({0, 0});
            }
            nodo = hijo[nodo][bit];
        }
    }
    // Mayor x XOR y con y entre los numeros insertados (el trie no debe estar vacio). O(31).
    int xorMaximoCon(int x) const {
        int nodo = 0, resultado = 0;
        for (int b = BITS - 1; b >= 0; --b) {
            int bit = (x >> b) & 1;
            int deseado = bit ^ 1;                // bit opuesto => XOR = 1 en esa posicion
            if (hijo[nodo][deseado] != 0) {
                resultado |= (1 << b);
                nodo = hijo[nodo][deseado];
            } else {
                nodo = hijo[nodo][bit];
            }
        }
        return resultado;
    }
};

int findMaximumXOR(const vector<int>& nums) {
    TrieBinario trie(nums.size());
    for (int x : nums) trie.insertar(x);
    int mejor = 0;
    for (int x : nums) mejor = max(mejor, trie.xorMaximoCon(x));
    return mejor;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<int> nums(n);
    for (int& x : nums) cin >> x;
    cout << findMaximumXOR(nums) << '\n';
    return 0;
}
