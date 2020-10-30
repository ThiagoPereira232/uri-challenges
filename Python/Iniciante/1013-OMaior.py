# -*- coding: utf-8 -*-

a, b, c = [int(x) for x in input().split()]

x = (a + b + abs(a - b))/2
maiorXC = (x + c + abs(x - c))/2

print('{:.0f} eh o maior'.format(maiorXC))
