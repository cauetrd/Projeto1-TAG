import networkx as nx
import matplotlib.pyplot as plt


# Função para extração de dados do arquivo e construção do grafo.   
def obter_dados():
    f = open("soc-dolphins.mtx","r")

    grafo = nx.Graph()
    adjlist = [[]]

    # O grafo está representado em duas formas, como um objeto Graph da biblioteca networkx 
    # e como uma lista de adjacências implementada manualmente.

    lines = []
    for line in f:
        if(line[0] != '%'):
            lines.append(line[:-1])

    f.close()

    for group in lines:
        if group == lines[0]:
            vertices = int(group.split()[0]) 
            arestas = int(group.split()[2])

            adjlist = [[] for _ in range(vertices+1)]   
            continue

        x1 = int(group.split()[0])
        x2 = int(group.split()[1])

        grafo.add_edge(x1,x2)
        adjlist[x1].append(x2)
        adjlist[x2].append(x1)
    print(f"Grafo construído com {vertices} vértices e {arestas} arestas")

    return grafo, adjlist, vertices, arestas


#Função recursiva do algoritmo de Bron-Kerbosch com pivotamento, para melhor performance.
def recursao_bron_kerbosch_com_pivotamento (adjlist, R, P, X, cliquesmaximais):
    if not P and not X:
        cliquesmaximais.append(R)
        return
    
    u = next(iter(P | X))
    vizinhosU = set(adjlist[u])

    for v in (P - vizinhosU):
        recursao_bron_kerbosch_com_pivotamento(adjlist, R | {v}, P & set(adjlist[v]), X & set(adjlist[v]), cliquesmaximais)
        P.remove(v)
        X.add(v)

#Função que inicia a recursão do algoritmo de Bron-Kerbosch com os parâmetros adequados e 
# retorna o conjunto de cliques maximais.
def bron_kerbosch(adjlist):
    cliquesmaximais = []
    R = set()
    P = set(range(1, len(adjlist)))
    X = set()


    recursao_bron_kerbosch_com_pivotamento(adjlist, R, P, X, cliquesmaximais)
    return sorted(cliquesmaximais, key=len) #Ordenação com base na quantidade de vértices para melhor visualização


#Função que constrói o grafo visualmente utilizando a biblioteca matplotlib.pyplot a partir
# do objeto Graph da biblioteca networkx.

def visualizacao_grafo(grafo, cliquesmaximais):

    pos = nx.spring_layout(grafo)  # Layout do grafo
    color_map = {}  # Mapeia cores para cada clique
    
    for idx, clique in enumerate(cliquesmaximais):
        for vertice in clique:
            color_map[vertice] = idx

    cores = [color_map.get(vertice, -1) for vertice in grafo.nodes]
    nx.draw(grafo, pos, with_labels=True, node_color=cores, cmap=plt.cm.Set3, node_size=500)
    plt.show()

#Função para obtenção dos coeficientes de aglomeração de cada vértice e médio do grafo
# utilizando métodos do objeto Graph da biblioteca networkx
def obter_coeficientes_aglomeracao(grafo):

    aglomeracao = nx.clustering(grafo) 
    aglomeracao_media = nx.average_clustering(grafo)
    return aglomeracao, aglomeracao_media

    






def main():
    grafo, adjlist, vertices, arestas = obter_dados()

    #Print graus dos vértices
    for vertice in range(1, vertices + 1):
        print(f"Grau do vértice {vertice}: {len(adjlist[vertice])}")


    cliquesmaximais = bron_kerbosch(adjlist)

    #Print conjunto de cliques maximais e suas quantidades de vértices
    print("Cliques maximais:")
    for clique in cliquesmaximais:
        print(f"Clique maximal com {len(clique)} vértices, sendo eles: {clique}")

    clustering, avg_clustering = obter_coeficientes_aglomeracao(grafo)

    #Print coeficiente de aglomeração de cada vértice
    for vertice, coeficiente in sorted(clustering.items()):
        print(f"Vértice {vertice}: {coeficiente:.4f}")

    #Print coeficiente de aglomeração médio do grafo
    print(f"\nCoeficiente médio de Aglomeração do Grafo: {avg_clustering:.4f}")

    #Chamada para função de construção gráfica do grafo
    visualizacao_grafo(grafo, cliquesmaximais)


if __name__ == "__main__":
    main()