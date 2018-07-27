from random import *
from config import *


# TODO: maybe get rid of max survival. start all genes with survival 1, and let them build it up in competition

def get_mutated_attribute(orig_value, attribute_min, attribute_max, mutation_quotient):
    attribute_range = float(attribute_max - attribute_min)
    mutation = randrange(attribute_range + 1) - attribute_range / 2
    mutation *= mutation_quotient
    mutation *= mutation_range_scalar

    mutated_value = int(orig_value + mutation)
    if mutated_value > attribute_max:
        mutated_value = attribute_max - (mutated_value - attribute_max)
    if mutated_value < attribute_min:
        mutated_value = attribute_min - (mutated_value - attribute_min)
    return mutated_value


def generate_random_gene(gene_id):
    survival = randint(survival_min, survival_max)
    copy_fidelity = randint(copy_fidelity_min, copy_fidelity_max)
    fecundity = randint(fecundity_min, fecundity_max)
    return Gene(gene_id, survival, copy_fidelity, fecundity)


def compare_survival(gene1, gene2):
    return gene1.survival - gene2.survival


def compare_copy_fidelity(gene1, gene2):
    return gene1.copy_fidelity - gene2.copy_fidelity


def compare_id(gene1, gene2):
    return gene1.id - gene2.id


class Gene:

    def __init__(self, gene_id, survival=0, copy_fidelity=0, fecundity=0):
        self.id = gene_id
        self.survival = survival
        self.copy_fidelity = copy_fidelity
        self.fecundity = fecundity

    def replicate(self):
        mutation_quotient = 1 - float(self.copy_fidelity) / copy_fidelity_max

        new_survival = get_mutated_attribute(
            self.survival, survival_min, survival_max, mutation_quotient)
        new_copy_fidelity = get_mutated_attribute(
            self.copy_fidelity, copy_fidelity_min, copy_fidelity_max, mutation_quotient)
        new_fecundity = get_mutated_attribute(
            self.fecundity, fecundity_min, fecundity_max, mutation_quotient)

        return Gene(self.id, new_survival, new_copy_fidelity, new_fecundity)

    def get_offspring(self):
        new_generation = []
        for i in range(self.fecundity):
            new_generation.append(self.replicate())
        return new_generation

    def __str__(self):
        return str(self.survival) + ',' + str(self.copy_fidelity) + ',' + str(self.fecundity)
