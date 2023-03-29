aa = int(input())

id = int(input())

an= int(input())

n = input()

ni = (an - aa) + id

if an < aa:
  print("Você não pode rejuvenecer.")
elif ni == id:
  print("Sua idade não mudou")
else:
  print(f"{n}, no ano de {an} você terá {id} anos")
