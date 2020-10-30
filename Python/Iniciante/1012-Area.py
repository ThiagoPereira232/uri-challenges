# -*- coding: utf-8 -*-

a, b, c = [float(x) for x in input().split()]

tr = (a * c)/2
ci = 3.14159 * (c ** 2)
t = ( (a + b) * c )/2
q = b ** 2
r = a * b

print(
f'''TRIANGULO: {tr:.3f}
CIRCULO: {ci:.3f}
TRAPEZIO: {t:.3f}
QUADRADO: {q:.3f}
RETANGULO: {r:.3f}'''
      )
