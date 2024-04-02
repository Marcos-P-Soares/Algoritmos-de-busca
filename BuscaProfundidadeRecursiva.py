import grafo


def busca_profundidade_recursiva(grafo, no_atual, objetivo, visitados=None, caminho=None):
    if visitados is None:
        visitados = set()  
    if caminho is None:
        caminho = []  

    visitados.add(no_atual) 
    caminho.append(no_atual)  

    if no_atual == objetivo:
        return caminho 

   
    for vizinho in grafo.neighbors(no_atual):
        if vizinho not in visitados:
            novo_caminho = busca_profundidade_recursiva(grafo, vizinho, objetivo, visitados, caminho[:])
            if novo_caminho is not None:
                return novo_caminho

    return None

#================ Execução ============================================

if __name__ == "__main__":
    mapa_romenia = grafo.mapa_romenia()
    no_inicial = 'Arad'
    objetivo = 'Bucharest'
    caminho = busca_profundidade_recursiva(mapa_romenia, no_inicial, objetivo)
    if caminho is not None:
        print("Caminho encontrado:", caminho)
    else:
        print("Caminho não encontrado")
