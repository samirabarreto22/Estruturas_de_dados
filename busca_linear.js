function busca_linear(lista,e){
    let encontrado = false
    for (let i of lista){
        if (e == i){
            encontrado = true
            break
        }
    }
    return encontrado
}

let lista = [,3,5,6,7,0,8]


console.log(busca_linear(lista, 10))
console.log(busca_linear(lista, 0))

