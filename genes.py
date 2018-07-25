import numpy as np
import config
from gene import Gene


class Genes(object):
    def __init__(self, survival, copy_fidelity, fecundity):
        self.survival = survival
        self.copy_fidelity = copy_fidelity
        self.fecundity = fecundity

    def __getitem__(self, item):
        return Gene(self.survival[item], self.copy_fidelity[item], self.fecundity[item])

    @classmethod
    def generate_random_genes(cls, initial_gene_count):
        survival = np.random.randint(low=config.survival_min, high=config.survival_max+1, size=initial_gene_count)
        copy_fidelity = np.random.randint(low=config.copy_fidelity_min, high=config.copy_fidelity_max+1, size=initial_gene_count)
        fecundity = np.random.randint(low=config.fecundity_min, high=config.fecundity_max+1, size=initial_gene_count)
        return Genes(survival, copy_fidelity, fecundity)

    def replicate_genes(self, minimum_survival):
        replicated_genes = np.where(self.survival >= minimum_survival)[0]
        print "hello"
