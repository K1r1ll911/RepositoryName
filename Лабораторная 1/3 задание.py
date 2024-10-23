# TODO Найдите количество книг, которое можно разместить на дискете
obiem=1.44*1024*1024
str=100
stroki=50
simvolov=25
simvol=4
kniga = 4 * 25 * 50 * 100
kol = 0

for i in range(100):
    kol+=1
    obiem-=kniga
    if obiem < kniga:
        break
print("Количество книг, помещающихся на дискету:", kol)