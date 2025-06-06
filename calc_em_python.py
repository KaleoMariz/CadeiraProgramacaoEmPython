def calculadora(): #Exibiçào da calculadora
    print("  CALCULADORA")
    print("  1  2  3  +\n  4  5  6  -\n  7  8  9  x\n  0  ,  .  =")

def calcular(calc):
    calc = calc.replace('x', '*') #Associando o 'x' a multiplicaçào
    calc = calc.replace(',', '.') #Associando ',' a quebra de inteiro (permitindo decimal)
    caracteres = '0123456789.+-*/' #Institui/valida os digitos que serão usados

    for c in calc:  #Garantir que o user só poderá escolher os caracteres que aparecem na calculadora
        if c not in caracteres:
            return "Erro"

    l = [] #Lista (que armazena valores em ordem) para posteriormente quebrar a expressão em operadores e numeros
    num = ''
    for c in calc: #"Para caracteres em expressao"
        if c in '0123456789.': #Se caracteres são...
            num += c #Atribui os digitos numerais a variável num
        else:
            if num == '': #Se num tiver vazio significa que há dois operadores ou que há operador primeiro que numero no inicio da expressao
                return "Erro"
            l.append(float(num)) #numero válido como string converte em float e adiciona a Lista (l)
            l.append(c) #adiciona o operador atual que é o caracter (+,-,* ou /)
            num = '' #reinicia a variavel num para capturar o prox número
    if num != '':
        l.append(float(num)) #pegar o ultimo numero da expressao depois que o loop terminar porque sem, a lista termina no ultimo operador

    # Primeira Ordem Matemática - Resolver Multiplicação e Divisão
    i=0
    while i<len(l): #Laço pra percorrer a Lista
        if l[i] == '*':
            l[i-1] = l[i-1]*l[i+1] #Faz a multiplicação e garante o resultado no lugar da expressão
            del l[i:i+2] #Remove o operador e o numero
            i-=1 #Faz o indice voltar uma posição para reavaliar
        elif l[i] == '/':
            if l[i+1]==0: #Verifica se o user quer dividir por 0
                return "Divisão por zero"
            l[i-1] = l[i-1]/l[i+1] #Faz a divisão
            del l[i:i+2]
            i-=1 # Remove e volta uma posição
        else: i+=1 #Se não encontrou multiplicação ou divisão, passa para a Segunda Ordem

    #Segunda Ordem Matemática - Resolver Adição e Subtração
    resultado = l[0] #numero na posição 0
    i=1 #operador na posição 1
    while i<len(l):
        operador=l[i] #operador
        prox_num=l[i+1] #numero seguinte
        if operador == '+': #soma o numero ao resultado acumulado
            resultado += prox_num
        elif operador == '-': #subtrai o numero ao resultado acumulado
            resultado -= prox_num
        i +=2 #avança o operador e o numero

    return str(round(resultado, 6)) #converte para string para exibir como texto na tela

calc = ""