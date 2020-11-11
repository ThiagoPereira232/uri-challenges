# -*- coding: utf-8 -*-

n = float(input())

print('NOTAS:')

n100 = n // 100
n = n - n100 * 100
print(f'{n100:.0f} nota(s) de R$ 100,00')

n50 = n // 50
n = n - n50 * 50
print(f'{n50:.0f} nota(s) de R$ 50,00')

n20 = n // 20
n = n - n20 * 20
print(f'{n20:.0f} nota(s) de R$ 20,00')

n10 = n // 10
n = n - n10 * 10
print(f'{n10:.0f} nota(s) de R$ 10,00')

n5 = n // 5
n = n - n5 * 5
print(f'{n5:.0f} nota(s) de R$ 5,00')

n2 = n // 2
n = n - n2 * 2
print(f'{n2:.0f} nota(s) de R$ 2,00')

print('MOEDAS:')

m1 = n // 1
n = n - m1 * 1
print(f'{m1:.0f} moeda(s) de R$ 1,00')

m50 = n // 0.5
n = n - m50 * 0.5
print(f'{m50:.0f} moeda(s) de R$ 0,50')

m25 = n // 0.25
n = n - m25 * 0.25
print(f'{m25:.0f} moeda(s) de R$ 0,25')

m10 = n // 0.1
n = n - m10 * 0.1
print(f'{m10:.0f} moeda(s) de R$ 0,10')

m5 = n // 0.05
n = n - m5 * 0.05
print(f'{m5:.0f} moeda(s) de R$ 0,05')

m01 = n // 0.01
n = n - m01 * 0.01
print(f'{m01:.0f} moeda(s) de R$ 0,01')
