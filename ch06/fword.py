#영어 단어장 만들기
import random

try:
    word = ['ant', 'bear', 'chicken', 'deer', 'fox', 'elephant','horse', 'lion','monkey','penguin']
    with open("./output/word.txt",'w') as f:
        for i in word:
            if i == word[-1]:
                f.write(i)
            else:
                f.write(i + " ")
    f.close()
except FileNotFoundError:
    print("안돼")
try:
    with open("./output/word.txt", 'r') as f:
        data = f.read().split() #공백문자로 구분 - 리스트로 변환
        # word = random.choice(data)
        print(word)

except FileNotFoundError:
    print("다메요")

