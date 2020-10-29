# -*- coding: utf-8 -*-

p1 = input().split(" ")
p2 = input().split(" ")

cod1, qtda1, valor1 = p1
cod2, qtda2, valor2 = p2

vl_pagar = (int(qtda1) * float(valor1)) + (int(qtda2) * float(valor2))

print(f'VALOR A PAGAR: R$ {vl_pagar:.2f}')
