/*
 * Problema 8 - Tema: Segment Tree (maximo + suma con descenso)
 * LeetCode 2286. Booking Concert Tickets in Groups (Hard)
 * https://leetcode.com/problems/booking-concert-tickets-in-groups/
 *
 * Sala con n filas de m asientos. libres[i] = asientos libres de la fila i (siempre
 * son los del final de la fila, porque se asigna de izquierda a derecha).
 *  - gather(k, maxRow): primera fila r <= maxRow con libres[r] >= k -> [r, m - libres[r]].
 *    Se obtiene descendiendo en un Segment Tree de MAXIMOS.
 *  - scatter(k, maxRow): si la SUMA de libres en [0, maxRow] es >= k, se ocupan asientos
 *    desde la fila de menor indice. Un puntero "primera fila no llena" evita recorrer
 *    filas ya llenas (cada fila se vacia una sola vez -> costo amortizado).
 *
 * Compilar : g++ -std=c++17 -O2 -Wall -Wextra -o p08 P08_LC2286_BookingConcertTickets.cpp
 * Formato local de E/S (en LeetCode solo se envia la clase BookMyShow):
 *   Linea 1 : n m q
 *   q lineas: "gather k maxRow" o "scatter k maxRow"
 *   Salida  : gather -> "fila asiento" o "[]";  scatter -> "true" o "false"
 */
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

class BookMyShow {
    int n;
    long long m;
    vector<long long> mx, sm;   // maximo y suma de asientos libres por nodo
    int primeraLibre = 0;       // filas < primeraLibre estan llenas

    void construir(int nodo, int l, int r) {
        if (l == r) { mx[nodo] = sm[nodo] = m; return; }
        int mid = (l + r) / 2;
        construir(2 * nodo, l, mid);
        construir(2 * nodo + 1, mid + 1, r);
        mx[nodo] = max(mx[2 * nodo], mx[2 * nodo + 1]);
        sm[nodo] = sm[2 * nodo] + sm[2 * nodo + 1];
    }
    void actualizar(int nodo, int l, int r, int pos, long long val) {
        if (l == r) { mx[nodo] = sm[nodo] = val; return; }
        int mid = (l + r) / 2;
        if (pos <= mid) actualizar(2 * nodo, l, mid, pos, val);
        else actualizar(2 * nodo + 1, mid + 1, r, pos, val);
        mx[nodo] = max(mx[2 * nodo], mx[2 * nodo + 1]);
        sm[nodo] = sm[2 * nodo] + sm[2 * nodo + 1];
    }
    // Primera fila en [l, r] ∩ [0, R] con libres >= k; -1 si no existe.
    int primeraConK(int nodo, int l, int r, int R, long long k) {
        if (l > R || mx[nodo] < k) return -1;
        if (l == r) return l;
        int mid = (l + r) / 2;
        int res = primeraConK(2 * nodo, l, mid, R, k);
        if (res != -1) return res;
        return primeraConK(2 * nodo + 1, mid + 1, r, R, k);
    }
    // Suma de libres en [0, R].
    long long sumaPrefijo(int nodo, int l, int r, int R) {
        if (l > R) return 0;
        if (r <= R) return sm[nodo];
        int mid = (l + r) / 2;
        return sumaPrefijo(2 * nodo, l, mid, R) + sumaPrefijo(2 * nodo + 1, mid + 1, r, R);
    }
    long long libres(int fila) {  // valor de la hoja
        int nodo = 1, l = 0, r = n - 1;
        while (l != r) {
            int mid = (l + r) / 2;
            if (fila <= mid) { nodo = 2 * nodo; r = mid; }
            else { nodo = 2 * nodo + 1; l = mid + 1; }
        }
        return mx[nodo];
    }

public:
    BookMyShow(int n_, int m_) : n(n_), m(m_), mx(4 * n_), sm(4 * n_) { construir(1, 0, n - 1); }

    vector<int> gather(int k, int maxRow) {
        int fila = primeraConK(1, 0, n - 1, maxRow, k);
        if (fila == -1) return {};
        long long lib = libres(fila);
        int asiento = (int)(m - lib);
        actualizar(1, 0, n - 1, fila, lib - k);
        return {fila, asiento};
    }

    bool scatter(int k, int maxRow) {
        if (sumaPrefijo(1, 0, n - 1, maxRow) < k) return false;
        long long resto = k;
        while (resto > 0) {
            long long lib = libres(primeraLibre);
            long long toma = min(lib, resto);
            actualizar(1, 0, n - 1, primeraLibre, lib - toma);
            resto -= toma;
            if (lib - toma == 0) ++primeraLibre;
        }
        return true;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m, q;
    if (!(cin >> n >> m >> q)) return 0;
    BookMyShow sala(n, m);
    while (q--) {
        string op;
        int k, maxRow;
        cin >> op >> k >> maxRow;
        if (op == "gather") {
            vector<int> r = sala.gather(k, maxRow);
            if (r.empty()) cout << "[]\n";
            else cout << r[0] << ' ' << r[1] << '\n';
        } else {
            cout << (sala.scatter(k, maxRow) ? "true" : "false") << '\n';
        }
    }
    return 0;
}
