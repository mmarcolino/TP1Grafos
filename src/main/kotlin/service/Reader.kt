package service
import java.io.File

class Reader {
    fun readFile(path:String): MutableList<String>{
        var inputs: MutableList<String> = mutableListOf()
        File(path).forEachLine { inputs.add(it.trim())}
        inputs.removeAt(0)
        return inputs
    }
}