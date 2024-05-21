class MyStack:
    def __init__(self):
        self.files = []

    def push(self, file):
        self.files.append(file)
        print(f"File '{file}' telah ditambahkan ke dalam laci.")

    def pop(self):
        if self.is_empty():
            print("Laci kosong.")
            return None
        else:
            file = self.files.pop()
            print(f"File '{file}' telah diambil dari laci.")
            return file

    def is_empty(self):
        return len(self.files) == 0

    def peek(self):
        if self.is_empty():
            print("Laci kosong.")
            return None
        else:
            return self.files[-1]

def main():
    laci = MyStack()
    while True:
        print("\nPilihan:")
        print("1. Tambahkan file ke dalam laci")
        print("2. Mengambil file dari laci")
        print("3. Lihat file teratas di dalam laci")
        print("4. Keluar")
        choice = input("Silahkan masukkan pilihan Anda: ")

        if choice == "1":
            file = input("Masukkan nama file yang anda ingin ditambahkan: ")
            laci.push(file)
        elif choice == "2":
            laci.pop()
        elif choice == "3":
            top_file = laci.peek()
            if top_file:
                print(f"File teratas di laci: {top_file}")
        elif choice == "4":
            print("Program berakhir.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")

if __name__ == "__main__":
    main()
