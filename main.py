from generateData import ProcessGenerator
from generateData import Process
from fcfs import fcfs
from lcfs import lcfs

def main():

    # Generowanie x procesów z czasami nadejścia x i czasami wykonania x
    generator = ProcessGenerator(num_processes=5, arrival_range=(0, 10), burst_mean=5, burst_std=2)
    processes = generator.generate()

   # Przykładowe dane wejściowe
    '''
    processes = [
    Process(1, 0, 5),
    Process(2, 2, 3),
    Process(3, 4, 1),
    Process(4, 6, 4),
    Process(5, 8, 2)
    ]
    '''
    fcfs(processes)
    lcfs(processes)

if __name__ == "__main__":
    main()
