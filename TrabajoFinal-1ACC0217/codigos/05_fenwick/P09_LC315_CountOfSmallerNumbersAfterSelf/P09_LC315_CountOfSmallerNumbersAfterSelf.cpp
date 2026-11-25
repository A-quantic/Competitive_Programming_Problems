/*
 * Problema 9 - Tema: Arbol Fenwick (Binary Indexed Tree)
 * LeetCode 315. Count of Smaller Numbers After Self
 * https://leetcode.com/problems/count-of-smaller-numbers-after-self/
 *
 * Se recorre nums de derecha a izquierda. El Fenwick mantiene, sobre el rango de ranks
 * (compresion de coordenadas), cuantos valores ya fueron vistos:
 *   counts[i] = query(rank(nums[i]) - 1)  ->  elementos vistos estrictamente menores
 *   update(rank(nums[i]), +1)             ->  registrar nums[i]
 * lowbit(i) = i & -i da el tamano del bloque que cubre bit[i].
 *
 * Compilar : g++ -std=c++17 -O2 -Wall -Wextra -o p09 P09_LC315_CountOfSmallerNumbersAfterSelf.cpp
 * Formato local: n / n enteros.   Salida: n enteros separados por espacios.
 */
#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

class Fenwick {
    int n;
    vector<int> bit;  // bit[i] = suma del bloque (i - lowbit(i), i]

    static int lowbit(int i) { return i & -i; }

public:
    explicit Fenwick(int n) : n(n), bit(n + 1, 0) {}

    void update(int i, int delta) {                 // O(log n): sube por i += lowbit(i)
        for (; i <= n; i += lowbit(i)) bit[i] += delta;
    }
    int query(int i) const {                        // suma del prefijo [1, i]: O(log n)
        int suma = 0;
        for (; i > 0; i -= lowbit(i)) suma += bit[i];
        return suma;
    }
    int rangeQuery(int l, int r) const {            // suma de [l, r] por diferencia de prefijos
        return query(r) - query(l - 1);
    }
};

vector<int> countSmaller(const vector<int>& nums) {
    int n = static_cast<int>(nums.size());
    vector<int> valores(nums);
    sort(valores.begin(), valores.end());
    valores.erase(unique(valores.begin(), valores.end()), valores.end());

    Fenwick fw(static_cast<int>(valores.size()));
    vector<int> counts(n, 0);
    for (int i = n - 1; i >= 0; --i) {
        int rank = static_cast<int>(lower_bound(valores.begin(), valores.end(), nums[i]) - valores.begin()) + 1;
        counts[i] = fw.query(rank - 1);             // estrictamente menores ya insertados
        fw.update(rank, 1);
    }
    return counts;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<int> nums(n);
    for (int& x : nums) cin >> x;
    vector<int> res = countSmaller(nums);
    for (int i = 0; i < n; ++i) cout << res[i] << (i + 1 < n ? ' ' : '\n');
    return 0;
}
