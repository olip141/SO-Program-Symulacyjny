import numpy as np
from typing import List, Tuple

class Process:
    def __init__(self, name, arrival_time, burst_time):
        self.name = name                  # indeks procesu
        self.arrival_time = arrival_time  # czas nadejścia
        self.burst_time = burst_time      # czas wykonywania
        self.completion_time = None       # czas zakończenia
        self.waiting_time = None          # czas oczekiwania

    def __repr__(self):
        return (f"Process(name={self.name}, arrival_time={self.arrival_time}, burst_time={self.burst_time}, "
                f"completion_time={self.completion_time}, waiting_time={self.waiting_time})")

class ProcessGenerator:
    def __init__(self, num_processes: int, arrival_range: Tuple[int, int], burst_mean: float, burst_std: float):
        self.num_processes = num_processes
        self.arrival_range = arrival_range
        self.burst_mean = burst_mean
        self.burst_std = burst_std

    def generate(self) -> List[Process]:
        arrival_times = np.random.randint(self.arrival_range[0], self.arrival_range[1] + 1, self.num_processes)
        burst_times = np.maximum(1, np.random.normal(self.burst_mean, self.burst_std, self.num_processes).astype(int))
        
        processes = [Process(name=i+1, arrival_time=arrival_time, burst_time=burst_time) 
                     for i, (arrival_time, burst_time) in enumerate(zip(arrival_times, burst_times))]
        
        # Sortujemy procesy według czasu nadejścia
        processes.sort(key=lambda p: p.arrival_time)
        return processes