import config
from gene import Gene
from random import random


def get_mutated_attribute(orig_value, attribute_range, fidelity):
    return orig_value + fidelity * (random(attribute_range) - attribute_range / 2)


def replicate(gene):
    fidelity_quotient = 1 - gene.copy_fidelity / config.copy_fidelity_max

    survival_range = config.survival_max - config.survival_min
    copy_fidelity_range = config.copy_fidelity_max - config.copy_fidelity_min
    fecundity_range = config.fecundity_max - config.fecundity_min

    new_survival = get_mutated_attribute(gene.survival, survival_range, fidelity_quotient)
    new_copy_fidelity = get_mutated_attribute(gene.copy_fidelity, copy_fidelity_range, fidelity_quotient)
    new_fecundity = get_mutated_attribute(gene.fecundity, fecundity_range, fidelity_quotient)

    return Gene(new_survival, new_copy_fidelity, new_fecundity)
