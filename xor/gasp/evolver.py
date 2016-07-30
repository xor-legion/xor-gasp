import random

import xor.gasp.ga as ga

def half_cross_genes(g1,g2):
    mid = int(len(g1) / 2)
    c1 = g1[:mid]
    c1.extend(g2[mid:])
    c2 = g2[:mid]
    c2.extend(g1[mid:])
    return c1, c2

def half_cross_shuffle_evolver(parents):
    ids = [x for x in range(len(parents))]
    random.SystemRandom().shuffle(ids)
    children = []
    for i in range(0,len(ids),2):
        c1, c2 = half_cross_genes(parents[i],parents[i+1])
        children.append(c1)
        children.append(c2)
    return children

def random_mutation(gene):
    if ga.random_int(20) % 20 == 1:
        pos = ga.random_int(len(gene))
        gene[pos] = ga.random_nucleotide()
    return gene

def random_cross_genes(g1,g2):
    mid = random.SystemRandom().randint(0,len(g1) - 1)
    c1 = g1[:mid] + g2[mid:] #c1.extend(g2[mid:])
    c2 = g2[:mid] + g1[mid:] #c2.extend(g1[mid:])
    c1 = random_mutation(c1)
    c2 = random_mutation(c2)
    return c1, c2

def random_cross_shuffle_evolver(parents):
    ids = [x for x in range(len(parents))]
    random.SystemRandom().shuffle(ids)
    children = []
    for i in range(0,len(ids),2):
        c1, c2 = random_cross_genes(parents[i],parents[i+1])
        children.append(c1)
        children.append(c2)
    return children
