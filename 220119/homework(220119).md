## 1. Built-in 함수

input() set() str() sum() max() 등등


```python
dir(__builtins__)
#을 통해 종류 확인가능
```

## 2. 정중앙 문자


```python
s = str(input())
def get_middle_char(s):

    return s[(len(s)-1)//2:len(s)//2+1]

print(get_middle_char(s))

```

    we
    

## 3. 위치인자와 키워드 인자


```python
def ssafy(name, location='서울'):
    print(f'{name}의 지역은 {location}입니다.')

ssafy('허준')
ssafy(location='대전', name='철수')
ssafy('영희', location='광주')
# 오류 없음
ssafy(name='길동', '구미')
# 오류 발생
```

    허준의 지역은 서울입니다.
    철수의 지역은 대전입니다.
    영희의 지역은 광주입니다.
    

## 4. 나의 반환값은


```python
def my_func(a, b):
    c = a + b
    print(c)

result = my_func(3, 7)
```

    10
    

## 5. 가변 인자 리스트


```python
def my_avg(*nums):
    sum = 0
    for n in nums:
        sum += n
    my_avg = sum/len(nums)
    print(my_avg)

my_avg(77, 83, 95, 80, 70)
```

    81.0
    

## 6.  이름공간


```python
지역 네임스페이스 < 전역 네임스페이스 < 빌트인 네임스페이스
```

## 7. 매개변수와 인자, 반환


```python
(1) 함수는 오직 하나의 객체만 반환할 수 있으므로 'return a, b'와
같이 쓸 수 없다.
(2) 함수에서 return을 작성하지 않으면 None 값을 반환한다.
(3) 함수의 매개변수(parameter)는 함수를 선언할 때 설정한 값이며,
전달 인자(argument)는 함수를 호출할 때 넘겨주는 값이다.
(4) 가변 인자를 설정할 때는 함수 선언 시 매개변수 앞에 * 을 붙이고, 
이 때는 함수내에서 tuple로 처리 된다.

(1)
```

## 8. 재귀함수


```python
재귀함수는 변수를 여러 개 만들 필요 없이 코드가 간결해진다. 그러나 많은 메모리 사용과 함께 속도가 느리다. 
반복문은 속도가 빠르지만 변수를 여러 개 설정해야하며 코드가 길다.
```
