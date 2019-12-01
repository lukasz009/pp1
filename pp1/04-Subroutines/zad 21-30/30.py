from functions import losuj

nums = []
odds = 0
evens = 0
N = 1000

for i in range(N):
    num = losuj()
    nums.append(num)
    if num % 2 == 0:
        evens += 1
    else:
        odds += 1

print('\
    Dla 1000 liczb losowych z przedziału <1,50>:\n\
    Liczby parzyste: {:.2f}%\n\
    Liczby nieparzyste: {: .2f} %'.format(evens/N*100, odds/N*100))
