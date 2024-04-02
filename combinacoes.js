function combinacoes(lista){
    if(lista.length == 0){
        return [[]]
    }
    let subconjunto = combinacoes(lista.slice(0, -1))
    let extra = lista.slice(-1)
    let novo = []
    for (sublista of subconjunto){
        novo.push([...sublista, ...extra])
    }
    return [...subconjunto, ...novo]
}
lista = [1,3,5,7,9]
console.log(`combinacoes (powerset): `, combinacoes(lista))