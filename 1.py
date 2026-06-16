def compress(text):
    if not text:
        return ""

    compressed = ""
    current_char = text[0]
    count = 1

    for char in text[1:]:
        if char == current_char:
            count += 1
        else:
            # Build string using format: Letter + Count (omit 1 for single letters)
            compressed += current_char + (str(count) if count > 1 else "")
            current_char = char
            count = 1

    # Add the last character
    compressed += current_char + (str(count) if count > 1 else "")
    return compressed


def decompress(text):
    decompressed = ""
    i = 0

    while i < len(text):
        char = text[i]
        i += 1

        # Check if the next character is a number
        count_str = ""
        while i < len(text) and text[i].isdigit():
            count_str += text[i]
            i += 1

        # Use the number found, or default to 1
        count = int(count_str) if count_str else 1
        decompressed += char * count

    return decompressed


# --- Example Usage ---
print(compress("AAACCCBBD"))  # Output: A3C3B2D
print(decompress("A3C3B2D"))  # Output: AAACCCBBD