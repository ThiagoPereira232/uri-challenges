# -*- coding: utf-8 -*-

n = int(input())

a = n // 365
n = n - a * 365

m = n // 30
n = n - m * 30

print(f'''{a} ano(s)
{m} mes(es)
{n} dia(s)''')
