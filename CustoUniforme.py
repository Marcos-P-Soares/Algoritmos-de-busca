import heapq # heapq: biblioteca que gerencia filas de prioridade
import grafo


def busca_uniforme(grafo, no_inicial, objetivo):

    queue = [(0, no_inicial, [no_inicial])]  # (custo_total, no_atual, caminho)
    visitados = set()

    while queue:
        custo, no, caminho = heapq.heappop(queue)
        if no == objetivo:
            return caminho
        if no not in visitados:
            visitados.add(no)
            for neighbor in grafo.neighbors(no):
                if neighbor not in visitados:
                    custo_vizinho = grafo[no][neighbor]['custo']
                    heapq.heappush(queue, (custo + custo_vizinho, neighbor, caminho + [neighbor]))  #Adiciona um item ao heap.
    return "Caminho não encontrado"

#================ Execução ============================================

if __name__ == "__main__":
    mapa_romenia = grafo.mapa_romenia()
    no_inicial = 'Arad'
    objetivo = 'Bucharest'
    caminho = busca_uniforme(mapa_romenia, no_inicial, objetivo)
    print("Caminho encontrado:", caminho)
