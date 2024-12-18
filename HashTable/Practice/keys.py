class HashTable:
    def __init__(self, size=7):
        self.data_map: list[list[list] | None] = [None] * size

    def __str__(self):
        result = []
        for i, val in enumerate(self.data_map):
            result.append(f"{i}: {val}")
        return str(result)

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)

    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def set_item(self, key: str, value: int):
        index = self.__hash(key)
        bucket = self.data_map[index]

        # Initialize the bucket if it is empty
        if bucket is None:
            bucket = []  # Replace 'None' with an empty list
            self.data_map[index] = bucket

        # Check if the key exists and update its value
        for i, (existing_key, _) in enumerate(bucket):
            if existing_key == key:
                # Update the value while maintaining a nested list structure
                bucket[i] = [key, value]
                return

        # Add the new key-value pair as a nested list
        bucket.append([key, value])

    def get_item(self, key: str):
        index = self.__hash(key)
        bucket = self.data_map[index]

        if bucket is None:
            return None

        for i, (existing_key, existing_value) in enumerate(bucket):
            if existing_key == key:
                return existing_value

    def keys(self):
        all_keys = []

        for bucket in self.data_map:
            # Skip if the 'bucket' is None
            if bucket is not None:
                # Collect the key from each nested bucket
                for existing_key, _ in bucket:
                    all_keys.append(existing_key)

        return all_keys


my_hash_table = HashTable()

my_hash_table.set_item('bolts', 1400)
my_hash_table.set_item('washers', 50)
my_hash_table.set_item('lumber', 70)

print(my_hash_table.keys())

"""
    EXPECTED OUTPUT:
    ----------------
    ['bolts', 'washers', 'lumber']

"""