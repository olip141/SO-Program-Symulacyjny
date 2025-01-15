import numpy as np
from typing import List, Tuple

class Process:

    # Klasa reprezentująca pojedynczy proces w systemie

    def __init__(self, name, arrival_time, burst_time):

        # Funkcja inicjalizuje obiekt klasy Process, który reprezentuje pojedynczy proces w systemie.

        self.name = name                  # Indeks procesu
        self.arrival_time = arrival_time  # Czas nadejścia procesu
        self.burst_time = burst_time      # Czas wykonywania procesu
        self.completion_time = None       # Czas zakończenia procesu (ustawiany po zakończeniu)
        self.waiting_time = None          # Czas oczekiwania procesu (ustawiany na podstawie zakończenia)


class ProcessGenerator:
    def __init__(self, num_processes: int, arrival_range: Tuple[int, int], arrival_std: float, burst_range: Tuple[float, float], burst_std: float):

        # Funkcja inicjalizuje obiekt klasy ProcessGenerator, który generuje procesy na podstawie określonych parametrów.

        self.num_processes = num_processes # Liczba procesów
        self.arrival_range = arrival_range # Zakres czasów nadejścia
        self.arrival_std = arrival_std     # Odchylenie standardowe czasów nadejścia
        self.burst_range = burst_range     # Zakres czasów wykonania procesów
        self.burst_std = burst_std         # Odchylenie standardowe czasów wykonania

    def generate(self) -> List[Process]:

        # Funkcja generuje listę procesów z losowymi czasami nadejścia oraz czasami wykonania.
        # Procesy są następnie sortowane po czasie nadejścia

        arrival_mean = (self.arrival_range[0] + self.arrival_range[1]) / 2                                              # Obliczenie średniego czasu nadejścia (średnia z zakresu)
        arrival_times = np.maximum(0, np.random.normal(arrival_mean, self.arrival_std, self.num_processes).astype(int)) # Generowanie czasów nadejścia z rozkładu normalnego (z odchyleniem standardowym)
        burst_means = np.random.uniform(self.burst_range[0], self.burst_range[1], self.num_processes)                   # Generowanie średnich czasów wykonania z rozkładu jednostajnego
        burst_times = np.maximum(1, np.random.normal(burst_means, self.burst_std).astype(int))                          # Generowanie czasów wykonania z rozkładu normalnego (z odchyleniem standardowym)
        
        # Tworzenie listy procesów na podstawie wygenerowanych czasów
        processes = [Process(name=i+1, arrival_time=arrival_time, burst_time=burst_time) 
                     for i, (arrival_time, burst_time) in enumerate(zip(arrival_times, burst_times))]
        
         # Sortowanie procesów po czasie nadejścia
        processes.sort(key=lambda p: p.arrival_time)

        return processes # Zwracanie posortowaną listę procesów
    
    
class PageSequenceGenerator:

    # Klasa generująca losowe sekwencje stron

    def __init__(self, sequence_length: int, page_range: int):

        # Funkcja inicjalizuje obiekt klasy PageSequenceGenerator, który generuje losowe sekwencje stron

        self.sequence_length = sequence_length
        self.page_range = page_range

    def generate(self) -> List[int]:

        # Funkcja generuje losową sekwencję stron o określonej długości i zakresie stron
        
        return np.random.randint(0, self.page_range, self.sequence_length).tolist()