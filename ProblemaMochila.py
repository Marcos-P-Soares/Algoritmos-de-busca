objetos = {
    'Livro': {
        'peso': 0.8,    
        'valor': 30.00  
    },
    'Laptop': {
        'peso': 2.0,      
        'valor': 1500.00  
    },
    'Caneta': {
        'peso': 0.05,   
        'valor': 3.50   
    },
    'Camera': {
        'peso': 1.2,     
        'valor': 800.00  
    },
    'Celular': {
        'peso': 0.2,     
        'valor': 1200.00  
    },
    'Oculos de Sol': {
        'peso': 0.1,     
        'valor': 150.00  
    },
    'Fones de Ouvido': {
        'peso': 0.05,    
        'valor': 50.00   
    },
    'Bola': {
        'peso': 0.1,      
        'valor': 100.00   
    },
    'Relogio': {
        'peso': 0.2,      
        'valor': 200.00   
    },
    'Garrafa de Água': {
        'peso': 0.3,      
        'valor': 10.00    
    },
    'Guarda-chuva': {
        'peso': 0.7,      
        'valor': 40.00    
    },
    'Tablet': {
        'peso': 0.7,      
        'valor': 700.00   
    },
    'Chaveiro': {
        'peso': 0.02,     
        'valor': 5.00     
    },
    'Corda': {
        'peso': 1.0,      
        'valor': 20.00    
    },
    'Carregador Portatil': {
        'peso': 0.3,      
        'valor': 80.00    
    },
    'Mapa': {
        'peso': 0.1,      
        'valor': 15.00    
    },
    'Bone': {
        'peso': 0.1,      
        'valor': 25.00    
    },
    'Luvas': {
        'peso': 0.3,      
        'valor': 35.00    
    },
    'Caixa de Ferramentas': {
        'peso': 2.0,      
        'valor': 250.00   
    },
    'Cadeado': {
        'peso': 0.2,      
        'valor': 30.00    
    }
}

def preencher_mochila(objetos, capacidade_maxima):
    items = [(objetos[item]['valor'] / objetos[item]['peso'], item) for item in objetos]

    items.sort(reverse=True, key=lambda x: x[0])

    mochila = []
    peso_total = 0
    valor_total = 0

    for valor_peso, item in items:
        peso_item = objetos[item]['peso']
        valor_item = objetos[item]['valor']

        if peso_total + peso_item <= capacidade_maxima:
            mochila.append(item)
            peso_total += peso_item
            valor_total += valor_item

    return mochila, peso_total, valor_total


capacidade_maxima = 3.0

mochila, peso_total, valor_total = preencher_mochila(objetos, capacidade_maxima)

print("Itens na mochila:")
for item in mochila:
    print(f"- {item}")

print(f"Peso total na mochila: {peso_total} kg")
print(f"Valor total na mochila: R${valor_total:.2f}")