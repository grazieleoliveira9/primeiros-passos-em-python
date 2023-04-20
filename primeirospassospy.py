print("Ola Mundo Python")
print("Bem vindo ao Python")

if 5 > 20:
    print("Cinco é maior do que dois")
    print("Fim do bloco do if.")

print("Fora do bloco if.")    

#imprime uma mensagem
print("Olá mundo!") # este é um comentário
print("Seja bem vindo")

"""
Isto é uma string
multiline, usada como
bloco de notas

"""

x = 5 
Y = "Graziele"
z = 4 # agora é do tipo int
z = "Logan" # agora é do tipo str

print(x)
print(Y)
print(type(x))
print(type(Y))


a = str(3) # a será "3"
b = int(3) # b será "3"
c = float(3) # c será "3.0"

# Camel Case 
myVariableCase = "John"

# Pascal Case
MyVariableCase = "John"

# Snake Case
my_variable_name = "John"


myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# 2myvar = "John"
# my-var = "John"
# my var = "John"

#a = "Laranja"
#b = "Banana
#c = "Cereja"

a, b, c = "Laranja", "Banana", "Cereja"

print(a)
print(b)
print(c)

#d = "Graziele"
#e = "Graziele"
#f = "Graziele"

d = e = f = "Graziele"

print(d)
print(e)
print(f)

# Coleçao de dados

frutas = {"Maça", "Banana", "Cereja"}

x, y, z = frutas

print(x)
print(y)
print(z)

a = "incrível"
print("python é " + a)


nome = "Graziele "
sobrenome = "Oliveira"
nomeCompleto = nome + sobrenome

print(nomeCompleto)

x = 5
y = 10 

print(x+y)

# Gera ERRO - Número + Texto, porém da pra transformar o numero numa string: 
num = 20 
texto = "carro" 
print(str(num) + texto)

# Criando uma função 

def myFunc(): 
    print("Python é incrível")

myFunc()
myFunc()
myFunc()

x = "incrível"
def myFunc(): 
    print("Python é " + x)

myFunc()
print("você é " + x)

# Para criar uma variável GLOBAL dentro de uma particular, defina primeiro a variavel como global depois defina
# valor a essa variável 

def myFunc(): 
    print("Python é " + x)
    y = "fantastico" #particular porque está dentro da função, então por fora da função nao tem valor
    global z #assim sua variavel fica visivel até fora da função
    z = "Bem vindo ao curso"

myFunc()
print(z)

# Tipo de texto:	str
# Tipos numéricos:	int, float, complex
# Tipos de sequência:	list, tuple, range
# Tipo de mapeamento:	dict
# Tipos de conjuntos:	set, frozenset
# Tipo booleano:	bool
# Tipos binários:	bytes, bytearray, memoryview

#### Definir o tipo de dados ####

x = "Hello World" # str
x = 20 # int
x = 20.5 # float
x = 1j # complex
x = ["apple", "banana", "cherry"] # list
x = ("apple", "banana", "cherry") # tuple
x = range(6) # range
x = {"name" : "John", "age" : 36} # dict
x = {"apple", "banana", "cherry"}	# set
x = frozenset({"apple", "banana", "cherry"}) # frozenset
x = True # bool
x = b"Hello" # bytes
x = bytearray(5) # bytearray
x = memoryview(bytes(5)) # memoryview

#### Configurando o Tipo de Dados Específico ####

x = str("Hello World") # str
x = int(20)	# int
x = float(20.5) # float
x = complex(1j)	# complex
x = list(("apple", "banana", "cherry"))	# list
x = tuple(("apple", "banana", "cherry")) # tuple
x = range(6) # range
x = dict(name="John", age=36) # dict
x = set(("apple", "banana", "cherry")) # set
x = frozenset(("apple", "banana", "cherry")) # frozenset
x = bool(5) # bool
x = bytes(5) # bytes
x = bytearray(5) # bytearray
x = memoryview(bytes(5)) # memoryview

x = "20"
print(x)
print(type(x))

x = int("20")
print(type(x))

p = "5"


import random
num = random.randrange(1, 10)

print(num)

import random

a = 1
b = 35656222554887711
c = -3255522

print(type(a))
print(type(b))
print(type(c))

d = 1.10
e = 1.0
f = -35.59
g = 35e3
h = 12E4
i = -87.7e100

print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))
print(type(i))

j = 3+5j
k = 5j
l = -5j

print(type(j))
print(type(k))
print(type(l))

#converter de int para float:
x = float(1)

#converter de float para int:
y = int(2.8)

#converter de float para complex:
z = complex(x)

print(x)
print(y)
print(z)

print(type(x))
print(type(y))
print(type(z))

num = random.randrange(1, 10)

print(num)
print(random.randrange(1, 10))
print("\n") #se usa isso para quebra de linha 

l = 1
m = 1.5
n = 4j

print(type(l))
print(type(m))
print(type(n))

p = 9

print(float(p))

# int() - constrói um número inteiro a partir de um literal inteiro, um literal flutuante (removendo todos os decimais) ou um literal de string (desde que a string represente um número inteiro)

# float() - constrói um número flutuante a partir de um literal inteiro, um literal flutuante ou um literal de string (desde que a string represente um flutuante ou um inteiro)

# str() - constrói uma string a partir de uma ampla variedade de tipos de dados, incluindo strings, literais inteiros e literais flutuantes

x = int(1)   # Será 1
y = int(2.8) # Será 2
z = int("3") # Será 3
print(x)
print(y)
print(z)

x = float(1)     # Será 1.0
y = float(2.8)   # Será 2.8
z = float("3")   # Será 3.0
w = float("4.2") # Será 4.2
print(x)
print(y)
print(z)
print(w)

x = str("s1") # Será 's1'
y = str(2)    # Será '2'
z = str(3.0)  # Será '3.0'
print(x)
print(y)
print(z)

a = 'Graziele'
b = "Seja bem vindo"
c = '''jgggldldddddddddddddddddddddddddddddddjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj
hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhjjjj''' #colocar 3 aspas pra mudar de linha
d = """jgggldldddddddddddddddddddddddddddddddjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj
hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhjjjj"""

e = "Ola mundo !"

#print(e[1]) #usado pra imprimir APENAS UMA LETRA 

#for x in "Graziele": #imprime letra por letra
    #print(x)

#x = len(e)
#print(len(e))

# IN - procurar se tem determinada condição numa variavel
txt = "Seja bem vindo ao curso de Python"
x = "vindo" in txt
print(x)
print("carro" in txt)


# IF - so executa o bloco de códigos se for verdadeira. No caso (print)
#if "vindo" in txt:
    #print("sim, 'vindo' está presente") #executa
    
if "lucas" in txt:
    print("sim, 'vindo' está presente") #nao aparece

    if "vindo" not in txt:
        print("'vindo' não está presente")

a = "Graziele Oliveira"
b = a.upper()
print(b)
print(a.lower())

a = "  Graziele Oliveira    "
print(a.strip())

a = "Graziele Oliveira"
b = print(a.replace("a", "x"))

a = "Carro, Moto, Caminhão"
print(a.split(","))


idade = 36
txt = "Eu sou Graziele e tenho {} anos de idade"

print(txt.format(idade))

quantidade = 3
item = "bolo"
valor = 14.99
meuPedido = "eu quero {} pedaços de {} por {} reais"
meuPedido2 = "Eu quero pagar {2} reais pelos {0} pedaços de {1}."

print(meuPedido.format(quantidade, item, valor))
print(meuPedido2.format(quantidade, item, valor))

txt = "Somos \"Vinkings\" do norte" #pra poder colocar aspas duplas dentro das aspas duplas
print(txt)
txt = "Ola\nMundo!"
print(txt) 
txt = "Ola\rMundo!"
print(txt) 
txt = "Ola\tMundo!"
print(txt)
txt = "Isso irá inserir um \\ (barra invertida)."
print(txt) 
txt = 'It\'s alright.'
print(txt) 
#Este exemplo apaga um caractere (backspace):
txt = "Ola \bMundo!"
print(txt) #Uma barra invertida seguida por um 'x' e um número hexadecimal representa um valor hexadecimal:
txt = "\x48\x65\x6c\x6c\x6f"
print(txt) 
#Uma barra invertida seguida por três inteiros resultará em um valor octal:
txt = "\110\145\154\154\157"
print(txt) 


# VALORES BOOLEANOS
print(10>9)
print(10==9)
print(10<9)

a = 200
b = 33
if b>a: 
    print("Sim, b é maior do que a")
else:
    print("Não, b não é maior do que a")

print(bool("Ola"))
print(bool(15))
print(bool(["Apple", "Cherry", "banana" ]))

# VALORES QUE RETORNAM FALSOS PORQUE ESTÃO VAZIOS
x = 0
y = ""
print(bool(x)) 
print(bool(y)) 
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

def myFunction():
    return True
print(myFunction())

if myFunction():
    print("sim")
else:
    print("nao")

    x = 200
print(isinstance(x, int))
