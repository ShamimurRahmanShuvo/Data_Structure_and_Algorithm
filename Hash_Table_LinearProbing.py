# Hash Table with Linear Probing

class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX

    def __getitem__(self, key):
        h = self.get_hash(key)
        if self.arr[h] is None:
            return
        prob_range = self.get_prob_range(h)
        for prob_index in prob_range:
            element = self.arr[prob_index]
            if element is None:
                return
            if element[0] == key:
                return element[1]

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        if self.arr[h] is None:
            self.arr[h] = (key, val)
        else:
            new_h = self.find_slot(key, h)
            self.arr[new_h] = (key, val)
        print(self.arr)

    def get_prob_range(self, index):
        return [*range(index, len(self.arr))] + [*range(0, index)]

    def find_slot(self, key, index):
        prob_range = self.get_prob_range(index)
        for prob_index in prob_range:
            if self.arr[prob_index] is None:
                return prob_index
            if self.arr[prob_index][0] == key:
                return prob_index
        raise Exception("Hashmap Full")

    def __delitem__(self, key):
        h = self.get_hash(key)
        prob_range = self.get_prob_range(h)
        for prob_index in prob_range:
            if self.arr[prob_index] is None:
                return
            if self.arr[prob_index][0] == key:
                self.arr[prob_index] = None
        print(self.arr)

if __name__ == '__main__':
    t = HashTable()
    print("Checking Range: ", [*range(5,8)] + [*range(0,4)])
    t["march 6"] = 20
    t["march 17"] = 88
    t["march 10"] = 29
    t["nov 1"] = 1
    t["march 33"] = 234
    t["april 1"] = 32
    t["april 2"] = 90
    t["april 3"] = 123
    t["dec 1"] = 234
    t["dec 2"] = 345
    del t["march 17"]