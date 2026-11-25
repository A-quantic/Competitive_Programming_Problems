# Trabajo Final — Fundamentos de Programación Competitiva (1ACC0217)

Universidad Peruana de Ciencias Aplicadas · Ciclo 2026-02

**Integrantes**
- Jose Emanuel Amaro Saravia (U20241C247)
- Juan Diego Bismarck Aquino (U202412941)

Quince problemas de nivel Medium o Hard resueltos en C++17, agrupados por los temas del curso.
Cada solución incluye su proyecto de Visual Studio 2022, ejemplos de prueba y una figura explicativa.

## Problemas

| # | Tema | Problema | Plataforma | Dificultad | Responsable |
|---|------|----------|-----------|-----------|-------------|
| P01 | Map | [Time Based Key-Value Store](https://leetcode.com/problems/time-based-key-value-store/) | LeetCode 981 | Medium | Jose Amaro |
| P02 | Map | [My Calendar II](https://leetcode.com/problems/my-calendar-ii/) | LeetCode 731 | Medium | Jose Amaro |
| P03 | KMP | [Shortest Palindrome](https://leetcode.com/problems/shortest-palindrome/) | LeetCode 214 | Hard | Jose Amaro |
| P04 | KMP | [Password](https://codeforces.com/problemset/problem/126/B) | Codeforces 126B | Rating 1700 | Jose Amaro |
| P05 | Algoritmo Z | [Sum of Scores of Built Strings](https://leetcode.com/problems/sum-of-scores-of-built-strings/) | LeetCode 2223 | Hard | Jose Amaro |
| P06 | Algoritmo Z | [Prefixes and Suffixes](https://codeforces.com/problemset/problem/432/D) | Codeforces 432D | Rating 2000 | Jose Amaro |
| P07 | Segment Tree | [Handling Sum Queries After Update](https://leetcode.com/problems/handling-sum-queries-after-update/) | LeetCode 2569 | Hard | Jose Amaro |
| P08 | Segment Tree | [Booking Concert Tickets in Groups](https://leetcode.com/problems/booking-concert-tickets-in-groups/) | LeetCode 2286 | Hard | Juan Diego Bismarck |
| P09 | Árbol de Fenwick | [Count of Smaller Numbers After Self](https://leetcode.com/problems/count-of-smaller-numbers-after-self/) | LeetCode 315 | Hard | Juan Diego Bismarck |
| P10 | Árbol de Fenwick | [Count Good Triplets in an Array](https://leetcode.com/problems/count-good-triplets-in-an-array/) | LeetCode 2179 | Hard | Juan Diego Bismarck |
| P11 | Árbol ternario | [Design Add and Search Words Data Structure](https://leetcode.com/problems/design-add-and-search-words-data-structure/) | LeetCode 211 | Medium | Jose Amaro |
| P12 | Trie | [Maximum XOR of Two Numbers in an Array](https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/) | LeetCode 421 | Medium | Juan Diego Bismarck |
| P13 | Trie | [Concatenated Words](https://leetcode.com/problems/concatenated-words/) | LeetCode 472 | Hard | Juan Diego Bismarck |
| P14 | Programación dinámica | [Burst Balloons](https://leetcode.com/problems/burst-balloons/) | LeetCode 312 | Hard | Juan Diego Bismarck |
| P15 | Programación dinámica | [Edit Distance](https://leetcode.com/problems/edit-distance/) | LeetCode 72 | Medium | Juan Diego Bismarck |

## Estructura

```
TrabajoFinal-1ACC0217/
├── TrabajoFinal_1ACC0217.sln      # solución de Visual Studio 2022 con los 15 proyectos
├── codigos/
│   ├── 01_map/                     # P01, P02
│   ├── 02_kmp/                     # P03, P04
│   ├── 03_z/                       # P05, P06
│   ├── 04_segment_tree/            # P07, P08
│   ├── 05_fenwick/                 # P09, P10
│   ├── 06_arbol_ternario/          # P11
│   ├── 07_trie/                    # P12, P13
│   └── 08_programacion_dinamica/   # P14, P15
│       └── Pxx_.../                # .cpp + .vcxproj + .sln propio
├── pruebas/
│   ├── validar.py                  # compila todo y verifica los ejemplos
│   └── ejemplos/                   # Pxx_k.in / Pxx_k.out
├── figuras/
│   ├── generar_figuras.py          # regenera las 15 figuras (matplotlib)
│   └── png/                        # p01.png ... p15.png
└── docs/
    └── Informe_Trabajo_Final_1ACC0217.docx
```

## Cómo compilar y ejecutar

**Visual Studio 2022:** abrir `TrabajoFinal_1ACC0217.sln` (o el `.sln` de un ejercicio), clic derecho en el
proyecto → *Establecer como proyecto de inicio* → `Ctrl + F5`, y escribir la entrada en la consola.

**g++:**

```bash
g++ -std=c++17 -O2 -Wall -Wextra -o p01 codigos/01_map/P01_LC981_TimeBasedKeyValueStore/P01_LC981_TimeBasedKeyValueStore.cpp
./p01 < pruebas/ejemplos/P01_1.in
```

**Pruebas automáticas** (compila los 15 y compara los 30 ejemplos):

```bash
python3 pruebas/validar.py
```

El formato de entrada y salida de cada programa está en el comentario inicial de su `.cpp`.
En LeetCode se envía solo la clase o función; el `main()` es el arnés local de pruebas.

## Figuras

Cada figura explica un ejercicio paso a paso con su ejemplo. Para regenerarlas:

```bash
pip install matplotlib
python3 figuras/generar_figuras.py
```
