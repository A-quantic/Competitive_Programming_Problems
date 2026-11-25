/*
 * Problema 10 - Tema: Arbol Fenwick (Binary Indexed Tree)
 * LeetCode 2179. Count Good Triplets in an Array
 * https://leetcode.com/problems/count-good-triplets-in-an-array/
 *
 * Sea a[i] = posicion en nums2 del valor nums1[i] (a es una permutacion de 0..n-1).
 * Una terna (x, y, z) es buena si sus posiciones crecen en ambos arreglos, es decir, si
 * existen i < j < k con a[i] < a[j] < a[k]. Fijando y = nums1[j]:
 *   left[j]  = #{ i < j : a[i] < a[j] }                  -> Fenwick (prefijo)
 *   right[j] = #{ k > j : a[k] > a[j] }
 *            = (n - 1 - a[j]) - (j - left[j])            (los mayores en total menos los ya vistos)
 * Respuesta = sum_j left[j] * right[j]   (hasta ~ n^3/27 -> long long).
 *
 * Compilar : g++ -std=c++17 -O2 -Wall -Wextra -o p10 P10_LC2179_CountGoodTripletsInAnArray.cpp
 * Formato local: n / nums1 / nums2.   Salida: el numero de ternas buenas.
 */
#include <iostream>
#include <vector>

using namespace std;

class Fenwick {
    int n;
    vector<int> bit;
    static int lowbit(int i) { return i & -i; }

public:
    explicit Fenwick(int n) : n(n), bit(n + 1, 0) {}
    void update(int i, int delta) {
        for (; i <= n; i += lowbit(i)) bit[i] += delta;
    }
    int query(int i) const {
        int suma = 0;
        for (; i > 0; i -= lowbit(i)) suma += bit[i];
        return suma;
    }
};

long long goodTriplets(const vector<int>& nums1, const vector<int>& nums2) {
    int n = static_cast<int>(nums1.size());
    vector<int> pos2(n);
    for (int i = 0; i < n; ++i) pos2[nums2[i]] = i;

    Fenwick fw(n);
    long long total = 0;
    for (int j = 0; j < n; ++j) {
        int a = pos2[nums1[j]];                    // posicion en nums2 (0-based)
        long long left = fw.query(a);              // vistos con posicion < a (indices 1..a)
        long long right = (n - 1 - a) - (j - left);
        total += left * right;
        fw.update(a + 1, 1);                       // Fenwick es 1-indexado
    }
    return total;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<int> nums1(n), nums2(n);
    for (int& x : nums1) cin >> x;
    for (int& x : nums2) cin >> x;
    cout << goodTriplets(nums1, nums2) << '\n';
    return 0;
}
