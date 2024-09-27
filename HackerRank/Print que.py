if __name__ == '__main__':
    n = int(input())

    lis = []
    for i in range(1, n+1):
        lis.append(i)

    print(*lis, sep='')
