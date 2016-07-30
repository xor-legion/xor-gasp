#!/usr/bin/env python3

import sys
from os import urandom
from sys import byteorder
import xor.bf.machine as bf

nucleotide = list("+-><[].,")

def random_int():
    return int.from_bytes(urandom(4),byteorder=byteorder)

def random_nucleotide():
    return nucleotide[random_int() % 8]

def mutate(gene):
    mutant = []
    mutant = [x for x in gene]
    pos = random_int() % len(gene)
    new = random_nucleotide()
    mutant[pos] = new
    return mutant

def cross_half(gene1,gene2):
    child = []
    if len(gene1) != len(gene2):
        return None
    if len(gene1) % 2 != 0:
        return None
    child = gene1[:int(len(gene1)/2)]
    child.extend(gene2[int(len(gene2)/2):])
    return child

def random_gene(n):
    new_gene = []
    for i in range(n):
        new_gene.append(random_nucleotide())
    return new_gene

def fit_gene(produced,expected):
    if len(produced) == 0:
        return 0 

    if produced == expected:
        return 1

    idx = produced.find(expected)
    if idx > -1:
       return 1 - (idx / len(produced))

    return 0

def fit_generation(genes):
    fitness = []
    for gene in genes:
        try:
            output = bf.evaluate(gene,max_ticks = 10000)
            fit = fit_gene(output,"hi")
            fitness.append(fit)
        except Exception:
            fitness.append(-1)

    return genes, fitness

def new_generation(genes,fitness,mutation_rate):
    children = []
    for i in range(len(genes)):
        j = i + 1
        if j >= len(genes):
            j = 0
        if random_int() % mutation_rate == 1:
            child = mutate(cross_half(genes[i],genes[j]))
        else:
            child = cross_half(genes[i],genes[j])
        children.append(child)
    return children

genes = []
for i in range(300):
    genes.append(random_gene(112))

for i in range(50000):
    sys.stdout.flush()
    genes, fitness = fit_generation(genes)
    genes = new_generation(genes,fitness,200)

    for j in range(len(genes)):
        if fitness[j] > 0:
            print("{}|{} - {}".format(i,fitness[j],"".join(genes[j])))
