def fifo(page_sequence, page_frames):
   
    # Argumenty funckji:
    # page_sequence (lista): sekwencja stron
    # page_frames (int): liczba dostępnych ramek

    frames = []
    page_faults = 0
    states = []

    # Pętla iteruje po kolejnych elementach sekwencji stron łącząc je z indeksem
    for i, page in enumerate(page_sequence):
        if page not in frames:
            page_faults += 1                    # Jeśli strona nie jest w ramkach występuje błąd brak strony (page fault)
            if len(frames) >= page_frames:
                frames.pop(0)                   # Usuwanie najdłużej znajdującej się w ramce strony, odpowiadającej id = 0 w liście
            frames.append(page)                 # Dodanie kolejnej strony z sekwencji do ramki
        states.append(list(frames))             # Dodanie stanu ramek do listy stanów

    return states, page_faults

def fifo_with_steps(page_sequence, page_frames):

    # Funkcja pokazująca działanie algorytmu FIFO krok po kroku

    states, page_faults = fifo(page_sequence, page_frames)

    print("\n----------------Algorytm FIFO----------------")
    print("\nKrok\tRamki")
    # Wyświetlanie kolejnych kroków i obecnego stanu ramek
    for i, state in enumerate(states):
        print(f"{i + 1}\t{state}")
    print("\nFIFO trafienia: ", (len(page_sequence) - page_faults))
    print("FIFO Błędy strony:", page_faults)