## 1. Type Class
# int, float, str, dict, set 등등

## 2. Magic Method
# __init__ 인스턴스 객체가 생성될 때 자동으로 호출되는 함수
# __del__  인스턴스 객체가 소멸(파괴)되기 직전에 자동으로 호출되는 함수
# __str__ 특정 객체를 출력(print()) 할 때 보여줄 내용을 정의
# __repr__ 객체를 따옴표를 사용하며 공식적으로 출력

## 3. Instance Method


- list - # .sort(), .append()
- str - # .upper(), .lower(), `.isalpha()
- dict - # .get(), .update()


## 4. Module Import

# fibo.py
def fibo_recursion(n):
    if n < 2:
        return n
    else:
        return fibo_recursion(n-1) + fibo_recursion(n-2)

from (a) import (b) as (c))

(a) : fibo
(b) : fibo_recursion
(c) : recursion

recursion(4)