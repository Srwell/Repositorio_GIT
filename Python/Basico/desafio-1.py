"""
Após realizar um input de dados, imprima na tela algumas das validações de caracteristicas deste dado.
"""

i = input("Digite algo: ")

print("\nTipo primitivo: {}".format(type(i)))
print("Só tem espaços? {}".format(i.isspace()))
print("É um numero? {}".format(i.isnumeric()))
print("È alfabético? {}".format(i.isalpha()))
print("É alphanumerico? {}".format(i.isalnum()))
print("Está todo em minusculo? {}".format(i.islower()))
print("Está todo em maiusculo? {}".format(i.isupper()))
print("Está captalizada? {}".format(i.istitle()))
