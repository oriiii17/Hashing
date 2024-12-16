# Slot = (h(key)+i ) % M

class BukuTelepon:
    def __init__(self):
        self.size = 6
        self.map = [None] * self.size
    def _getHash(self, key):
        hash = 0
        for char in str(key):
            hash += ord(char) # mendapatkan nilai ASCII
        return hash % self.size
    def _probing(self, key):
        for index in range(self.size):
            # probeHash = (self._getHash(key)+index) % self.size
            probeHash = self._linearProbing(key, index)
            # valid bila index adalah None atau ber-flag deleted
            if (self.map[probeHash] is None) or (self.map[probeHash] == 'deleted'):
            return probeHash
 
        return None
 
    # melakukan linear probing
    def _linearProbing(self, key, index):
        return (self._getHash(key)+index) % self.size
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
            key_hash = self._probing(key)
            if key_hash is None:
                print("Buku telephone sudah penuh")
                return False
 
        self.map[key_hash] = list([key_value])
        return False
 
    def getPhoneNumber(self, key):
        key_hash = self._getHash(key)
        if (self.map[key_hash] is not None) and (self.map[key_hash] != 'deleted'):
            for index in range(self.size):
                #mencari dengan melakukan probing
                key_hash = self._linearProbing(key, index)
                # periksa apakah key adalah data yg akan dihapus
                if(self.map[key_hash][0][0] == key):
                    return self.map[key_hash][0][1]
 
        print("Key ", key, " tidak ditemukan")
        return "None"
 
    def delete(self, key):
        key_hash = self._getHash(key)
        if self.map[key_hash] is None:
            return False
        for index in range(self.size):
            #menghapus dengan melakukan linear probing
            key_hash = self._linearProbing(key, index)
            # periksa apakah key adalah data yg akan dihapus
            if(self.map[key_hash][0][0] == key):
                print("deleting ", key)
                self.map[key_hash] = "deleted"
                return True
 
        print("Key ", key, " tidak ditemukan")
        return False
    
    def print(self):
        print('---Buku Telephone----')
        for item in self.map:
            if item is not None:
            print(str(item))