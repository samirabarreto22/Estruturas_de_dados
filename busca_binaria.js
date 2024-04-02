function busca_binaria(lista, e){
    
    function busca(lista, e, inicio, fim){
        if (inicio == fim){
            return lista[inicio] == e
        }
    }
    let meio = Math.floor((inicio + fim)/ 2)
    if (lista[meio] == e){
        return true
    }else if (lista[meio] > e){
        if (inicio == meio){
            return false
        } else {
            return busca (lista, e, inicio, meio -1)
        }
    }else{
        return busca(lista, e, meio + 1, fim)
    }


    if (lista.length == 0){
        return false
    }else{
        return busca(lista, e, 0, lista.length - 1)
    }
}