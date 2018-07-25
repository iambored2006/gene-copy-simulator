import simulator

if __name__ == '__main__':
    with open('c:/gene_log.txt', 'w+') as log:
        sim = simulator.Simulator()
        sim.run(generations=1000, log_file=log)
