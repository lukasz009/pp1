from statistics import mean, median, stdev

tab = [21600, 4350, 3920, 5590, 3250, 4010]
print('\
    Średnia arytmetyczna: {0}\n\
    Mediana: {1}\n\
    Odchylenie standardowe: {2}\n\
    '.format(
    mean(tab),
    median(tab),
    stdev(tab)
))
