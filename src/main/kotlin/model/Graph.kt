package model
import java.util.regex.Pattern

class Graph {
    //Lista de Adjacencia
    private val graph: MutableList<MutableList<Int>> = mutableListOf()
    //Lista de vértices visitados
    private val visited: MutableList<Boolean> = mutableListOf()
    //Tempo de descoberta, tempo de término
    private val td: MutableList<Int> = mutableListOf()
    private val tt: MutableList<Int> = mutableListOf()
    //Lista de listas de arestas (indice x possui uma lista de todos vértices de x)
    private val edges: MutableList<MutableList<String>> = mutableListOf()
    //Contador universal
    private var counter:Int = 0
    //Lista de ciclos
    private val cycles: MutableList<MutableList<Int>> = mutableListOf()
    private val search: MutableList<Int> = mutableListOf()

    /**
     * Retorna a lista de adjacencia do grafo.
     */
    fun getGraph(): MutableList<MutableList<Int>> = graph

    /**
     * Retorna a lista de adjacencia do grafo.
     */
    fun getCycles(): MutableList<MutableList<Int>> = cycles

    /**
     * Inicializa a lista de adjacencia e as variáveos auxiliares.
     * @param vertices Lista das relações entre os vértices
     * @constructor Construtor da classe Graph
     */
    fun setGraph(vertices: List<String>){
        var sucessores: MutableList<Int> = mutableListOf()
        var index: Int = 1
        graph.add(mutableListOf())
        visited.add(false)
        td.add(0)
        tt.add(0)
        edges.add(mutableListOf())
        for(i in vertices){
            val words = i.split(Pattern.compile("\\D+"))
            if (words[0].toInt() == index && vertices.indexOf(i) != vertices.size -1){
                sucessores.add(words[1].trim().toInt())
            }
            else{
                index ++
                sucessores.sort()
                graph.add(sucessores)
                visited.add( false)
                td.add(0)
                tt.add(0)
                edges.add(mutableListOf())
                sucessores = mutableListOf()
                sucessores.add(words[1].trim().toInt())
            }
        }

    }

    /**
     * Reverte a lista de adjacencia baseada em sucessores para predecessores e retorna ela.
     * @param n Vértice desejado.
     * @return **predecessores** lista de predecessores do vértice desejado
     */
    fun procuraPredecessores(n: Int): List<Int>{
        var predecessores: MutableList<Int> = mutableListOf()
        for(vertice in graph){
            for (p in vertice){
                if (p == n){
                    predecessores.add(graph.indexOf(vertice))
                }
            }
        }
        return predecessores
    }

    /**
     * Chama o método recursivo da busca em profundidade.
     * @param g Vértice desejado.
     * @return **edges** lista de listas de arestas com suas classificações
     */
    fun depthFirstSearch(g: Int): MutableList<MutableList<String>> {
        executeDepthFirstSearch(g)
        return edges
    }

    /**
     * Executa a busca em profundiade a partir do vértice g.
     * @param g Vértice desejado
     * @receiver depthFirstSearch
     */
    private fun executeDepthFirstSearch(g: Int){
        visited[g] = true
        counter++
        td[g] = counter
        print("$g ")
        search.add(g)
        val ite:Iterator<Int> = graph[g].listIterator()
        while (ite.hasNext()){
            val adj = ite.next()
            if (!visited[adj]){
                executeDepthFirstSearch(adj)
                edges[g].add("${g}-${adj} = Arvore")
            }
            else{
                if(tt.get(adj) == 0){
                    edges[g].add("${g}-${adj} = Retorno")
                    val list: MutableList<Int> = mutableListOf()
                    for (i in search.lastIndex downTo 0){
                        if (i != adj) list.add(i)
                        else{
                            list.add(i)
                            break
                        }
                    }
                    cycles.add(list)
                }
                else if(td[g] < td[adj]) edges[g].add("${g}-${adj} = Avanco")
                else edges[g].add("${g}-${adj} = Cruzamento")
            }
        }
        counter ++
        tt[g] = counter
    }
}