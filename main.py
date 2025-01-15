from generateData import Process
from generateData import ProcessGenerator
from generateData import PageSequenceGenerator
from fcfs import fcfs_with_steps
from lcfs import lcfs_with_steps
from fifo import fifo_with_steps
from lru import lru_with_steps

def main():

    # Funckja main prezentuje przykładowe użycie algorytmów FCFS, LCFS, FIFO i LRU na przykładowych wybieralnych danych

    # Dane procesów dla algorytmów FCFS i LCFS
    #'''
    generator = ProcessGenerator(num_processes=5, arrival_range=(0, 10), arrival_std=2, burst_range=(4, 7), burst_std=2)
    processes = generator.generate()
    #'''

    # Dane dla algorytmów FCFS i LCFS użytych w sprawozdaniu
    '''
    processes = [Process(name=1, arrival_time=0, burst_time=5),
                    Process(name=2, arrival_time=2, burst_time=3),
                    Process(name=3, arrival_time=4, burst_time=1),
                    Process(name=4, arrival_time=6, burst_time=4),
                    Process(name=5, arrival_time=8, burst_time=2)]
    '''
  
    # Dane dla algorytmów FIFO i LRU
    #'''
    page_sequence_generator = PageSequenceGenerator(sequence_length=20, page_range=10)  
    page_sequence = page_sequence_generator.generate()
    page_frames = 4 
    #'''
    
    # Dane dla algorytmów FIFO i LRU użytych w sprawozdaniu
    '''
    page_sequence = [7,	0,	1,	2,	0,	3,	0,	1,	0]
    page_frames = 2
    '''
  
    # Wywołanie funkcji pokazujących działanie algorytmów FCFS i LCFS krok po kroku
    fcfs_with_steps(processes)
    lcfs_with_steps(processes)

    print("\n------------------------------------------------------------------------------")

    print("\nSekwencja stron:", page_sequence)
    # Wywołanie funkcji pokazujących działanie algorytmów FIFO i LRU krok po kroku
    fifo_with_steps(page_sequence, page_frames)
    lru_with_steps(page_sequence, page_frames)
    
if __name__ == "__main__":
    main()
