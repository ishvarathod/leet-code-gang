def lengthOfLongestSubstring(s: str) -> int:
    max_string = ""
    max_count = 0
    for char in s:
        if char in max_string:
            max_string = max_string + char
            index = max_string.find(char)
            max_string = max_string[index+1:]
        else:
            max_string = max_string + char

            
            if len(max_string) > max_count:            
                max_count = len(max_string)

    return max_count




def main():
    # s = "aab"
    # s = "dvdf"
    s ="aabaab!bb"


    print(lengthOfLongestSubstring(s))



if __name__ == "__main__":
    main()