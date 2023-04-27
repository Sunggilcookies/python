#입력 받아 파일 쓰기
# a모드 추가저장 가능함 (w모드 초기화 됌)
with open("./output/input2.txt",'w') as f:
    while True:
        text = input("저장할 내용을 입력해 주세요(종료-z) :")
        if text == 'z':
            break

        f.write(text)
        f.write('\n')
