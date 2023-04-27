#파일 쓰기

#파일 열기

#파일 쓰기
try:
    f = open("c:/pyfile/file1.txt", "w")
    f.write('hello\n')
    f.write('100') #숫자형은 문자형으로 변환
    n = 10 * 2
    f.write(str(n)+'\n')

    for i in range(1,11):
        text=f'{i}번째 줄입니다.\n'
        f.write(text)

#파일 종료
    f.close()
except:
    print("파일쓰기에 실패했습니다.")