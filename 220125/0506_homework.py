# 1. 모음 count

def count_vowels(words):
    vowels = 'aeiou'
    result = 0
    for vowel in vowels:
        result += words.count(vowel)
    return result

print(count_vowels('apple'))
print(count_vowels('banana'))

# 2. 문자열 조작
4


# 3. 
def only_square_area(widths, heights):
    p_square = []

    for width in widths:
        for height in heights:
            if width == height:
                p_square.append(width * height)
    return p_square

print(only_square_area([32, 55, 63], [13, 32, 40, 55]))

# 4.
numbers = [3, 10, 1, 15, 6]
a = numbers.sort()
b = sorted(numbers)
print(a)
print(b)

# 5.
gambles = ['go', 'stop', 'double']
   
gambles.extend('check')

print(gambles) # ['go', 'stop', 'double', 'c', 'h', 'e', 'c', 'k']

gambles.append('check')
   
print(gambles) # ['go', 'stop', 'double', 'c', 'h', 'e', 'c', 'k', 'check']

# 6.
a = [1, 2, 3, 4, 5]
b = a

a[2] = 5 

print(a)
print(b)

# 를 수행할때 [1, 2, 5, 4, 5]가 요구사항에 맞게 똑같이 나옴
