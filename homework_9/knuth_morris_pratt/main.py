

def kmp_search(text, target):
    def build_kmp_table(target):
        m = len(target)
        kmp_table = [0] * m
        length = 0

        i = 1
        while i < m:
            if target[i] == target[length]:
                length += 1
                kmp_table[i] = length
                i += 1
            else:
                if length != 0:
                    length = kmp_table[length - 1]
                else:
                    kmp_table[i] = 0
                    i += 1
        
        return kmp_table

    n, m = len(text), len(target)
    
    if m == 0:
        return []
    if n == 0 or m > n:
        return []
    
    kmp_table = build_kmp_table(target)
    
    results = []
    
    i = j = 0     
    while i < n:
        if target[j] == text[i]:
            i += 1
            j += 1
        
        if j == m:
            results.append(i - j)
            j = kmp_table[j - 1]
        elif i < n and target[j] != text[i]:
            if j != 0:
                j = kmp_table[j - 1]
            else:
                i += 1
    
    return results
