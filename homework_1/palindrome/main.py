def is_palindrome(n):
    n_str = str(n)
    n_len = len(n_str)

    return n_str[:n_len // 2] == n_str[::-1][:n_len // 2]
