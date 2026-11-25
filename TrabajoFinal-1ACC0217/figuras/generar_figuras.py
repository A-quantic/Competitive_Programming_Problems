#!/usr/bin/env python3
"""Genera las 15 figuras explicativas (figuras/png/p01.png ... p15.png).
Requiere: pip install matplotlib
"""
import os, runpy
AQUI = os.path.dirname(os.path.abspath(__file__))
for i in range(1, 6):
    runpy.run_path(os.path.join(AQUI, f"figuras_parte{i}.py"), run_name="__main__")
print("Figuras generadas en", os.path.join(AQUI, "png"))
