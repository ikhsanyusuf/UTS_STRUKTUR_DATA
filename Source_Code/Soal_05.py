from collections import deque

class AntrianBank:
    def __init__(self):
        self.antrian = deque()

    def masuk(self, pelanggan):
        self.antrian.append(pelanggan)
    
    def keluar(self):
        if self.antrian:
            return self.antrian.popleft()
        else:
            return "Antrian kosong"
