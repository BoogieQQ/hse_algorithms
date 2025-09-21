from main import count_primes

def test_examples():
    assert count_primes(10) == 4
    assert count_primes(1) == 0

def test_known_numbers():
    known_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 
                   43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
                   101, 103, 107, 109, 113, 127, 131, 137, 139, 149]
    
    for i in range(1, known_primes[-1]+1):
        expected = sum([e in known_primes for e in range(1, i)])
        assert count_primes(i) == expected, f"Failed for n={i}"

def test_negative_numbers():
    assert count_primes(-1) == 0 
    assert count_primes(-5) == 0

def test_zero_numbers():
    assert count_primes(0) == 0
