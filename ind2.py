#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Вариант2
#В списке, состоящем из вещественных элементов, вычислить:
#1) сумму отрицательных элементов списка;
#2) произведение элементов списка, расположенных между максимальным и минимальным элементами.
#Упорядочить элементы списка по возрастанию.

import sys

if __name__ == '__main__':
    A = tuple(map(float, input("Ввод:" ).split()))
    B = list(A)
    rez = 0
# 1)
    for i in A:
        if i < 0:
            rez += i
    print("1)""%.2f" % rez)

# 2)
    S = []
    a_min = a_max = A[0]
    i_min = i_max = 0
    b = [abs(i) for i in B]
    for i, item in enumerate(b):
        if item < a_min:
            i_min, a_min = i, item
        if item >= a_max:
            i_max, a_max = i, item
    A_new = B[i_min:i_max+1]
    rez = 1
    for j in A_new:
        rez *= j
    print(rez)
    B.sort()
    print(tuple(B))

