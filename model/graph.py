import copy

class Graph:
    def __init__(_self, adjacency_list: list[list]):
        _self.adjacency_list = adjacency_list
        _self.visited = [0] * len(adjacency_list)
        _self.td = [0] * len(adjacency_list)
        _self.tt = [0] * len(adjacency_list)
        _self.edges = [[] for _ in range(len(adjacency_list))]
        _self.conter = 0
        _self.cycles = []
        _self.search = []
        _self.number_of_searches = 0
        
    def procura_predecessores(_self, n: int):
        predecessores = []
        for vertex in _self.adjacency_list:
            for p in vertex:
                if p == n:
                    predecessores.append(_self.adjacency_list.index(vertex))  
        return predecessores
    
    def _copy(_self):
        new_graph = copy.deepcopy(_self)
        return new_graph
    
    def remove_vertex(_self, v: int):
        removed = _self._copy()
        removed.adjacency_list[v] = []
        removed.visited[v] = None
        for vertex in removed.adjacency_list:
            while v in vertex:
                vertex.remove(v)
        return removed
    
    def convert_to_undirected(_self):
        undirected = _self._copy()
        for i in range(1, len(undirected.adjacency_list)):
            for j in undirected.procura_predecessores(i):
                if not j in undirected.adjacency_list[i]:
                    undirected.adjacency_list[i].append(j)
        return undirected
    
    def depth_first_search(_self):
        _self.visited[0] = None
        _self.counter = 0
        _self.number_of_searches = 0
        for i in range(1, len(_self.adjacency_list)):
            if _self.visited[i] == 1:
                _self.visited[i] = 0
                _self.tt[i] = 0
                _self.td[i] = 0
        _self.cycles.clear()    
        _self.search.clear() 
        while (0 in _self.visited):
            not_visited = _self.visited.index(0)
            _self.search.append(not_visited)
            _self.number_of_searches += 1
            _self.execute_dfs(not_visited)
        return  _self.search
    
    def execute_dfs(_self, v):
        _self.visited[v] = 1
        _self.conter += 1
        _self.td[v] = _self.conter
        ite = iter(_self.adjacency_list[v])
        while True:
            try:
                adj = next(ite)
                if (not _self.visited[adj]):
                    _self.edges[v].append(f"{v} - {adj} = arvore")
                    _self.search.append(adj)
                    _self.execute_dfs(adj)
                else:
                    flag = False
                    if _self.tt[adj] == 0:
                        _self.edges[v].append(f"{v} - {adj} = retorno")
                        list = []
                        list.append(adj)
                        for i in reversed(range(0, len(_self.search))):
                            if _self.search[i] != adj: list.append(_self.search[i])
                            else:
                                list.append(_self.search[i])
                                break
                        for cycle in _self.cycles:
                            if all(elem in cycle  for elem in list) and all(elem in list for elem in cycle ):
                                flag = True
                        if not flag: 
                            list.reverse()
                            _self.cycles.append(list)
                    elif _self.td[v] < _self.td[adj]: _self.edges[v].append(f"{v} - {adj} = Avanco")
                    else: _self.edges[v].append(f"{v} - {adj} = Cruzamento")
            except StopIteration:
                break
        _self.conter += 1
        _self.tt[v] = _self.conter
        
    def tarjanUtil(_self, u, low, stackMember, st):
        _self.td[u] = _self.conter
        low[u] = _self.conter
        _self.conter += 1
        stackMember[u] = True
        st.append(u)
 
        for v in _self.adjacency_list[u]:
            if _self.td[v] == 0:
                _self.tarjanUtil(v, low, stackMember, st)
                low[u] = min(low[u], low[v])
            elif stackMember[v] == True:
                low[u] = min(low[u], _self.td[v])
        w = -1
        if low[u] == _self.td[u]:
            while w != u:
                w = st.pop()
                print(w, end=" ")
                stackMember[w] = False
            print()
            
    def tarjan(_self):
        _self.conter = 0
        _self.td = [0] * len(_self.adjacency_list)
        low = [0] * len(_self.adjacency_list)
        stackMember = [False] * len(_self.adjacency_list)
        st = []
        for i in range(1, len(_self.adjacency_list)):
            if _self.td[i] == 0:
                _self.tarjanUtil(i, low, stackMember, st)
            