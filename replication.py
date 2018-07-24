import config
from gene import Gene


def replicate(gene):
    copy_quotient = gene.copy_fidelity / config.copy_fidelity_max
    new_gene = Gene()
