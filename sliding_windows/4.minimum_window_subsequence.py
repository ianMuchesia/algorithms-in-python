def min_window(str1, str2):
    
    p = q = 0
    
    while q < len(str2) and p < len(str1):
        
        if str2[q] == str1[p]:
            q+=1
        
        p+=1
    
   
    
   
    return ""


min_window("abcdebdde", "bde")

def min_window(str1, str2):
    if not str1 or not str2:
        return ""

    char_count = {}
    for char in str2:
        char_count[char] = char_count.get(char, 0) + 1

    required_chars = len(char_count)
    formed_chars = 0
    left = right = 0
    min_len = float('inf')
    result = ""

    while right < len(str1):
        current_char = str1[right]

        if current_char in char_count:
            char_count[current_char] -= 1
            if char_count[current_char] == 0:
                formed_chars += 1

        while formed_chars == required_chars:
            if right - left + 1 < min_len:
                min_len = right - left + 1
                result = str1[left:right + 1]

            if str1[left] in char_count:
                char_count[str1[left]] += 1
                if char_count[str1[left]] > 0:
                    formed_chars -= 1

            left += 1

        right += 1

    return result

result = min_window("abcdebdde", "bde")
print(result)
