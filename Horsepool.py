def build_shift_table(pattern):
    table = {}
    pattern_length = len(pattern)
    
    for i in range(pattern_length - 1):
        table[pattern[i]] = pattern_length - 1 - i
    
    return table

def horspool_search(text, pattern):
    text_length = len(text)
    pattern_length = len(pattern)
    shift_table = build_shift_table(pattern)
    
    i = pattern_length - 1
    while i < text_length:
        k = 0
        while k < pattern_length and pattern[pattern_length - 1 - k] == text[i - k]:
            k += 1
        if k == pattern_length:
            return i - pattern_length + 1
        else:
            i += shift_table.get(text[i], pattern_length)
    
    return -1


text = "This is an example text for testing Horspool algorithm."
pattern = "Horspool"
index = horspool_search(text, pattern)

if index != -1:
    print("Pattern found at index:", index)
else:
    print("Pattern not found in the text.")
//Pattern found at index: 47
///
