import config
import gene


class Simulator:

    def __init__(self, initial_gene_count=100):
        self.genes = []
        for i in range(initial_gene_count):
            self.genes.append(gene.generate_random_gene(i))

    def run_generation(self, max_generation_size):
        replicated_genes = []
        for g in self.genes:
            replicated_genes.extend(g.get_offspring())

        replicated_genes.sort(gene.compare_survival, reverse=True)
        self.genes = replicated_genes[:min(len(replicated_genes), max_generation_size)]

    def run(self, generations=100, max_generation_size=50, log_file=None):
        final_id_log = ''
        final_log = ''
        for i in range(generations):
            self.run_generation(max_generation_size)
            final_id_log += ','.join(map(lambda x: str(x), sorted(map(lambda x: x.id, self.genes)))) + '\n'
            log = self.to_string()
            if log_file is None:
                print log
            else:
                final_log += log + '\n'

        log_file.write(final_log)
        log_file.write('\n\n')
        log_file.write(final_id_log)

    def to_string(self, compare=gene.compare_id):
        return '|'.join(map(str, sorted(self.genes, cmp=compare, reverse=True)))
