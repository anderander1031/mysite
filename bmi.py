def table():
    with open('bmi.txt') as f:
         first = f.readline()
         hs.first.split()
         fmt = '{:>10}{:>10}{:>10}{:>10}{:>10}{:>10}'
         print(fmt.format(hs[0], hs[1], hs[2], hs[3], 'BMI', 'MEMO'))
         print('-' * 60)
         for line in f:
             tks = line.strip().split()
             name, gender, h, w = tks[0], tks[1], float(tks[2]), float(tks[3])
             