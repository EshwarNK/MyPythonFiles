'''Implementation of Hash Tables
The idea of a dictionary used as a hash table to get and retrieve items using keys is often
referred to as a mapping. In our implementation we will have the following methods:

HashTable() Create a new, empty map. It returns an empty map collection.
put(key,val) Add a new key-value pair to the map. If the key is already in the map then replace the old value with the new value.
get(key) Given a key, return the value stored in the map or None otherwise.
del Delete the key-value pair from the map using a statement of the form del map[key].
len() Return the number of key-value pairs stored
in the map in Return True for a statement of the form key in map, if the given key is in the map, False otherwise.'''

class HashTable(object):

    def __init__(self, size):       #initializing our hash table
        self.size = size
        self.slots = [None] * self.size #[None, None.....]
        self.data = [None] * self.size

    def put(self, key, data): # To put in a piece of data to the correct key

        hashvalue = self.hashfunction(key, len(self.slots))

        if self.slots[hashvalue] == None:       #If the slot is empty, we fill in the key and the data in the corresponding slot
            # print(key, data)
            self.slots[hashvalue] = key
            self.data[hashvalue] = data

        else:       #If the key already exists, we go ahead and replace the old value

            if self.slots[hashvalue] == key:
                self.slots[hashvalue] = data

            else:       # If the key does not exist, we go ahead and find the next available slot

                nextslot = self.rehash(hashvalue, len(self.slots)) #When a collission occurs, we get into the next slot

                while self.slots[nextslot] != None and self.slots[nextslot] != key: #To find the next empty slot
                    nextslot = self.rehash(nextslot, len(self.slots))

                if self.slots == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data


    def hashfunction(self, key, size):  # Remainder method
        return key%size

    def rehash(self, oldhash, size):
        return (oldhash+1)%size

    def get(self, key):     # To find the data given the key
        startslot = self.hashfunction(key, len(self.slots))     # To tell what start do we start off in our search
        data = None
        stop = None
        found = None
        position = startslot

        while self.slots[position] != None and not found and not stop:  #Continue as long as it is not empty

            if self.slots[position] == key:
                found = True
                data = self.data[position]

            else:
                position = self.rehash(position, len(self.slots))   #Continue to the next slot
                if position == startslot:
                    stop = True
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key,data)

h = HashTable(5)
h[1] = 'One'
h[2] = 'Two'
h[3] = 'Three'
print(h[1])
print(h[2])
print(h[3])


