# 1. pip

# (2)git bash에서 (1)faker를 설치

# 2. Bagic Usages

from faker import Faker # 클래스 Faker를 faker에서 가져옴
fake = Faker() # fake는 Faker의 인스턴스 
fake.name() # .name 메서드

# 3. 
#(a) init
#(b) self
#(c) locale='en_US'

# 4.

# seed는 클래스메서드, seed_instance는 인스턴스 메서드

# 5.

#1: 이도윤
#2: 박예준, 최건우 등 랜덤으로 결과가 계속 변함
#seed_instance()는 인스턴스 메소드(인스턴스 fake에 .seed_instance()를 호출했기 때문)
#seed()는 클래스에 속하는 모든 인스턴스에 영향을 주는 용도로 쓰일 수 있고,
#seed_instance()는 해당 인스턴스에만 영향을 주는 용도로 쓰일 수 있다.