function fatorial(x){
    let resposta = 1
    while (x > 1){
        resposta = resposta * x
        x = x - 1
    }
    return resposta
}

console.log(fatorial(5))