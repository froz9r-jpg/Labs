import sys
from collections import deque


def zalivka_polia(pole, ryadok, stovpets, tsilovy_kolir, kolir_zaminy):
    if tsilovy_kolir == kolir_zaminy:
        return pole
    if pole[ryadok][stovpets] != tsilovy_kolir:
        return pole

    kilkist_ryadkiv = len(pole)
    kilkist_stovptsiv = len(pole[0])
    cherha = deque()
    cherha.append((ryadok, stovpets))
    pole[ryadok][stovpets] = kolir_zaminy

    while cherha:
        r, s = cherha.popleft()
        for dr, ds in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, ns = r + dr, s + ds
            if 0 <= nr < kilkist_ryadkiv and 0 <= ns < kilkist_stovptsiv and pole[nr][ns] == tsilovy_kolir:
                pole[nr][ns] = kolir_zaminy
                cherha.append((nr, ns))

    return pole


def holovna():
    with open('input.txt', 'r', encoding='utf-8') as f:
        ryadky = [ryadok.strip() for ryadok in f if ryadok.strip()]

    vysota, shyryna = map(int, ryadky[0].split(','))
    pochatkovyi_ryadok, pochatkovyi_stovpets = map(int, ryadky[1].split(','))
    kolir_zaminy = ryadky[2].strip("'\"")

    pole = []
    for ryadok in ryadky[3:]:
        ryadok = ryadok.strip().rstrip(',')
        klitynky = [k.strip().strip("'\"") for k in ryadok.strip('[]').split(',')]
        pole.append(klitynky)

    tsilovy_kolir = pole[pochatkovyi_ryadok][pochatkovyi_stovpets]
    pole = zalivka_polia(pole, pochatkovyi_ryadok, pochatkovyi_stovpets, tsilovy_kolir, kolir_zaminy)

    with open('output.txt', 'w', encoding='utf-8') as f:
        for ryadok in pole:
            formatovano = "[" + ", ".join(f"'{k}'" for k in ryadok) + "]"
            f.write(formatovano + "\n")

    print("output.txt:")
    for ryadok in pole:
        print("[" + ", ".join(f"'{k}'" for k in ryadok) + "]")


if __name__ == '__main__':
    holovna()