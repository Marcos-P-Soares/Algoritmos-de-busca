import matplotlib.pyplot as plot
import networkx as nx

def mapa_romenia():
    mapa = nx.Graph()

    mapa.add_nodes_from([
        ('Arad'),
        ('Zerind'),
        ('Oradea'),
        ('Sibiu'),
        ('Timisoara'),
        ('Lugoj'),
        ('Mehadia'),
        ('Drobeta'),
        ('Craiova'),
        ('Rimnicu'),
        ('Fagaras'),
        ('Pitesti'),
        ('Bucharest'),
        ('Giurgiu'),
        ('Urziceni'),
        ('Hirsova'),
        ('Eforie'),
        ('Vaslui'),
        ('Iasi'),
        ('Neamt')
        ])

    mapa.add_edges_from([
        ('Arad' , 'Zerind', {'custo': 75}),
        ('Arad' , 'Timisoara', {'custo': 118}),
        ('Arad' , 'Sibiu', {'custo': 140}),
        ('Zerind','Oradea',{'custo': 71}),
        ('Sibiu','Rimnicu',{'custo': 80}),
        ('Sibiu','Fagaras',{'custo': 99}),
        ('Timisoara','Lugoj', {'custo': 111}),
        ('Oradea','Sibiu',{'custo':151}),
        ('Lugoj','Mehadia',{'custo':70}),
        ('Mehadia','Drobeta',{'custo':75}),
        ('Drobeta','Craiova',{'custo':120}),
        ('Rimnicu','Craiova',{'custo':146}),
        ('Rimnicu','Pitesti',{'custo':97}),
        ('Fagaras','Bucharest',{'custo':211}),
        ('Pitesti','Bucharest',{'custo':101}),
        ('Bucharest','Giurgiu',{'custo':90}),
        ('Bucharest','Urziceni',{'custo':85}),
        ('Urziceni','Hirsova',{'custo':98}),
        ('Urziceni','Vaslui',{'custo':142}),
        ('Hirsova','Eforie',{'custo':86}),
        ('Vaslui','Iasi',{'custo':92}),
        ('Iasi','Neamt',{'custo':87})
    ])

    return mapa
# pos = nx.random_layout(mapa)

# edge_labels = {(u,v):d['custo'] for u,v,d in mapa.edges(data=True)}

# nx.draw(mapa, node_color="gray", with_labels=True)

# nx.draw_networkx_edge_labels(mapa, edge_labels= edge_labels)
# plot.margins(0.2)

# plot.show()


