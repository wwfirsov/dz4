def zarplata():

    virabotka = int(input('Выработка: '))
    stavka = int(input('Ставка в часах: '))
    premiya = int(input('Премия: '))

    zp = virabotka * stavka + premiya

    return zp