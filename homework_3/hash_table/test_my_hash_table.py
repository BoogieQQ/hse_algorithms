import pytest
from main import MyHashTable 


def test_initialization():
    ht = MyHashTable()
    assert ht.max_size == 8
    assert ht.size == 0
    assert len(ht.hash_table) == 8
    assert all(len(bucket) == 0 for bucket in ht.hash_table)

def test_initialization_with_custom_max_size():
    ht = MyHashTable(max_size=16)
    assert ht.max_size == 16
    assert ht.size == 0
    assert len(ht.hash_table) == 16

def test_get_index():
    ht = MyHashTable()
    key = "k1"
    index = ht._get_index(key)
    expected_index = hash(key) % 8
    assert index == expected_index
    assert 0 <= index < 8

def test_get_bucket():
    ht = MyHashTable()
    key = "k1"
    bucket = ht._get_bucket(key)
    index = ht._get_index(key)
    assert bucket is ht.hash_table[index]

def test_put_and_get():
    ht = MyHashTable()
    ht.put("k1", "v1")
    ht.put("k2", "v2")
    ht.put("k3", "v3")
    
    assert ht.get("k1") == "v1"
    assert ht.get("k2") == "v2"
    assert ht.get("k3") == "v3"
    assert ht.size == 3

def test_put_update_existing_key():
    ht = MyHashTable()
    ht.put("k1", "v1")
    ht.put("k1", "v12")
    
    assert ht.get("k1") == "v12"
    assert ht.size == 1 

def test_get_not_exist_key():
    ht = MyHashTable()
    assert ht.get("k1") is None
    assert ht.get("k1", 0) == 0

def test_delete():
    ht = MyHashTable()
    ht.put("k1", "м1")
    ht.put("k2", "v2")
    
    ht.delete("k1")
    assert ht.get("k1") is None
    assert ht.size == 1
    assert ht.get("k2") == "v2"

def test_delete_not_exist_key():
    ht = MyHashTable()
    ht.put("k1", "v1")
    
    with pytest.raises(KeyError, match="Key `k2` not found"):
        ht.delete("k2")
    
    assert ht.get("k1") == "v1"
    assert ht.size == 1

def test_contains():
    ht = MyHashTable()
    ht.put("k1", "v1")
    
    assert ht.contains("k1") is True
    assert ht.contains("k2") is False

def test_len():
    ht = MyHashTable()
    assert len(ht) == 0
    
    ht.put("k1", "v1")
    assert len(ht) == 1
    
    ht.put("k2", "v2")
    assert len(ht) == 2
    
    ht.delete("k2")
    assert len(ht) == 1

def test_keys():
    ht = MyHashTable()
    ht.put("k1", "v1")
    ht.put("k2", "v2")
    ht.put("k3", "v3")
    
    keys = ht.keys()
    assert len(keys) == 3
    assert "k1" in keys
    assert "k2" in keys
    assert "k3" in keys

def test_values():
    ht = MyHashTable()
    ht.put("k1", "v1")
    ht.put("k2", "v2")
    ht.put("k3", "v3")

    values = ht.values()
    assert len(values) == 3
    assert "v1" in values
    assert "v2" in values
    assert "v3" in values

def test_items():
    ht = MyHashTable()
    ht.put("k1", "v1")
    ht.put("k2", "v2")
    ht.put("k3", "v3")
    
    items = ht.items()
    assert len(items) == 3
    assert ("k1", "v1") in items
    assert ("k2", "v2") in items
    assert ("k3", "v3") in items

def test_resize_trigger():
    ht = MyHashTable(max_size=2)
    
    ht.put("k1", "v1")
    ht.put("k2", "v2")
    
    assert ht.max_size == 4 
    assert ht.size == 2
    
    assert ht.get("k1") == "v1"
    assert ht.get("k2") == "v2"


def test_collision_handling():
    ht = MyHashTable(max_size=1)  
    
    ht.put("k1", "v1", block_resize=True)
    ht.put("k2", "v2", block_resize=True)
    ht.put("k3", "v3", block_resize=True)
    
    assert ht.size == 3
    assert len(ht._get_bucket("k4")) == 3
    
    assert ht.get("k1") == "v1"
    assert ht.get("k2") == "v2"
    assert ht.get("k3") == "v3"

def test_update_value_in_collision_bucket():
    ht = MyHashTable(max_size=1)  
    
    ht.put("k1", "v1", block_resize=True)
    ht.put("k2", "v2", block_resize=True)
    ht.put("k1", "v12", block_resize=True)
    
    assert ht.size == 2
    assert ht.get("k1") == "v12"
    assert ht.get("k2") == "v2"

def test_delete_from_collision_bucket():
    ht = MyHashTable(max_size=1)  
    
    ht.put("k1", "v1", block_resize=True)
    ht.put("k2", "v2", block_resize=True)
    ht.put("k3", "v3", block_resize=True)
    
    ht.delete("k2")
    assert ht.size == 2
    assert ht.get("k1") == "v1"
    assert ht.get("k2") is None
    assert ht.get("k3") == "v3"

    ht.delete("k1")
    assert ht.size == 1
    assert ht.get("k1") is None
    assert ht.get("k2") is None
    assert ht.get("k3") == "v3"

    ht.delete("k3")
    assert ht.size == 0
    assert ht.get("k1") is None
    assert ht.get("k2") is None
    assert ht.get("k3") is None

def test_recreate_with_new_size():
    ht = MyHashTable(max_size=2)
    ht.put("k1", "v1", block_resize=True)
    ht.put("k2", "v2", block_resize=True)
    
    original_size = ht.size
    ht._recreate_with_new_size(8)
    
    assert ht.max_size == 8
    assert ht.size == original_size
    assert ht.get("k1") == "v1"
    assert ht.get("k2") == "v2"
