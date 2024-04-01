from collections import deque
import grafo


def busca_em_largura(grafo, no_inicial, objetivo):

    queue = deque([(no_inicial, [no_inicial])])
    visited = set()

    while queue:
        node, path = queue.popleft()
        if node == objetivo:
            return path
        if node not in visited:
            visited.add(node)
            for neighbor in grafo.neighbors(node):
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))
    return "Caminho não encontrado"

#================ Execução ============================================

if __name__ == "__main__":
    mapa_romenia = grafo.mapa_romenia()
    no_inicial = 'Arad'
    objetivo = 'Bucharest'
    path = busca_em_largura(mapa_romenia, no_inicial, objetivo)
    print("Caminho encontrado:", path)
    
