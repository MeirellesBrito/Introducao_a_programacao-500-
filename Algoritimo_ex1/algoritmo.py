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
    print("Mario:",a)
else:
    print("Mario:",b)"""

#algoritmo 112 Entrar com dois números e imprimir o menor numero (suponha números diferentes).
"""a = input("DIgite 1 numero: ")
b = input("DIgite 2 numero: ")
if(a<b):
    print("Mario:",a)
else:
    print("Mario:",b)"""

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





#algoritmo 298 Numa universidade, os alunos das turmas de informática fizeram uma prova de
"""algoritmos. Cada turma possui um número de alunos. Criar um algoritmo que im-prima:
 quantidade de alunos aprovados;
média de cada turma;
percentual de reprovados."""
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












