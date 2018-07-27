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

        # TODO: shuffle genes with equivalent survival value
        # TODO: so as to increase competition between rivaling strands of equal value
        replicated_genes.sort(gene.compare_survival, reverse=True)
        self.genes = replicated_genes[:min(len(replicated_genes), max_generation_size)]

    def run(self, generations=100, max_generation_size=100, log_file=None):
        final_id_log = ''
        final_data_log = ''
        for i in range(generations):
            final_data_log += '|'.join(map(str, sorted(self.genes, cmp=gene.compare_id, reverse=True))) + '\n'
            final_id_log += ','.join(map(lambda x: str(x), sorted(map(lambda x: x.id, self.genes)))) + '\n'
            self.run_generation(max_generation_size)

        log_file.write(final_data_log)
        log_file.write('\n\n')
        log_file.write(final_id_log)
