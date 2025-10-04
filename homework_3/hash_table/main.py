class MyHashTable:
    def __init__(self, max_size=8):
        self.max_size = max_size
        self.size = 0
        self.hash_table = [[] for _ in range(max_size)]
    
    def _get_index(self, key):
        return hash(key) % self.max_size
    
    def _is_resize(self):
        return self.max_size - self.size == 1
    
    def _get_bucket(self, key):
        index = self._get_index(key)
        bucket = self.hash_table[index]
        return bucket
    
    def _recreate_with_new_size(self, new_max_size):
        old_table = self.hash_table
        self.max_size = new_max_size
        self.hash_table = [[] for _ in range(new_max_size)]
        self.size = 0
        
        for bucket in old_table:
            for key, value in bucket:
                self.put(key, value)
    
    def __len__(self):
        return self.size
    
    def put(self, key, value, block_resize=False):
        if self._is_resize() and not block_resize:
            self._recreate_with_new_size(self.max_size * 2)
        
        bucket = self._get_bucket(key)
        
        # Обновление, если ключ существует
        for i, (existing_key, _) in enumerate(bucket):
            if existing_key == key:
                bucket[i] = (key, value)
                return
            
        # Добавление новой пары иначе
        bucket.append((key, value))
        self.size += 1
    
    def get(self, key, default=None):
        bucket = self._get_bucket(key)
        
        for existing_key, value in bucket:
            if existing_key == key:
                return value
        
        return default
    
    def delete(self, key):
        bucket = self._get_bucket(key)
        
        for i, (existing_key, _) in enumerate(bucket):
            if existing_key == key:
                del bucket[i]
                self.size -= 1
                return
                
        raise KeyError(f"Key `{key}` not found")
        
    
    def contains(self, key):
        return self.get(key) is not None
    
    def keys(self):
        keys_list = []
        for bucket in self.hash_table:
            for key, _ in bucket:
                keys_list.append(key)
        return keys_list
    
    def values(self):
        values = []
        for bucket in self.hash_table:
            for _, value in bucket:
                values.append(value)
        return values
    
    def items(self):
        items = []
        for bucket in self.hash_table:
            for item in bucket:
                items.append(item)
        return items
    