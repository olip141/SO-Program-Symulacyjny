from fifo import fifo
from lru import lru
from generateData import PageSequenceGenerator
import os

def save_test_data(test_number, page_sequence, page_frames):
    folder = "DaneTestoweFIFOLRU"
    os.makedirs(folder, exist_ok=True)
    filename = os.path.join(folder, f"test_data_{test_number}.txt")
    with open(filename, 'w') as file:
        file.write(f"Nr testu: {test_number}\n")
        file.write(f"page_sequence = {page_sequence}\n")
        file.write(f"page_frames = {page_frames}\n")

def save_results(filename, page_sequence, page_faults, algorithm_name):
    folder = "WynikiEksperymentówFIFOLRU"
    os.makedirs(folder, exist_ok=True)
    filepath = os.path.join(folder, filename)
    with open(filepath, 'w') as file:
        file.write(f"Algorytm: {algorithm_name}\n")
        file.write(f"Sekwencja stron: {page_sequence}\n")
        file.write(f"{algorithm_name} Błędy strony: {page_faults}\n")
        
# Eksperyment 1: Mała liczba ramek

def eksperyment1():
    page_sequence = [1, 7, 5, 1, 2, 5, 7, 7, 2, 1]
    page_frames = 3

    save_test_data(1, page_sequence, page_frames)

    states, page_faults = fifo(page_sequence, page_frames)
    states2, page_faults2 = lru(page_sequence, page_frames)

    print("\nEksperyment 1 (Mała liczba ramek):")
    print("FIFO Błędy strony:", page_faults)
    print("LRU Błędy strony:", page_faults2)
    save_results("eksperyment1_FIFO.txt", page_sequence, page_faults, "FIFO")
    save_results("eksperyment1_LRU.txt", page_sequence, page_faults2, "LRU")

# Eksperyment 2: Duża liczba ramek

def eksperyment2():
    page_sequence = [1, 7, 5, 1, 2, 5, 7, 7, 2, 1]
    page_frames = 20

    save_test_data(2, page_sequence, page_frames)

    states, page_faults = fifo(page_sequence, page_frames)
    states2, page_faults2 = lru(page_sequence, page_frames)

    print("\nEksperyment 2 (Duża liczba ramek):")
    print("FIFO Błędy strony:", page_faults)
    print("LRU Błędy strony:", page_faults2)
    save_results("eksperyment2_FIFO.txt", page_sequence, page_faults, "FIFO")
    save_results("eksperyment2_LRU.txt", page_sequence, page_faults2, "LRU")

# Eksperyment 3: Efekt Belady'ego

def eksperyment3():
    page_sequence = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
    for frames in [3, 4, 5]:

        save_test_data(f"3_{frames}_Belady", page_sequence, frames)

        states, page_faults = fifo(page_sequence, frames)
        states2, page_faults2 = lru(page_sequence, frames)
        print(f"\nEksperyment 3 (Belady, {frames} ramki):")
        print("FIFO Błędy strony:", page_faults)
        print("LRU Błędy strony:", page_faults2)
        save_results(f"eksperyment3_FIFO(Belady,{frames} ramki).txt", page_sequence, page_faults, "FIFO")
        save_results(f"eksperyment3_LRU(Belady,{frames} ramki).txt", page_sequence, page_faults2, "LRU")

# Eksperyment 4: Lokalność odniesienia

def eksperyment4():
    page_sequence = [1, 2, 1, 3, 2, 1, 4, 5, 4, 6, 5, 4, 1, 2, 1, 3]
    page_frames = 4

    save_test_data(4, page_sequence, page_frames)

    states, page_faults = fifo(page_sequence, page_frames)
    states2, page_faults2 = lru(page_sequence, page_frames)
    print("\nEksperyment 4 (Lokalność):")
    print("FIFO Błędy strony:", page_faults)
    print("LRU Błędy strony:", page_faults2)
    save_results("eksperyment4_FIFO.txt", page_sequence, page_faults, "FIFO")
    save_results("eksperyment4_LRU.txt", page_sequence, page_faults2, "LRU")

# Eksperyment 5: Sekwencja losowa

def eksperyment5():
    page_sequence_generator = PageSequenceGenerator(sequence_length=20, page_range=10)
    page_sequence = page_sequence_generator.generate()
    page_frames = 5

    save_test_data(5, page_sequence, page_frames)

    states, page_faults = fifo(page_sequence, page_frames)
    states2, page_faults2 = lru(page_sequence, page_frames)
    print("\nEksperyment 5 (Losowa sekwencja):")
    print("FIFO Błędy strony:", page_faults)
    print("LRU Błędy strony:", page_faults2)
    save_results("eksperyment5_FIFO.txt", page_sequence, page_faults, "FIFO")
    save_results("eksperyment5_LRU.txt", page_sequence, page_faults2, "LRU")

# Eksperyment 6: Monotoniczny wzrost

def eksperyment6():
    page_sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    page_frames = 3

    save_test_data(6, page_sequence, page_frames)

    states, page_faults = fifo(page_sequence, page_frames)
    states2, page_faults2 = lru(page_sequence, page_frames)
    print("\nEksperyment 6 (Monotoniczny wzrost):")
    print("FIFO Błędy strony:", page_faults)
    print("LRU Błędy strony:", page_faults2)
    save_results("eksperyment6_FIFO.txt", page_sequence, page_faults, "FIFO")
    save_results("eksperyment6_LRU.txt", page_sequence, page_faults2, "LRU")

# Eksperyment 7: Duża powtarzalność jednej strony

def eksperyment7():
    page_sequence = [1, 2, 1, 4, 1, 6, 1, 8, 1, 10, 2, 1, 3, 1, 5, 1, 7, 1, 9, 1]
    page_frames = 3

    save_test_data(7, page_sequence, page_frames)

    states, page_faults = fifo(page_sequence, page_frames)
    states2, page_faults2 = lru(page_sequence, page_frames)
    print("\nEksperyment 7 (Duża powtarzalność jednej strony):")
    print("FIFO Błędy strony:", page_faults)
    print("LRU Błędy strony:", page_faults2)
    save_results("eksperyment7_FIFO.txt", page_sequence, page_faults, "FIFO")
    save_results("eksperyment7_LRU.txt", page_sequence, page_faults2, "LRU")

# Wywołanie eksperymentów

eksperyment1()
eksperyment2()
eksperyment3()
eksperyment4()
eksperyment5()
eksperyment6()
eksperyment7()