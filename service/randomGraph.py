import random

class RandomGraph:
    def _salvarGrafo(_self, grafo):
        with open("resources\graph.txt", 'w') as file:
            for i in range(1, len(grafo)):
                for j in range(len(grafo[i])):
                    line:str = str(grafo[i][j])
                    file.write(line)
                file.write("\n")

    def random_graph(_self, n, p):
        lista_de_adjacencia = [[] for _ in range(n +1)]
        for i in range(1, len(lista_de_adjacencia)):
            for j in range(1, len(lista_de_adjacencia)):
                probabilidade = random.random()
                if i != j and probabilidade < p:
                    lista_de_adjacencia[i].append(j)
        _self._salvarGrafo(lista_de_adjacencia)
        return lista_de_adjacencia