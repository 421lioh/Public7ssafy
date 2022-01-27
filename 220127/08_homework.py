# 1. Circle 인스턴스 만들기

class Circle:
    pi = 3.14

    def __init__(self, r, x, y):
        self.r = r
        self.x = x
        self.y = y
    
    def area(self):
        return Circle.pi * self.r * self.r
    
    def circumference(self):
        return 2 * Circle.pi * self.r
    
    def center(self):
        return (self.x, self.y)
    
circle = Circle(3, 2, 4)

print(circle.area())
print(circle.circumference())

# 2. 개와 새는 동물이다

class Animal:
    def __init__(self, name):
        self.name = name
        
    def walk(self):
        print(f'{self.name}! 걷는다!')
        
    def eat(self):
        print(f'{self.name}! 먹는다!')
## 여기서 부터 작성
class Dog(Animal):

    def walk(self):
        print(f'{self.name}! 달린다!')
        
    def bark(self):
        print(f'{self.name}! 먹는다!')  
              
class Bird(Animal):
        
    def fly(self):
        print(f'{self.name}! 푸드덕!')
##
dog = Dog('멍멍이')
dog.walk()
dog.bark()

bird = Bird('구구')
bird.walk()
bird.eat()
bird.fly()

## 3. 오류 종류

ZeroDivisionError # 0으로 나눌때
NameError # 변수가 정의되지 않음
TypeError # 자료형 사용 잘못됨
IndexError # Index의 범위를 벗어남
KeyError # Key가 없거나 문제가 있음
ModuleNotFoundError # 모듈이 안보임
ImportError # Import 대상이 없는경우(?)