import random
import sys

nucleotides = list('.,<>[]+-')

def random_int(n):
    return random.SystemRandom().randint(0,n-1)

def random_nucleotide():
    p = random_int(len(nucleotides))
    return nucleotides[p]

def random_gene(n):
    gene = []
    for i in range(n):
        gene.append(random_nucleotide())
    return gene

def generate_random_population(population_size,gene_size):
    population = []
    for i in range(population_size):
        population.append(random_gene(gene_size))
    return population
