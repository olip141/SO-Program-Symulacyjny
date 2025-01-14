from generateData import Process

def fcfs(processes):
    # Sortowanie procesów względem czasu nadejścia
    processes.sort(key=lambda p: p.arrival_time)
    
    current_time = 0
    done_processes = []

    for process in processes:
        # Jeśli bieżący czas jest mniejszy niż czas nadejścia procesu,
        # proces zacznie się wykonywać dopiero od momentu nadejścia
        if current_time < process.arrival_time:
            current_time = process.arrival_time  # Czekamy na proces, jeśli jego czas nadejścia jest późniejszy

        # Czas zakończenia procesu
        process.completion_time = current_time + process.burst_time  # Zakończenie procesu to czas rozpoczęcia + czas trwania - 1
        process.waiting_time = current_time - process.arrival_time  # Czas oczekiwania
        current_time = process.completion_time  # Następny proces zaczyna się po zakończeniu obecnego
        done_processes.append(process)

    print("\n--------------------------------ALGORYTM FCFS---------------------------------")
    print("Proces | Czas nadejścia  | Czas wykonania | Czas zakończenia| Czas oczekiwania")
    for process in done_processes:
        print(f"{process.name:6} | {process.arrival_time:15} | {process.burst_time:14} | {process.completion_time:15} | {process.waiting_time:16}")

    # Obliczanie i wypisywanie średniego czasu oczekiwania
    average_waiting_time = sum(p.waiting_time for p in done_processes) / len(done_processes)
    print(f"Średni czas oczekiwania: {average_waiting_time:.2f}")