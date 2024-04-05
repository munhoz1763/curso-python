n1 = int(input('qual numero voce quer ver a tabuada?: '))
multi = 0
cont = 10
for mult in range(cont):
    multi = multi + 1
    print('{} x {}: {}'.format(n1, multi, n1 * multi))
