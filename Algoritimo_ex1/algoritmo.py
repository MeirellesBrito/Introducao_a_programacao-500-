#algoritmo 23 Entrar comum número inteiro de 3 casas e imprimir o algarismo da casadas deze-nas.
"""a = int(input("digite um valor: "))
d = a % 100 / 10
print("algorsmo da cada das dezenas: ", int(d))"""

#algoritmo 24 Lembre-se sempre disto: quando você montar uma expressão com div e %, se div vier antes de %, coloque parênteses para priorizar uma operação de hierarquia menor.
"""a = int(input("digite um valor: "))
d = (a / 10) % 10
print("algorsmo da cada das dezenas: ", int(d))"""

#algoritmo 25 Entrar com uma data no formato ddmmaa e imprimir: dia, mês e ano separados. 
"""data = int(input("Digite data no formato ddmmaa: "))
dia = data // 10000
mes = data % 10000 / 100
ano = data % 100
print("Dia",int(dia))
print("Mes",int(mes))
print("Ano",int(ano))"""

#algoritmo 26 Entrar com uma data no formato ddmmaa e imprimir no formato mmddaa.
"""data = int(input("Digite data no formato ddmmaa: "))
dia = data // 10000
mes = data % 10000 / 100
ano = data % 100
ndata = mes *10000 + dia * 100 + ano
print("Dia",int(dia))
print("Mes",int(mes))
print("Ano",int(ano))
print("data no formato MMDDAA",int(ndata))"""

#algoritmo 27
"""x = 2
y = 5
print("valor do X e:",x ," valor do Y e:",y)
x + 1
y - 1
print("novo valor do X e :", x , "novo valor do Y e :",y)"""

#algoritmo 28 Imprimir a mensagem: "É PRECISO FAZER TODOS OS ALGORITMOS PARA APRENDER". 
"""print("E PRECISO FAZER TODOS OS ALGORITMOS PARA APRENDER")"""

#algoritmo 29 Imprimir seu nome. 
"""nome = input("<Seu nome >") 
print(nome)"""

#algoritmo 30 Criar um algoritmo que imprima o produto entre 28 e 43. 
"""produto = 28 * 43
print("O produto entre os dois e: ", int(produto))"""

#algoritmo 31 Criar um algoritmo que imprima a média aritmética entre os números 8, 9 e 7.
"""ma = (8 + 9 + 7) / 3
print("A media aritmetica e: ", float(ma))"""

#algoritmo 32 Ler um número inteiro e imprimi-lo.
"""num = int(input("entre com um numero: "))
print(num)"""

#algoritmo 33 Ler dois números inteiros e imprimi-los
"""x = int(input("entre com um numero: "))
b = int(input("entre com outro numero: "))
print("1 Numero:", x)
print("2 Numero:", b)"""

#algoritmo 34 Ler um número inteiro e imprimir seu sucessor e seu antecessor.
"""x = int(input("digite um numero"))
print("no sucessor e:", x + 1, " o antecessor e:", x - 1)"""

#algoritmo 35 Ler nome, endereço e telefone e imprimi-los. 
"""nome = input("Nome ")
endereco = input("Endereço ")
telefone = input("Telefone ")
print("Nome",nome,"Endereco: ",endereco ,"Telefone: ", telefone)"""

#algoritmo 36 Ler dois números inteiros e imprimir a soma. Antes do resultado, deverá aparecer a mensagem: Soma.
"""a = int(input("digite o primeiro valor: "))
b = int(input("digite o segundo valor: "))
print("Soma :",a + b)"""

#algoritmo 37 Ler dois números inteiros e imprimir o produto.
"""a = int(input("entre com um numero: "))
b = int(input("entre com outro numero: "))
print("produto: ", a * b)"""

#algoritmo 38 Ler um numero real(float) e imprimir a terça parte deste numero
"""a = float(input("entre com um numero com ponto: "))
print("na terça parte e: ", a /3)"""

#algoritmo 39 Entrar com dois numeros reais(float) e imprimir a media aritmética com a mensagem media antes do resultado
"""nota1 = float(input("digite 1 nota "))
nota2 = float(input("digite 2 nota "))
nota3 = float(input("digite 3 nota "))
print("Media", (nota1 + nota2 + nota3)/ 3)"""

#algoritmo 40 Entrar com dois numeros inteiros e imprimir a seguinte saída:
"""val1 = int(input("nentre com o dividendo: "))
val2 = int(input("entre com divisor: "))
print("dividendo:", val1, " divisor:",val2, " quociente:",val1 / val2," resto:",val1 % val2)"""

#algoritmo 41 Entrar com quatro números e imprimir a média ponderada, sabendo-se que os pesos são respectivamente: 1, 2, 3 e 4. 
"""a = float(input("entre com 1 numero: "))
b = float(input("entre com 2 numero: "))
c = float(input("entre com 3 numero: "))
d = float(input("entre com 4 numero: "))
print("Media ponderada: ", (a*1 + b*2 + c*3 + d*4)/10)"""

#algoritmo 42 Entrar com um ângulo em graus e imprimir: seno, co-seno, tangente, secante, co-secante e co-tangente deste ângulo. 
"""angulo = float(input("digite um angulo em graus: "))
import math
rang = angulo*math.pi /180
print("seno", math.sin(rang))
print("co-seno:", math.cos(rang))
print("tangente:", math.tan(rang))
print("co-secante:", 1/math.sin(rang))
print("secante:", 1/math.cos(rang))
print("secante:", 1/math.tan(rang))"""

#algoritmo 43 Entrar com um número e imprimir o logaritmo desse número na base 10
"""numero = float(input("entre com um numero: "))
import math
print("logaritmo: ", math.log(numero) / math.log(10))"""

#algoritmo 44 Entrar com o número e a base em que se deseja calcular o logaritmo desse número e imprimi-lo. 
"""num = float(input("entre com o logaritando: "))
base = float(input("entre com a base: "))
import math
logaritmo = math.log(num) / math.log(base)
print("O logaritmo deb",num,"bna baseb",base,"be:b",logaritmo)"""

#algoritmo 45 Entrar com um número e imprimir a seguinte saída:
"""num = float(input("DIgite um numero: "))
import math
quad = num **2
raizqiad = math.pow(num,1/2) #http://www.bosontreinamentos.com.br/programacao-em-python/como-calcular-a-raiz-quadrada-de-um-numero-em-python/
print("numero: ",num)
print("quadrado: ",quad)
print("raiz quadrada: ",raizqiad)"""

#algoritmo 46 Fazer um algoritmo que possa entrar com o saldo de uma aplicação e imprima o  novo saldo, considerando o reajuste de 1%.
"""saldo = float(input("Digite Saldo: "))
print("Novo Saldo: ", saldo * 1.50) # 1% = 1.02| 5%=1.05 | 50%= 1.50"""

#algoritmo 47 Entrar com um número no formato CDU e imprimir invertido: UDC. (Exemplo: 123, sairá 321.) O número deverá ser armazenado em outra variável antes de ser impresso.
"""num = int(input("entre com um numero de 3 digitos: "))
c = num / 100
d = num % 100 / 10
u = num % 10
print("Numero: ",num)
print("invertido: ",int(u*100 + d*10 + c)) #erro no (c)"""

#algoritmo 48 Antes de o racionamento de energia ser decretado, quase ninguém falava em quilowatts; mas, agora, todos incorporaram essa palavra em seu vocabulário.
# Sabendo-se que 100 quilowatts de energia custa um sétimo do salário mínimo, fazer um algoritmo que receba o valor do salário mínimo e a quantidade de quilo watts gasta por uma residência e calcule. Imprima: 
"""real = float(input("Entre com o salario minimo: "))
qtdade = float(input("entre com a quantidade em quilowatt: "))
# divide por 7 para achar o preço de 100 Kw e por 100 para achar de 1 Kw
preco = real / 700
vp = preco * qtdade
vd = vp * 0.9
print("preco do quilowatt:" , preco, " valor a ser pago:",vp," valor com desconto: ", vd)"""

#algoritmo 49 Entrar com um nome e imprimir
"""todo nome: 
primeiro caractere: 
ultimo caractere: 
do primeiro ate o terceiro: 
quarto caractere: 
todos menos o primeiro: 
os dois ultimos:"""
"""nome = str(input("entre com o nome: "))
print("todo nome: ",nome)
print("Primeiro caractere",nome[0])
print("ultimo caractere: ",nome[-1])
print("primeiro ao terceiro caractere: ",nome[0:3])
print("quarto caracter: ",nome[3])
print("todos menos o primeiro: ",nome[1:])
print("os dois ultimos: ",nome[-2:])"""

#algoritmo 50 Entrar com a base e a altura de um retângulo e imprimir a seguinte saída: perimetro area diagonal: 
"""base = float(input("DIgite base: "))
altura = float(input("Digite altura: "))
import math
perimetro = 2*(base + altura)
area = base*altura
diagonal = math.pow(base**2 + altura**2 , 1/2)
print("perimetro = ", perimetro)
print("area = ", area)
print("diagonal = ",diagonal)"""

#algoritmo 51 Entrar com o raio de um cfrculo e imprimir a seguinte saída: peri metro: area:
"""import math
raio = float(input("Digite raio :"))
perimetro = 2* math.pi*math.pow(raio, 1/2)
area = math.pi*math.pow(raio, 1/2) **2
print("perimetro: ", perimetro)
print("area: ",area)"""

#algoritmo 52 Entrar com o lado de um quadrado e imprimir: peri metro: area: diagonal: 
"""import math
lado = float(input("Digite o lado do quadrado: "))
perimetro = 4 * lado
area = lado ** 2
diagonal = lado * math.pow(2,1/2)
print("Perimetro: ",perimetro)
print("Area: ",area)
print("diagonal: ",diagonal)"""

#algoritmo 53 Entrar com os lados a, b, c de um paralelepípedo. Calcular e imprimir a diagonal.
"""import math
a = float(input("Entre com a base: "))
b = float(input("entre com a altura: "))
c = float(input("Entre com a profundidade: "))
diagonal = math.pow(a**2 + b**2 + c**2, 1/2)
print("diagonal: ",diagonal)"""

#algoritmo 54 Criar um algoritmo que calcule e imprima a área de um triângulo.
"""a = float(input("Entre com a base: "))
b = float(input("Entre com a altura de um triangulo: "))
print("Area =",(a*b)/2)"""

#algoritmo 55 Criar um algoritmo que calcule e imprima a área de um losango. 
"""diagmaior = float(input("media da diagonal maior: "))
diagmenor = float(input("Medida da diagonal menor: "))
area = (diagmaior * diagmenor)/2
print("Area = ",area)"""

#algoritmo 56 entrar com nome e idade. imprimir a seguinte saida: nome , idade:
"""nome = str(input("DIgite o nome: "))
idade = int(input("Diite a idade: "))
print("")
print("nome =",nome)
print("Idade = ",idade)"""

#algoritmo 57 Entrar com as notas da PR 1 e PR2 e imprimir a média final: truncada: arredondada: 
"""pr1 = float(input("Digite a pr1: "))
pr2 = float(input("Digite a pr2: "))
mf= (pr1 + pr2)/2
print("MEdia trucada = ",float(mf - 0.5)+0.001)
print("Media arredondada =",int(mf+0.001))"""

#algoritmo 58
"""from math import log

xnum1 = float(input("Informe x1: "))
xnum2 = float(input("Informe x2: "))
xnum3 = float(input("Informe x3: "))

x = xnum1 + (xnum2 / (xnum3 + xnum1)) + 2 * (xnum1 - xnum2) + log(64) / log(2)

print("X = {:.2f}".format(x))"""
#algoritmo 59
"""import math

co = float(input("Insira o cateto oposto: "))
ca = float(input("Insira o cateto adjacente: "))

hipotenusa = math.hypot(co, ca)

print("A hipotenusa é {:.2f}".format(hipotenusa))"""

#algoritmo 60
"""pa = float(input("Insira o primeiro termo: "))
razao = float(input("Insira a razão: "))

dec = pa + 9 * razao

print("O 10° termo desta P.A é : {:.2f}".format(dec))"""
#algoritmo 61
"""pg = float(input("Insira o primeiro termo: "))
razao = float(input("Insira a razão: "))

quinto = pg * razao ** 4

print("O 5° termo desta P.G é: {:.2f}".format(quinto))
#algoritmo 62
produto = float(input("Insira o valor do produto: "))

preco = produto - (produto * 9) / 100

print("Preço com desconto: {:.2f}".format(preco))"""
#algoritmo 63
"""vahr = float(input("Informe o valor da hora-aula: "))
quantidadeAulas = int(input("Informe o número de aulas dadas: "))
percetualDesconto = int(input("Informe o percentual de desconto do INSS: "))

valor = vahr * quantidadeAulas
salarioLiquido = valor - (valor * percetualDesconto) / 100

print("Salário líquido: R${:.2f}".format(salarioLiquido))"""
#algoritmo 64
"""celcius = float(input("Informe a temperatura em C°: "))

f = (9 * celcius + 160) / 5

print("O valor da temperatura {:.2f}C° em fahrenheit é {:.2f}F°".format(celcius, f))"""
#algoritmo 65
"""from cmath import pi

raio = float(input("Informe o raio da lata de óleo: "))
altura = float(input("Informe a altura da lata de óleo: "))

volume = pi * raio**2 * altura

print("O volume da lata é {:.2f}".format(volume))"""
#algoritmo 66
"""velocidade = int(input("Informe a velocidade média: "))
tempo = int(input("Informe o tempo gasto em horas: "))

distancia = velocidade * tempo
litro = distancia / 12

print("A velocidade média é {}km, o tempo gasto na viagem foi de {}h, a distância percorrida foi de {}km e a quantidade de combustível gasto foi de {:.2f} litros".format(velocidade, tempo, distancia, litro))"""
#algoritmo 67
"""valor = float(input("Informe o valor da prestação: "))
taxa = float(input("Informe a taxa da prestação: "))
tempo = int(input("Informe o tempo de atraso(em meses): "))

prest = valor + ((valor * taxa) / 100) * tempo

print("O valor da prestação é de R${:.2f}".format(prest))"""
#algoritmo 68
"""a = int(input("Informe valor de A: "))
b = int(input("Informe valor de B: "))

n1 = b
b = a

print("A = {}, B = {}".format(n1, b))"""
#algoritmo 69
"""numerador = float(input("Informe o numerador: "))
denominador = float(input("Informe o denominador: "))

dec = numerador / denominador

print("O valor da fração em decimal é {:.2f}".format(dec))"""
#algoritmo 70
"""valor = float(input("Informe o valor da conta: "))

newvalor = valor + (valor * 10) / 100

print("O valor total da conta com a gorjeta será de R${}".format(newvalor))"""
#algoritmo 71
"""hora = int(input("Informe a hora atual: "))
minuto = int(input("Informe o minutos: "))

tminuto = hora * 60 + minuto

print("Já se passaram {} minutos".format(tminuto))"""
#algoritmo 72
"""deposito = float(input("Informe o valor do depósito: "))
juros = float(input("Informe a taxa de juros: "))

valorTotal = deposito + (deposito * juros) / 100

print("O valor total depois do rendimento é R${}".format(valorTotal))"""
#algoritmo 73
"""from math import trunc

num = float(input("Digite um número real: "))

print("Parte inteira: {}".format(trunc(num)))
print("Parte fracionária: {}".format(num % (trunc(num))))
print("Número arredondado: {}".format(round(num)))"""

#algoritmo 74
"""salMin = float(input("Informe o valor do salário minimo: "))
salPess = float(input("Informe o valor do salario da pessoa: "))

total = salPess / salMin

print("A pessoa ganha {:.2f} salários minimos!".format(total))"""

#algoritmo 75 Criar um algoritmo que leia o peso de uma pessoa, só a parte inteira, calcular e
"""imprimir:
o peso da pessoa em gramas
novo peso em gramas se a pessoa engordar 12%"""
"""peso = int(input("entre com seu peso, só a parte inteira: "))
pesogramas = peso *1000
novopeso = pesogramas*1.12
print("\nPeso em gramas: ",pesogramas)
print("Novo peso: ",novopeso)"""

#algoritmo 76 Criar um algoritmo que leia um número entre O e 60 e imprimir o seu sucessor, sabendo
# que o sucessor de 60 é 0. Não pode ser utilizado nenhum comando de seleção e nem de repetição.
"""num = float(input("Digite numero: "))
print("sucessor: ",(num+1) %61)"""

#algoritmo 77 Ler dois números reais e imprimir o quadrado da diferença do primeiro valor pelo segundo e a diferença dos quadrados.
"""a = float(input("Digite 1 numero: "))
b = float(input("Digite 2 numero: "))
d=(a-b)**2
q =a**2 - b**2
print("\no quadrado da diferenca =",d ,"\ndiferenca dos quadrados =", q)"""

#algoritmo 78 Dado um polígono convexo de n lados, podemos calcular o número de diagonais
# diferentes (nd) desse polígono pela fórmula : nd = n (n —3)! 2. Fazer um algoritmo 
# que leia quantos lados tem o polígono, calcule e escreva o número de diagonais 
# diferentes (nd) do mesmo. 
"""n = int(input("Digite o numero de lado do poligono: "))
nd = n * (n - 3)/2
print("Numero de diagonais: ",nd)"""

#algoritmo 79 Uma pessoa resolveu fazer uma aplicação em uma poupança programada. Para calcular seu rendimento, ela deverá fornecer o valor constante da aplicação mensal, 
# ataxa e o número de meses. Sabendo-se que a fórmula usada para este cálculo é:
"""p = float(input("DIgiteo valor da aplocacao: "))
i = float(input("DIgite a taxa (0-1 ): "))
n = int(input("Digite o numero de meses: "))
va = p * (((1+i)**n)-1)/i
print("O valor acumulado e: ",va)"""

#algoritmo 80 Criar um algoritmo que leia a quantidade de fitas que uma locadora de vídeo possui e o valor que ela cobra por cada aluguel, mostrando as informações pedidas a seguir:
""" Sabendo que um terço das fitas são alugadas por mês, exiba o
faturamento anual da locadora;
Quando o cliente atrasa a entrega, é cobrada uma multa de 10% sobre o
valor do aluguel. Sabendo que um décimo das fitas alugadas no mês são
devolvidas com atraso, calcule o valor ganho com multas por mês;
Sabendo ainda que 2% de fitas se estragam ao longo do ano, e um décimo
do total é comprado para reposição, exiba a quantidade de fitas que a locadora
terá no final do ano."""
"""quant = int(input("DIgite a quantidade de fitas: "))
valAluguel = float(input("Digite o valor do aluguel: "))
fatAnual = quant/3 * valAluguel*2
print("\n Faturamento anual: ",fatAnual)
multas=valAluguel*0.1*(quant/3)/10 
print("\n Multa mensais: ",multas)
quantFinal = quant - quant *0.02 + quant/10; #quant * 1.08
print("\n Quantidade fitas no final do ano: ",quantFinal)"""

#algoritmo 81 Criar um algoritmo que, dado um número de conta corrente com três dígitos, retorne o seu dígito verificador, o qual é calculado da seguinte maneira:
"""conta = int(input("Digite conta de tresdigitos: "))
d1 = conta /100
d2 = conta %100 / 10
d3 = conta % 100 % 10
inv = d3 *100 + d2 *10 +d1
soma = conta + inv
d1= (soma / 100)*1
d2 = (soma % 100 /10)*2
d3 = (soma %100 %10)*3
#print("02* teste d1",int(d1),"teste d2",int(d2),"teste d3",int(d3))
#print("teste: ",int(d1+d2+d3))
digito= int((d1+d2+d3)%10)
print("\nDigito verificador: ",int(digito))"""

#algoritmo 83 Ler um número e, se ele for positivo, imprimir seu inverso; caso contrário, imprimir o valor absoluto do número.
"""numero = float(input("Digite numro: "))
if(numero > 0):
    print("invalido: ",1/ numero)
else:
    print("absoluto: ",numero * (-1))
    print("absoluto: ",numero)"""

#algoritmo 84 Ler um número e imprimir se ele é par ou ímpar.
"""a = int(input("Digite o numero: "))
if (a % 2 ==0):
    print("Numero PAR") 
else:
    print("Numero IMPAR") """  

#algoritmo 85 Muitas vezes, em algumas aplicações, sentiremos a necessidade de tomar
#outras decisões dentro de uma das alternativas da estrutura do se; a isso
#chamamos de ses aninhados. Vejamos um exemplo clássico de algoritmos:
"""a = float(input("DIgite 1 numero: "))
b = float(input("DIgite 2 numero: "))
c = float(input("DIgite 3 numero: "))
if(a > b):
    if(a >c):
        max=a
    else:
        max=c
else:
    if (b>c):
        max=b
    else:
        max = c
print("\n",max)"""

#algoritmo 86 Ler um número e imprimir se ele é positivo, negativo ou nulo.
"""num = float(input("Digite numero: "))
if(num > 0):
    print("POSITIVO")
else:
    if (num<0):
        print("NEGATIVO")
    else:
        print("NULO")"""

#algoritmo 87
"""resp = input("Qual a capital do Brasil? ")
if (resp == "BRASÍLIA" or resp == "Brasília"):
    print("PARABÉNS")
else:
    if(resp== "brasília" or resp=="BRASÍLIA" or resp=="Brazilia" or resp=="brazilia"):
        print("\nCERTO! Mas atenção para grafia: Brasília ou BRASÍLIA")
    else:
        print("ERRADO! estude mais!")"""

#algoritmo 88  Algoritmo Calculadora
#print("""\n\n\t\t\t\t*************
#\t\t\t\t*CALCULADORA*
#\t\t\t\t+ para somar
#\t\t\t\t- para subtrair
#\t\t\t\t* para multiplocar
#\t\t\t\t/ para dividir 
#\t\t\t\t*************""")
"""resp = input("DIgite opcao: ")
if(resp=="+"):
    a = float(input("DIgite o primeiro numero com ponto: "))
    b = float(input("Digite o senundo numero com ponto: "))
    print("SOMA: ",a+b)
else:
    if(resp=="-"):
        a = float(input("DIgite o primeiro numero com ponto: "))
        b = float(input("Digite o senundo numero com ponto: "))
        print("SUBTRACAO: ",a-b)
    else:
        if(resp=="*"):
            a = float(input("DIgite o primeiro numero com ponto: "))
            b = float(input("Digite o senundo numero com ponto: "))  
            print("MULTIPLICACAO: ",a*b)
        else:
            if(resp=="/"):
                a = float(input("DIgite o primeiro numero com ponto: "))
                b = float(input("Digite o senundo numero com ponto: ")) 
                print("DIVISAO: ",a/b)
            else:
                print("\nOPCAO NAO DISPONIVEL!!") """

#algoritmo 89
"""print("planetas que podem ser analisados: \n[1] Mercurio \n[2] Venus \n[3] Marte"
"\n[4] Jupiter \n[5] Saturno \n[6] Urano")
op = int(input("escolha o planeta a ser analisado: "))
if (op > 6 or op < 0):
    print ("Valor invalido")
else:
    pterra = float(input("Entre com um peso na terra: "))
    match op:
        case 1:
            print(f"Seu peso no planeta terra é: {(pterra/10)*.37}")
        case 2:
            print(f"Seu peso no planeta terra e: {(pterra/10)*0.88}")
        case 3:
            print(f"Seu peso no planeta terra e: {(pterra/10)*0.38}")
        case 4:
            print(f"Seu peso no planeta terra e: {(pterra/10)*2.64}")
        case 5:
            print(f"Seu peso no planeta terra e: {(pterra/10)*1.15}")
        case 6:
            print(f"Seu peso no planeta terra e: {(pterra/10)*1.17}")"""

#algoritmo 90 Entrar com um número e imprimi-lo caso seja maior que 20.
"""num = int(input("Digite um numero: "))
if (num > 20):
    print(num)"""

#algoritmo 91 Construir um algoritmo que leia dois valores numéricos inteiros e efetue a adição; caso o resultado seja maior que 10, apresentá-lo.
"""num1 = int(input("Digite 1 numero: "))
num2 = int(input("Digite 2 numero: "))
soma = num1 + num2
if(soma >10):
    print("Soma: ",soma)"""

#algoritmo 92 Construir um algoritmo que leia dois números e efetue a adição. Caso o valor somado seja maior que 20, este deverá ser apresentado somando-se a ele mais 8;
#caso o valor somado seja menor ou igual a 20, este deverá ser apresentado subtraindo-se 5.
"""num1 = float(input("Digite 1 numero: "))
num2 = float(input("Digite 2 numero: "))
soma = num1 + num2
if(soma >20. ):
    print("SOma: ",soma+8)
else:
    print("Soma: ",soma-5)"""

#algoritmo 93 Entrar com um número e imprimir a raiz quadrada do número caso ele seja positivo e o quadrado do número caso ele seja negativo.
"""numero = float(input("Digite um numero: "))
import math
if(numero >0):
    print("Raiz: ",math.pow(numero, 1/2))
else:
    if(numero<0):
        print("Quadrado: ", numero **2)"""

#algoritmo 94 Entrar com um número e imprimir uma das mensagens: é multiplo de 3 ou não é multiplo de 3.
"""numero = int(input("Digite numero:"))
if (numero %3 ==0 ):
    print("Multiplo de 3")
else:
    print("Nao e multiplo de 3")"""

#algoritmo 95 Entrar com um número e informar se ele é ou não divisível por 5.
"""numero = int(input("Digite um numero: "))
if(numero %5 ==0):
    print("E Divisivel por 5")
else:
    print("Nao e divisivel por 5")"""

#algoritmo 96 Entrar com um número e informar se ele é divisível por 3 e por 7.
"""numero = int(input("Digite o Numero: "))
if(numero % 3 == 0 and numero % 7 == 0):
    print("Divisivel por [3] e por [7]")
else:
    print("Nao e divisivel por [3] e por [7]")"""

#algoritmo 97 Entrar comum número e informarse ele é divisívelpor 10, por 5, por2 ouse não é divisível por nenhum destes.
"""numero= int(input("digite numero: "))
if (numero %10==0):
    print("Multiplo de [10]")
else:
    if(numero %2 ==0):
        print("Miltiplo de [2]")
    else:
        if(numero % 5==0):
            print("Muntiplo de [5]")
        else:
            print("Nao e Multiplo de [2] nem de [5]")"""

#algoritmo 98 A prefeitura do Rio de Janeiro abriu uma linha de crédito para os funcionários estatutários. O valor máximo da prestação não poderá ultrapassar 30% do salário
#bruto Fazer um algoritmo que permita entrar com o salário bruto e o valor da prestação e informar se o empréstimo pode ou não ser concedido.
"""sb = float(input("Digite o salario: "))
vp = float(input("Digite o valor da prestacao: "))
if(vp <=0.3 *sb):
    print("Emprestimo concedido")
else:
    print("Emprestimo negado")"""

#algoritmo 99 Ler um número inteiro de 3 casas decimais e imprimir se o algarismo da casa das centenas é par ou ímpar.
"""num=int(input("Numero de 3 algarismo: "))
c=num /100
if(c%2==0):
    print("O algarismo das centenas e par: ",c)
else:
    print("O algarismo das centenas e impar: ",c)"""

#algoritmo 100 Ler um número inteiro de 4 casas e imprimir se é ou não múltiplo de quatro o número 
# formado pelos algarismos que estão nas casas das unidades de milhar e das centenas.
"""num=int(input("Numero de 4 algarismo: "))
c = num /100
if(c % 4 == 0):
    print("o numero e multiplo de 4: ",c)
else:
    print("O numero nao e multiplo de 4: ",c)"""

#algoritmo 101 Construir um algoritmo que indique se o número digitado está compreendido entre 20 e 90 ou não.
"""num = float(input("Digite um numero "))
if( num > 20. and num < 90. ):
    print("O numeri esta na faixa de 20 a 90, exclusive")
else:
    print("O numero esta fora da faixa de 20 a 90")"""

#algoritmo 102 Entrar com um número e imprimir uma das mensagens: maior do que 20, igual a 20 ou menor do que 20.
"""numero = float(input("Digite um numero: "))
if(numero > 20):
    print("Maior que 20")
else:
    if(numero <20):
        print("Menor que 20")
    else:
        print("Igual a 20")"""

#algoritmo 103 Entrar com o ano de nascimento de uma pessoa e o ano atual. Imprimira idade da
#pessoa. Não se esqueça de verificar se o ano de nascimento é um ano válido.
"""anoa = int(input("Entre com ano atual: "))
anon = int(input("Entre comano de nascimento: "))
if(anon > anoa):
    print("Ano de Nacimento Invalido")
else:
    print("Idade: ",anoa-anon)"""

#algoritmo 104 Entrar com nome, sexo e idade de uma pessoa. Se a pessoa for do sexo feminino e
#tiver menos que 25 anos, imprimir nome e a mensagem: ACEITA. Caso contrário,
#imprimir nome e a mensagem: NÃO ACEITA. (Considerar f ou F.)
"""nome = input("Digite Nome: ")
sexo = input("Digite sexo: ")
idade = int(input("Digite idade: "))
if ((sexo =="F" or sexo=="f") and idade<25):
    print(nome,"ACEITO")
else:
    print(nome,"NAO ACEITO")"""

#algoritmo 105 Entrar com a sigla do estado de uma pessoa e imprimir uma das mensagens:
"""sigla = input("Digite sigla: ")
if(sigla =="RJ" or sigla=="rj"):
    print("Carioca")
else:
    if(sigla=="SP" or sigla == "sp"):
        print("Paulista")
    else:
        if(sigla=="MG" or sigla=="mg"):
            print("Mineiro")
        else:
            print("outro estado")"""

#algoritmo 106 Entrar com um nome e imprimi-lo se o primeiro caractere for a letra A (considerar letra minúscula ou maiúscula).
"""nome = input("Digite seu nome: ")
letra = nome[0]
if(letra=="A" or letra =="a"):
    print(": ",nome)"""

#algoritmo 107 Entrar com o nome de uma pessoa e so imprimi-lo se o prenome for JOSE
"""nome = str(input("DIgite Seu nome completo: "))
if(nome[:4] =="JOSE"  or nome[-4:]=="JOSE"):
    print("",nome)"""

#algoritmo 108 Idem ao anterior, porém considerar: JOSÉ, José ou josé.
"""nome =input("DIgite Seu nome completo: ")
if(nome[:4] =="JOSE" or nome[:4] =="jose" or nome[:4] =="Jose"  or nome[-4:]=="JOSE" or nome[-4:]=="jose" or nome[-4:]=="Jose"):
    print("",nome)"""

#algoritmo 109 Criar um algoritmo que entre com dois nomes e imprimi-los em ordem alfabética.
"""nome1 = input("Digite o 1 nome: ")
nome2 = input("Digite o 2 nome: ")
if(nome1<nome2):
    print(nome1,"",nome2)
else:
    print(nome2," ",nome1)"""

#algoritmo 110 Criar um algoritmo que leia dois números e imprimir uma mensagem dizendo se são iguais ou diferentes.
"""a = float(input("DIgite o 1 numero: "))
b = float(input("Digite o 2 numero: "))
if(a==b):
    print("Iguais")
else:
    print("Diferentes")"""

#algoritmo 111 Entrarcom dois números e imprimir o maiornúmero (suponha números diferentes).
"""a = input("DIgite 1 numero: ")
b = input("DIgite 2 numero: ")
if(a>b):
    print("maior:",a)
else:
    print("menor:",b)"""

#algoritmo 112 Entrar com dois números e imprimir o menor numero (suponha números diferentes).
"""a = input("DIgite 1 numero: ")
b = input("DIgite 2 numero: ")
if(a<b):
    print("menor:",a)
else:
    print("maior:",b)"""

#algoritmo 113 Entrar com dois números e imprimi-los em ordem crescente (suponha números diferentes).
"""a = input("DIgite 1 numero: ")
b = input("DIgite 2 numero: ")
if(a<b):
    print(a," ",b)
else:
    print(b," ",a)"""

#algoritmo 114 Entrar com dois números e imprimi-los em ordem decrescente (suponha números diferentes).
"""a = input("DIgite 1 numero: ")
b = input("DIgite 2 numero: ")
if(a>b):
    print(a," ",b)
else:
    print(b," ",a)"""

#algoritmo 115 Criar o algoritmo que deixe entrar com dois números e imprimir o quadrado do menor número e a raiz quadrada do maior número, se for possível.
"""a = float(input("DIgite 1 numero: "))
b = float(input("DIgite 2 numero: "))
import math
if(a>b):
    print(math.pow(a,1/2),"",b**2)
else:
    if(b>a):
        print("",math.pow(b,1/2),"",a**2)
    else:
        print("Numero iguais")"""

#algoritmo 116 Entrar com três números e imprimir o maior número (suponha números diferentes).
"""a = float(input("DIgite 1 numero: "))
b = float(input("DIgite 2 numero: "))
c = float(input("DIgite 3 numero: "))
if(a>b):
    if(a>c):
        print("Maior: ",a)
    else:
        print("Maior: ",c)
else:
    if(b>c):
        print("Maior: ",b)
    else:
        print("Maior: ",c)

a = float(input("DIgite 1 numero: "))
b = float(input("DIgite 2 numero: "))
c = float(input("DIgite 3 numero: "))
if(a>b or a>c):
    print("Maior: ",a)
else:
    if(b>c):
        print("Maior: ",b)
    else:
        print("Maior: ",c)"""

#algoritmo 117 Entrar com três nu" meros e armazenar o maior numero na varia" vel de nome maior(suponha números diferentes)
"""a = float(input("DIgite 1 numero: "))
b = float(input("DIgite 2 numero: "))
c = float(input("DIgite 3 numero: "))
maior=0
if(a>b):
    Maior = a
else:
    Maior = b
if(c > maior):
    maior=c
print("Maior: ",maior)

a = float(input("DIgite 1 numero: "))
b = float(input("DIgite 2 numero: "))
c = float(input("DIgite 3 numero: "))
maior=a
if(b>maior):
    maior=b
if(c > maior):
    maior=c
print("maior: ",maior)"""

#algoritmo 118 Entrar com três números e imprimi-los em ordem crescente (suponha números diferentes).
"""a = float(input("DIgite 1 numero: "))
b = float(input("DIgite 2 numero: "))
c = float(input("DIgite 3 numero: "))
if (a>b):
    aux=a;a=b;b=aux
if(a>c):
    aux=a;a=c;c=aux
if(b>c):
    aux=b;b=c;c=aux
print("Ordem Cresecnte: ",a," ",b," ",c)"""

#algoritmo 119 Entrar com três números e imprimi-los em ordem decrescente (suponha números diferentes).
"""a = float(input("DIgite 1 numero: "))
b = float(input("DIgite 2 numero: "))
c = float(input("DIgite 3 numero: "))
if (a>b):
    aux = a; a = b; b = aux
if(a>c):
    aux = a; a = c; c = aux
if(b>c):
    aux =b;b = c; c = aux;
    aux=b;b=c;c=aux
print("Ordem Cresecnte: ",c," ",b," ",a)"""

#algoritmo 120 Entrar com três números e armazená-los em três variáveis com os seguintes nomes maior, intermediário e menor (suponha numeros diferentes)
"""a = float(input("DIgite 1 numero: "))
b = float(input("DIgite 2 numero: "))
c = float(input("DIgite 3 numero: "))
intermediario =0
menor=0
if(a>b):
    if(c>a):
        maior=c
        intermediario=c
        menor=b
    else:
        if(c>b):
            maior = a
            intermediario = c
            menor=b
else:
    if(c>b):
        maior=c
        intermediario=b
        menor=a
    else:
        maior=b
        intermediario=a
        menor=c

print("\nMaior:",maior)
print("Intermediario:",intermediario)
print("Menor:",menor)
print("\n")

a = float(input("DIgite 1 numero: "))
b = float(input("DIgite 2 numero: "))
c = float(input("DIgite 3 numero: "))
if(a>b):
    aux=a;a=b;b=aux
if(a>c):
    aux=a;a=c;c=aux
if(b>c):
    aux=b;b=c;c=aux
maior=c
intermediario=b
menor=a
print("\nMaior:",maior)
print("Intermediario:",intermediario)
print("Menor:",menor)
print("\n")"""

#algoritmo 121 Efetuara leitura de cinco números inteiros diferentes e identificar o maior e o menorvalor.
"""n1 = float(input("DIgite 1 numero: "))
n2 = float(input("DIgite 2 numero: "))
n3 = float(input("DIgite 3 numero: "))
n4 = float(input("DIgite 4 numero: "))
n5 = float(input("DIgite 5 numero: "))
intermediario =0
menor=0
if(n1 != n2 or n1 != n3 or n1 != n4 or n1 !=n5 or n2!=n3 or n2!= n4 or n2!=n5 or n3!=n4 or n3!=n5 or n4!=n5):
    if(n1>n2):
        maior =n1; menor =n2
    else:
        maior = n2; menor=n1
    if(n3>maior):
        maior=n3
    else:
        if(n3<menor):
            menor=n3
    if(n4>maior):
        maior=n4
    else:
        if(n4<menor):
            menor=n4
        if(n5>maior):
            maior=n5
        else:
            if(n5<menor):
                menor=n5
                print("Maior= ",maior)
                print("Menor= ", menor)
else:
    print("Os valores devem ser diferentes")"""

#algoritmo 122 Ler três números e imprimir se eles podem ou não ser lados de um triângulo.
"""a=float(input("DIgite 1 lado: "))
b=float(input("DIgite 2 lado: "))
c=float(input("DIgite 3 lado: "))
if(a<b+c or b<a+c or c<a+b):
    print("\n Podem ser lados de triangulo")
else:
    print("\nNao podem ser lador de um triangulo")"""
    
#algoritmo 123 Ler três números, os possíveis lados de um triângulo, e imprimira classificação se gundo os lados
"""a=float(input("DIgite 1 lado: "))
b=float(input("DIgite 2 lado: "))
c=float(input("DIgite 3 lado: "))
if(a<b+c or b<a+c or c<a+b):
    if(a==b or a==c):
        print("Triangulo equilatero")
    else:
        if(a==b != a==c != b==c):
            print("Triangulo isosceles")
        else:
            print("triangulo escaleno")
else:
    print("As medidas nao formam um triangulo")"""

#algoritmo 124 Ler três números, os possíveis lados de um triângulo, e imprimira classificação segundo os ângulos.
"""a=float(input("DIgite 1 lado: "))
b=float(input("DIgite 2 lado: "))
c=float(input("DIgite 3 lado: "))
if( a<b+c or b<a+c or c<a+b):
    if(a>b or a>c):
        maior =a**2; lados=b**2+c**2
    else:
        maior = c **2; lados=a**2+b**2
    if(maior==lados):
        print("Triangulo Retangulo")
    else:
        if(maior>lados):
            print("Trianulo Obtusangulo")
        else:
            print("Triangulo Acutangulo")
else:
    print("\nAs medidas nao foram um triangulo")"""

#algoritmo 125 Entrar com a idade de uma pessoa e informar se é maior de idade se é menor deidade se é maior de 65 anos 
"""idade = int(input("Digite sua idade: "))
if(idade>=65):
    print("Maior de 65")
else:
    if(idade>=18):
        print("Maior de idade")
    else:
        print("Menor de idade")"""

#algoritmo 126 Ler um número e imprimir se ele é iguala 5, a 200, a 400, se está no intervalo entre 500 e 1000, inclusive, ou se ele está fora dos escopos anteriores.
"""x= float(input("Digite valor de x: "))
if (x==5.):
    print("O numero e o 5")
else:
    if(x==200.):
        print("O numero e o 200")
    else:
        if(x==400.):
            print("O numero e o 400 ")
        else:
            if( x >=500. or x <=1000.):
                print("Interevalo 500-1000")
            else:
                print("Fora do escopo")"""

#algoritmo 127 Entrar com nome, nota da PR e nota da PR2 de um aluno. Imprimir nome, nota da PR1, nota da PR2, média e uma das mensagens: Aprovado, Reprovado ou em
#Prova Final (a média é 7 para aprovação, menor que 3 para reprovação e as demais em prova final).
"""nome=input("Digite nome: ")
nota1=float(input("Digite 1 nota: "))
nota2=float(input("Digite 2 nota: "))
media = (nota1+nota2)/2
if(media>=7):
    print(nome," ",media,"AP")
else:
    if(media<3.):
        print(nome," ",media,"RP")
    else:
        print(nome," ",media,"PF")"""

#algoritmo 128 Entrar com um verbo no infinitivo e imprimir uma das mensagens:  verbo não está no infinitivo
# verbo da 1 conjugação
# verbo da 2 conjugação
# verbo da 3 conjugação
"""verbo = input("Digite um verbo: ")
letra = verbo[-1]
fin = verbo[-2:]
if(letra == "R" or letra == "r"):
    if(fin == 'ar' or fin == "AR"):
        print("verbo da 1° conjugação")
    
    elif(fin == 'er' or fin == "ER"):
        print("verbo da 2° conjugação")
        
    elif(fin == "ir" or fin == "IR"):
        print("Verbo da 3° conjugação")
    else:
        print("Não existe verbo com terminação ur")
else:
    print("Não é um verbo no infinitivo")"""
    

#algoritmo 129 Entrar com o salário de uma pessoa e imprimir o desconto do INSS segundo a tabela a seguir
#menor ou igual a R$ 600,00 isento 
#maior que R$ 600,00 e menor ou igual a R$ 1200,00 20% 
#maior que R$ 1200,00 e menor ou igual a R$2000,00 25% 
#maior que R$ 2000,00 
"""salario= float(input("Digite o salario: "))
if(salario <= 600):
    desconto = 0
else:
    if(salario<=1200):
        desconto = salario*0.25
    else:
        desconto=salario*0.30
print("Desconto: ",desconto)"""

#algoritmo 130 Um comerciante comprou um produto e quer vendê-lo com um lucro de 45% se o valor da compra for menor que R$ 20,00; caso contrário, o lucro será de 30%. Entrar com o valor do produto e imprimir o valor da venda.
"""valor=float(input("Digite valor do produto: "))
if(valor <20):
    print("Valor de venda: ",valor *1.45)
else:
    print("Valor de venda: ",valor*1.3)"""

#algoritmo 131 A turma de Programação 1, por ter muitos alunos, será dividida em dias de provas. 
#Após um estudo feito pelo coordenador, decidiu-se dividi-la em três grupos. 
#Fazer um algoritmo que leia o nome do aluno e indicar a sala em que ele deverá 
#fazer as provas, tendo em vista a tabela a seguir e sabendo-se que todas as salas 
#se encontram no bloco F:
"""nome=input("Digite o nome: ")
L=nome
if((L>="A" and L<="K") or (L>="a" and L<="k")):
    print("\n",nome," sala:102")
else:
    if((L>="L" and L<="N") or (L>="l" and L<="n")):
        print("\n",nome," sala:102")
    else:
        if((L>="O" and L<="Z") or (L>="o" and L<="z")):
            print("\n",nome," sala:103")
        else:
            print("NOME INVALIDO")"""

#algoritmo 132 Fazer um algoritmo que possa converter uma determinada quantia dada em reais para uma das seguintes moedas: 
# f- franco suíço 
# / - libra esterlina 
# d - dólar 
# m - marco alemão
"""r = float(input("DIgite valor em reais a ser convertido: "))
moeda=input(" Digite (f- franco suico) (l - libra esterlina) (d - dolar) (m- marco alemao): ")
if(moeda=="f" or moeda=="F"):
    f=float(input("digite valor de um franco suico em reais: "))
    print("Total de francos suicos: ",r/f)
else:
    if(moeda=="l" or moeda=="L"):
        l= float(input("DIgite valor de uma libra esterlina em reais: "))
        print("Total de libras esterlinas: ", r /l)
    else: 
        if(moeda =="d" or moeda=="D"):
            d= float(input("DIgite valor de um dolar em reais: "))
            print("Total de dolares: ", r /d)
        else:
            if(moeda=="m" or moeda=="M"):
                m = float(input("Digite valor de um marco alemao em reais: "))
                print("TOtal de marcos alemaes: ",r/m )
            else:
                print("Moeda desconhecida")"""

#algoritmo 133 Segundo uma tabela medica o peso ideal esta relacionado com a altura e o sexo 
#Fazer um algoritmo que receba a altura e o sexo de uma pessoa, calcular e imprima o seu peso ideal utilizando as seguintes formulas m
#para homens: (72.7 * H) -58 
#para mulheres (62 1 * H) -44 7
"""h=float(input("Entre com a altura: "))
sexo= input("Entre com o sexo M / F: ")
if(sexo=="M" or sexo=="m"):
    peso=72.7*h-58
else:
    peso = 62.1 *h -44.7
print("Seu peso ideal e: ",peso)"""

#algoritmo 134 A confederação brasileira de natação irá promover eliminatórias para o próximo 
#mundial Fazer um algoritmo que receba a idade de um nadador e imprimir a sua 
#categoria segundo a tabela a seguir: 
"""idade=int(input("Entre com a idade: "))
if(idade <5):
    print("Na exite categoria para essa idade")
else:
    if(idade<=7):
        print("Categoria Infantil A")
    else:
        if(idade < 10):
            print("Categoria Infantil B")
        else:
            if(idade<=13):
                print("Categoria Infantil A")
            else:
                if(idade<=13):
                    print("Categoria Juvenil A")
                else:
                    if(idade<=17):
                        print("Categoria Juvenil B") 
                    else:
                        print("Categoria Senior")"""

#algoritmo 135 Criar um algoritmo que leia a idade de uma pessoa e informara sua classe eleitoral: 
# não-eleitor (abaixo de 16 anos) 
# eleitor obrigatório (entre 18 e 65 anos) 
#eleitor facultativo (entre 16 e 18 anos e maior de 65 anos)
"""idade=int(input("Entre com a idade: "))
if(idade <16):
    print("Nao eleitor ")
else:
    if(idade> 65):
        print("Eleitor facultativo")
    else:
        print("Eleitor facultativo")"""

#algoritmo 136 Depois da liberação do governo para as mensalidades dos planos de saúde, as 
#pessoas começaram a fazer pesquisas para descobrir um bom plano, não muito 
#caro. Um vendedor de um plano de saúde apresentou a tabela a seguir. Criar um 
#algoritmo que entre com o nome e a idade de uma pessoa e imprimir o nome e o 
#valor que ela deverá pagar. 
# ate l0 anos -R$ 30 00 
# acima de 10 até 29 anos - R$ 60,00 
#acima de 29 até 45 anos - R$ 120,00 
# acima de 45 até 59 anos - R$ 150,00 
# acima de 59 até 65 anos - R$ 250,00 
# maior que 65 anos - R$ 400,0
"""nome=input("Entre com nome: ")
idade=int(input("Entre com a idade: "))
if(idade<=10):
    print("\n",nome," pagara R$30,00")
else:
    if(idade<=29):
        print("\n",nome," pagara R$60,00")
    else:
        if(idade<=45):
            print("\n",nome," pagara R$120,00")
        else:
            if(idade<=59):
                print("\n",nome," pagara R$150,00")
            else:
                if(idade<=65):
                    print("\n",nome," pagara R$250,00")
                else:
                    print("\n",nome," pagara R$400,00")"""

#algoritmo 137 Ler três valores inteiros (variáveis a, b e c) e efetuar o cálculo da equação de segundo grau, apresentando: as duas raízes, separa os valores informados for pos- sívelfazero cálculo (deita positivo ou zero); a mensagem "Não há raízes reais", se 
#não for possível fazer o cálculo (deita negativo); e a mensagem "Não é equação 
#do segundo grau", se o valor de a for iguala zero. 
"""import math
a=float(input("Entre com o Valor de a: "))
c=float(input("Entre com o Valor de c: "))
b=float(input("Entre com o Valor de b: "))
if(a==0):
    print("Nao e esquacao de 2 grau")
else:
    d=b**2-4*a*c
    if(d>=0):
        d= math.pow(d,1/2)
        x1=(-b+d)/(2*a)
        x2=(-b-d)/(2*a)
        print("\nX1=",x1,"\t\tX2=",x2)
    else:
        print("\n Nao ha raizes reais")"""

#algoritmo 138 Ler um número inteiro entre 1 e 12 e escrever o mês correspondente. Caso o 
#usuário digite um número fora desse intervalo, deverá aparecer uma mensagem 
#informando que não existe mês com este número. 
"""num= int(input("DIgite um numero de 1 -12: "))

if(num==1):
    print("Janeiro")
else:
    if(num==2):
        print("fevereiro")
    else:
        if(num==3):
            print("Marco")
        else:
            if(num==4):
                print("abril")
            else:
                if(num==5):
                    print("maio")
                else:
                    if(num==6):
                        print("junho")
                    else:
                        if(num==7):
                            print("julho")
                        else:
                            if(num==8):
                                print("agosto")
                            else:
                                if(num==9):
                                    print("setembro")
                                else:
                                    if(num==10):
                                        print("outrubro")
                                    else:
                                        if(num==11):
                                            print("novembro")
                                        else:
                                            if(num==12):
                                                print("dezembro")
                                            else:
                                                print("Nao existe mes correspondente")"""

#algoritmo 139 Sabendo que somente os municípios que possuem mais de 20.000 eleitores aptos têm segundo turno nas eleições para prefeito caso o primeiro colocado não 
#tenha mais do que 50% dos votos, fazer um algoritmo que leia o nome do município, a quantidade de eleitores aptos, o número de votos do candidato mais votad
"""nome = input("digite nome do Municipio: ")   
ne= int(input("nuero de eleitores aptos: "))
votos= int(input("Numero de votos do candidato mais votado: "))
if(ne >20000 and votos <= ne/2):
    print("\n",nome ,"terá segundo turno")
else:
    print("\n",nome ,"nao tera segundo turno")"""

#algoritmo 140 Um restaurante faz uma promoção semanal de descontos para clientes de acordo 
#com as iniciais do nome da pessoa. Criar um algoritmo que leia o primeiro nome 
#do cliente, o valor de sua conta e se o nome iniciar com as letras A, D, M ou 5, dar 
#um desconto de 30%. Para o cliente cujo nome não se inicia por nenhuma dessas 
#letras, exibir a mensagem "Que pena. Nesta semana o desconto não é para seu 
#nome; mas continue nos prestigiando que sua vez chegara".
"""nome = input("Digite nome: ")
vc=int(input("Digite valor da conta: "))
L=nome[0]
if(L=="A" or L=="a" or L=="D" or L=="d" or L=="M" or L=="m" or L=="S" or L=="s"):
    print("\n",nome," Valor da conta com desconto: R$ ",vc*0.7)
else:
    print("Que pena. Nesta semana o desconto não é para seu nome; mas continue nos prestigiando que sua vez chegará")"""

#algoritmo 141 Criar um algoritmo que leia o nome e o total de pontos de três finalistas de um 
#campeonato de pingue-pongue e exibir a colocação da seguinte forma: 
#Vencedor:_______ XXXX ptos 
#Segundo colocado: XXXX ptos 
#Terceiro colocado: XXXX ptos 
"""n1= input("DIgite 1 nome: ")
p1= int(input("DIgite pontos: "))
n2= input("DIgite 2 nome: ")
p2= int(input("DIgite pontos: "))
n3= input("DIgite 3 nome: ")
p3= int(input("DIgite pontos: "))
aux= int =0
if(p1 < p2):
    aux = p1; p1 = p2; p2 = aux; auxn = n1; n1 = n2; n2 = auxn
if(p1 < p3):
    aux = p1; p1 = p3; p3 = aux; auxn = n1; n1 = n3; n3 = auxn
if(p2 < p3):
    aux = p2; p2 = p3; p3 = aux; auxn = n2; n2 = n3; n3 = auxn
print("\nVENCEDOR : ", n1, " ",p1, " pontos")
print("\nSEGUNDO COLOCADO : ", n2, " ",p2, " pontos")
print("\nTERCEIRO COLOCADO: ", n3, " ",p3, " pontos")"""

#algoritmo 142 Em um campeonato nacional de arco-e-flecha, tem-se equipes de três jogadores 
#para cada estado. Sabendo-se que os arqueiros de uma equipe não obtiveram o 
#mesmo número de pontos, criar um algoritmo que informe se uma equipe foi 
#classificada, de acordo com a seguinte especificação: 
# ler os pontos obtidos por cada jogador da equipe; 
# mostrar esses valores em ordem decrescente; 
# se a soma dos pontos for maior do que 100, imprimir a média aritmética 
# entre eles; senão, imprimir a mensagem "Equipe desclassificada '
"""p1 = int(input("Digite os pontos do primeiro jogador: "))
p2 = int(input("Digite os pontos do segundojogador: "))
p3 = int(input("Digite os pontos do terceiro jogador: "))
aux=0
if(p1>p2):
    aux= p1 ; p1= p2; p2= aux
if(p1>p3):
    aux= p1 ; p1= p3; p3= aux
if(p2>p3):
    aux= p2 ; p2= p3; p3= aux
print("\npl=", p1, "\np2=", p2, "\np3=",p3)
soma = p1+p2+p3
if(soma>100):
    print("Media=",soma/3.2)
else:
    print("Equipe desclassificada!")"""

#algoritmo 143 Criar um algoritmo que verifique a(s) letra(s) central(is) de uma palavra Se o numero de caracteres for ímpar, ele verifica se a letra central é uma vogal; caso cont
"""
ppalavra = input("Informe uma palavra: ")

contagem = len(palavra)

if(contagem % 2 == 0):
    print('Par')

else:
    print('Ímpar')"""

#algoritmo 144 O banco XXX concederá um crédito especial com juros de 2% aos seus clientes de 
#acordo com o saldo médio no último ano. Fazer um algoritmo que leia o saldo médio de um cliente e calcule o valor do crédito de acordo com a tabela a seguir. 
#Imprimir uma mensagem informando o saldo médio e o valor do crédito. 
#SALDO MÉDIO PERCENTUAL 
#de O a 500 nenhum crédito 
#de 501 a 1000 30% do valor do saldo médio 
#de 1001 a 3000 40% do valor do saldo médio 
#acima de 3001 50% do valor do saldo médio 
"""saldomedio= float(input("Digite saldo medio: "))
if(saldomedio<501.):
    credito=0.
else:
    if(saldomedio<1001.):
        credito = saldomedio *0.3
    else:
        if(saldomedio<3001.):
            credito=saldomedio*0.4
        else:
            credito=saldomedio*0.5
if(credito!= 0.):
    print("Como seu saldo era de:",saldomedio,"seu credito sera de:",credito)
else:
    print("\nComo seu saldo era de:", saldomedio, 8 ,"voce nao tera nenhum credito")"""

#algoritmo 145 A biblioteca de uma universidade deseja fazer um algoritmo que leia o nome do 
#livro que será emprestado, o tipo de usuário (professor ou aluno) e possa imprimir um recibo conforme mostrado a seguir. Considerar que o professor tem dez 
#dias para devolver o livro e o aluno só três dias. 
#Nome do livro 
#Tipo de usuário: 
# Total de Dias:
"""livro = input("Digite nome do Livro: ")
tipo = input("Digite: professor/aluno: ")
if(tipo == "professor" or tipo == "Professor" or tipo == "PROFESSOR"):
    dia=10
else:
    if(tipo == "aluno" or tipo == "Aluno" or tipo == "ALUNO"):
        dia=3
    else:
        dia=0
    if(dia==0):
        print("Tipo de usuario desconhecido")
    else:
        print("\n\nnome do livro: ",livro)
        print("nome tipo e usuarui: ",tipo)
        print("total de dias: ",dia)"""

#algoritmo 146 Fazer um algoritmo que leia o percurso em quilômetros, o tipo do carro e informe 
#o consumo estimado de combustível, sabendo-se que um carro tipo C faz 12 km 
#com um litro de gasolina, um tipo B faz 9 km e o tipo C, 8 km por litro. 
"""tipo=input("Digite tipo de carro(A / B / C): ")
percurso=float(input("Digite percurso: "))
if(tipo=="C" or tipo == "c"):
    consumo=percurso/12
else:
    if(tipo=="B" or tipo=="b"):
        consumo = percurso/10
    else:
        if(tipo=="A" or tipo=="a"):
            consumo = 0
    if(consumo!=0.):
        print("\nConsumo estimado em litros: ",consumo)
    else:
        print("\nModelo inexistente")"""

#algoritmo 147 Criar um algoritmo que informe a quantidade total de calorias de uma refeição a 
#partir da escolha do usuário 'que deverá informar o prato, a sobremesa e bebida 
"""caloria=0
op=int(input("Digite (1-Vegetariano) (2-peixe) (3-frango) (4-carne): "))
if(op==1):
    caloria=caloria+180
else:
    if(op==2):
        caloria=caloria+230
    else:
        if(op==3):
            caloria=caloria+250
        else:
            if(op==4):
                caloria=caloria+350
op=int(input("\nDigite (1- Abacaxi) (2-soverte diet) (3-Suco de melao) (4-refrigerante diet): "))
if(op==1):
    caloria=caloria+75
else:
    if(op==2):
        caloria=caloria+110
    else:
        if(op==3):
            caloria=caloria+170
        else:
            if(op==4):
                caloria=caloria+200
op=int(input("\nDigite (1-cha) (2-Suco de laranja) (3-Mousse diet) (4-musse de chocolate): "))
if(op==1):
    caloria=caloria+20
else:
    if(op==2):
        caloria=caloria+70
    else:
        if(op==3):
            caloria=caloria+100
        else:
            if(op==4):
                caloria=caloria+65
print("Total de calorias: ",caloria)"""

#algoritmo 148 Criar um algoritmo que leia o destino do passageiro, se a viagem inclui retorno 
#(ida e volta) e informar o preço da passagem conforme atabela a seguir.
"""op= int(input("\nDigite (1- Regiao Norte) (2- Regiao Nordeste) (3- Regiao Centro-Oeste) (4-Regiao Sul): "))
iv = int(input("Digite (1-Ida) (2-Ida e Volta) :"))
if(op ==1):
    if(iv==1):
        print("\nO valor da passagem de ida para R.Norte R$500.00")
    else:
        print("\nO valor da passagem de ida-volta para R.Norte: R$950.00")
else:
    if(op==2):
        if(op==1):
            print( "\nO valor da passagem de ida para R.Sul: R$300.00")
        else:
            print("\nO valor da passagem de ida-volta para R.Sul: R$550.00")
    else:
        print("Opcao Inecistente")"""

#algoritmo 149 Um comerciante calcula o valor da venda, tendo em vista a tabela a seguir:
#Criar o algoritmo que possa entrar com nome do produto e valor da compra e imprimir o nome do produto e o valor da venda. 
"""vvenda =0
nomep=(input("Digite nome do produto: "))
vcompra=float(input("Digite valor da compra: "))
if(vcompra<10.):
    vvenda=vcompra*1.7
else:
    if(vcompra<30.):
        vvenda=vcompra*1.5
    else:
        if(vcompra<50.):
            vvenda=vcompra*1.4
            vvenda=vcompra*1.3
print("\n " , nomep, " sera vendido por R$",vvenda + 0.001)"""

#algoritmo 150 Criar um algoritmo que leia um ângulo em graus e apresente: 
# o seno do ângulo, se o ângulo pertencer a um quadrante par; 
# o co-seno do ângulo, se o ângulo pertencer a um quadrante ímpar.
"""import math
ang=float(input("Digite angulo em grus: "))
rang=ang*math.pi/180
if((rang > math.pi/2 and rang<=math.pi) or (rang>3*math.pi/2 and rang <=2-math.pi)):
    print("seno: ",math.sin(rang))
else:
    print("con-seno: ",math.cos(rang))"""

#algoritmo 151 Um endocrinologista deseja controlar a saúde de seus pacientes e, para isso, se 
#utiliza do Índice de Massa Corporal (IMC). Sabendo-se que o lMCé calculado através da seguinte fórmula:
"""peso=float(input("Digite peso: "))
altura=float(input("Diite altura: "))
imc = peso/altura**2
if(imc<20):
    print("abaixo do peso")
else:
    if(imc<=25):
        print("normal")
    else:
        if(imc<=30):
            print("execsso de peso")
        else:
            if(imc<=35):
                print("obesidade ")
            else:
                print("O obesidade norbida")"""

#algoritmo 152 Criar um algoritmo que a partir da idade e peso do paciente calcule a dosagem de 
#determinado medicamento e imprima a receita informando quantas gotas do 
#medicamento o paciente deve tomar por dose Considere que o medicamento em 
#questão possui 500 mg por ml e que cada ml corresponde a 20 gotas 
#Adultos ou adolescentes desde 12 anos, inclusive, se tiverem peso igual ou 
#acima de 60 quilos devem tomar 1000 mg; com peso abaixo de 60 quilos devem 
#tomar 875 mg. 
#Para crianças e adolescentes abaixo de 12 anos é dosagem é calculada pelo 
"""peso=float(input("Digite peso: "))
idade=int(input("Digite idade: "))
gotas=500/20
if(peso<5):
    print("nao pode tomar remedio porquenao tem peso (Consulte um medico)")
else:
    if(idade>=12):
        if(peso>=60):
            print("Tomar",100/gotas," gotas")
        else:
            print("Tomar ",875/gotas," Gotas")
    else:
        if(peso<=9):
            print("Tomar ",125/gotas," gotas")
        else:
            if(peso<=16):
                print("Tomar ",250/gotas," gotas")
            if(peso <= 24):
                print("Tomar ",375/gotas," gotas")
            else:
                if(peso<=30):
                    print("Tomar ",500/gotas," gotas")
                else:
                    print("Tomar ",750/gotas," gotas")"""

#algoritmo 153 O prefeito do Rio de Janeiro contratou uma firma especializada para manter os níveis 
#de poluição considerados ideiais para um país do 1 2mundo. As indústrias, maiores 
#responsáveis pela poluição, foram classificadas em três grupos. Sabendo-se que a 
#escala utilizada varia de 0,05 e que o índice de poluição aceitável até 0, 25, fazer um 
#algoritmo que possa imprimir intimações de acordo com o índice e a tabela a seguir:
#índice indústrias que receberão intimação 
# 0,3       1 grupo 
# 0,4       1 e 2 grupos 
# 0.5       1 , 2 e 3 grupos 
"""indice = float(input("Digite indice de poluicao: "))
if(indice>=0.5):
    print("\nsuspender atividades as industrias dos grupos 1, 2 e 3")
else:
    if(indice>=0.4):
        print("\nsuspender atividades as industrias dos grupos 1 e 2 ")
    else:
        if(indice>=0.3):
            print("\nsuspender atividades as industrias dos grupos 1 ")
        else:
            print("\nindice de poluicao aceitavel para todos os grupos ")"""

#algoritmo 154 
"""placa=input("Digite placa: ")
p = placa[0]
if(p=="1"):
     print("Janeiro")
else:
    if(p=="2"):
        print("fevereiro")
    else:
        if(p=="3"):
            print("Marco")
        else:
            if(p=="4"):
                print("abril")
            else:
                if(p=="5"):
                    print("maio")
                else:
                    if(p=="6"):
                        print("junho")
                    else:
                        if(p=="7"):
                            print("julho")
                        else:
                            if(p=="8"):
                                print("agosto")
                            else:
                                if(p=="9"):
                                    print("setembro")
                                else:
                                    if(p=="0"):
                                        print("outrubro")
                                    else:
                                        print("\nOpcao invalida")"""

#algoritmo 155 Ler uma palavra e, se ela começar pela letra L ou D (também deve ser considerado 
#1 ou d), formar uma nova palavra que terá os dois primeiros caracteres e o último, 
#caso contrário a nova palavra será formada por todos os caracteres menos o primeiro. 
"""pal=input("Digite palavra: ")
letra=pal[0]
if(letra =="l" or letra =="L" or letra =="d" or letra =="D"):
    pal1=pal[:2]
    pal2=pal[-2:]
    print("teste",pal1+pal2)
else:
    pal1=pal[1:]
    print("palavra: ",pal1)"""

#algoritmo 156 Criar um algoritmo que leia uma data (dia, mês e ano em separado) e imprima se a data é válida ou não. 
"""dia=int(input("Digite o dia: "))
mes=int(input("Digite o mes: "))
ano=int(input("Digite o ano: "))
if(ano>=1):
    vd=1
    if(mes<1 or mes> 12 or dia<1 or dia>31):
        vd=0
    else:
        if((mes==4 or mes==6 or mes==9 or mes==11) and dia>30):
            vd=0
        else:
            if(mes==2):
                if((ano % 4==0 and ano % 100 !=0)or ano %400==0):
                    if(dia>29):
                        vd=0
                else:
                    if(dia>28):
                        vd=0
    print("DATA VALIDA")                    
else:
    vd=0
    if(vd==0):
        print("DATA INVALIDA")"""

#algoritmo 157 Criar um algoritmo que leia uma data (no formato ddmmaaaa) e imprimir se a data e valida ou não
"""data=int(input("Data no formato ddmmaaaa  "))
dia = data / 1000000
mes = data % 1000000 / 10000
ano = data %10000
if(ano>=1):
    vd=1
    if(mes<1 or mes> 12 or dia<1 or dia>31):
        vd=0
    else:
        if((mes==4 or mes==6 or mes==9 or mes==11) and dia>30):
            vd=0
        else:
            if(mes==2):
                if((ano % 4==0 and ano % 100 !=0)or ano %400==0):
                    if(dia>29):
                        vd=0
                else:
                    if(dia>28):
                        vd=0
    print(data,"DATA VALIDA")                  
else:
    vd=0
    if(vd==0):
        print("DATA INVALIDA")"""

#algoritmo 158 Criar um algoritmo que entre com o valor dex calcule e imprima o valor de f(x)
"""x=float(input("Digite o valor de x: "))
if(x!=2.):
    fx=8/(2-x)
    print("f(x)=",fx)
else:
    print("NAO PODE SER FEITA")"""

#algoritmo 159 Criar um algoritmo que entre com o valor dex calcule e imprima o valor de f(x) 
"""import math
x=float(input("Digite o valor de x: "))
if(x>4. or x<(-4.)):
    fx=(5*x+3)/math.pow(x**2-16,1/2)
    print("f(x)=",fx)
else:
    print("NAO PODE SER FEITA")"""

#algoritmo 160 ntrar com o valor de x e imprimir y:
"""x=float(input("Digite o valor de x: "))
if(x<=1.):
    y=1.
else:
    if(x<=3.):
        y=x**2
    else:
        y=x**3
print("valor de f(x)=",y)"""

#algoritmo 161 Criar um algoritmo que entre com cinco números e imprimir o quadrado de cada número.
"""c=0
while(c<=4):
    c+=1
    num=float(input("Numero: "))
    print("Quadrado: ",num**2)"""
 
#algoritmo 162 Criar um algoritmo que imprima todos os números pares no intervalo 1-10
"""c=0
while(c<=9):
    c+=2
    print("Numero: ",c) """
    
#algoritmo 163   
"""voltaLagoa = 0
abdominais = 1
while (voltaLagoa<=3):  
    print("\n",voltaLagoa,"a volta na Logoa")
    voltaLagoa+=1
    while(abdominais<=5):
        print("\n ", abdominais, "o abdominal")
        abdominais += 1"""

#algoritmo 164
"""a=1
print("Comecei")
while(a<=50000):
    a+=1
    print(a)
print("FIM") """   
    
#algoritmo 165    
"""a=1
print("zona 1")
while(a<=8):
    a+=1
    print("zona",a)"""
    
#algoritmo 166
"""L=0
c=0
print("\nTODOS\n")
while(L<=9):
    L+=1
    while(c<=9):
        c+=1 
        print(c,"-",L,"\t")  """
        
#algoritmo 167  
"""L=0;c=0;t=0
print("\nACIMA DA DIAGONAL PRINCIPAL\n")
while(L<=8):
    L+=1
    while(c<=9):
        c+=1 
        print("\t",L,"-",c) 
        while(t<=L):
            t+=1
            print("\t")"""
 
#algoritmo 168 
"""import pandas as pd


ordem = 10

matriz: str = ([[0 for x in range(ordem)] for x in range(ordem)])

for i in range(ordem):
    for j in range(ordem):
      if i == j:
        matriz[i][j] = i+1, j+1


print("Com Pandas")        

df = pd.DataFrame(matriz)
print(df)

print("")
print("Maneira antiga")
for i in range(1, 11):
    print("\n")
    for j in range(1, 11):
        if i == j:
          print(f"{i}-{j}  ", end='  ')
        else:
            print("  ", end="   ") """

#algoritmo 169
"""L=1;c=0
print("\nABAIXO DA DIAGONAL PRINCIPAL\n")
while(L<=9): 
    L+=1
    print("") 
    while(c<L):
        c+=1
        print(L,"-",c,"")"""
        
#algoritmo 170  
"""L=1;c=0
print("\nACIMA DA DIAGONAL SECUNDARIA\n")
while(L<=8): 
    L+=1
    while(c<10-L):
        c+=1
        print(c,"-",L,"") """     
          
#algoritmo 171
""" print("\nDIAGONAL SECUNDARIA\n")
L=1;t=10-L
while(L<=8): 
    L+=1
    while(t>=1):
        t-=1
        print(t,"-",11-L,"")  """  
#algoritmo 172 
""" print("\nABAIXO DA DIAGONAL SECUNDÁRIA\n")
L=2;t=11-L;c=12-L
while(L<=10): 
    L+=1
    while(t>=1):
        t-=1
        while(c<=10):
            c+=1
            print(t,"-",c,"") """   

#algoritmo 173
"""L=0;c=0
print("\nT ODOS\n")
while(L<=9): 
    L+=1
    while(c<=9): 
        c+=1
        print(L, "-" ,c, "\t")"""   

#algoritmo 174 Imprimir todos os números de 1 até 100.
"""a=0
while(a<=99): 
    a+=1
    print(a)"""
    
#algoritmo 175 Imprimir todos os números de 100 até 1.
"""a=101
while(a>=2): 
    a-=1
    print(a) """  
    
#algoritmo 176 Imprimir os 100 primeiros pares. 
"""a=0
while(a<=199): 
    a+=1+1
    print(a)"""
    
#algoritmo 177 Imprimir os múltiplos de 5, no intervalo de 1 até 500. 
"""a=5
while(a<=499): 
    print(a) 
    a+=5"""   
    
#algoritmo 178 Imprimir o quadrado dos numeros de 1 ate 20 
"""   a=1
while(a<=20):
    a+=1
    print(a^2)"""   
   
#algoritmo 179 Criar um algoritmo que imprima os numeros pares no intervalo de 1 a 600      
""" i=2
while(i<=198):
    i+=2
    print(i)""" 
    
#algoritmo 180 Criar um algoritmo que imprima os números de 120 a 300.
""" i=119
while(i<=299):
    i+=1
    print(i)""" 
    
#algoritmo 181 Criar um algoritmo que imprima todos os numeros de 1 ate 100 e a soma deles
""" i=0
while(i<=99):
    i+=1
    print(i)
print("\nSomatorio de 1 a 100 e :",i+i)""" 

#algoritmo 182 Entrar com 10 números e imprimir a metade de cada número. 
""" i=0
while(i<=9):
    i+=1
    numero= float(input("Digite Numero: "))
    print("METDADE: ",numero/2)""" 
    
#algoritmo 183 Entrar com 10 números e imprimir o quadrado de cada número. 
""" i=0
while(i<=9):
    i+=1
    numero= float(input("Digite Numero: "))
    print("METDADE: ",numero**2)"""
    
#algoritmo 184  Entrar com 8 números e, para cada número, imprimir o logaritmo desse número na base 10. 
"""import math
i=0
while(i<=7):
    i+=1
    numero= float(input("Digite Numero: "))
    if(numero>0):
        print("METDADE: ",math.log(numero)/math.log(10))
    else: 
        print("\nNao fao logaritmo de numero negativo")"""  
    
#algoritmo 185 Entrar com 15 números e imprimir a raiz quadrada de cada número. 
"""  import math
i=0
while(i<=14):
    i+=1
    numero= float(input("Digite Numero: "))
    if(numero>0):
        print("Raiz: ",math.pow(numero,1/2))
    else: 
        print("\nNao fao Raiz de numero negativo")"""      

#algoritmo 186 Entrar com quatro números e imprimir o cubo e a raiz cúbica de cada número.
"""   import math
i=0
while(i<=3):
    i+=1
    numero= float(input("Digite Numero: "))
    print("Cubo: ",numero**3)
    if(numero>0):
        print("Raiz: ",numero**(1/3))
    else: 
        print("\nNao fao Raiz de numero negativo")"""
    
#algoritmo 187 Criar um algoritmo que calcule e imprima o valor de b". O valor de n deverá ser maior do que 1 e inteiro e o valor de b maior ou igual a 2 e inteiro.   
""" base= int(input("Digite a base inteira e maior do que 1: "))    
expo= int(input("Digite expoente inteiro maior que 1:  "))
i=0
if(base>=2 and expo>1):
    pot=1
    while(i<=expo):
        pot*=base
        i+=1
        print("potencia: ", pot)
else:
    print("Nao satisfazem")""" 

#algoritmo 188 Criar um algoritmo que imprima uma tabela de conversão de polegadas para centímetros. Deseja-se que na tabela conste valores desde 1 polegada até 20 polegadas inteiras. 
"""print("Conversao de polegadas para centimetros")
L=0
while(L<=20):
    L+=1
    print("\n", L, " equivale(m) a ",L*2.54, "II cm")"""
    
#algoritmo 189 Criar um algoritmo que imprima a tabela de conversão de graus Celsius-Fahrenheit 
#para o intervalo desejado pelo usuário. O algoritmo deve solicitar ao usuário o li - mite superior, o limite inferior do intervalo e o decremento. 
#Fórmula de conversão: C =5 (F - 32) / 9
""" f1=int(input("entre com a temperatura maior em Fahrenheit: "))
f2=int(input("entre com a temperatura menor em Fahrenheit: "))
dec=int(input("entre com decremento: "))
t=f1
while(t>=f2):
    t=t-dec
    print("temperatura em graus Cesius: ",5*(t-32)/9)""" 
     
#algoritmo 190 Entrar com um nome, idade e sexo de 20 pessoas. Imprimir o nome se a pessoa for do sexo masculino e tiver mais de 21 anos. 
"""i=0
while(i<=10):
    nome=str(input("Digite seu nome: "))
    sexo=str(input("Digite seu sexo: "))
    idade=int(input("Digite sua idade: "))
    if(sexo[0]=="m" or sexo[0]=="M" and idade>=21):
        print("\n",nome)"""
 
#algoritmo 191 Criar um algoritmo que leia um nÚmero que será o limite suprior de um intervalo e 
#o incremento (incr) Imprimir todos os numeros naturais no intervalo de O ate esse 
#numero Suponha que os dois numeros lidos são maiores do que zero Exemplo
"""limite=int(input("Digite o numero limite: "))
incr= int(input("e o incremento pressionando: ")) 
i=0
while(i<=limite):
    i=i+incr
    print(i," ")"""   

#algoritmo 192 Criar um algoritmo que leia um número que será o limite superior de um intervalo 
#e imprimir todos os números ímpares menores do que esse número. Exemplo: 
#Limite superior: 15     Saída: 1 3 5 7 9 11 13     
"""  num=int(input("Digite um numero: "))
vf=num-3
i=-1
while(i<=vf):
    i=i+2
    print(i)"""  
    
#algoritmo 193 Criar um algoritmo que leia um número que servirá para controlar os números pares que serão impressos a partir de 2. 
# Exemplo: Quantos: 3    Saída: 2 4 6 8   
"""  num=int(input("Digite um numero: "))
vf=num*2
i=0
while(i<=vf):
    i=i+2
    print(i)"""      
    
#algoritmo 194 Criar um algoritmo que leia um número e imprima todos os números de 1 até o número lido e o seu produto.
# Exemplo: número: 3 Saída: 1 2 3 4     
"""      num=int(input("Digite um numero: "))
i=0
produto=1
while(i<=num):
    i+=1
    produto*=i
    print(i," ")
print("Produto de 1 a ",num,": ",produto)"""      

#algoritmo 195 Criar um algoritmo que imprima a soma dos números pares entre 25 e 200. 
""" soma=0
i=26
while(i<=198):
    i+=2
    soma+=i
    print(i,"Soma 26-200: ",soma)"""    
    
#algoritmo 196 Criar um algoritmo que leia um número (num) e imprima a soma dos números múltiplos dé 5 no intervalo aberto entre 1 e num. Suponha que num será maior que zero.     
""" soma =0
i=5
num=int(input("Digite um numero maior que zero: "))
num=num-1
while(i<num):
    i+=5
    soma+=i
    print("Soma dos multiplos de 5: ",soma)""" 

#algoritmo 197 Criar um algoritmo que leia um número que servirá para controlar os primeiros números ímpares. Deverá ser impressa a soma desses números. Suponha que num será maior que zero. 
#Quantos: 5 Saída: 25 
#( 1 3 5 7 9) - primeiros ímpares
""" num=int(input("Digite um numero maior que zero: "))
impar=0
i=1
while(i<=num*2 ):
    i+=2
    impar+=i
    print("",impar)""" 

#algoritmo 198 Criar um algoritmo que leia os limites inferior e superior de um intervalo e impri - ma todos os números naturais no intervalo fechado. Suponha que os dados digitados são para um intervalo crescente. Exemplo: 
"""ini=int(input("Limite inferior,: "))
f=int(input("Limite superior: "))
i=ini
while(i<=f):
    print(i)
    i+=1"""

#algoritmo 199 Criar um algoritmo que leia os limites inferior e superior de um intervalo e impri - ma todos os números múltiplos de 6 no intervalo fechado. Suponha que os dados digitados são para um intervalo crescente. Exemplo: 
#Limite inferior: 5      Saída: 5 11 
#Limite superior: 13 
"""ini=int(input("Limite inferior: "))
f=int(input("Limite superior: "))
i=ini
if(ini % 6 ==0 ):
    ini+=6
else:
    ini=ini+(6-(ini % 6))
    f=f-1
while(i<=f):
    print(i)
    i+=6"""
    
#algoritmo 200 Criar um algoritmo que leia os limites inferior e superior de um intervalo e o número cujos múltiplos se deseja que sejam impressos no intervalo aberto. Suponha que os dados digitados sãopara um intervalo crescente. E    
"""superior = int(input("Digite o limite superior: "))
inferior = int(input("Digite o limite inferior: "))
intervalo = int(input("Digite o intervalo: "))

mult = 0
for i in range(inferior, superior + 1):
    if(i % intervalo == 0):
        print(i)"""

#algoritmo 201  Criar um algoritmo que leia os limites inferior e superior de um intervalo e imprima todos os números pares no intervalo aberto e seu somatório. Suponha que os dados digitados são para um intervalo crescente. 
"""superior = int(input("Digite o limite superior: "))
inferior = int(input("Digite o limite inferior: "))
intervalo = int(input("Digite o intervalo: "))

soma = 0
for i in range(inferior, superior + 1):
    if(i % 2 == 1):
        soma = soma + i       
print(soma)"""
#algoritmo 202 Criar um algoritmo que leia um número (num) da entrada e imprima os múltiplos de 3 e 5 ao mesmo tempo no intervalo de 1 a num. Exemplo
""" num = int(input("Digite um número maior que 15: "))
for i in range(1, num + 1):
    if(i % 3 == 0 and i % 5 == 0):
        print(i) """    

#algoritmo 203 """ """ 
"""num = int(input("Digite a quantidade de números: "))

for i in range(1, num + 1):
    n = int(input(f"Digite o {i}° número: "))
    multi = n * 3
    print(f"Multiplo: {multi}")
     """ 

#algoritmo 204 """ """ 
"""num = int(input("Digite a quantidade de números: "))

maior = 0
for i in range(1, num + 1):
    n = int(input(f"Digite o {i}° número: "))
    if(n > maior):
        maior = n
print(maior)
     """ 

#algoritmo 205
"""quant = int(input("Digite a quantidade de números: "))
num = int(input("Digite um número: "))

maior = num
for i in range(1, quant + 1):
    n = int(input(f"Digite o {i}° número: "))
    if(n > maior):
        maior = n
print(f"Maior: {maior}")
     """ 
#algoritmo 206 
"""quant = int(input("Digite a quantidade de números: "))
num = int(input("Digite um número: "))

maior = num
menor = num
for i in range(1, quant + 1):
    n = int(input(f"Digite o {i}° número: "))
    if(n > maior):
        maior = n
    elif(n < menor):
        menor = n
print(f"Maior: {maior}\nMenor: {menor}")
     """

#algoritmo 207
"""n1 = int(input("Digite o multiplicando: "))
n2 = int(input("Digite o multiplicador: "))

soma = 0
for i in range(1, n2):
    soma = soma + n1

print(f"Produto: {soma}")
     """ 

#algoritmo 208 " 
"""for i in range(1, 11):
    termo = i + i
    print(f"{i}° termo é {termo}") """ 

#algoritmo 209 
"""t1 = int(input("Digite o 1° termo: "))
t2 = int(input("Digite o 2° termo: "))
n = int(input("Número de termos: "))

aux = t1 + t2
for i in range(aux, n + 1):
    termo = aux + i
    print(f"{i}° termo é {termo}") """

#algoritmo 210 
"""t1 = int(input("Digite o 1° termo: "))
t2 = int(input("Digite o 2° termo: "))


aux = t1 + t2
for i in range(aux, 11):
    if(i % 2 == 1):
        termo = aux + i
        print(f"{i}° termo é {termo}")
    else:
        termo = aux - i
        print(f"{i}° termo é {termo}") """

#algoritmo 211 
"""for i in range(10, 101):
    if(i % 10 != 0):
        aux = i // 10
        if(i % aux == 0):    
            print(i) """

#algoritmo 212 
"""soma = 0
for i in range(20):
    quad = i**2
    if(quad < 225):
        soma = soma + i
        print(soma) """

#algoritmo 213 
"""soma = 0
for i in range(1,21):
    nota = float(input(f"Informe a {i}° nota: "))
    soma = soma + nota
print("Média: {:.2f}".format(soma / 20)) """

#algoritmo 214 
"""soma = 0
for i in range(1, 16):
    nome = input("Informe seu nome: ")
    pr1 = float(input("Informe sua 1° nota: "))
    pr2 = float(input("Informe sua 2° nota: "))
    media = (pr1 + pr2) / 2
    print(f"Nome: {nome}, nota 1: {pr1}, nota 2: {pr2} e a média: {media}")
    soma = soma + media
print("Média da sala: {:.2f}".format(soma / 15)) """

#algoritmo 215 
"""num = int(input("Digite um número: "))

for i in range(1, num):
    if(num % i == 0):
        print(i) """

#algoritmo 216 
"""soma = 0
for i in range(1, 201):
    num = int(input("Informe um número: "))
    if(num % 2 == 0):
        soma = soma + 1
print("Pares: {}\nImpares:{}".format(soma, 200 - soma))
"""

#algoritmo 217 
"""for i in range(1, 8):
    nome = input("Digite seu nome: ")
    quant = len(nome)
    print(f"Esse nome tem {quant} letras") """

#algoritmo 218 
"""for i in range(1, 12):
    nome = input("Digite seu nome: ")
    prim = nome[0]
    print(prim) """

#algoritmo 219 
"""vezes = int(input("Informe o números de vezes que deseja imprimir a palavra SOL: "))
for i in range(1, vezes + 1):
    print("Sol")  """

#algoritmo 220 
"""nome = input("Digite seu nome: ")

vezes = len(nome)
for i in range(vezes + 1):
    i = nome
    print(i) """

#algoritmo 221 
"""nome = input("Digite uma palavra: ")
vezes = len(nome)
for i in range(0, vezes):
    print(nome[i]) """

#algoritmo 222 
"""nome = input("Digite uma palavra: ")

vezes = len(nome)
for i in range(1, vezes + 1):
    print(nome[-i], end="") """

#algoritmo 233 
""" n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

if(n1 > n2):
    for i in range(n2, n1 + 1):
        print(i)
else:
    for i in range(n1, n2 + 1):
        print(i)"""


#algoritmo 234 
"""for i in range(10):
    nome = input("Digite seu nome: ")
    salario = float(input("Digite o valor do seu salário bruto: "))
    if(salario < 600):
        print("Nome: {}\nSalário: {:.2f}".format(nome, salario))
    elif(salario >= 600 and salario < 1500):
        salario -= salario * 0.1
        print("Nome: {}\nSalário: {:.2f}".format(nome, salario))
    else:
        salario -= salario * 0.15
        print("Nome: {}\nSalário: {:.2f}".format(nome, salario)) """

#algoritmo 235 
"""maior = 0
menor = -1

for i in range(1, 11):
    n = int(input(f"Digite o {i}° número: "))
    if(n > maior):
        maior = n
        
    else:
        if(n < menor):
            menor = n
print("Maior:",maior)
print("Menor:",menor)          """

#algoritmo 236 
"""termos = int(input("Digite um número: "))
h = 0

for i in range(1, termos):
    h = (h + 1) / i
    print(f"soma: {h:.2f}") """

#algoritmo 237 
"""termos = int(input("Digite um número: "))
h = 0

for i in range(1, termos):
    if(i % 2 == 1):
        h = (h + 1)/ i
    else:
        h = (h - 2)/ i
    print(f"soma: {h:.2f}") """

#algoritmo 238 Ler o numero de termos da serie (N) e imprimir o valor de 5 sendo
"""h=0
num=float(input("Digite numero: "))
n=num
for c in range(1,num+1):
    h+=c/n
    n-=-1
print("Soma: ",h)"""

#algoritmo 239 Implementar um algoritmo para calcular o valor de eX O valor de X devera ser digitado. O valor de eX será calculado pela soma dos 10 primeiros termos da serie a seguir
"""fat=1
x=0
x=float(input("digite valor de x: "))
soma=1.
for c in range(1,9,+1):
    fat=fat*c
    soma=soma+x**c/fat
print("valor de e elevado a ",x,": ",soma)"""

#algoritmo 240 Implementar um algoritmo para calcular o sen(X). O valor de X deverá ser digitado em graus. O valor do seno de Xserá calculado pela soma dos 10 primeiros ter -mos da série a seguir:
"""import math
seno=0.;expden=1
x=float(input("Digite valor de x: "))
x*=math.pow(x,1/2)/180
for c in range(1,10,+1):
    fat=1
    for d in range(1,expden,+1):
        fat*=d
        if(c%2==0):
            seno = seno- x ** expden / fat
        else:
            seno = seno + x ** expden / fat
        expden+=2
print("seno",seno)"""
            
#algoritmo 241 riar um algoritmo que deixe escolher qual a tabuada de multiplicar que se deseja imprimir. 
"""n=int(input("Qual tabuada: "))
if(n>0):
    print("TABUADA do ",n)
    for c in range(1,10,+1):
        print("\n3",c," ",3*c)"""

#algoritmo 242 Criar um algoritmo que deixe escolher qual a tabuada de multiplicar que se deseja imprimir.
"""n=int(input("qual tabuada? "))
if(n>0):
    print("TABUADA do ",n,)
    for c in range(1,10,+1):
        print(n," ",c," ",n*c)
else:
    print("Nao exite tabuada")"""
#algoritmo 243 Entrar com uma mensagem e imprimir quantas letras A E / O e U tem esta mensagem (considerar minúscula e maiúscula)
"""c=0;ce=0;ci=0;co=0;cu=0;ca=0
msg=input("Digite uma mensagem: ")
for L in range(msg[0],+1):
    letra=msg[0]
    if(letra=="a" or letra=="A"):
        ca+=1
    else:
        if(letra=="e" or letra=="E"):
            ce+=1
            if(letra=="i" or letra=="I"):
                ci+=1
                if(letra=="o" or letra=="O"):
                    co+=1
                    if(letra=="u" or letra=="U"):
                        cu+=1
print("Total de letras A: ",ca)
print("Total de letras E: ",ce)
print("Total de letras I: ",ci)
print("Total de letras O: ",co)
print("Total de letras U: ",cu)"""
                
#algoritmo 244 Entrar com uma mensagem e criptogra fá-Ia da seguinte maneira:
"""msg=input("Digite uma mensagem: ")
for L in range(0,msg[0],+1):
    letra=msg[0]
    if(letra=="a" or letra=="A"):
        print("X")
    else:
        if(letra=="e" or letra=="E"):
            print("W")
        else:
            if(letra=="o" or letra=="O"):
                print("K")
            else:
                if(letra=="u" or letra=="U"):
                    print(letra)"""

#algoritmo 245 Criar um algoritmo que receba a idade e o peso de 20 pessoas. Calcular e imprimir 
#as médias dos pesos das pessoas da mesma faixa etária. As faixas etárias são: de 1 
#a 10 anos, de 11 a 20 anos, de 21 a 30 anos e maiores de 30 anos. 
"""p1 =0.; p2=0.; p3 =0.; p4 =0.; c1=0; c2=0; c3=0; c4=0
for l in range(1,21,1):
    idade=float(input("Digite a idade: "))
    peso=float(input("Digite o peso: "))
    if(idade<=10):
        c1+=1;p1+=peso
    else:
        if(idade<=20):
            c2+=1;p2+=peso
        else:
            if(idade<=30):
                c3+=1;p3+=peso
            else:
                c4+=1;p4+=peso
    if(c1!=0):
        print("Media dos pesos 1-10: ",p1/c1)
    else:
        print("Ninguem com idades de 1-10")
        if(c2!=0):
            print("Media dos pesos 11-20")
        else:
            print("Ninguem com idades de 11-20")
        if(c3!=0):
            print("Ninguem com idades de 11-20")
        else:
            print("Ninguem com idades de 21_301")
        if(c4!=0):
            print("Media dos pesos maiores que 30: ")
        else:
            print("Ninguem com idades maiores que 30")"""

#algoritmo 246 No dia da estréia do filme "Senhor dos Anéis 'Ç uma grande emissora de TV reali - zou uma pesquisa logo após o encerramento do filme. Cada espectador respondeu a um questionário no qual constava sua idade e a sua opinião em relação ao 
#filme: excelente -3; bom -2; regular- 1. Criar um algoritmo que receba a idade 
#e a opinião de 20 espectadores, calcule e imprima:
"""idadegot = 0; opexc = 0; opbom = 0; opregular = 0
for i in range(1,15,1):
    idade=float(input("Digite idade: "))
    op=float(input("Digite opiniao: excelente - 3; bom - 2; regular - 1: "))
    if(op==3):
        opexc+=1
        idadegot+=idade
    else:
        if(op==1):
            opregular+=1
        else:
            if(op==2):
                opbom+=1
if(opexc!=0):
    print("Media de idade das pessoas que responderam excelente:",idadegot/ opexc)
else:
    print("Ninguem que tenha escolhido excelente")
if(opregular!=0):
    print("Quantidade de pessoas que responderam regular:")
else:
    print("Ninguem que tenhaescolhido regular")
if(opbom!=0):
    print("A porcentagem das pessoas que respondeu bom: ",opbom*100/15)
else:
    print("Ninguem que tenha escolhido bom")"""

#algoritmo 247 Num campeonato europeu de volleyball, se inscreveram 30 países. Sabendo-se 
#que na lista oficial de cada país consta, além de outros dados, peso e idade de 12 
#jogadores criar um algoritmo que apresente as seguintes informações 
# o peso médio e a idade média de cada um dos times; 
# o peso medio e a idade media de todos os participantes
"""totpeso=0;totid=0
for i in range(1,31,1):
    somapeso=0;somaid=0
    for x in range(1,12,1):
        peso=float(input("Digite peso: "))
        id=float(input("Digite idade: "))
        somapeso+=peso ; somaid+=id
    print("peso medio do tme: ",somapeso/12)
    print("idade media do time: ",somaid/12)
    totpeso+=somapeso; totid+=somaid
print("peso medio de todos os times: ",totpeso/360)
print("idade medio de todos os times: ",totid/360)"""

#algoritmo 248
#algoritmo 249

#algoritmo 250 imprimir todas as tabuadas de multiplicar de 1 ate 10
"""for L in range(1,10,1):
    print("TABUADA DO ",L)
    for c in range(1,10,1):
        r=input("Pressione entre: ")"""

#algoritmo 251 Criar um algoritmo para imprimir uma tabela para DEZ times num torneio de rodada dupla
"""for L in range(1,10,1):
    for c in range(1,10,1):
        if(L!=c):
            print("time:",L," time:",c,"_______")
    r=input("Pressione entre: ")"""

#algoritmo 252 Criar um algoritmo para imprimir uma tabela para DEZ times num torneio de rodada simples. 
"""for L in range(1,9,1):
    for c in range(1,10,1):
        print("ime : ",L, " time : ", c, " ";)
        r=input("Pressione entre: ")"""

#algoritmo 253 Criar um algoritmo que entre com dez mensagens, e, para cada mensagem, imprimir quantas letras A tem (considerar maiúsculas e minúscula
"""for i in range(10):
    ca=0
    msg=input("Digite uma mensagem: ")
    for c in range(0, len(msg)):
        letra=msg[c]
        if(letra=="a" or letra=="A"):
            ca+=1
    print("Total de letras a: ",ca)"""

#algoritmo 254 Criar um algoritmo que entre com dez notas de cada aluno de uma turma de 20 alunos e imprima: 
# a média de cada aluno 
# a média da turma 
# o percentual de alunos que tiveram medias maiores ou iguais a 5.0. 
"""somat=0
cap=0
for L in range(1,20,1):
    somaa=0
    for c in range(1,10,1):
        nota=int(input("Digite ", c,"a nota do aluno ",L,))
        somaa+=nota
    media=somaa/10
    if(media>=5):"""
#algoritmo 255

#algoritmo 256
#algoritmo 257 Criar um algoritmo que leia o valor de N imprima a sequência a seguire o resultado
"""y=int(input("Digite o numero de termos: "))
soma=0;c=0;s=1
for L in range(y,0,-1):
    fat=1
    for z in range(1,L,1):
        fat1=1
        for z in range(1,c,1):
            fat1*=z
            if(s==1):
                print(L,"/",c^2,"! -",soma=soma+fat/(fat1^2))
                s=0
            else:
                print(L,"/",c^2,"! -",soma=soma-fat/(fat1^2))
                s=1
            c+=2"""

#algoritmo 258 Nos exemplos a seguir, mostraremos a importância da chave e da inicialização da variável que faz parte da expressão que controla a re
"""while(num > 0):
    num=float(input("Digite um numero: "))
    print("Dobro do numero: ",num*2)
# Fali: Variável num não-inicializada."""

#algoritmo 259
"""num=float(input("Digite um numero: "))
while(num > 0.):
    print("Dobro do numero: ",num*2)
#Observação: O algoritmo entra em loop"""

#algoritmo 260
"""Explicando: 
Tendo em vista que nossa experiência anterior falhou, nossa segunda tendência 
é deslocar a leitura para fora da estrutura. 
Mas, desta vez, teremos outro problema: o algoritmo entra em Ioop pois nunca mais 
atribuímos valor à variável num. É preciso interromper pressionando <ctrl> <c>. """

"""num=float(input("Digite um numero: "))
while(num > 0.):
    print("Dobro do numero: ",num*2)
    num=float(input("Digite numero: "))"""
    
#algoritmo 261 Simulando a estrutura do faca enquanto 
"""import math

print("MENU-um pouco de tudo")
print("A - Armazena na variavel menor e imprime o nome que tiver o menor numero de caracteres entre tres")
print("B - Gera e imprime uma nova palavra")
print("C - Calcula e imprime a raiz a quarta de um numero")
print("F - Finalizar")
op=input("\nOPCAO: ")
if(op=="A" or op=="a"):
    i=1
    p1=input("Digite {i} palavra")
    i+=1
    p2=input("Digite {i} palavra")
    i+=1
    p3=input("Digite {i} palavra")
    i+=1
    if(len(p1)<len(p2)):
        menor=p1
    else:
        menor=p2
    if(len(p3)<len(menor)):
        menor=p3
        print("\n",menor)
else:
    if(op=="B" or op=="b"):
        p1=input("Digite uma palavra: ")
        if(len(p1)>5):
            n=len(p1)-2
            p2=len(p1)
            p3=len(p1,n)
            np=len(p2,p3)
            print("\n",np)
        else:
            n=len(p1)-3
            np=len(p1,n)
            print("",np)

    else:
        if (op=="C" or op=="c"):
            num=float(input("Digie um numero: "))
            if(num>=0.):
                print("\naiz a quarta:",math.pow(num,(1/2)/2))
            else:
                print("NAO PODE SER FEITA:")
        else:
            if(op=="F" or op=="f"):
                print("\n\n\n\t\t\t\tFINALIZANDO")
            else:
                print("\nopcao invalida")"""

#algoritmo 262 Entrar com numeros e imprimir o triplo de cada numero O algoritmo acaba quando entrar o numero -999 
"""num=float(input("Digite numero ou -999. para terminar: "))
while(num!=-999.):
    print("Triplo: ",num*3)
    num=float(input("Digite numero ou -999. para terminar: "))"""

#algoritmo 263 Entrar com números enquanto forem positivos e imprimir quantos números foram digitados. 
"""a=0
num=float(input("Digite numero positivo: "))
while(num>0.):
    a+=1;num=float(input("Digite numero positivo: "))"""

#algoritmo 264 Entrar com vários números positivos e imprimira média dos números digitados. 
"""a=0
soma=0
num=float(input("DIgite numero positivo: "))
while(num>0):
    a+=1
    soma+=num
    num=float(input("DIgite numero positivo: "))
print("Media: ",soma/a)"""

#algoritmo 265 Ler vários números e informar quantos números entre 100 e 200 foram digitados. 
#Quando o valor O (zero) for lido, o algoritmo deverá cessar sua execução. 
"""a=0
num=float(input("Digite numero ou 0 para sair: "))
while(num!=0.):
    if(num>=100 and num <=200):
        a+=1
    num=float(input("Digite numero ou 0 para sair: "))
print("total:",a)"""

#algoritmo 266 Entrar com nomes enquanto forem diferentes de FIM e imprimir o primeiro caractere de cada nome.
"""nome=input("Digite nime ou FIM para terminar: ")
while(nome != "FIM" or nome !="fim" or nome!="Fim"):
    print(nome)
    nome=input("Digite nime ou FIM para terminar: ")"""

#algoritmo 267
"""prof=input("Digite profissao ou FIm para sair: ")
a=0
while(prof != "FIM" and prof != "Fim" and prof != "fim"):
    if(prof=="DENTISTA" or prof=="Dentista" or prof=="dentista"):
        a+=1
    prof=input("Digite profissao ou FIm para sair: ")
print("total de dentista: ",a)"""
#algoritmo 268 Entrar com sexo de várias pessoas e imprimir quantas pessoas são do sexo mascu -lino (considerar m ou M). 
"""a=0
sexo=input("Digite sexo(M/F) ou @ para sair: ")
while(sexo[0]!="@"):
    if(sexo[0]=="M" or sexo[0]=="m"):
        a+=1
    sexo=input("Digite sexo(M/F) ou @ para sair: ")
print("TOtal de pessoas de sexo masculino: ",a)"""

#algoritmo 269 Entrar com números e imprimir o quadrado de cada número até entrar um número múltiplo de 6 que deverá ter seu quadrado também impresso. 
"""num=int(input("Digite numero ou multiplo de 6 para acabar: "))
print("quadrado: ",num^2)
while(num%6!=0):
    print("\n")"""

#algoritmo 270 Ler vários numeros ate entrar o numero -999 Para cada numero imprimirseus divisores
"""num=int(input("DIgite numero ou -999 para acabar: "))
while(num!=-999):
    print(num/2)
    num=int(input("DIgite numero ou -999 para acabar: "))"""

#algoritmo 271 Dado um país A, com 5.000.000 de habitantes e uma taxa de natalidade de 3% ao 
#ano, e um país B com 7.000.000 de habitantes e uma taxa de natalidade de 2% 
#ao ano calcular e imprimir o tempo necessario para que a população do pais A ultrapasse a população do pais B
"""a = 5000000.
b = 7000000.
anos=0
while(a<=b):
    a*=1.03
    b*=1.02
    anos+=1
print("Anos:",anos)"""

#algoritmo 272 Chico tem 1,50m e cresce 2 centímetros por ano, enquanto Juca tem 1, 1 O e cresce 3 centímetros por ano. Construir um algoritmo que calcule e imprima quantos anos serão necessários para que Juca seja maior que Chico. 
"""c=1.5
j=1.1
anos=0
while(j<=c):
    c+=0.02
    j+=0.03
    anos+=1
print("anos:",anos)"""

#algoritmo 273 Uma empresa de fornecimento de energia elétrica faz a leitura mensal dos medi- dores de consumo. Para cada consumidor, são digitados os seguintes dados: 
# número do consumidor 
#quantidade de kWh consumidos durante o mês 
#im tipo (código) do consumidor 
#1 - residencial, preço em reais por kWh = 0,3 
#2- comercial, preço em reais por kWh = 0,5 
#3 - industrial, preço em reais por kWh = 0,7 
#Os dados devem ser lidos até que seja encontrado um consumidor com número O 
#(zero). Calcular e imprimir: 
# o custo total para cada consumidor 
# o total de consumo para os três tipos de consumidor 
# a média de consumo dos tipos 1 e 2 
"""c12 = 0; total = 0.;total12 = 0.
codigo=int(input("digite codigo(1-res 2-com 3-ind) ou O para sair: "))
while(codigo!=0):
    qtde=float(input("Digite quatidadede KWH: "))
    total+=qtde
    if(codigo==1):
        print("custo:",qtde*0.3)
        c12+=1
        total12+=qtde
    else:
        if(codigo==2):
            print("custo:",qtde*0.5)
            c12+=1
            total12+=qtde
        else:
            if(codigo==3):
                print("Custo:",qtde*0.70)
    codigo=int(input("digite codigo(1-res 2-com 3-ind) ou O para sair: "))
    print("total consumido em 1-2-3:",total)
    if(c12!=0):
        print("media 1-2:",total12/12)
    else:
        print("\nNenhum consumidor na faixa1-2")"""

#algoritmo 274 Criar um algoritmo que deixe entrar com 10 números positivos e imprima raiz 
#quadrada de cada número. Para cada entrada de dados deverá haver um trecho 
#de proteção para que um número negativo não seja aceito. 
"""import math

for a in range(1,10,1):

    num=float(input(f"Entre com {1}° numero: "))
    while(num<=0):
        num=float(input(f"Entre com {2}° numero maior do que O: "))
    print("Raiz quadrada: ",math.pow(num,1/2))"""

#algoritmo 275 Criar um algoritmo que leia vários números inteiros e apresente o fatorial de cada 
#número. O algoritmo se encerra quando se digita um número menor do que 1.

#algoritmo 276
#algoritmo 277
#algoritmo 278
#algoritmo 279
#algoritmo 280

#algoritmo 281
#algoritmo 282
#algoritmo 283
#algoritmo 284
#algoritmo 285
#algoritmo 286
#algoritmo 287
#algoritmo 288
#algoritmo 289
#algoritmo 290
#algoritmo 291
#algoritmo 292
#algoritmo 293
#algoritmo 294
#algoritmo 295
#algoritmo 296
#algoritmo 297

#algoritmo 298 Numa universidade, os alunos das turmas de informática fizeram uma prova de
"""algoritmos. Cada turma possui um número de alunos. Criar um algoritmo que im-prima:
quantidade de alunos aprovados;
média de cada turma;
percentual de reprovados"""
"""a = 1 ;contap = 0; total = 0; x=0; r=0; apor=0
nt = int(input("digite o numero de turmas "))
while(a <= nt):
    sn = 0
    print("digite o numero de aluno da turma",a)
    na = int(input(":"))
    print("teste0 [",contap,"]")
    total += na
    print("teste1 [",contap,"]")
    x=1
    while(x <= na):
        print("Digite a nota do aluno da turma",x)
        nota = float(input(":"))
        if(nota >= 7.0):
            apor += 1
            contap += 1
            sn += nota
            x+=1
        print("teste2 [",contap,"]")
        if(nota < 7.0):
            contap += 1
            sn += nota
            x+=1
            r+=1
        print("Media da turma ",a,": ",sn/na)
    a+=1
print("Foram aprovados ", apor," alunos.")
print("\nPercentual de alunos reprovados: ",(r/contap)*100,"%")"""

#algoritmo 299 Os alunos de informática tiveram cinco provas: 1, 2, 3, 4 e 5. Criar um algoritmo que imprima:
"""
Nome dos que foram aprovados em todas as matérias;
Nome dos alunos aprovados nas matérias 1 e 4;
A porcentagem dos aprovados na matéria 3."""
"""x = 0
qa = int(input("Digite a quantidade de alunos: "))  
cont = 0
while(x < qa):
    nome = input("Digite o Nome ")
    n1 = float(input("[Digite a nota na prova 1]: "))
    n2 = float(input("[Digite a nota na prova 2]: "))
    n3 = float(input("[Digite a nota na prova 3]: "))
    n4 = float(input("[Digite a nota na prova 4]: "))
    n5 = float(input("[Digite a nota na prova 5]: "))
    if(n1 >=7.0 and n4 >=7.0):
        if(n2 >=7.0 and n3 >= 7.0 and n5 >=7.0):
            print("Parabens! ", nome, " voce foi aprovado em todas as materias!")
        else:
            print( nome, " voce passou nas materias 1 e 4;")
    if(n3 >= 7.0):
        cont+=1
    x+=1    
print("\nporcentagem dos aprovados na materia 3 : ",(cont*100)/qa)""" 

#algoritmo 300 Uma pesquisa de opinião realizada no Rio de Janeiro, teve as seguintes perguntas:
"""Qual seu time de coração?
1-Fluminense;
2-Botafogo;
3-Vasco;
4-Flamengo;
5-Outros
Onde você mora?
1-RJ;
2-Niterói;
3-Outros;
Qual o seu salário?
Criar um algoritmo que imprima:
o número de torcedores por clube;
m a média salarial dos torcedores do Botafogo;
m o número de pessoas moradoras do Rio de Janeiro, torcedores de outros
clubes;
o número de pessoas de Niterói torcedoras do Fluminense; """
"""from turtle import back
op = 0
x = 0
contflu = 0
contflu2 = 0
contbot = 0
msal = 0
contvas = 0
contfla = 0
contout2 = 0
while x < 50 :
    op = int(input("Digite [1-FLU] || [2-BOTA] || [3-VASCO] || [4-FLA] || [5-Outros] || [0-SAIR]  ")) 
    if( op == 0 ):
        break
    if( op != 0 ):
        x += 1
        if(op >1 or op<5  ):
            if( op == 1):
                contflu += 1
            if(op == 2):
                contbot += 1                          
            if(op == 3):
                contvas += 1
            if(op==4):
                contfla += 1
            if(op==5):
                contout2 += 1   
            op2 = int(input("Onde voce mora [1-RJ] [2-Niteroi] [3-Outros] "))
            if(op2 == 2):
                contflu2 += 1   
            sal = float(input("Qual o seu salario? "))     
msal += sal
print("Total de torcedores do Fluminense :", contflu)
print("Total de torcedores do Botafogo :", contbot)
print("Total de torcedores do Vasco :", contvas)
print("Total de torcedores do Flamengo :", contfla)
print("Total de torcedores de outros clubes :", contout2)
if(contbot != 0):
    print("Media salarial dos torcedores do Botafogo: ",float(msal/contbot))
else:
    print("Nenhum torcedor do Botafogo")
    print("\nTotal de pessoas do Rio de Janeiro torcedores de outros clubes :",contout2)
    print("\nTotal de pessoas de Niteroi torcedores do Fluminense: ", contflu2) """ 

#algoritmo 301 Criar um algoritmo que imprima a porcentagem dos alunos que gasta acima de 
#R$ 200,00 com outras despesas, o número de alunos com renda pessoal maior 
#que renda familiar e a porcentagem gasta com alimentação e outras despesas em 
#relação às rendas pessoal e familiar.
"""n=0
cont=0
cont2=0
rp= float(input("Digite sua renda pessoal ou O. para acabar: "))
while(rp>0):
    n+1
    rf=float(input("Digite renda familiar fora a sua: "))
    totali= float(input("Digite quanto gasta com alimentacao: "))
    totout= float(input("Digite quanto gasta com outras despesas:  "))
    if(totout>200):
        cont+1
        if(rp>rf):
            cont2+1
            print("\n" , ((totali+totout)*100)/(rp+rf),"%" " sao gastos com alimentos + despesas em relacao a renda pessoal e familiar")
            rp=float(input("Digite sua renda pessoal ou 0. para acabar: "))
            print("\n",((cont*100)/n,2),"%" " dos alunos gastam acima de R$ 200,00 com outras despesas")
            print("\nNumero de alunos com renda pessoal maior que a familiar",cont2)"""

#algoritmo 302 Uma agência de turismo quer fazer um levantamento das praias da cidade para uma 
#programação turística de verão, sabendo-se que cada praia tem um nome e uma distancia (em km) do hotel. Criar um algoritmo que forneça os seguintes dados: 
# porcentagem de turistas nas praias próprias do hotel; 
# a praia mais distante; 
#nome e distância das praias não-próprias com distância do hotel maior que 10 km; 
"""a=0;cont=0;mdist=0
nome=input("Digite o nome da praia ou @ para terminar: ")
while(nome != "@"):
    a+=1
    dist=float(input("Qual a distancia do hotel:  "))
    cond=input("Praia P(ropria) ou N(nao propria)?")
    while(cond!="p"and cond!="P" and cond!="n"and cond!="N"):
        cond=input("Atencao! Digite somente P(ropria) ou N(ao propria)?")
    if(cond=="P" or cond=="p"):
            cont+=1
    else:
        if(dist>10):
            print("Nome da praia:",nome)
            print("Distancia hotel:",dist)
    if(dist>mdist):
        mdist=dist; mnome=nome
        nome=input("Digite o nome da praia ou @ para terminar: ")
print("\nA porcentagem de turistas nas praias proprias foi de: ",(cont*100)/a,"%")
print("Praia mais distante :",mnome)"""

#algoritmo 303Criar um algoritmo que ajude o DETRAN a saber o total de recursos que foram arrecadados com a aplicação de multas de trânsito. 
#O algoritmo deve ler as seguintes informações para cada motorista: 
#número da carteira de motorista (de 1 a 4327), 
#número de multas; 
#valor de cada uma das multas. 
#Deve ser impresso o valor da dívida para cada motorista e ao final da leitura o total de 
#recursos arrecadados (somatório de todas as multas). O algoritmo deverá imprimir 
#também o número da carteira do motorista que obteve o maior número de multas. 
"""total=0
mnmult=0
c=1
cart=int(input("\ndigite carteira de motorista ou 0 para terminar: "))
while(cart!=0):
    nmult=int(input("Digite numero de multas: "))
    if(nmult > mnmult):
        mnmult = nmult; mcart = cart; 
        while(c<=nmult):
            c+=1
            valor=float(input("Digite valor da multa: "))
            total+=valor
            print("\ncarteira: ",cart)
            print("\nvalor a pagar: ",total)
            cart=int(input("\ndigite carteira de motorista ou 0 para terminar: "))
            print("\nnumero da carteira com maior numero de multas ",mcart)"""
         
#algoritmo 304 Criar um algoritmo que leia um conjunto de valores inteiros positivos e cujo ulti - mo valor e 1 Dentre os valores lidos o algoritmo deve imprimir 
#Q menor valor dentre os maiores que 100 e menores que 1000; 
#A média desses valores dentre os maiores que 100 e menores que 1000; 
#A soma desses valores dentre os maiores que 100 e menores que 1000 
#A soma de todos os valores lidos o valor -1" não deve ser considerado 
#Se nenhum valor estiver dentro do intervalo o algoritmo deve imprimir uma 
#mensagem para o usuario explicando o ocorrido 
"""cont =0; tot1=0; tot2 =0
num=int(input("Digite numero ou -1 para acabar: "))
menor=1001
while(num > -1):
    tot2+=num
    if(num>10 and num<100):
        cont+1;tot1+num
    if(num<menor):
        menor=num
    num=int(input("Digite numero ou -1 para acabar: "))
    if(cont!=0):
        print("Menor entre 100 e 1000: ",menor)
        print("Media entre 100 e 1000: ",tot1/cont)
        print("Soma entre 100 e 1000: ",tot1)
    else:
        print("Nao foi digitado numero entre 100 e 1000")
        print("Soma de totas: ",tot2)"""
             
#algoritmo 305 Criar um algoritmo que gerencie as contas correntes dos clientes do Banco Qir 
#Cup, um banco ítalo-anglo-franco-luso-nipo-brasileiro. O algoritmo deverá ler, 
#para cada cliente, o código do cliente (tipo inteiro), saldo anterior (tipo real) e as 
#movimentações da conta. 
#Cada movimentação é composta por um código (tipo caractere, C, D ou F, indi- cando Crédito, Débito ou fim das movimentações deste cliente) e um valor (tipo 
#real). Deverá ser impresso, para cada cliente, o seu código e o saldo atual (após o 
#processamento das movimentações). 
#Ao final, deverá ser impresso o total de dinheiro em caixa no banco (soma dos saldos de todos os clientes) e o código do cliente que possui o maior saldo.
# O algorit - mo se encerra quando se digita um código menor ou igual a zero
"""tot = 0
n1=int(input("Entre com o codigo do cliente ou codigo menor ou igual a O para terminar: "))
maior=-999999999.00
while(n1> 0):
    n2=int(input("Entre com o saldo anterior: "))
    n3=input("Entre com o tipo de movimentacao C(Credito) D(Debito) F(fim das movimentacoes deste cliente): ")
    while(n3!="f" and n3!="F"):
        n4=int(input("Entre com o valor da movimentacao: "))
        if(n3=="c" or n3=="C"):
            n2+=n4
            if(n3=="d"or n3=="D"):
                n2-=n4
        n3=input("Entre com o tipo de movimentacao C(Credito) D(Debito) F(fim das movimentacoes deste cliente): ")
    print("Seu codigo e ",n1," Saldo atua",n2)
    tot+=n2
    if(n2>maior):
        maiorcod =n1;maior=n2
        n1=int(input("\nEntre com o codigo do cliente ou codigo menor ou igual a O para terminar : "))
print("total de dinheiro em banco : ", tot)
print(maiorcod, " E o codigo do cliente com maior saldo: ", maior)"""
    
#algoritmo 306  A TELEMAR deseja calcular as contas telefônicas de seus assinantes através do computador. 
#algoritmo 307
#algoritmo 308
#algoritmo 309
#algoritmo 310
#algoritmo 311
#algoritmo 312
#algoritmo 313
#algoritmo 314
#algoritmo 315
#algoritmo 316
#algoritmo 317
#algoritmo 318
#algoritmo 319
#algoritmo 320
#algoritmo 321
#algoritmo 322
#algoritmo 323
#algoritmo 324




    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
















    
    
    
    
    
