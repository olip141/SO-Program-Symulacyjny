from generateData import ProcessGenerator
from generateData import Process
from fcfs import fcfs
from lcfs import lcfs

def eksperyment1():

    # 25 procesów o losowych czasach nadejścia (0-100) i wykonania w czasie = 5
    generator = ProcessGenerator(num_processes=25, arrival_range=(0, 100), burst_mean=5, burst_std=2)
    processes = generator.generate()

    fcfs(processes)
    lcfs(processes)

def eksperyment2():

    # 75 procesów o losowych czasach nadejścia (0-100) i wykonania w czasie = 5
    generator = ProcessGenerator(num_processes=75, arrival_range=(0, 100), burst_mean=5, burst_std=2)
    processes = generator.generate()

    fcfs(processes)
    lcfs(processes)

def eksperyment3():
    # 125 procesów o losowych czasach nadejścia (0-100) i wykonania w czasie = 5
    generator = ProcessGenerator(num_processes=125, arrival_range=(0, 100), burst_mean=5, burst_std=2)
    processes = generator.generate()

    fcfs(processes)
    lcfs(processes)

eksperyment2()