Executable File  6 lines (6 sloc)  189 Bytes
#!/usr/bin/python3
def remove_char_at(str, n):
    """Create a copy of the string without the character at position n"""
    if n < 0:
        return (str)
    return (str[:n] + str[n+1:])
