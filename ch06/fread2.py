#season 파일 읽기

try:
    f = open("c:/pyfile/season.txt", 'r')

    data = f.read()
    print(data)


    f.close()
except FileNotFoundError:
    print("file x")