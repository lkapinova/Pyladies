print("Vítej v jednoduché kalkulačce. Můžeš tu sčítat, odečítat, násobit a dělit dvě čísla.")
n1 = int(input("Zadej první číslo: "))
n2 = int(input("Zadej druhé číslo: "))
op = input("Zadej znak pro požadovanou matematickou operaci (+, -, *, /): ")

if op == "+":
    n = n1 + n2
if op == "-":
    n = n1 - n2
if op == "*":
    n = n1 * n2
if op == "/" and n2 == 0:
  print("Nulou nelze dělit. Zkus zadat hodnoty znovu.")    
if op == "/":
    n = n1 / n2

print(n1,op,n2,' =', n)