import simulator

if __name__ == '__main__':
    with open('c:/gene_log.txt', 'w+') as log:
        sim = simulator.Simulator()
        sim.run(generations=50, minimum_survival=90, log_file=log)
