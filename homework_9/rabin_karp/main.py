def rabin_karp(text, target, base=256, prime=101):
    n, m = len(text), len(target)
    
    if m == 0 or n < m:
        return []
    
    results = []
    
    target_hash = 0
    text_hash = 0
    h = base**(m-1) % prime

    for i in range(m):
        target_hash = (target_hash * base + ord(target[i])) % prime
        text_hash   = (text_hash * base   + ord(text[i]))   % prime
    
    for i in range(n - m + 1):
        if target_hash == text_hash:
            if text[i:i + m] == target:
                results.append(i)
        
        if i < n - m:
            text_hash = (base * (text_hash - ord(text[i]) * h) + ord(text[i + m])) % prime
            
            text_hash = text_hash if text_hash >= 0 else text_hash + prime
    
    return results
