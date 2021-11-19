# Hash Table without collision handling

class HashTable:
    def __init__(self):
        self.max = 100
        self.arr = [None for i in range(self.max)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)          # ord(char) gets the ASCII value
        return h % self.max

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val

    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]

    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None

if __name__ == '__main__':
    t = HashTable()
    t['march 9'] = 130
    t['march 1'] = 70
    t['dec 17'] = 20
    print(t.arr)
    del t['dec 17']
    print(t['dec 17'])
