package model
import java.util.regex.Pattern

class Graph {
    private val graph: MutableList<MutableList<Int>> = mutableListOf()
    private val visited: MutableList<Boolean> = mutableListOf()
    private val td: MutableList<Int> = mutableListOf()
    private val tt: MutableList<Int> = mutableListOf()
    private val edges: MutableList<MutableList<String>> = mutableListOf()
    private var counter:Int = 0

    fun getGraph(): MutableList<MutableList<Int>> = graph

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

    fun depthFirstSearch(g: Int): MutableList<MutableList<String>> {
        executeDepthFirstSearch(g)
        return edges
    }
    private fun executeDepthFirstSearch(g: Int){
        visited[g] = true
        counter++
        td[g] = counter
        print("$g ")
        val ite:Iterator<Int> = graph[g].listIterator()
        while (ite.hasNext()){
            val adj = ite.next()
            if (!visited[adj]){
                executeDepthFirstSearch(adj)
                edges[g].add("${g}-${adj} = Arvore")
            }
            else{
                if(tt.get(adj) == 0) edges[g].add("${g}-${adj} = Retorno")
                else if(td[g] < td[adj]) edges[g].add("${g}-${adj} = Avanco")
                else edges[g].add("${g}-${adj} = Cruzamento")
            }
        }
        counter ++
        tt[g] = counter
    }
}