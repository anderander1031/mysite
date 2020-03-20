def for_loop():
    for i in range(1, 6):
        print(i)

for_loop()

def pr_nums(n):
    for i in range(0, n+1):
        print(i, end=" ")
    print()

def pr_range(a, b):
    for i in range(a, b):
        print(i, end=" ")
    print()

    def pr_odds(n):
        x =1
        for i in range(n):
            print(x, end=" ")
            x += 2
        print()

    pr_ood(5)

    pr_odds(5)

    def pr_odds2(n):
        for i in range(n):
            print(i*2+1, end=" ")
        print()

    pr_odds2(5)

    def pr_odds3(n):
        for i in range(1, 2*n, 2):
            =print(i, ends=" ")
        print()

    pr_odd3(n)

def rect_for(m, n, ch):
    for i in range(m):
        for j in range(n):
            print(ch, end=" ")
        print()
rect_for(3, 5, '$')

def rect_while(m, n, ch):
    i = 0
    while i < m:
        j = 0
        while j < n:
            print(ch, end=" ")
            j += 1
        print()
        i += 1
rect_while(3, 5, '$')

def rect_str(m, n, ch):
    for i in range(m):
        print((ch+" ") * n)
rect_str(3, 5, '$')

def frame(m, n, ch='*'):
    for i in range(n):
        print(" ", ends="")
    print(ch)

frame(5, 6, '#')
frame(7, 15, '@')

def square_numbers(n):
    i= 1
    while i < n:
        print(i,end=" ")
        i += 1
        print()

square_numbers(25)

def pr_digits(n):
    while n > 100:
        print(n % 10, end= " ")
        n = n / 10
    print()

pr_digits(5764)
pr_digits(123456)