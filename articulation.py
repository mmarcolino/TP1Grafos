from model.graph import Graph

class GraphService:
    def __init__(_self):
        _self.numberOfArticulations = 0
        _self.articulations = []

    def findArticulations(_self, graph: Graph):
        copy = graph.convert_to_undirected()
        copy.depth_first_search()
        search1 = copy.number_of_searches
        for i in range(1, len(graph.adjacency_list)):
            graphTeste = copy.remove_vertex(i)
            graphTeste.depth_first_search()
            search2 = graphTeste.number_of_searches
            if search1 < search2:
                _self.numberOfArticulations += 1
                _self.articulations.append(i)

        return _self.numberOfArticulations