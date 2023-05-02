import os
import re

class Reader:
    def _readFile(_self, path:str) -> list:
        inputs = []
        with open(path, 'r') as f:
            for line in f:
                inputs.append(line.strip())
        inputs.pop(0)
        return inputs
    
    def transforma_em_lista(_self, path:str):
        lista_de_adjacencia = []
        arestas = _self._readFile(path= path)
        
        sucessores = []
        index = 1
        lista_de_adjacencia.append([])
        
        for i in arestas:
            words = re.findall(r'\d+', i)
            if int(words[0]) == index and arestas.index(i) != len(arestas) - 1:
                sucessores.append(int(words[1].strip()))
            else:
                index += 1
                sucessores.sort()
                lista_de_adjacencia.append(sucessores)
                if index < int(words[0]):
                    for j in range(index, int(words[0])):
                        lista_de_adjacencia.append([])
                        index += 1
                sucessores = [int(words[1].strip())]
        lista_de_adjacencia.append(sucessores)
        return lista_de_adjacencia