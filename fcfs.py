from generateData import Process

def fcfs(processes):

    # Funkcja implementująca algorytm FCFS (First-Come-First-Served)
    
    current_time = 0      # Aktualny czas w systemie
    done_processes = []   # Lista przechowująca zakończone procesy

    # Iteracja po procesach w kolejności ich nadejścia
    for process in processes:
        if current_time < process.arrival_time: # Jeśli proces przybywa po bieżącym czasie, ustawienie czasu na czas nadejścia tego procesu
            current_time = process.arrival_time

        process.completion_time = current_time + process.burst_time # Obliczenie czasu zakończenia procesu
        process.waiting_time = current_time - process.arrival_time  # Obliczenie czasu oczekiwania procesu
        current_time = process.completion_time                      # Aktualizacja bieżącego czasu na czas zakończenia procesu
        done_processes.append(process)                              # Dodanie procesu do listy zakończonychy procesów

    # Obliczenie średniego czasu oczekiwania
    average_waiting_time = sum(p.waiting_time for p in done_processes) / len(done_processes)

    return done_processes, average_waiting_time


def fcfs_with_steps(processes):

    # Funkcja pokazująca działanie algorytmu FCFS krok po kroku

    done_processes, average_waiting_time = fcfs(processes)

    print("\n--------------------------------ALGORYTM FCFS---------------------------------")
    print("Proces | Czas nadejścia  | Czas wykonania | Czas zakończenia| Czas oczekiwania")

    # Iteracja przez wszystkie zakończone procesy
    for process in done_processes:
        print(f"{process.name:6} | {process.arrival_time:15} | {process.burst_time:14} | {process.completion_time:15} | {process.waiting_time:16}")

    print("Średni czas oczekiwania dla FCFS:", average_waiting_time)