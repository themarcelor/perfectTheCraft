# -*- coding: utf-8 -*-
"""
 A palindrome is a string that reads the same forward and backward, 
 for example, radar, toot, and madam.
"""


palim = "radar"
notPalim = "sam"


def isPalindrome(str):
        str.lower()
        left  =0
        right = len(str) - 1
        while(left <= right):
                while(left <= len(str) and not str[left].isalpha()):
                        left+=1
                while(right > 0 and not str[right].isalpha()):
                        right-=1
                if ( (left > len(str) or right < 0) or (str[left] != str[right])):
                  return False

                left+=1
                right-=1
        return True



if __name__ == '__main__':
       print(isPalindrome(palim))
       print(isPalindrome(notPalim))