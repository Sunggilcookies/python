import argparse

def get_args():
    parser = argparse.ArgumentParser(
        description="Picnic Game",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    # 명령행 인수 : -n(축약형), --name
    parser.add_argument('item',
                        metavar='str',
                        nargs='+', #인수를 1개 이상 전달함
                        help='item(s) to bring')
    parser.add_argument('-s',
                        '--sorted',
                        action='store_true',  # 인수를 1개 이상 전달함
                        help='Sort the items')

    return parser.parse_args() # 명령줄 인수를 반환

def main():
    args = get_args()
    items = args.item # 리스트
    # print(args.word)
    num = len(items) # 아이템의개수

    #정렬 기능 구현
    if args.sorted:
        items.sort()


    bringing = ''
    if num == 1: #글자가 한개면
        bringing = items[0]
    elif num == 2: #글자가 두개면 and 붙임
        bringing = ' and '.join(items)
    else:   #쉼표로 나누고 마지막에 and 붙임
        items[-1] = ' and ' + items[-1]
        bringing = ', '.join(items)

    print('You are bringing {}.'.format(bringing))


if __name__ == "__main__":
    main()