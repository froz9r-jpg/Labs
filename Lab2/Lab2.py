def quick_sort(khomyachky, kilkist):
    if len(khomyachky) <= 1:
        return khomyachky
    
    opora = khomyachky[len(khomyachky) // 2]
    opora_vitrata = opora[0] + opora[1] * (kilkist - 1)
    
    menshe = []
    rivne = []
    bilshe = []
    
    for h in khomyachky:
        vitrata = h[0] + h[1] * (kilkist - 1)
        if vitrata < opora_vitrata:
            menshe.append(h)
        elif vitrata == opora_vitrata:
            rivne.append(h)
        else:
            bilshe.append(h)
    
    return quick_sort(menshe, kilkist) + rivne + quick_sort(bilshe, kilkist)


def znayty_maksymalnu_kilkist(zapas, zagalna_kilkist, khomyachky):
    rezultat = 0
    for kilkist in range(1, zagalna_kilkist + 1):
        posortovani = quick_sort(khomyachky, kilkist)
        grupa = posortovani[:kilkist]
        zideno = 0
        for khomyachok in grupa:
            zideno += khomyachok[0] + khomyachok[1] * (kilkist - 1)
        if zideno <= zapas:
            rezultat = kilkist
    return rezultat