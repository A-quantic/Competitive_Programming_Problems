/*
 * Problema 7 - Tema: Segment Tree (con propagacion lazy)
 * LeetCode 2569. Handling Sum Queries After Update
 * https://leetcode.com/problems/handling-sum-queries-after-update/
 *
 * Observacion: la consulta tipo 2 solo necesita C = (numero de unos en nums1). Por tanto
 * se mantiene sum(nums2) como un acumulador y un Segment Tree sobre nums1 que soporta:
 *   - actualizacion de rango: invertir bits en [l, r]   (lazy: bandera "flip")
 *   - consulta de rango: cantidad de unos en [l, r]
 * Tipo 1 -> flip(l, r); Tipo 2 -> suma += p * unos(0, n-1); Tipo 3 -> responder suma.
 * Magnitud maxima: p*C*q <= 10^6 * 10^5 * 10^5 = 10^16 -> long long.
 *
 * Compilar : g++ -std=c++17 -O2 -Wall -Wextra -o p07 P07_LC2569_HandlingSumQueriesAfterUpdate.cpp
 * Formato local: n / nums1 (n enteros) / nums2 (n enteros) / q / q lineas "t a b".
 * Salida: respuestas de las consultas tipo 3, separadas por espacios, en una linea.
 */
#include <iostream>
#include <vector>

using namespace std;

class SegmentTreeFlip {
    int n;
    vector<int> unos;    // unos[nodo] = cantidad de unos en el intervalo del nodo
    vector<char> flip;   // flip[nodo] = 1 si el intervalo hijo esta pendiente de inversion

    void construir(int nodo, int lo, int hi, const vector<int>& a) {
        if (lo == hi) { unos[nodo] = a[lo]; return; }
        int mid = (lo + hi) / 2;
        construir(2 * nodo, lo, mid, a);
        construir(2 * nodo + 1, mid + 1, hi, a);
        unos[nodo] = unos[2 * nodo] + unos[2 * nodo + 1];
    }
    void aplicar(int nodo, int lo, int hi) {   // invierte todo el intervalo del nodo
        unos[nodo] = (hi - lo + 1) - unos[nodo];
        flip[nodo] ^= 1;
    }
    void empujar(int nodo, int lo, int hi) {   // propaga la bandera a los hijos
        if (!flip[nodo]) return;
        int mid = (lo + hi) / 2;
        aplicar(2 * nodo, lo, mid);
        aplicar(2 * nodo + 1, mid + 1, hi);
        flip[nodo] = 0;
    }
    void invertir(int nodo, int lo, int hi, int l, int r) {
        if (r < lo || hi < l) return;
        if (l <= lo && hi <= r) { aplicar(nodo, lo, hi); return; }
        empujar(nodo, lo, hi);
        int mid = (lo + hi) / 2;
        invertir(2 * nodo, lo, mid, l, r);
        invertir(2 * nodo + 1, mid + 1, hi, l, r);
        unos[nodo] = unos[2 * nodo] + unos[2 * nodo + 1];
    }
    int contar(int nodo, int lo, int hi, int l, int r) {
        if (r < lo || hi < l) return 0;
        if (l <= lo && hi <= r) return unos[nodo];
        empujar(nodo, lo, hi);
        int mid = (lo + hi) / 2;
        return contar(2 * nodo, lo, mid, l, r) + contar(2 * nodo + 1, mid + 1, hi, l, r);
    }

public:
    explicit SegmentTreeFlip(const vector<int>& a)
        : n(static_cast<int>(a.size())), unos(4 * a.size(), 0), flip(4 * a.size(), 0) {
        construir(1, 0, n - 1, a);                      // O(n)
    }
    void invertir(int l, int r) { invertir(1, 0, n - 1, l, r); }   // O(log n)
    int contar(int l, int r) { return contar(1, 0, n - 1, l, r); } // O(log n)
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<int> nums1(n);
    for (int& x : nums1) cin >> x;
    long long suma = 0;
    for (int i = 0; i < n; ++i) { long long v; cin >> v; suma += v; }

    SegmentTreeFlip st(nums1);
    int q;
    cin >> q;
    bool primero = true;
    while (q--) {
        long long t, a, b;
        cin >> t >> a >> b;
        if (t == 1) {
            st.invertir(static_cast<int>(a), static_cast<int>(b));
        } else if (t == 2) {
            suma += a * st.contar(0, n - 1);
        } else {
            if (!primero) cout << ' ';
            cout << suma;
            primero = false;
        }
    }
    cout << '\n';
    return 0;
}
