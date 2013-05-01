def is_palindrome(string):
    i = 0
    while i < len(string) / 2:
        if string[i] != string[-(i+1)]:
            return False
        i += 1
    return True
