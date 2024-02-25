'''You are given an encoded string s. To decode the string to a tape, the encoded string is read one character at a time and the following steps are taken:

If the character read is a letter, that letter is written onto the tape.
If the character read is a digit d, the entire current tape is repeatedly written d - 1 more times in total.
Given an integer k, return the kth letter (1-indexed) in the decoded string.



Example 1:

Input: s = "leet2code3", k = 10
Output: "o"
Explanation: The decoded string is "leetleetcodeleetleetcodeleetleetcode".
The 10th letter in the string is "o".
Example 2:

Input: s = "ha22", k = 5
Output: "h"
Explanation: The decoded string is "hahahaha".
The 5th letter is "h".
Example 3:

Input: s = "a2345678999999999999999", k = 1
Output: "a"
Explanation: The decoded string is "a" repeated 8301530446056247680 times.
The 1st letter is "a".
 

Constraints:

2 <= s.length <= 100
s consists of lowercase English letters and digits 2 through 9.
s starts with a letter.
1 <= k <= 109
It is guaranteed that k is less than or equal to the length of the decoded string.
The decoded string is guaranteed to have less than 263 letters.

Level : Medium'''

# class Solution:

#     def getNums(self, s: str) -> list:
#         numList = []
#         charList = []
#         s_ex = ''
#         for i in s:
#             if i.isdigit():
#                 numList.append(int(i))
#                 charList.append(s_ex)
#             else:
#                 s_ex+=i
#         return numList,charList

#     def decodeAtIndex(self, s: str, k: int) -> str:
#         numList = self.getNums(s)
#         s_extention = ''
#         while sum(numList)!=0:

       

#         return ''

class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        length = 0  # Initialize a variable to keep track of the length of the decoded string.
        s0 = 0  # Initialize a variable to store the index where decoding begins.

        # Loop through the characters in the input string 's' using enumerate to get both index and character.
        for i, c in enumerate(s):
            if c.isalpha():  # If the character is an alphabet (letter):
                length += 1  # Increase the length of the decoded string by 1.
                if k == length:  # If the current length is equal to the target 'k':
                    return c  # Return the current character as it's the result.
            else:  # If the character is a digit (number):
                length *= int(c)  # Multiply the current length by the numeric value of the digit.
                print('length: ',length)

            if k <= length:  # If the target 'k' is less than or equal to the current length:
                s0 = i  # Store the current index as the starting point for the next loop.
                print('length break: ',length)
                print('s0 : ',s0)
                break

        # Loop backward from the starting point to the beginning of the string.
        for i in range(s0, -1, -1):
            c = s[i]
            k %= length  # Take the modulo of 'k' with the current length.
            if k == 0 and c.isalpha():  # If 'k' becomes 0 and the character is an alphabet:
                return c  # Return the current character as it's the result.
            if c.isdigit():  # If the character is a digit (number):
                length //= int(c)  # Divide the current length by the numeric value of the digit.
            else:  # If the character is not a digit (e.g., a special character):
                length -= 1  # Subtract 1 from the current length.

        return "X" 


if __name__== '__main__':
    s = 'Leet2Code3'
    k = 15
    ansObj = Solution()
    print(ansObj.decodeAtIndex(s, k))
