from generateData import Process

def lcfs(processes):
    # Stos do przechowywania procesów w odwrotnej kolejności przybycia
    stack = []
    current_time = 0
    index = 0
    done_processes = []
    
    while index < len(processes) or stack:
        # Dodaj procesy, które już nadeszły i nie zostały jeszcze wzięte do stosu
        while index < len(processes) and processes[index].arrival_time <= current_time:
            stack.append(processes[index])
            index += 1

        if stack:
            # Wybierz proces do wykonania (ostatni dodany do stosu)
            current_process = stack.pop()  # LCFS: wybieramy ostatni proces w stosie
            current_process.completion_time = current_time + current_process.burst_time
            current_process.waiting_time = current_process.completion_time - current_process.arrival_time - current_process.burst_time
            current_time = current_process.completion_time 
            done_processes.append(current_process)
        else:
            # Jeśli stos jest pusty, przesuń czas do momentu, kiedy przyjdzie następny proces
            current_time = processes[index].arrival_time

    # Wypisanie wyników
    print("\n--------------------------------ALGORYTM LCFS---------------------------------")
    print("Proces | Czas nadejścia  | Czas wykonania | Czas zakończenia| Czas oczekiwania")
    for process in done_processes:
        print(f"{process.name:6} | {process.arrival_time:15} | {process.burst_time:14} | {process.completion_time:15} | {process.waiting_time:16}")

    # Obliczanie i wypisywanie średniego czasu oczekiwania
    average_waiting_time = sum(p.waiting_time for p in done_processes) / len(done_processes)
    print(f"Średni czas oczekiwania: {average_waiting_time:.2f}")