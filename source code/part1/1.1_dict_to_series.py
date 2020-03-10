﻿# -*- coding: utf-8 -*-

# pandas 불러오기 
import pandas as pd

# k:v 구조를 갖는 딕셔너리를 만들고, 변수 dict_data에 저장
dict_data = {'a': 1, 'b': 2, 'c': 3}

# 판다스 Series() 함수로 딕셔너리(dict_data)를 시리즈로 변환. 변수 sr에 저장 
sr = pd.Series(dict_data)

# 변수 sr의 자료형 출력
print(type(sr))
print('\n')

# 변수 sr에 저장되어 있는 시리즈 객체를 출력
print(sr)

# dtype:int 64 => 시리즈를 구성하는 데이터값의 자료형(dtype)은 정수형(int64)이다.

print(sr[0])
print(sr[1])
print(sr[2])
print('=======\n')
print(sr.a)
print(sr.b)
print(sr.c)