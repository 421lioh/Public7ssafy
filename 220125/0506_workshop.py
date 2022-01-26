## 1. 평균 점수 구하기

from ast import Continue


def get_dict_avg(student):
    scores = []
   
    for score in student.values():
       scores.append(score)
   
    result = sum(scores) / len(student)
    return result

print(get_dict_avg({'python' : 80, 'algorithm' : 90, 'django' : 89, 'web' : 83}))

## 2. 혈액형 분류하기

def count_blood(lst):

    dct = {'A': 0, 'B': 0, 'O':0, 'AB': 0}
    
    for item in lst:
        dct[item] += 1

    return dct

print(count_blood([
    'A', 'B', 'A', 'O', 'AB', 'AB',
    'O', 'A', 'B', 'O', 'B', 'AB',
]))


## 3. 무엇이 중복일까

def duplicated_letters(string):

    dct = {x:0 for x in set(string)}
    
    result = []
    
    for char in string:
        dct[char] += 1
    

    for key in dct.keys():
        if dct[key] >= 2:
            result.append(key)
    

    return sorted(result)

print(duplicated_letters('apple'))
print(duplicated_letters('banana'))

## 4. 소대소대

def low_and_up(word):
    sodae = ''
    for idx, char in enumerate(word):
        if idx % 2 == 0:
            sodae += char.lower()
        else:
            sodae += char.upper()
    return sodae

print(low_and_up('apple'))
print(low_and_up('banana'))

## 5. 솔로 천국
def lonely(lst):
    # 리스트 result 초기화
    result = []
    
    # range와 len 함수를 사용해 전달 받은 리스트 lst의 길이를 구하고
    # 0부터 길이-1까지의 숫자를 하나씩 사용해 반복
    for i in range(len(lst)):
        # 만약 i가 0이라면, 즉 첫 번째 반복이라면
        if i == 0:
            result.append(lst[i])

        else:
            if lst[i-1] == lst[i]:
                pass

            else:
                result.append(lst[i])
                

    return result

print(lonely([1, 1, 3, 3, 0, 1, 1]))
print(lonely([4, 4, 4, 3, 3]))
