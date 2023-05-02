from model.graph import Graph 
from service.reader import Reader
from articulation import GraphService
from service.randomGraph import RandomGraph
import time

option = -1
while option != 0:
    option = int(input("Insira 1 caso queira passar um path de grafo, 2 para gerar um novo ou 0 para finalizar: "))
    reader = Reader()
    random_graph = RandomGraph()
    if option == 1:
        lista = reader.transforma_em_lista(r"C:\\Users\\mathe\\OneDrive\\Área de Trabalho\\exemplo.txt")
    elif option == 2:
        size = int(input("Insira o número total de vértices: "))
        probability = float(input("Insira a probabilidade da existencia de arestas entre vértices (0.0 até 1.0): "))
        lista = random_graph.random_graph(size, probability)
    elif option == 0:
        break
    else:
        continue
    grafo = Graph(lista)
    articulation = GraphService()
    numINput = int(input("Insira um número dentre o número total de vertices do arquivo desejado: "))
    print(f"Número inserido: {numINput}")
    print(f"Grau de saída: {len(grafo.adjacency_list[numINput])}")
    print(f"Grau de entrada: {len(grafo.procura_predecessores(numINput))}")
    print(f"Sucessores: {grafo.adjacency_list[numINput]}")
    print(f"Predecessores: {grafo.procura_predecessores(numINput)}")
    print(f"DFS: {grafo.depth_first_search()}")
    print(f"Classificacao das arestas: {grafo.edges[numINput]}")
    method_option = -1
    while method_option != 0:
        method_option = int(input("Insira 1 caso queira descobrir os ciclos, 2 para articulacoes, 3 para ambos via tarjan ou 0 para finalizar: "))
        if method_option == 1:
            start = time.time()
            print(f"Número de ciclos: {len(grafo.cycles)}")
            print(f"Ciclos: {grafo.cycles}")
            end = time.time()
            print("Tempo de execucação: ", (end - start) * 10**3, "ms")
        elif method_option == 2:
            start = time.time()
            print(f"Número de Articulações: {articulation.findArticulations(grafo)}")
            print(f"Articulações: {articulation.articulations}")
            end = time.time()
            print("Tempo de execucação: ", (end - start) * 10**3, "ms")
        elif method_option == 3:
            start = time.time()
            print("Componentes fortemente conexos no grafo(tarjan): ")
            grafo.tarjan()
            end = time.time()
            print("Tempo de execucação: ", (end - start) * 10**3, "ms")
        elif method_option == 0:
            break
        else:
            continue
        