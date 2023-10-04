class Stack:
    def __init__(self):
        self.items = []

    def masuk(self, pelanggan):
        self.items.append(pelanggan)

    def keluar(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "kosong"
        
    def is_empty(self):
        return len(self.items) == 0
