import random
import config


def get_mutated_attribute(orig_value, attribute_min, attribute_max, fidelity):
    attribute_range = attribute_max - attribute_min
    mutated_value = orig_value + int(fidelity * (random.randrange(attribute_range) - attribute_range / 2))
    return min(max(mutated_value, attribute_min), attribute_max)


def generate_random_gene():
    survival = random.randint(config.survival_min, config.survival_max)
    copy_fidelity = random.randint(config.copy_fidelity_min, config.copy_fidelity_max)
    fecundity = random.randint(config.fecundity_min, config.fecundity_max)
    return Gene(survival, copy_fidelity, fecundity)


def compare_survival(gene1, gene2):
    return gene1.survival - gene2.survival


def compare_copy_fidelity(gene1, gene2):
    return gene1.copy_fidelity - gene2.copy_fidelity


class Gene:

    def __init__(self, survival=0, copy_fidelity=0, fecundity=0):
        self.survival = survival
        self.copy_fidelity = copy_fidelity
        self.fecundity = fecundity

    def replicate(self):
        fidelity_quotient = 1 - float(self.copy_fidelity) / config.copy_fidelity_max

        new_survival = get_mutated_attribute(
            self.survival, config.survival_min, config.survival_max, fidelity_quotient)
        new_copy_fidelity = get_mutated_attribute(
            self.copy_fidelity, config.copy_fidelity_min, config.copy_fidelity_max, fidelity_quotient)
        new_fecundity = get_mutated_attribute(
            self.fecundity, config.fecundity_min, config.fecundity_max, fidelity_quotient)

        return Gene(new_survival, new_copy_fidelity, new_fecundity)

    def get_offspring(self):
        new_generation = []
        for i in range(self.fecundity):
            new_generation.append(self.replicate())
        return new_generation

    def __str__(self):
        return str(self.survival) + ',' + str(self.copy_fidelity) + ',' + str(self.fecundity)
