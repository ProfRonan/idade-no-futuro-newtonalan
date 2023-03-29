aa = int(input())

id = int(input())

an= int(input())

n = input()

ni = (an - aa) + id

if an < aa:
  print(f"{n}, no ano de {an} você terá {ni}")
elif ni == id:
  print(f"{n}, no ano de {an} você terá {id} anos")
else:
  print(f"{n}, no ano de {an} você terá {ni} anos")
