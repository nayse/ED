h = 1
tam = 100
fim = False
while h < tam and not fim:
    if 3*h+1 < tam:
        h = 3*h+1
    else:
        fim = True

print(h)