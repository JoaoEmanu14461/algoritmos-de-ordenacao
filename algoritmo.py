import random

dados = []         
tamanho = 0         
topo = -1           
inicio = 0          
fim = -1            
quantidade = 0      
estrutura_atual = None   
criada = False      


#bubble, selection e insertion
def ordenacao_bolha(A):
    n = len(A)
    for i in range(n):
        for j in range(0, len(A) - 1):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]


def ordenacao_selecao(A):
    n = len(A)
    for i in range(n):
        minimo = i
        for j in range(i + 1, n):
            if A[minimo] > A[j]:
                minimo = j
        A[i], A[minimo] = A[minimo], A[i]


def ordenacao_insercao(A):
    n = len(A)
    for j in range(1, n):
        chave = A[j]
        i = j - 1
        while i >= 0 and A[i] > chave:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = chave



def criar_estrutura(tipo):
    global dados, tamanho, topo, inicio, fim, quantidade, estrutura_atual, criada

    try:
        tam = int(input("Informe o tamanho da estrutura: "))
        if tam <= 0:
            print("Tamanho inválido! Deve ser maior que zero.")
            return
    except ValueError:
        print("Valor inválido!")
        return

    dados = [None] * tam
    tamanho = tam
    topo = -1
    inicio = 0
    fim = -1
    quantidade = 0
    estrutura_atual = tipo
    criada = True
    print(f"{tipo.capitalize()} criada com capacidade para {tam} elementos.")


#pilha
def push_pilha():
    global topo, quantidade
    if topo == tamanho - 1:
        print("Pilha cheia! Não é possível armazenar.")
        return
    try:
        valor = int(input("Digite o valor a armazenar: "))
    except ValueError:
        print("Valor inválido!")
        return
    topo += 1
    dados[topo] = valor
    quantidade += 1
    print(f"Valor {valor} empilhado.")


def pop_pilha():
    global topo, quantidade
    if topo == -1:
        print("Pilha vazia! Nada a extrair.")
        return
    valor = dados[topo]
    dados[topo] = None
    topo -= 1
    quantidade -= 1
    print(f"Valor {valor} desempilhado.")


def show_pilha():
    if topo == -1:
        print("Pilha vazia.")
        return
    print("Pilha (topo -> base):")
    for i in range(topo, -1, -1):
        print(f"  [{i}] = {dados[i]}")


#fila
def enqueue_fila():
    global fim, quantidade
    if quantidade == tamanho:
        print("Fila cheia! Não é possível armazenar.")
        return
    try:
        valor = int(input("Digite o valor a armazenar: "))
    except ValueError:
        print("Valor inválido!")
        return
    fim += 1
    dados[fim] = valor
    quantidade += 1
    print(f"Valor {valor} enfileirado.")


def dequeue_fila():
    global inicio, fim, quantidade
    if quantidade == 0:
        print("Fila vazia! Nada a extrair.")
        return
    valor = dados[inicio]
    
    for i in range(inicio, fim):
        dados[i] = dados[i + 1]
    dados[fim] = None
    fim -= 1
    quantidade -= 1
    print(f"Valor {valor} desenfileirado.")


def show_fila():
    if quantidade == 0:
        print("Fila vazia.")
        return
    print("Fila (início -> fim):")
    for i in range(inicio, fim + 1):
        print(f"  [{i}] = {dados[i]}")


#fila circular
def enqueue_circular():
    global fim, quantidade
    if quantidade == tamanho:
        print("Fila circular cheia! Não é possível armazenar.")
        return
    try:
        valor = int(input("Digite o valor a armazenar: "))
    except ValueError:
        print("Valor inválido!")
        return
    fim = (fim + 1) % tamanho
    dados[fim] = valor
    quantidade += 1
    print(f"Valor {valor} enfileirado (posição {fim}).")


def dequeue_circular():
    global inicio, quantidade
    if quantidade == 0:
        print("Fila circular vazia! Nada a extrair.")
        return
    valor = dados[inicio]
    dados[inicio] = None
    inicio = (inicio + 1) % tamanho
    quantidade -= 1
    print(f"Valor {valor} desenfileirado.")


def show_circular():
    if quantidade == 0:
        print("Fila circular vazia.")
        return
    print("Fila circular (início -> fim):")
    idx = inicio
    for _ in range(quantidade):
        print(f"  [{idx}] = {dados[idx]}")
        idx = (idx + 1) % tamanho


#Menus
def menu_principal():
    print("\n***********************************")
    print("| Estruturas de Dados e Ordenação |")
    print("-----------------------------------")
    print("| 1 - PILHA                       |")
    print("| 2 - FILA                        |")
    print("| 3 - FILA CIRCULAR               |")
    print("| 4 - ORDENAR                     |")
    print("| 5 - SAIR                        |")
    print("-----------------------------------")
    try:
        return int(input("Digite a opção desejada: "))
    except ValueError:
        return -1


def menu_estrutura(nome):
    print(f"\n-----------------------------------")
    print(f"| {nome.capitalize():<31}|")
    print("-----------------------------------")
    print("| 1 - Criar estrutura             |")
    print("| 2 - Armazenar valor             |")
    print("| 3 - Extrair valor               |")
    print("| 4 - Imprimir conteúdo           |")
    print("| 5 - Voltar ao menu anterior     |")
    print("-----------------------------------")
    try:
        return int(input("Digite a opção desejada: "))
    except ValueError:
        return -1


def menu_ordenar():
    print("\n-----------------------------------")
    print("| ORDENAR                         |")
    print("-----------------------------------")
    print("| 1 - Bubble Sort                 |")
    print("| 2 - Selection Sort              |")
    print("| 3 - Insertion Sort              |")
    print("| 4 - Voltar ao menu anterior     |")
    print("-----------------------------------")
    try:
        return int(input("Digite a opção desejada: "))
    except ValueError:
        return -1


#Controladores de menus
def controlar_estrutura(tipo):
    global criada
    while True:
        opt = menu_estrutura(tipo)
        if opt == 5:
            print("Voltando ao menu anterior...")
            break

       
        if opt in (2, 3, 4) and not criada:
            print("Nenhuma estrutura foi criada ainda. Escolha 'Criar estrutura' primeiro.")
            continue
        if opt in (2, 3, 4) and estrutura_atual != tipo:
            print(f"A estrutura atual é '{estrutura_atual}'. Crie uma {tipo} primeiro.")
            continue

        if opt == 1:
            criar_estrutura(tipo)
        elif opt == 2:
            if tipo == "pilha":
                push_pilha()
            elif tipo == "fila":
                enqueue_fila()
            else:
                enqueue_circular()
        elif opt == 3:
            if tipo == "pilha":
                pop_pilha()
            elif tipo == "fila":
                dequeue_fila()
            else:
                dequeue_circular()
        elif opt == 4:
            if tipo == "pilha":
                show_pilha()
            elif tipo == "fila":
                show_fila()
            else:
                show_circular()
        else:
            print("Opção inexistente")


def controlar_ordenar():
    while True:
        opt = menu_ordenar()
        if opt == 4:
            print("Voltando ao menu anterior...")
            break

        if not criada:
            print("Nenhuma estrutura foi criada ainda.")
            print("Escolha primeiro PILHA, FILA ou FILA CIRCULAR no menu principal.")
            continue

        if opt in (1, 2, 3):
            if quantidade == 0:
                print("A estrutura está vazia. Não há o que ordenar.")
                continue
            
            valores = [v for v in dados if v is not None]

            if opt == 1:
                ordenacao_bolha(valores)
                print("Ordenado com Bubble Sort.")
            elif opt == 2:
                ordenacao_selecao(valores)
                print("Ordenado com Selection Sort.")
            else:
                ordenacao_insercao(valores)
                print("Ordenado com Insertion Sort.")

            
            _reescrever_vetor(valores)
            print("Vetor ordenado:", dados)
        else:
            print("Opção inexistente")


def _reescrever_vetor(valores):
    global dados, inicio, fim, topo, quantidade
    for i in range(tamanho):
        dados[i] = None

    for i, v in enumerate(valores):
        dados[i] = v


    if estrutura_atual == "pilha":
        topo = quantidade - 1
    elif estrutura_atual == "fila":
        inicio = 0
        fim = quantidade - 1
    else:  
        inicio = 0
        fim = quantidade - 1   


#principal
def main():
    while True:
        opt1 = menu_principal()

        if opt1 == 5:
            break
        elif opt1 == 1:
            controlar_estrutura("pilha")
        elif opt1 == 2:
            controlar_estrutura("fila")
        elif opt1 == 3:
            controlar_estrutura("fila circular")
        elif opt1 == 4:
            controlar_ordenar()
        else:
            print("Opção inexistente")

    print("Programa finalizado")


if __name__ == "__main__":
    main()