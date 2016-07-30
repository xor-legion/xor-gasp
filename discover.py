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

population_size = 500
target_gene = "++++"
gene_size = len(target_gene)
evolutions = 10000
iterations = 1000

#-------------------

generate_next_generation = ev.random_cross_shuffle_evolver

for iter in range(iterations):

    population = ga.generate_random_population(population_size,gene_size)
    population_set = set(["".join(gene) for gene in population])
    evolution = 1

    while True:

        if target_gene in population_set:
            print("{},{}".format(evolution,len(population_set)))
            sys.stdout.flush()
            break

        population = generate_next_generation(population)
        population_set.update(["".join(gene) for gene in population])
        evolution += 1
