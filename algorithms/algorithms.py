import html
import re
import string
from typing import Any, Callable, List, Optional, Union


def celsius_to_fahrenheit(c_temp: Union[str, int]) -> int:
    """
    The algorithm to convert from Celsius to Fahrenheit is the temperature in Celsius times 9/5, plus 32.
    """
    temp = float(c_temp)
    return (temp * (9 / 5)) + 32


def reverse_string(data: str) -> str:
    """
    Return the reverse of a passed string.
    """
    # reverse = []
    # i = len(data) - 1
    # while i >= 0:
    #     reverse.append(data[i])
    #     i -= 1
    return data[::-1]


def factorialize(number: int) -> int:
    """
    Return a factorial of a passed integer.
    A factorial is the product of an integer and all the integers below it;
    e.g. factorial four (4!) is equal to 24. (Symbol: !)
    """
    values = range(1, number + 1)
    x = 1
    for y in list(values):
        x *= y
    return x


def longest_word_in_string(data: str) -> str:
    """
    Locates and returns the longest word in a string using RegEx.
    If there are two words tied for longest, it will return the first.
    """
    longest = ""
    for word in data.split(" "):
        if len(word) > len(longest):
            longest = word
    return longest


def largest_number_in_arrays(arr: List[float]) -> float:
    """
    Given an array of arrays of numbers, return the largest.
    """
    result = []
    for x in arr:
        result.append(sorted(x, reverse=True)[0])
    return result


def confirm_ending(data: str, target: str) -> bool:
    """
    Check if a string (first argument, str) ends with the given target string (second argument, target).
    """
    return data.endswith(target)


def toddler(data: str, times: int) -> str:
    """
    Repeat a given string str (first argument) for num times (second argument).
    Return an empty string if num is not a positive number.
    """
    return data * times if times >= 0 else ""


def truncate_string(data: str, max_length: int) -> str:
    """
    Truncate a string (first argument) if it is longer than the given maximum string length (second argument).
    Return the truncated string with a ... ending.
    """
    return data if len(data) <= max_length else data[:max_length] + "..."


def finders_keepers(data: List[Any], test: Callable) -> Optional[Any]:
    """
    Create a function that looks through an array (first argument) and returns the first element in the array
    that passes a truth test (second argument). If no element passes the test, return None.
    """
    check = list(filter(test, data))
    return None if check == [] else check[0]


def slice_n_splice(arr1: List[Any], arr2: List[Any], pos: int) -> List[Any]:
    """
    You are given two arrays and an index. Copy each element of the first array into the second array, in order.
    Begin inserting elements at index n of the second array.
    Return the resulting array. The input arrays should remain the same after the function runs.
    """
    final = arr2.copy()
    for item in arr1:
        final.insert(pos, item)
        pos += 1
    return final


def getIndexToIns(array: list, value: float) -> int:
    """
    Return the lowest index at which a value (second argument)
    should be inserted into an array (first argument) once it has been sorted.  The returned value should be a number.
    For example, getIndexToIns([1,2,3,4], 1.5) should return 1 because it is greater than 1 (index 0),
    but less than 2 (index 1).
    Likewise, getIndexToIns([20,3,5], 19) should return 2 because once the array has been sorted
    it will look like [3,5,20] and 19 is less than 20 (index 2) and greater than 5 (index 1).
    """
    array.sort()
    if (array == []) or (value <= array[0]):
        return 0
    for x in array:
        try:
            if (value >= x) and (value <= array[array.index(x) + 1]):
                return array.index(x) + 1
        except IndexError:
            return len(array)


def mutations(array: List[str]) -> bool:
    """
    Return true if the string in the first element of the array contains all of the letters of the
    string in the second element of the array.
    For example, ["hello", "Hello"], should return true because all of the letters in the second string
    are present in the first, ignoring case.
    The arguments ["hello", "hey"] should return false because the string "hello" does not contain a "y".
    Lastly, ["Alien", "line"], should return true because all of the letters in "line" are present in "Alien".
    """
    check = []
    # Create the first array in lowercase
    for letter in list(array[0]):
        check.append(letter.lower())
    # Iterate through the letters of the second array, in lowercase
    for letter in list(array[1]):
        if letter.lower() not in check:
            return False
    return True


def chunky_monkey(array: list, size: int) -> List[list]:
    """
    Write a function that splits an array (first argument) into groups the length of size (second argument)
    and returns them as a two-dimensional array.
    """
    result = []
    temp = []
    i = 1
    while len(array) > 0:
        while len(temp) < size and len(array) > 0:
            try:
                temp.append(array.pop(0))
                i += 1
            except ValueError:
                break
        result.append(temp)
        temp = []
        i = 0
    return result


def sum_all_numbers(array: List[Union[str, int]]) -> int:
    """
    We'll pass you an list of two numbers. Return the sum of those two numbers plus the sum of all the numbers
    between them. The lowest number will not always come first.
    """
    # I'm being kind and allowing strings. You're welcome.
    data = []
    for x in array:
        data.append(int(x))
    # Let's make sure the lowest number comes first
    data.sort()
    # Put together a range object we can create a list from
    values = range(data[0], data[1] + 1)
    # Add all items in the list together
    x = 0
    for y in list(values):
        x += y
    return x


def diff_arrays(arr1: List[Any], arr2: List[Any]) -> List[Any]:
    """
    Compare two arrays and return a new array with any items only found in one of the two given arrays, but not both.
    In other words, return the symmetric difference of the two arrays.
    """
    final = []
    for item in arr1:
        if item not in arr2:
            final.append(item)
    for item in arr2:
        if item not in arr1:
            final.append(item)
    return final


def seek_and_destroy(arr: list, *args) -> list:
    """
    You will be provided with an initial array (the first argument in the destroyer function),
    followed by one or more arguments. Remove all elements from the initial array that are of the
    same value as these arguments.
    """
    for item in args:
        while item in arr:
            arr.pop(arr.index(item))
    return arr


def wherefore_art_thou(objects: List[dict], seeker: dict) -> Optional[dict]:
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
    result = []
    for item in objects:
        truthy = []
        for k, v in seeker.items():
            if k in item and item[k] == v:
                truthy.append(True)
            else:
                truthy.append(False)
        if False not in truthy:
            result.append(item)
    return result if len(result) > 0 else None


def spinal_tap_case(data: str) -> str:
    """
    Convert a string to spinal case. Spinal case is all-lowercase-words-joined-by-dashes.
    """
    # Add a space before capital letters to account for camelCase
    # Sorry, no Scotsmen allowed...
    test = re.sub(r"(?<![A-Z])(?<!^)([A-Z])", r" \1", data)
    # Check for word boundaries
    words = re.findall(r"\b\w+", test)
    if words == []:
        words = re.findall(r"[a-zA-Z][^A-Z]*", data)
    # Underscores don't count, so deal with them
    if "_" in data:
        return "-".join(word.lower() for word in data.split("_"))
    return "-".join(word.lower() for word in words)


def pig_latin(phrase: str) -> str:
    """
    Translate the provided string to pig latin.
    Pig Latin takes the first consonant (or consonant cluster) of an English word,
    moves it to the end of the word and suffixes an "ay".
    If a word begins with a vowel you just add "way" to the end.
    If a word does not contain a vowel, just add "ay" to the end.
    Input strings are guaranteed to be English words in all lowercase.
    """
    vowels = ("a", "e", "i", "o", "u")
    result = []
    append = ["-", "a", "y"]
    array = list(phrase)

    vowels = list(filter(lambda x: x in vowels, array))
    if len(vowels) == 0:
        return "".join(array) + "-ay"
    if array[0] in vowels:
        return "".join(array) + "-way"

    i = 1
    for letter in array:
        if letter in vowels:
            break
        append.insert(i, letter)
        i += 1
    result = array[i - 1:]
    for suffix in append:
        result.append(suffix)
    return "".join(result)


def myReplace(phrase: str, original: str, new: str) -> str:
    """
    Perform a search and replace on the sentence using the arguments provided and return the new sentence.
    First argument is the sentence to perform the search and replace on.
    Second argument is the word that you will be replacing (before).
    Third argument is what you will be replacing the second argument with (after).
    myReplace("Let's go to the store", "store", "mall") should return "Let us go to the mall".
    """
    return phrase.replace(original, new)


def dna_pairing(original: str) -> list:
    """
    The DNA strand is missing the pairing element. Take each character, get its pair,
    and return the results as a 2d array.
    Base pairs are a pair of AT and CG. Match the missing element to the provided character.
    Return the provided character as the first element in each array.
    For example, for the input GCG, return [["G", "C"], ["C","G"],["G", "C"]]
    """
    base_pairs = {"A": "T", "C": "G", "T": "A", "G": "C"}
    result = []
    for letter in list(original):
        result.append([letter, base_pairs[letter]])
    return result


def missing_letters(letter_range: str) -> Optional[str]:
    """
    Find the missing letter in the passed letter range and return it.
    """
    map = []
    for letter in list(letter_range):
        map.append(ord(letter))
    for num in map:
        if map.index(num) != 0:
            try:
                map.index(num - 1)
            except ValueError:
                return chr(num - 1)
    return None


def uniteUnique(*args) -> list:
    """
    uniteUnique([1, 3, 2], [5, 2, 1, 4], [2, 1]) should return [1, 3, 2, 5, 4].
    uniteUnique([1, 2, 3], [5, 2, 1]) should return [1, 2, 3, 5].
    uniteUnique([1, 2, 3], [5, 2, 1, 4], [2, 1], [6, 7, 8]) should return [1, 2, 3, 5, 4, 6, 7, 8].
    """
    result = []
    for arg in args:
        for num in arg:
            if num not in result:
                result.append(num)
    return result


def convertHTML(text: str) -> str:
    """
    convertHTML("Dolce & Gabbana") should return Dolce &amp; Gabbana.
    convertHTML("Hamburgers < Pizza < Tacos") should return Hamburgers &lt; Pizza &lt; Tacos.
    convertHTML("Sixty > twelve") should return Sixty &gt; twelve.
    convertHTML('Stuff in "quotation marks"') should return Stuff in &quot;quotation marks&quot;.
    convertHTML("Schindler's List") should return Schindler&apos;s List.
    convertHTML("<>") should return &lt;&gt;.
    convertHTML("abc") should return abc.
    """
    return html.escape(text)


def sumFibs(num: int) -> int:
    """
    Given a positive integer num, return the sum of all odd Fibonacci numbers that are less than or equal to num.
    The first two numbers in the Fibonacci sequence are 1 and 1. Every additional number in the sequence is the
    sum of the two previous numbers. The first six numbers of the Fibonacci sequence are 1, 1, 2, 3, 5 and 8.
    For example, sumFibs(10) should return 10 because all odd Fibonacci numbers less than or equal to 10 are
    1, 1, 3, and 5.
    """
    # Generate Fibonacci sequence until the last number is greater than the passed num
    fibonacci = [1, 1, 2]
    while fibonacci[-1] < num:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    # Start adding
    result = 0
    for x in fibonacci:
        if x <= num and x % 2 != 0:
            result += x
    return result


def eratosthenes(num: int) -> List[int]:
    """Generate a list of prime numbers up to num."""
    # TODO: Why isn't this including the num?
    result = []
    prime = [True for i in range(num + 1)]
    p = 2
    while (p * p <= num):
        if prime[p]:
            for i in range(p * p, num + 1, p):
                prime[i] = False
        p += 1
    for p in range(2, num):
        if prime[p]:
            result.append(p)
    return result


# print(eratosthenes(977))


def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3, int(n**0.5) + 1, 2):
        if sieve[i]:
            sieve[i * i::2 * i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]


# print(primes(977))


def sum_all_primes(num: int) -> int:
    """
    Sum all the prime numbers up to and including the provided number.
    A prime number is defined as a number greater than one and having only two divisors, one and itself.
    For example, 2 is a prime number because it's only divisible by one and two.
    The provided number may not be a prime.
    """

    # Generate a list of primes up to and including the provided number
    # primes = [2]
    # i = 1
    # while i < num:
    #     if 2**(i - 1) % i == 1:
    #         primes.append(i)
    #     i += 1
    prime_nums = primes(num)
    # Starting summin'
    sum = 0
    for number in prime_nums:
        if number <= num:
            sum += number
    return sum


# print(sum_all_primes(977))


def smallest_common_multiple(arr: List[int]) -> int:
    """
    Find the smallest common multiple of the provided parameters that can be evenly divided by both,
    as well as by all sequential numbers in the range between these parameters.
    The range will be an array of two numbers that will not necessarily be in numerical order.
    For example, if given 1 and 3, find the smallest common multiple of both 1 and 3 that is also
    evenly divisible by all numbers between 1 and 3. The answer here would be 6.
    """
    arr.sort()
    i = 1
    answer = []
    while True:
        answer.clear()
        multiple = arr[0] * arr[1] * i
        for number in list(range(arr[0], arr[1] + 1)):
            if multiple % number != 0:
                answer.append(False)
        i += 1
        if False not in answer:
            return multiple


def drop_it(arr: list, func: Callable) -> list:
    """
    Given the array arr, iterate through and remove each element starting from the first element (the 0 index)
    until the function func returns true when the iterated element is passed through it.
    Then return the rest of the array once the condition is satisfied, otherwise,
    arr should be returned as an empty array.

    Example:
    drop_it([1, 2, 3, 4], lambda x: x >= 3) should return [3, 4]
    """
    f = filter(func, arr)
    return list(f)


def steamroller(arr: List[Any]) -> list:
    """
    Flatten a nested array. You must account for varying levels of nesting.
    """
    return sum(
        ([x] if not isinstance(x, list) else steamroller(x) for x in arr), [])


def binary_translator(binary: str) -> str:
    """
    Return an English translated sentence of the passed binary string.
    The binary string will be space separated.
    binary_translator("01000001 01110010 01100101 01101110 00100111 01110100 00100000 01100010 01101111 01101110 01100110 01101001 01110010 01100101 01110011 00100000 01100110 01110101 01101110 00100001 00111111") should return "Aren't bonfires fun!?"
    binary_translator("01001001 00100000 01101100 01101111 01110110 01100101 00100000 01000110 01110010 01100101 01100101 01000011 01101111 01100100 01100101 01000011 01100001 01101101 01110000 00100001") should return "I love FreeCodeCamp!"
    """
    result = []
    for letter in binary.split():
        result.append(chr(int(letter, 2)))
    return "".join(result)


def rot13(phrase: str) -> str:
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
    # Available, but shouldn't be used necessarily:
    # import codecs
    # codecs.encode(phrase, 'rot_13')
    # Uppercase letters A-Z are 65-90
    result = []
    arr = list(phrase)
    for letter in arr:
        if letter not in string.ascii_uppercase:
            result.append(letter)
        if letter in string.ascii_uppercase:
            new_value = ord(letter) + 13
            if new_value > 90:
                new_value -= 26
            result.append(chr(new_value))
    return "".join(result)


def palindrome(word: str) -> bool:
    """"
    Return True if the given string is a palindrome. Otherwise, return False.
    You'll need to remove all non-alphanumeric characters (punctuation, spaces and symbols) and turn
    everything into the same case (lower or upper case) in order to check for palindromes.
    We'll pass strings with varying formats, such as "racecar", "RaceCar", and "race CAR" among others.
    We'll also pass strings with special symbols, such as "2A3*3a2", "2A3 3a2", and "2_A3*3#A2"
    """
    check = list("".join(x for x in word.lower() if x.isalnum()))
    reverse = check.copy()
    reverse.reverse()
    if check == reverse:
        return True
    return False
