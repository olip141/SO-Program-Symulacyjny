def lru(page_sequence, page_frames):
   
    # Argumenty funckji:
    # page_sequence (lista): sekwencja stron
    # page_frames (int): liczba dostępnych ramek
    
    frames = []
    recent_use = {}
    page_faults = 0
    states = []

    # Pętla iteruje po kolejnych elementach sekwencji stron łącząc je z indeksem (time)
    for time, page in enumerate(page_sequence):
        if page not in frames:
            page_faults += 1                                        # Jeśli strona nie jest w ramkach występuje błąd braku strony (page fault)
            if len(frames) >= page_frames:
                lru_page = min(frames, key=lambda p: recent_use[p]) # Znalezienie strony w ramkach, użytej w jak najmniejszym czasie funkcją min
                frames.remove(lru_page)                             # Usunięcie strony w ramkach, użytej w jak najmniejszym czasie
            frames.append(page)
        recent_use[page] = time                                     # Aktualizacja w jakim czasie użyto strony
        states.append(list(frames))                                 # Dodanie stanu ramek do listy stanów

    return states, page_faults

def lru_with_steps(page_sequence, page_frames):

    # Funkcja pokazująca działanie algorytmu LRU krok po kroku

    states, page_faults = lru(page_sequence, page_frames)

    print("\n----------------Algorytm LRU----------------")
    print("\nKrok\tRamki")
    # Wyświetlanie kolejnych kroków i obecnego stanu ramek
    for i, state in enumerate(states):
        print(f"{i + 1}\t{state}")
    print("\nLRU trafienia: ", (len(page_sequence) - page_faults))
    print("LRU Błędy strony:", page_faults)