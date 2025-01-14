from generateData import ProcessGenerator
from fcfs import fcfs
from lcfs import lcfs
import os

def save_results(filename, average_waiting_time, algorithm_name,test_number):
    folder = "WynikiEksperymentów"
    os.makedirs(folder, exist_ok=True)
    filepath = os.path.join(folder, filename)
    with open(filepath, 'w') as file:
        file.write(f"Eksperyment nr: {test_number}\n")
        file.write(f"Algorytm: {algorithm_name}\n")
        file.write(f"Średni czas oczekiwania dla {algorithm_name}: {average_waiting_time}\n")

def eksperyment1():

    # 25 procesów o losowych czasach nadejścia = (0-100) i wykonania w czasie = 5
    generator = ProcessGenerator(num_processes=25, arrival_range=(0, 100), arrival_std=0, burst_range=(5, 5), burst_std=0)
    processes = generator.generate()

    done_procesess, average_waiting_time = fcfs(processes)
    done_procesess2, average_waiting_time2 = lcfs(processes)

    print("\nEksperyment 1:")
    print("Średni czas oczekiwania dla FCFS:", average_waiting_time)
    print("Średni czas oczekiwania dla LCFS:", average_waiting_time2)
    save_results("eksperyment1_FCFS.txt", average_waiting_time, "FCFS","1")
    save_results("eksperyment1_LCFS.txt", average_waiting_time2, "LCFS","1")


def eksperyment2():

    # 75 procesów o losowych czasach nadejścia = (0-100) i wykonania w czasie = 5
    generator = ProcessGenerator(num_processes=75, arrival_range=(0, 100), arrival_std=0, burst_range=(5, 5), burst_std=0)
    processes = generator.generate()

    done_procesess, average_waiting_time = fcfs(processes)
    done_procesess2, average_waiting_time2 = lcfs(processes)

    print("\nEksperyment 2:")
    print("Średni czas oczekiwania dla FCFS:", average_waiting_time)
    print("Średni czas oczekiwania dla LCFS:", average_waiting_time2)
    save_results("eksperyment2_FCFS.txt", average_waiting_time, "FCFS", "2")
    save_results("eksperyment2_LCFS.txt", average_waiting_time2, "LCFS", "2")

def eksperyment3():
    # 125 procesów o losowych czasach nadejścia = (0-100) i wykonania w czasie = 5
    generator = ProcessGenerator(num_processes=125, arrival_range=(0, 100), arrival_std=0, burst_range=(5, 5), burst_std=0)
    processes = generator.generate()

    done_procesess, average_waiting_time = fcfs(processes)
    done_procesess2, average_waiting_time2 = lcfs(processes)

    print("\nEksperyment 3:")
    print("Średni czas oczekiwania dla FCFS:", average_waiting_time)
    print("Średni czas oczekiwania dla LCFS:", average_waiting_time2)
    save_results("eksperyment3_FCFS.txt", average_waiting_time, "FCFS", "3")
    save_results("eksperyment3_LCFS.txt", average_waiting_time2, "LCFS", "3")

def eksperyment4():
    # 25 procesów o czasie nadejścia = 0 i wykonania w czasie = (1 - 10)
    generator = ProcessGenerator(num_processes=25, arrival_range=(0, 0), arrival_std=0, burst_range=(1, 10), burst_std=0)
    processes = generator.generate()

    done_procesess, average_waiting_time = fcfs(processes)
    done_procesess2, average_waiting_time2 = lcfs(processes)

    print("\nEksperyment 4:")
    print("Średni czas oczekiwania dla FCFS:", average_waiting_time)
    print("Średni czas oczekiwania dla LCFS:", average_waiting_time2)
    save_results("eksperyment4_FCFS.txt", average_waiting_time, "FCFS", "4")
    save_results("eksperyment4_LCFS.txt", average_waiting_time2, "LCFS", "4")

def eksperyment5():
    # 75 procesów o czasie nadejścia = 0 i wykonania w czasie = (1 - 10)
    generator = ProcessGenerator(num_processes=75, arrival_range=(0, 0), arrival_std=0, burst_range=(1, 10), burst_std=0)
    processes = generator.generate()
    
    done_procesess, average_waiting_time = fcfs(processes)
    done_procesess2, average_waiting_time2 = lcfs(processes)

    print("\nEksperyment 5:")
    print("Średni czas oczekiwania dla FCFS:", average_waiting_time)
    print("Średni czas oczekiwania dla LCFS:", average_waiting_time2)
    save_results("eksperyment5_FCFS.txt", average_waiting_time, "FCFS", "5")
    save_results("eksperyment5_LCFS.txt", average_waiting_time2, "LCFS", "5")

def eksperyment6():
    # 125 procesów o czasie nadejścia = 0 i wykonania w czasie = (1 - 10)
    generator = ProcessGenerator(num_processes=125, arrival_range=(0, 0), arrival_std=0, burst_range=(1, 10), burst_std=0)
    processes = generator.generate()

    done_procesess, average_waiting_time = fcfs(processes)
    done_procesess2, average_waiting_time2 = lcfs(processes)

    print("\nEksperyment 6:")
    print("Średni czas oczekiwania dla FCFS:", average_waiting_time)
    print("Średni czas oczekiwania dla LCFS:", average_waiting_time2)
    save_results("eksperyment6_FCFS.txt", average_waiting_time, "FCFS", "6")
    save_results("eksperyment6_LCFS.txt", average_waiting_time2, "LCFS", "6")

def eksperyment7():
    # 25 procesów o czasie nadejścia wykonania w czasie = 10 z odch. std. = 5
    generator = ProcessGenerator(num_processes=25, arrival_range=(10, 10), arrival_std=4, burst_range=(10, 10), burst_std=5)
    processes = generator.generate()
    
    done_procesess, average_waiting_time = fcfs(processes)
    done_procesess2, average_waiting_time2 = lcfs(processes)

    print("\nEksperyment 7:")
    print("Średni czas oczekiwania dla FCFS:", average_waiting_time)
    print("Średni czas oczekiwania dla LCFS:", average_waiting_time2)
    save_results("eksperyment7_FCFS.txt", average_waiting_time, "FCFS", "7")
    save_results("eksperyment7_LCFS.txt", average_waiting_time2, "LCFS", "7")

def eksperyment8():
    # 75 procesów o czasie nadejścia wykonania w czasie = 20 z odch. std. = 5
    generator = ProcessGenerator(num_processes=75, arrival_range=(20, 20), arrival_std=5, burst_range=(20, 20), burst_std=5)
    processes = generator.generate()
    
    done_procesess, average_waiting_time = fcfs(processes)
    done_procesess2, average_waiting_time2 = lcfs(processes)

    print("\nEksperyment 8:")
    print("Średni czas oczekiwania dla FCFS:", average_waiting_time)
    print("Średni czas oczekiwania dla LCFS:", average_waiting_time2)
    save_results("eksperyment8_FCFS.txt", average_waiting_time, "FCFS", "8")
    save_results("eksperyment8_LCFS.txt", average_waiting_time2, "LCFS", "8")

def eksperyment9():
    # 125 procesów o czasie nadejścia wykonania w czasie = 30 z odch. std. = 5
    generator = ProcessGenerator(num_processes=125, arrival_range=(30, 30), arrival_std=5, burst_range=(30, 30), burst_std=5)
    processes = generator.generate()

    done_procesess, average_waiting_time = fcfs(processes)
    done_procesess2, average_waiting_time2 = lcfs(processes)

    print("\nEksperyment 9:")
    print("Średni czas oczekiwania dla FCFS:", average_waiting_time)
    print("Średni czas oczekiwania dla LCFS:", average_waiting_time2)
    save_results("eksperyment9_FCFS.txt", average_waiting_time, "FCFS", "9")
    save_results("eksperyment9_LCFS.txt", average_waiting_time2, "LCFS", "9")

def eksperyment10():
    # 200 procesów o losowych czasach nadejścia (0-500) i wykonania w czasie (1-20)
    generator = ProcessGenerator(num_processes=200, arrival_range=(0, 500), arrival_std=10, burst_range=(1, 20), burst_std=5)
    processes = generator.generate()

    done_procesess, average_waiting_time = fcfs(processes)
    done_procesess2, average_waiting_time2 = lcfs(processes)

    print("\nEksperyment 10:")
    print("Średni czas oczekiwania dla FCFS:", average_waiting_time)
    print("Średni czas oczekiwania dla LCFS:", average_waiting_time2)
    save_results("eksperyment10_FCFS.txt", average_waiting_time, "FCFS", "10")
    save_results("eksperyment10_LCFS.txt", average_waiting_time2, "LCFS", "10")

def eksperyment11():
    # 200 procesów o losowych czasach nadejścia i wykonania, gdzie czas wykonania jest dynamiczny
    generator = ProcessGenerator(num_processes=200, arrival_range=(0, 500), arrival_std=20, burst_range=(1, 20), burst_std=15)
    processes = generator.generate()

    done_procesess, average_waiting_time = fcfs(processes)
    done_procesess2, average_waiting_time2 = lcfs(processes)

    print("\nEksperyment 11:")
    print("Średni czas oczekiwania dla FCFS:", average_waiting_time)
    print("Średni czas oczekiwania dla LCFS:", average_waiting_time2)
    save_results("eksperyment11_FCFS.txt", average_waiting_time, "FCFS", "11")
    save_results("eksperyment11_LCFS.txt", average_waiting_time2, "LCFS", "11")

def eksperyment12():
    # 250 procesów o losowych czasach nadejścia i wykonania, z dużą zmiennością (odch. std. = 10)
    generator = ProcessGenerator(num_processes=250, arrival_range=(0, 1000), arrival_std=50, burst_range=(1, 50), burst_std=20)
    processes = generator.generate()

    done_procesess, average_waiting_time = fcfs(processes)
    done_procesess2, average_waiting_time2 = lcfs(processes)

    print("\nEksperyment 12:")
    print("Średni czas oczekiwania dla FCFS:", average_waiting_time)
    print("Średni czas oczekiwania dla LCFS:", average_waiting_time2)
    save_results("eksperyment12_FCFS.txt", average_waiting_time, "FCFS", "12")
    save_results("eksperyment12_LCFS.txt", average_waiting_time2, "LCFS", "12")


# Wywołanie eksperymentów
eksperyment1()
eksperyment2()
eksperyment3()
eksperyment4()
eksperyment5()
eksperyment6()
eksperyment7()
eksperyment8()
eksperyment9()
eksperyment10()  
eksperyment11()  
eksperyment12()  