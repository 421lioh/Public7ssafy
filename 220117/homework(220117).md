```python
# 220117 homework

## Python 01. 데이터 & 제어문

### 1. 파이썬 예약어

import keyword
print(keyword.kwlist)

```

    ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
    


```python
### 2. 실수 비교

num1 = 0.1 * 3
num2 = 0.3

abs(num1 - num2) <= 1e-10
```




    True




```python
### 3. 이스케이프 시퀀스

'\\n'
'\\t'
'\\\\'

```


```python
### 4. String Interpolation

name = '철수'
f'안녕, {name}야'


```




    '안녕, 철수야'




```python
### 5. 형 변환

str(1)


```




    '1'




```python
int('30')
```




    30




```python
int(5)
```




    5




```python
bool('50')
```




    True




```python
int('3.5')

#오류 발생 코드
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    Input In [14], in <module>
    ----> 1 int('3.5')
    

    ValueError: invalid literal for int() with base 10: '3.5'



```python
### 6. 네모 만들기

for i in range(9):           
    for j in range(5):      
        print('*', end='')  
    print()        
```

    *****
    *****
    *****
    *****
    *****
    *****
    *****
    *****
    *****
    


```python
### 7.

print('\"파일은 c: \\WIndows\\Users\\내문서\\Python에 저장이 되었습니다." 나는 생각했다. \'cd를 써서 git bash로 들어가 봐야지.\'')
```

    "파일은 c: \WIndows\Users\내문서\Python에 저장이 되었습니다." 나는 생각했다. 'cd를 써서 git bash로 들어가 봐야지.'
    


```python
### 8.


   (-b + (b**2 - 4*a*c)**(1/2)) / (2*a)
   (-b - (b**2 - 4*a*c)**(1/2)) / (2*a)
   ```

```


```python
## Python 02. 데이터 & 제어문
```


```python
### 1. Mutable & Immutable

Mutable : List, set, dictionary
Immutable : String, Tuple, Range
```


```python
### 2. 홀수만 담기

list(range(1,50)[0:50:2])
```




    [1,
     3,
     5,
     7,
     9,
     11,
     13,
     15,
     17,
     19,
     21,
     23,
     25,
     27,
     29,
     31,
     33,
     35,
     37,
     39,
     41,
     43,
     45,
     47,
     49]




```python
### 3. Dictionary 만들기

```


```python
stu_list = {'기안': '84', '메시': '87'}
stu_list.keys()

```




    dict_keys(['기안', '메시'])




```python
stu_list.values()
```




    dict_values(['84', '87'])




```python
stu_list.items()
```




    dict_items([('기안', '84'), ('메시', '87')])




```python
### 4. 반복문으로 네모 출력
```


```python
for i in range(9):           
    for j in range(5):      
        print('*', end='')  
    print()                   
```

    *****
    *****
    *****
    *****
    *****
    *****
    *****
    *****
    *****
    


```python
### 5. 조건 표현식

temp = 36.5
print('입실 불가') if temp >= 37.5 else print('입실 가능')
```


```python
### 6. 평균 구하기 ??
scores = [80, 89, 99, 83]
print(sum(scores) / len(scores))
```




    87.75




```python

```
