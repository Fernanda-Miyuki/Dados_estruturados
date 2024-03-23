#numeros = [19,19,18,25,30,18,26]
#print(numeros[5])

import os
import glob

arquivo ='dataset.csv'
arquivo= open(arquivo,'r')

dados = arquivo.readlines()
pula=0
#for i in range(100):
    #print(str(i+1) + " Hello")

somatorio =0
experiente= 0
for i in range(len(dados)):
    if i == 0:
        continue
    idade= dados[i].split(',')[1].replace('\n','').replace(' ', '')
    if int(idade) > experiente:
        experiente= int(idade)
        aux = i
    somatorio = int(somatorio) + int(idade)
    print(i, experiente)

print(somatorio)

media = somatorio / (len(dados)-1)
print("Média de idade:",media)
print("Maior idade:", experiente)

nome_experiente= dados[aux].split(',')[0].replace('\n','').replace(' ', '')
idade_experiente = dados[aux].split(',')[1].replace('\n','').replace(' ', '')

print(experiente)
print(nome_experiente, idade_experiente)