
import model.Graph
import service.Reader

fun main(args: Array<String>) {
    //Lê o arquivo e transforma em uma lista de string, contendo cada linha
    val lista: List<String> = Reader().readFile("C:\\Users\\mathe\\Downloads\\graph-test-100.txt")
    //cria um grafo direcionado, mapeando os vertices pelas relações de suceções
    val grafo = Graph()
    grafo.setGraph(lista)
    //Lê o input do número
    print("Insira um número dentre o número total de vertices don arquivo desejado: ")
    val numINput = readlnOrNull()?.toInt()
    //Printando
    println("Número inserido: $numINput")
    println("Grau de saída: ${grafo.getGraph()[numINput!!].size}")
    println("Grau de entrada: ${grafo.procuraPredecessores(numINput).size}")
    println("Sucessores: ${grafo.getGraph()[numINput]}")
    println("Predecessores: ${grafo.procuraPredecessores(numINput)}")
    print("DFS: ")
    val arestas: MutableList<MutableList<String>> = grafo.depthFirstSearch(numINput)
    println()
    println("Classificacao das arestas: ${arestas[numINput]}")
}