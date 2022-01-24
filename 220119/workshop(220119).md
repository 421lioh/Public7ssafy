## 1. List의 합 구하기


```python
lst =[([1, 2, 3, 4, 5])]

def list_sum(numbers):
    sum_value = 0
    for number in numbers:
        sum_value += number
    return sum_value

```

## 2. Dictionary로 이루어진 List의 합 구하기


```python
dic_1 = {'name': 'kim', 'age': 12}
dic_2 = {'name': 'lee', 'age': 4}

def dict_list_sum(infos):
    age_sum = 0
    for info in infos:
        age_sum += info['age']
    return age_sum


```

## 3. 2차원 리스트 전체 합


```python
def all_list_sum(numbers):
    list_sum = 0
    for number in numbers:
        for num in number:
            list_sum += num
        return list_sum
    
print(all_list_sum([[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]]))
```

    1
    

## 4. 숫자의 의미


```python
def get_secret_word(numbers):
    word = ''
    for number in numbers:
        word += chr(number)
    return word

print(get_secret_word([83, 115, 65, 102, 89]))
```

    SsAfY
    

## 5. 내 이름의 합


```python
def get_secret_number(word):
    hap = 0
    
    for char in word:
        hap += ord(char)
        
    return hap

print(get_secret_number('tom'))
```

    336
    

## 6. 강한 이름


```python
def get_strong_word(word1, word2):
    word1_sum = 0
    word2_sum = 0
    
    for char in word1:
        word1_sum += ord(char)
        
    for char in word2:
        word2_sum += ord(char)
        
    if word1_sum > word2_sum:
        return word1
    else:
        return word2
    
print(get_strong_word('tom', 'john'))
```

    john
    


```python

```
