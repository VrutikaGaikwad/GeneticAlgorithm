# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 22:04:01 2021

@author: VRUTIKA
"""

#imports
import random

#initailizing population
population=["10101010","11110000","01010101","00001111","10111011","01000100","11100111","00000000"]

#Calculating fitness value
binary=[]
for i in range(len(population)):
    binary.append(int(population[i],2))

#printing poplution and it's fitness value
for i in range(len(population)):
    print("Individual [",i,"]: ",population[i],"\tFitness: ",binary[i])

#selection function
def selection(n):
    if n==2:
        parent1=random.choice(population)
        parent2=random.choice(population)
        if parent1 == parent2:
            parent1,parent2=selection(2)
        return parent1,parent2
    if n==1:
        parent=random.choice(population)
        return parent


#Crossover function
def crossover():
    parent1,parent2=selection(2)
    print("Selected Individuals\nParent 1: ",parent1,"\tFitness: ",binary[population.index(parent1)],"\nParent 2: ",parent2,"\tFitness: ",binary[population.index(parent2)],"\n")
    crossover_point=random.choice(range(1,7))
    #print("Crossover Point: ",crossover_point,"\n")
    child1=parent1[:crossover_point]+parent2[crossover_point:]
    child2=parent2[:crossover_point]+parent1[crossover_point:]
    f_child1=int(child1,2)
    f_child2=int(child2,2)
    print("Child 1: ",child1,"\tFitness: ",f_child1)
    print("Child 2:",child2,"\tFitness: ",f_child2)
    print()
    #Child1 assessment
    if(f_child1>f_child2):
       print(child1,"  Survives to next generation")
    else:
       print(child2,"  Survives to next generation") 

       
#Mutation function
def mutation():
    parent=selection(1)
    print("Selected Individual: ",parent,"\tFitness: ",binary[population.index(parent)])
    mutate_bit=random.choice(range(0,7))
    #print("Mutation Bit: ",mutate_bit+1)
    child_list=list(parent)
    if child_list[mutate_bit]=='1':
        child_list[mutate_bit]='0'
    else:
        child_list[mutate_bit]='1'
    child_str="".join(child_list)
    child=int(child_str,2)
    print("\nMutated Child: ",child_str,"\tFitness: ",child,"\n")
    if(child<=binary[population.index(parent)]):
       print("Child has not evolved")
    if(child>binary[population.index(parent)]):
       print("Child has evolved")

#Selecting Evolution process
while True:
    evolution=input("\nPlease Enter Choice(or to Quit type exit)\nCrossover or Mutation:").lower()
    if evolution=="crossover":
        crossover()
    elif evolution=="mutation":
        mutation()
    elif evolution=="exit":
        break
    else:
        print("Please enter a valid choice")
