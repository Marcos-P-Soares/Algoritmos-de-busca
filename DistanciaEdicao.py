def distancia_edicao_gulosa(a, b):
    m = len(a)
    n = len(b)
    
    i = 0
    j = 0
    dist = 0
    
    while i < m and j < n:
        if a[i] != b[j]:
            if i + 1 < m and a[i + 1] == b[j]:
                i += 1
            elif j + 1 < n and a[i] == b[j + 1]:
                j += 1
            else:
                i += 1
                j += 1
            dist += 1
        else:
            i += 1
            j += 1
    
    dist += (m - i) + (n - j)
    
    return dist


resultado1 = distancia_edicao_gulosa("asar", "casa")
print("Distancia de edicao (asar -> casa):", resultado1)

resultado2 = distancia_edicao_gulosa("inserir", "insercao")
print("Distancia de edicao (inserir -> insercao):", resultado2)

resultado3 = distancia_edicao_gulosa("kitten", "sitting")
print("Distancia de edicao (kitten -> sitting):", resultado3)

resultado4 = distancia_edicao_gulosa("abcde", "bcde")
print("Distancia de edicao (abcde -> bcde):", resultado4)
