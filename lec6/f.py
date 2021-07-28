def CheckRange(r1, r2, n):
    if r1 <= n <= r2:
        print(f'{n} in range [{r1}, {r2}]')
        return
    else:
        print(f'{n} not in range [{r1}, {r2}]')
        return

r1, r2 = input('Enter range: ').split()
num = int(input('Enter num: '))
CheckRange(int(r1), int(r2), num)