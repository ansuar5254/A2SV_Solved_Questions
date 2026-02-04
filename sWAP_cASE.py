def swap_case(s):
    result = []
    for i in range(len(s)):
        if s[i].islower():
            result.append(s[i].upper())
        elif s[i].isupper():
            result.append(s[i].lower())
        else:
            result.append(s[i])
    return ''.join(result)
        

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
