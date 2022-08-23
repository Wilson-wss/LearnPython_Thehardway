"""
def cheese_and_crackers(cheese_count, boxes_of_crackers):#aqui foi criada a função cheese_and_crackers, com dois parametros cheese_count e boxes_of_crackers
    print(f"You have {cheese_count} cheeses!") #aqui eu vou imprimir o parametro passado lá embaixo para a função
    print(f"You have {boxes_of_crackers} boxes of crackers!")#aqui também vou imprimir o outro parametro
    print("Man that's enough for a party!")
    print("Get a blanket.\n")


print ("We can just give function numbers directly:")
cheese_and_crackers(20,30)#aqui eu passo os parametros 20 e 30 para a função cheese_and_crackers


print("OR, we can use variables from our script:")
amount_of_cheese = 10 #aqui e na proxima linha eu crio duas varáveis para a função e atribuo valores inteiros para elas
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)#aqui eu chamo a função cheese_and_crackers e coloco as varáveis´criadas acima


print("We can even do math inside too:")
cheese_and_crackers(10+20, 5+6)#aqui eu faço operações matemáticas dentro da função


print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese+100, amount_of_crackers+1000) #aqui eu combino varáveis com operações matemáticas
"""

#AGORA VOU CRIAR MINHA PROPRIA FUNÇÃO

def wilson_dev(python, java):
    print(f"Python é uma linguagem de programação {python}!")
    print(f"Java é uma linguagem de programação {java}!")
    print("Mas eu vou aprender as duas!")


print("Até 2024 eu estarei morando no Canadá, porque eu vou ser Dev!")
wilson_dev ('foda', 'desconhecida')


python = 'foda'
java = 'desconhecida'
wilson_dev(python, java)


wilson_dev(python*10, java*20)
