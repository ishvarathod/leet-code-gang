def lengthOfLongestSubstring(s: str) -> int:
    max_string = ""
    max_count = 0
    for char in s:
        if char in max_string:
            index = s.find(char)
            max_string = max_string[index + 1:]
            max_string = max_string + char

            print("max_string if in str and go back=", repr(max_string))

        
            print("max_string if in str =", repr(max_string))

        else:
            max_string = max_string + char
            print("max_string if not in str =", repr(max_string))

            
            if len(max_string) > max_count:            
                max_count = len(max_string)

    return max_count




def main():
    # s = "aab"
    s = "dvdf"
    print(lengthOfLongestSubstring(s))



if __name__ == "__main__":
    main()