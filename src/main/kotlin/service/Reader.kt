package service
import java.io.File

class Reader {
    /**
     * Lê um arquivo TXT e forma uma lista de adjacencia de sucessão.
     * @param path string que representa o endereço do arquivo
     * @return retorna a lista de relações entre vértices
     */
    fun readFile(path:String): MutableList<String>{
        var inputs: MutableList<String> = mutableListOf()
        File(path).forEachLine { inputs.add(it.trim())}
        inputs.removeAt(0)
        return inputs
    }
}