#!/usr/bin/env python3
"""Compila los 15 ejercicios con g++ y verifica los ejemplos de pruebas/ejemplos/.

Uso (desde la raiz del repositorio):
    python3 pruebas/validar.py
Requiere g++ con soporte de C++17.
"""
import glob
import os
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BIN = os.path.join(RAIZ, "build")
os.makedirs(BIN, exist_ok=True)

fuentes = sorted(glob.glob(os.path.join(RAIZ, "codigos", "*", "*", "*.cpp")))
binarios = {}
for f in fuentes:
    nombre = os.path.basename(f)[:3]  # P01, P02, ...
    salida = os.path.join(BIN, nombre + (".exe" if os.name == "nt" else ""))
    r = subprocess.run(["g++", "-std=c++17", "-O2", "-Wall", "-Wextra", "-o", salida, f],
                       capture_output=True, text=True)
    estado = "OK" if r.returncode == 0 and not r.stderr.strip() else "ADVERTENCIAS/ERROR"
    print(f"[compilar] {os.path.basename(f):50s} {estado}")
    if r.returncode != 0:
        print(r.stderr)
        sys.exit(1)
    binarios[nombre] = salida

ok = total = 0
for entrada in sorted(glob.glob(os.path.join(RAIZ, "pruebas", "ejemplos", "*.in"))):
    caso = os.path.basename(entrada)[:-3]
    esperado = open(entrada[:-3] + ".out", encoding="utf-8").read().split("\n")
    with open(entrada, encoding="utf-8") as fin:
        r = subprocess.run([binarios[caso[:3]]], stdin=fin, capture_output=True, text=True)
    obtenido = [l.rstrip() for l in r.stdout.rstrip("\n").split("\n")]
    esperado = [l.rstrip() for l in "\n".join(esperado).rstrip("\n").split("\n")]
    total += 1
    if obtenido == esperado:
        ok += 1
        print(f"[ejemplo]  {caso:10s} OK")
    else:
        print(f"[ejemplo]  {caso:10s} FALLA\n  esperado: {esperado}\n  obtenido: {obtenido}")
print(f"\n{ok}/{total} ejemplos correctos")
sys.exit(0 if ok == total else 1)
