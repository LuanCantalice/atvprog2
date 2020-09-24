qtd = int(input("Quantidade de colchões: "))

h = int(input("Informe a altura da porta: "))
b = int(input("Informe a largura da porta: "))

i=1

for x in range(1, qtd+1):
    print("\nColchão %i :" %i)
    i+=1

    l = int(input("Informe a largura do colchão: "))
    c = int(input("Informe a comprimento do colchão: "))
    a = int(input("Informe a altura do colchão: "))

    if(l<=h and (l>0 and c>0 and a>0)):
        print("PASSA")
    elif(l>h):
        print("EMPERRA")
    else:
        print("DIMENSÕES INVÁLIDAS")
