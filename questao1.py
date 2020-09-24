n = int(input("Informe a quantidade de treinos: "))
recorde = float(input("Informe o Recorde Regional: "))
temp = float(input("Digite o tempo 1: "))
i = 1
maior = temp
menor = temp
soma = temp

for x in range(1, n):
    x+=1
    i+=1
    temps = float(input("Digite o tempo %i: " %i))
    soma+=temps
    if(temps>maior):
        maior = temps
    elif(temps<menor):
        menor = temps
    else:
        pass

media = soma/n

print("Maior tempo: ", maior, "segundos")
print("Menor tempo: ", menor, "segundos")
print("Média: %.1f" %media)

if(menor>recorde):
    print("Você está acima do recorde! :( ")
elif(media<recorde):
    print("Você está abaixo do recorde! :)")
else:
    print("Você está com o mesmo tempo do recorde!")
