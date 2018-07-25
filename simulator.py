import gene
from genes import Genes


class Simulator:

    def __init__(self, initial_gene_count=100):
        self.genes = Genes.generate_random_genes(initial_gene_count)

    def run_generation(self, minimum_survival=80):
        self.genes.replicate_genes(minimum_survival)
        replicated_genes = []
        for g in self.genes:
            if g.survival >= minimum_survival:
                replicated_genes.extend(g.get_offspring())

        self.genes = replicated_genes

    def run(self, generations=100, minimum_survival=80, log_file=None):
        final_log = ''
        for i in range(generations):
            self.run_generation(minimum_survival)
            log = self.to_string()
            if log_file is None:
                print log
            else:
                final_log += log + '\n'

        log_file.write(final_log)

    def to_string(self, compare=gene.compare_survival):
        return "|".join(map(str, sorted(self.genes, cmp=compare, reverse=True)))
