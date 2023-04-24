#import Student2
#import 모듈이름
import Student as student

from Student2 import Student
#form 모듈이름 import 클래스 이름

"""
st1 = Student('이셋',3)
st1.info()
"""

#객체 리스트 생성
student= [
    Student("김하나", 1),
    Student("박둘", 2),
    Student("이셋", 3)

]
# 특정한 학생
print(student[0])
print(student[1])
# 전체 조회
# for i in s:
#     print[i]

for i in student:
 print(i)