
# Problem Statement
#
# The keycaps on a keyboard have been switched around, and the user is now trying to remember what he was trying to type.
# Create a class CeyKaps containing the method decipher that takes a string typed, representing the visible message on the screen, and a tuple (string) switched, representing the keycap switches. The method should return the original intended message (what keys the user thought he was pressing).
# A keycap can be switched around more than once. For example, if someone switched around 'A' and 'S', then switched around 'S' and 'D', then 'D' would be where 'A' originally was, 'S' where 'D' was, and 'A' where 'S' was.
# The elements of switches will be formatted as (quotes added for clarity) "*:*", where the *'s represent the keycaps to be switched. The above example would be represented as: {"A:S","S:D","D:A"}, or alternately as {"S:A","D:S","A:D"} or any other such combination. The order of the keycaps doesn't matter, but the order of the switches does.
# Definition
#
# Class:
# CeyKaps
# Method:
# decipher
# Parameters:
# string, tuple (string)
# Returns:
# string
# Method signature:
# def decipher(self, typed, switches):

# Limits
#
# Time limit (s):
# 2.000
# Memory limit (MB):
# 64
# Notes
# -
# There is no restriction on how many times keycaps can be switched. It is perfectly possible to return to the original keyboard configuration.
# Constraints
# -
# typed will be between 1 and 50 characters in length, inclusive.
# -
# each character of typed will be an uppercase letter ('A'-'Z').
# -
# switches will contain between 1 and 50 elements, inclusive.
# -
# each element of switched will be formatted as (quotes added for clarity) "*:*" where each * represents a single uppercase letter ('A'-'Z'), inclusive, but both *'s do not represent the same letter.
# Examples
# 0)

#
# "AAAAA"
# {"A:B","B:C","A:D"}
# Returns: "CCCCC"
# At first, all keys look right. After the A:B switch, A looks like B and B looks like A. After the B:C switch, A looks like C, B looks like A, and C looks like B. The third switch is irrelevant. Since "AAAAA" is what comes out, Timmy must have been pressing "CCCCC".
# 1)

#
# "ABCDE"
# {"A:B","B:C","C:D","D:E","E:A"}
# Returns: "AEBCD"

# 2)

#
# "IHWSIOTCHEDMYKEYCAPSARWUND"
# {"W:O","W:I"}
# Returns: "WHOSWITCHEDMYKEYCAPSAROUND"

# This problem statement is the exclusive and proprietary property of TopCoder, Inc. Any unauthorized use or reproduction of this information without the prior written consent of TopCoder, Inc. is strictly prohibited. (c)2003, TopCoder, Inc. All rights reserved.

# 183 points, own solution without looking at editorial


class CeyKaps(object):

    def decipher(self, typed, switches):

        cipher_keyboard = [chr(num) for num in range(65, 91)]

        switches = [switch.split(":") for switch in switches]

        def find_letter_index(letter):
            return cipher_keyboard.index(letter)

        for switch in switches:
            letter1_index = find_letter_index(switch[0])
            letter2_index = find_letter_index(switch[1])
            cipher_keyboard[letter1_index], cipher_keyboard[letter2_index] = cipher_keyboard[letter2_index], cipher_keyboard[letter1_index]

        deciphered = []
        for letter in typed:
            deciphered.append(cipher_keyboard[ord(letter) - 65])

        return "".join(deciphered)


CeyKaps().decipher("ABCDE", ("A:B", "B:C", "C:D", "D:E", "E:A"))
CeyKaps().decipher("IHWSIOTCHEDMYKEYCAPSARWUND", ("W:O", "W:I"))
CeyKaps().decipher("AAAAA", ("A:B", "B:C", "A:D"))
