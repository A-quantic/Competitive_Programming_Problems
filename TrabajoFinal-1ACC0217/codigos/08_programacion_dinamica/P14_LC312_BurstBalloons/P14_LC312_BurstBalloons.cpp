/*
 * Problema 14 - Tema: Programacion Dinamica (DP sobre intervalos)
 * LeetCode 312. Burst Balloons
 * https://leetcode.com/problems/burst-balloons/
 *
 * Se agregan centinelas arr[0] = arr[n+1] = 1.
 * ESTADO     : f[i][j] = maximas monedas al explotar TODOS los globos estrictamente entre i y j.
 * RECURRENCIA: sea k el ULTIMO globo que explota en (i, j); en ese momento sus vecinos son i y j:
 *              f[i][j] = max_{i<k<j} ( f[i][k] + f[k][j] + arr[i]*arr[k]*arr[j] )
 * CASO BASE  : f[i][i+1] = 0 (no hay globos entre i e i+1).
 * ORDEN      : por longitud creciente del intervalo (j - i), de 2 a n+1.
 * RESPUESTA  : f[0][n+1].
 *
 * Compilar : g++ -std=c++17 -O2 -Wall -Wextra -o p14 P14_LC312_BurstBalloons.cpp
 * Formato local: n / n enteros.   Salida: el maximo de monedas.
 */
#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

long long maxCoins(const vector<int>& nums) {
    int n = static_cast<int>(nums.size());
    vector<long long> arr(n + 2, 1);
    for (int i = 0; i < n; ++i) arr[i + 1] = nums[i];

    vector<vector<long long>> f(n + 2, vector<long long>(n + 2, 0));  // f[i][i+1] = 0
    for (int longitud = 2; longitud <= n + 1; ++longitud) {
        for (int i = 0; i + longitud <= n + 1; ++i) {
            int j = i + longitud;
            for (int k = i + 1; k < j; ++k)          // k = ultimo globo en explotar
                f[i][j] = max(f[i][j], f[i][k] + f[k][j] + arr[i] * arr[k] * arr[j]);
        }
    }
    return f[0][n + 1];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<int> nums(n);
    for (int& x : nums) cin >> x;
    cout << maxCoins(nums) << '\n';
    return 0;
}
