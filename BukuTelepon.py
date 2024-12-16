class BukuTelepon:
    def __init__(self):
        self.size = 6
        self.map = [None] * self.size

    def _getHash(self, key):
        hash = 0
        for char in str(key):
            hash += ord(char) # mendapatkan nilai ASCII
        return hash % self.size
 
    # menambahkan key pada hash table
    def add(self, key, value):
        # periksa apakah key_hash sudah terpakai
        key_hash = self._getHash(key)
        # buat pasangan key value
        key_value = [key, value]
 
        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            return True
        else:
            print("Key Hash ", key_hash, " sudah terisi")
            return False
    def getPhoneNumber(self, key):
        key_hash = self._getHash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        print("Key ",key, " tidak ditemukan")
        return "None"
    #Menghapus
    def delete(self, key):
        key_hash = self._getHash(key)
        # pastikan key_hash tidak kosong
        if self.map[key_hash] is None:
            return False
        for i in range(0, len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash] = None
                return True
        print("Key ",key, " tidak ditemukan")
        return False
    def print(self):
        print('---Buku Telepon----')
        for item in self.map:
            if item is not None:
                print(str(item))

h = BukuTelepon()
h.add('Dendy', '567-8888')
h.add('Yuan', '293-6753')
h.add('Anton', '333-8233')
h.add('Adi', '293-8625')
h.add('Dida', '293-8625')
h.print()
h.delete('Dida')
h.print()
print('Anton: ' + h.getPhoneNumber('Anton'))