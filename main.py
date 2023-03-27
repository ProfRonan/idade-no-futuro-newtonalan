#aa = Ano Atual
#an = Ano "Novo"
#id = Idade
#n = Nome

aa = int(input("Digite o ano atual: "))
print(" ")

id = int(input("Digite, agora, a idade que você completou ou irá completar esse ano. "))
print(" ")

an= int(input("Digite, dessa vez, o ano que você deseja saber sua idade: "))
print(" ")

n = input("Digite, por fim, o seu nome: ")
print(" ")

print("L o a d i n g . . .")
print(" ")

ni = (an - aa) + id

print(f"{n}, no ano de {an} você completará {ni} anos de idade.")
