def main():
    s = "babad"

    longest_palindrome = ""
    longest_palindrome_length = 0

    for i in range(len(s)):
        l, r = i, i
        while l >=0 and r <= len(s) and s[l]==s[r]:
            if (r- l +1) > longest_palindrome_length:
                if longest_palindrome

                
            

    


if __name__ == "__main__":
    main()