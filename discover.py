#!/usr/bin/env python3

import sys

import xor.gasp.ga as ga
import xor.gasp.evolver as ev

def output_population(population):
    j = 0
    print("Genes in population:")
    for gene in population:
        print("G ",j," ","".join(gene))
        j += 1

def output_population_set(population_set):
    j = 0
    print("Genes in population set:")
    for gene in population_set:
        print("G ",j," ",gene)
        j += 1

#population_size = 300
#gene_size = 27
#evolutions = 10000
#target_gene = "++++++[>++++++++++<-]>+++++"

population_size = 500
gene_size = 8
evolutions = 10000
target_gene = "++++++++"

#-------------------

population = ga.generate_random_population(population_size,gene_size)
population_set = set(["".join(gene) for gene in population])

generate_next_generation = ev.random_cross_shuffle_evolver

#print(len(population))
#print(len(population_set))

evolution = 0
last_set_size = len(population_set)
print("Set size: ",last_set_size)

#for i in range(evolutions):
while True:
    population = generate_next_generation(population)
    population_set.update(["".join(gene) for gene in population])
    if target_gene in population_set:
        print("Found in evolution : ",evolution)
        print("Population set size: ",len(population_set))
        break
    evolution += 1
    if last_set_size < len(population_set):
        last_set_size = len(population_set)
        print("E ",evolution," / Set size: ",last_set_size)
    

    #output_population(population)
    #output_population_set(population_set)
    #print(i,len(population),len(population_set))
    #sys.stdout.flush()
