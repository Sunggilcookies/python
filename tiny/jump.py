import argparse

def get_args():
    parser = argparse.ArgumentParser(
        description="Jump the Five",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    # 명령행 인수 : -n(축약형), --name
    parser.add_argument('text',
                        metavar='str', #인수를 1개 이상 전달함
                        help='Input text')

    return parser.parse_args() # 명령줄 인수를 반환

def main():
    args = get_args()
    # print(args.text)
    jumper = {'1':'9','2':'8','3':'7','4':'6','5':'0','6':'4','7':'3','8':'2','9':'1','0':'5'}

    for char in args.text:
        print(jumper.get(char, char), end='')
    '''
# 새로운 문자열 만들기
    new_text = ''
    for char in text:
        new_text = new_text + jumper.get(char, char)
    print(new_text)
    
# 2. 새로운 리스트 마늗ㄹ기
    new_text = []
    for char in text:
        new_text.append(jumper.get(char, char))
    print(''.join(new_text))
    
# 3. 리스트 내포로 만들기
    new_text = []
    for char in text:
        new_text.append(jumper.get(char, char))

    print(''.join(new_text))
    '''
# 방법 4 - 리스트 내포
#     print(''.join([jumper.get(char, char) for char in args.text]))



if __name__=="__main__":
    main()