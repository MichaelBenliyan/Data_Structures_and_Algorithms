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
        count = 0
        while count < self.MAX:
            if self.arr[h][0] == key:
                return self.arr[h][1]
            else:
                h = (h+1) % self.MAX
                count += 1
        return None

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        count = 0
        while count < self.MAX:
            if self.arr[h] is None or self.arr[h][0] == key:
                self.arr[h] = (key, val)
                return True
            else:
                h = (h+1) % self.MAX
                count += 1
        raise Exception("Hashmap is Full")

    def __delitem__(self, key):
        h = self.get_hash(key)
        count = 0
        while count < self.MAX:
            if self.arr[h][0] == key:
                self.arr[h] = None
                return True
            else:
                h = (h + 1) % self.MAX
                count += 1
        return False


t = HashTable()
t["march 6"] = 20
t["march 17"] = 88
print(t.arr)
t["march 17"] = 29
print(t.arr)
t["nov 1"] = 1
print(t.arr)
t["march 33"] = 234
print(t.arr)
print(t["march 33"])
t["march 33"] = 999
print(t.arr)
print(t["march 33"])
t["april 1"]=87
print(t.arr)
t["april 2"]=123
print(t.arr)
t["april 3"]=234234
print(t.arr)
t["april 4"]=91
print(t.arr)
t["May 22"]=4
print(t.arr)
t["May 7"]=47
print(t.arr)
del t["april 2"]
print(t.arr)
t["Jan 1"]=0
print(t.arr)