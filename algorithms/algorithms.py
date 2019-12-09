from typing import Union


def celsius_to_fahrenheit(c_temp: Union[str, float]) -> float:
    """
    For information on type annotations in Python, visit:
    https://docs.python.org/3/library/typing.html
    The algorithm to convert from Celsius to Fahrenheit is the temperature in Celsius times 9/5, plus 32.
    """
    return


def reverse_string():
    """
    Return the reverse of a passed string.
    """
    return


def factorialize():
    """
    Return a factorial of a passed integer.
    A factorial is the product of an integer and all the integers below it;
    e.g. factorial four (4!) is equal to 24. (Symbol: !)
    """
    return


def longest_word_in_string():
    """
    Locates and returns the longest word in a string using RegEx.
    If there are two words tied for longest, it should return the first.
    """
    return


def largest_number_in_arrays():
    """
    Given an array of arrays of numbers, return the largest.
    """
    return


def confirm_ending():
    """
    Check if a string (first argument, str) ends with the given target string (second argument, target).
    """
    return


def toddler():
    """
    Repeat a given string str (first argument) for num times (second argument).
    Return an empty string if num is not a positive number.
    """
    return


def truncate_string():
    """
    Truncate a string (first argument) if it is longer than the given maximum string length (second argument).
    Return the truncated string with a ... ending.
    """
    return


def finders_keepers():
    """
    Create a function that looks through an array (first argument) and returns the first element in the array
    that passes a truth test (second argument). If no element passes the test, return None.
    """
    return


def slice_n_splice():
    """
    You are given two arrays and an index. Copy each element of the first array into the second array, in order.
    Begin inserting elements at index n of the second array.
    Return the resulting array. The input arrays should remain the same after the function runs.
    """
    return


def getIndexToIns():
    """
    Return the lowest index at which a value (second argument)
    should be inserted into an array (first argument) once it has been sorted.  The returned value should be a number.
    For example, getIndexToIns([1,2,3,4], 1.5) should return 1 because it is greater than 1 (index 0),
    but less than 2 (index 1).
    Likewise, getIndexToIns([20,3,5], 19) should return 2 because once the array has been sorted
    it will look like [3,5,20] and 19 is less than 20 (index 2) and greater than 5 (index 1).
    """
    return


def mutations():
    """
    Return true if the string in the first element of the array contains all of the letters of the
    string in the second element of the array.
    For example, ["hello", "Hello"], should return true because all of the letters in the second string
    are present in the first, ignoring case.
    The arguments ["hello", "hey"] should return false because the string "hello" does not contain a "y".
    Lastly, ["Alien", "line"], should return true because all of the letters in "line" are present in "Alien".
    """
    return


def chunky_monkey():
    """
    Write a function that splits an array (first argument) into groups the length of size (second argument)
    and returns them as a two-dimensional array.
    """
    return


def sum_all_numbers():
    """
    We'll pass you an list of two numbers. Return the sum of those two numbers plus the sum of all the numbers
    between them. The lowest number will not always come first.
    """
    return


def diff_arrays():
    """
    Compare two arrays and return a new array with any items only found in one of the two given arrays, but not both.
    In other words, return the symmetric difference of the two arrays.
    """
    return


def seek_and_destroy():
    """
    You will be provided with an initial array (the first argument in the destroyer function),
    followed by one or more arguments. Remove all elements from the initial array that are of the
    same value as these arguments.
    """
    return


def wherefore_art_thou():
    """
    Make a function that looks through an array of objects (first argument) and returns an array of
    all objects that have matching name and value pairs (second argument).
    Each name and value pair of the source object has to be present in the object from the collection
    if it is to be included in the returned array.
    For example, if the first argument is
    [{ first: "Romeo", last: "Montague" }, { first: "Mercutio", last: null }, { first: "Tybalt", last: "Capulet" }],
    and the second argument is { last: "Capulet" },
    then you must return the third object from the array (the first argument),
    because it contains the name and its value, that was passed on as the second argument.
    """
    return


def spinal_tap_case():
    """
    Convert a string to spinal case. Spinal case is all-lowercase-words-joined-by-dashes.
    """
    return


def pig_latin():
    """
    Translate the provided string to pig latin.
    Pig Latin takes the first consonant (or consonant cluster) of an English word,
    moves it to the end of the word and suffixes an "ay".
    If a word begins with a vowel you just add "way" to the end.
    If a word does not contain a vowel, just add "ay" to the end.
    Input strings are guaranteed to be English words in all lowercase.
    """
    return


def myReplace():
    """
    Perform a search and replace on the sentence using the arguments provided and return the new sentence.
    First argument is the sentence to perform the search and replace on.
    Second argument is the word that you will be replacing (before).
    Third argument is what you will be replacing the second argument with (after).
    myReplace("Let's go to the store", "store", "mall") should return "Let us go to the mall".
    """
    return


def dna_pairing():
    """
    The DNA strand is missing the pairing element. Take each character, get its pair,
    and return the results as a 2d array.
    Base pairs are a pair of AT and CG. Match the missing element to the provided character.
    Return the provided character as the first element in each array.
    For example, for the input GCG, return [["G", "C"], ["C","G"],["G", "C"]]
    """
    return


def missing_letters():
    """
    Find the missing letter in the passed letter range and return it.
    """
    return


def uniteUnique():
    """
    uniteUnique([1, 3, 2], [5, 2, 1, 4], [2, 1]) should return [1, 3, 2, 5, 4].
    uniteUnique([1, 2, 3], [5, 2, 1]) should return [1, 2, 3, 5].
    uniteUnique([1, 2, 3], [5, 2, 1, 4], [2, 1], [6, 7, 8]) should return [1, 2, 3, 5, 4, 6, 7, 8].
    """
    return


def convertHTML():
    """
    convertHTML("Dolce & Gabbana") should return Dolce &amp; Gabbana.
    convertHTML("Hamburgers < Pizza < Tacos") should return Hamburgers &lt; Pizza &lt; Tacos.
    convertHTML("Sixty > twelve") should return Sixty &gt; twelve.
    convertHTML('Stuff in "quotation marks"') should return Stuff in &quot;quotation marks&quot;.
    convertHTML("Schindler's List") should return Schindler&apos;s List.
    convertHTML("<>") should return &lt;&gt;.
    convertHTML("abc") should return abc.
    """
    return


def sumFibs():
    """
    Given a positive integer num, return the sum of all odd Fibonacci numbers that are less than or equal to num.
    The first two numbers in the Fibonacci sequence are 1 and 1. Every additional number in the sequence is the
    sum of the two previous numbers. The first six numbers of the Fibonacci sequence are 1, 1, 2, 3, 5 and 8.
    For example, sumFibs(10) should return 10 because all odd Fibonacci numbers less than or equal to 10 are
    1, 1, 3, and 5.
    """
    return


def sum_all_primes():
    """
    Sum all the prime numbers up to and including the provided number.
    A prime number is defined as a number greater than one and having only two divisors, one and itself.
    For example, 2 is a prime number because it's only divisible by one and two.
    The provided number may not be a prime.
    """
    return


def smallest_common_multiple():
    """
    Find the smallest common multiple of the provided parameters that can be evenly divided by both,
    as well as by all sequential numbers in the range between these parameters.
    The range will be an array of two numbers that will not necessarily be in numerical order.
    For example, if given 1 and 3, find the smallest common multiple of both 1 and 3 that is also
    evenly divisible by all numbers between 1 and 3. The answer here would be 6.
    """
    return


def drop_it():
    """
    Given the array arr, iterate through and remove each element starting from the first element (the 0 index)
    until the function func returns true when the iterated element is passed through it.
    Then return the rest of the array once the condition is satisfied, otherwise,
    arr should be returned as an empty array.

    Example:
    drop_it([1, 2, 3, 4], lambda x: x >= 3) should return [3, 4]
    """
    return


def steamroller():
    """
    Flatten a nested array. You must account for varying levels of nesting.
    """
    return


def binary_translator():
    """
    Return an English translated sentence of the passed binary string.
    The binary string will be space separated.
    binary_translator("01000001 01110010 01100101 01101110 00100111 01110100 00100000 01100010 01101111 01101110 01100110 01101001 01110010 01100101 01110011 00100000 01100110 01110101 01101110 00100001 00111111") should return "Aren't bonfires fun!?"
    binary_translator("01001001 00100000 01101100 01101111 01110110 01100101 00100000 01000110 01110010 01100101 01100101 01000011 01101111 01100100 01100101 01000011 01100001 01101101 01110000 00100001") should return "I love FreeCodeCamp!"
    """
    return


def rot13():
    """
    One of the simplest and most widely known ciphers is a Caesar cipher, also known as a shift cipher.
    In a shift cipher the meanings of the letters are shifted by some set amount.
    A common modern use is the ROT13 cipher, where the values of the letters are shifted by 13 places.
    Thus 'A' ↔ 'N', 'B' ↔ 'O' and so on.
    Write a function which takes a ROT13 encoded string as input and returns a decoded string.
    All letters will be uppercase. Do not transform any non-alphabetic character (i.e. spaces, punctuation),
    but do pass them on.
    rot13("SERR PBQR PNZC") should decode to FREE CODE CAMP
    rot13("SERR CVMMN!") should decode to FREE PIZZA!
    rot13("SERR YBIR?") should decode to FREE LOVE?
    rot13("GUR DHVPX OEBJA SBK WHZCF BIRE GUR YNML QBT.") should decode to THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.
    """
    return


def palindrome():
    """"
    Return True if the given string is a palindrome. Otherwise, return False.
    You'll need to remove all non-alphanumeric characters (punctuation, spaces and symbols) and turn
    everything into the same case (lower or upper case) in order to check for palindromes.
    We'll pass strings with varying formats, such as "racecar", "RaceCar", and "race CAR" among others.
    We'll also pass strings with special symbols, such as "2A3*3a2", "2A3 3a2", and "2_A3*3#A2"
    """
    return
