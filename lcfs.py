from generateData import Process 

def lcfs(processes):

    # Funkcja implementująca algorytm LCFS (Last-Come-First-Served)

    stack = []              # Stos do przechowywania procesów w odwrotnej kolejności przybycia (zgodnie z algorytmem LCFS)
    current_time = 0        # Aktualny czas w systemie
    index = 0               # Indeks procesu, który jest obecnie rozważany
    done_processes = []     # Lista przechowująca zakończone procesy

    # Pętla, która działa dopóki mamy procesy do obsłużenia lub stos nie jest pusty
    while index < len(processes) or stack:  
        # Dodaje procesy, które już nadeszły do stosu (procesy przybywające do bieżącego momentu czasu)
        while index < len(processes) and processes[index].arrival_time <= current_time: 
            stack.append(processes[index])  # Dodaj proces do stosu
            index += 1  

        # Jeśli stos nie jest pusty, wybiera proces do wykonania
        if stack:
    
            current_process = stack.pop() # Usunięcie procesu ze stosu
            
            current_process.completion_time = current_time + current_process.burst_time                                                # Obliczenie czasu zakończenia procesu
            current_process.waiting_time = current_process.completion_time - current_process.arrival_time - current_process.burst_time # Obliczenie czasu oczekiwania procesu
            current_time = current_process.completion_time                                                                             # Aktualizacja bieżącego czasu na czas zakończenia procesu
            done_processes.append(current_process)                                                                                     # Dodanie procesu do listy zakończonych procesów
        else:
            current_time = processes[index].arrival_time # Jeśli stos jest pusty, to czekamy na kolejny proces, który nadchodzi

    # Obliczenie średniego czasu oczekiwania
    average_waiting_time = sum(p.waiting_time for p in done_processes) / len(done_processes)

    return done_processes, average_waiting_time


def lcfs_with_steps(processes):

    # Funkcja pokazująca działanie algorytmu LCFS krok po kroku

    done_processes, average_waiting_time = lcfs(processes)

    print("\n--------------------------------ALGORYTM LCFS---------------------------------")
    print("Proces | Czas nadejścia  | Czas wykonania | Czas zakończenia| Czas oczekiwania")
    
    # Iteracja przez wszystkie zakończone procesy
    for process in done_processes:
        print(f"{process.name:6} | {process.arrival_time:15} | {process.burst_time:14} | {process.completion_time:15} | {process.waiting_time:16}")

   
    print("Średni czas oczekiwania dla LCFS:", average_waiting_time)
