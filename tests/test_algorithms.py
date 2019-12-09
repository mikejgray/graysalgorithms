import pytest

from algorithms import algorithms


@pytest.mark.parametrize(("input", "expected"), [
    (-30, -22),
    (-10, 14),
    (0, 32),
    (20, 68),
    (30, 86)
])
class TestCelsius:
    def test1(self, input, expected):
        assert type(algorithms.celsius_to_fahrenheit(input)) == float

    def test2(self, input, expected):
        assert algorithms.celsius_to_fahrenheit(input) == expected


class TestReverseString:
    def tests(self):
        assert type(algorithms.reverse_string("hello")) == str
        assert algorithms.reverse_string("hello") == "olleh"
        assert algorithms.reverse_string("Howdy") == "ydwoH"
        assert (
            algorithms.reverse_string("Greetings from Earth") == "htraE morf sgniteerG"
        )


class TestFactorialize:
    def tests(self):
        assert type(algorithms.factorialize(5)) == int
        assert algorithms.factorialize(5) == 120
        assert algorithms.factorialize(10) == 3628800
        assert algorithms.factorialize(20) == 2432902008176640000
        assert algorithms.factorialize(0) == 1


class TestLongestWord:
    def tests(self):
        assert type(
            algorithms.longest_word_in_string(
                "The quick brown fox jumped over the lazy dog"
            )
        ) == str
        assert len(
            algorithms.longest_word_in_string(
                "The quick brown fox jumped over the lazy dog"
            )
        ) == 6
        assert algorithms.longest_word_in_string("May the force be with you") == "force"
        assert algorithms.longest_word_in_string("Google do a barrel roll") == "Google"
        assert (
            algorithms.longest_word_in_string(
                "What is the average airspeed velocity of an unladen swallow"
            )
            == "airspeed"
        )
        assert (
            algorithms.longest_word_in_string(
                "What if we try a super-long word such as otorhinolaryngology"
            )
            == "otorhinolaryngology"
        )


class TestLargestNumber:
    def tests(self):
        assert (
            type(
                algorithms.largest_number_in_arrays(
                    [
                        [4, 5, 1, 3],
                        [13, 27, 18, 26],
                        [32, 35, 37, 39],
                        [1000, 1001, 857, 1],
                    ]
                )
            )
            == list
        )
        assert algorithms.largest_number_in_arrays(
            [[13, 27, 18, 26], [4, 5, 1, 3], [32, 35, 37, 39], [1000, 1001, 857, 1]]
        ) == [27, 5, 39, 1001]
        assert algorithms.largest_number_in_arrays(
            [[4, 9, 1, 3], [13, 35, 18, 26], [32, 35, 97, 39], [1000000, 1001, 857, 1]]
        ) == [9, 35, 97, 1000000]
        assert algorithms.largest_number_in_arrays(
            [[17, 23, 25, 12], [25, 7, 34, 48], [4, -10, 18, 21], [-72, -3, -17, -10]]
        ) == [25, 48, 21, -3]


class TestConfirmEnding:
    def tests(self):
        assert algorithms.confirm_ending("Bastian", "n")
        assert algorithms.confirm_ending("Congratulation", "on")
        assert not algorithms.confirm_ending("Connor", "n")
        assert not algorithms.confirm_ending(
            "Walking on water and developing software from a specification are easy if both are frozen",
            "specification",
        )
        assert algorithms.confirm_ending("He has to give me a new name", "name")
        assert algorithms.confirm_ending("Open sesame", "same")
        assert not algorithms.confirm_ending("Open sesame", "pen")
        assert not algorithms.confirm_ending("Open sesame", "game")
        assert not algorithms.confirm_ending(
            "If you want to save our world, you must hurry. We dont know how much longer we can withstand the nothing",
            "mountain",
        )
        assert algorithms.confirm_ending("Abstraction", "action")
        # TODO: Your code should not use the built-in method .endswith() to solve the challenge


class TestToddler:
    def tests(self):
        assert algorithms.toddler("*", 3) == "***"
        assert algorithms.toddler("abc", 3) == "abcabcabc"
        assert algorithms.toddler("abc", 4) == "abcabcabcabc"
        assert algorithms.toddler("abc", 1) == "abc"
        assert algorithms.toddler("*", 8) == "********"
        assert algorithms.toddler("abc", 0) == ""


class TestTruncate:
    def tests(self):
        assert (
            algorithms.truncate_string("A-tisket a-tasket A green and yellow basket", 8)
            == "A-tisket..."
        )
        assert (
            algorithms.truncate_string(
                "Peter Piper picked a peck of pickled peppers", 11
            )
            == "Peter Piper..."
        )
        assert (
            algorithms.truncate_string(
                "A-tisket a-tasket A green and yellow basket",
                len("A-tisket a-tasket A green and yellow basket"),
            )
            == "A-tisket a-tasket A green and yellow basket"
        )
        assert (
            algorithms.truncate_string(
                "A-tisket a-tasket A green and yellow basket",
                len("A-tisket a-tasket A green and yellow basket") + 2,
            )
            == "A-tisket a-tasket A green and yellow basket"
        )
        assert algorithms.truncate_string("A-", 1) == "A..."
        assert algorithms.truncate_string("Absolutely Longer", 2) == "Ab..."


class TestFinders:
    def tests(self):
        assert (
            algorithms.finders_keepers([1, 3, 5, 8, 9, 10], lambda num: num % 2 == 0)
            == 8
        )
        assert not algorithms.finders_keepers([1, 3, 5, 9], lambda num: num % 2 == 0)


class TestSliceAndSplice:
    def tests(self):
        assert algorithms.slice_n_splice([1, 2, 3], [4, 5], 1) == [4, 1, 2, 3, 5]
        assert algorithms.slice_n_splice([1, 2], ["a", "b"], 1) == ["a", 1, 2, "b"]
        assert algorithms.slice_n_splice(
            ["claw", "tentacle"], ["head", "shoulders", "knees", "toes"], 2
        ) == ["head", "shoulders", "claw", "tentacle", "knees", "toes"]
        # TODO: Verify that the original arguments were not mutated


class TestGetIndexToIns:
    def tests(self):
        assert algorithms.getIndexToIns([10, 20, 30, 40, 50], 35) == 3
        assert type(algorithms.getIndexToIns([10, 20, 30, 40, 50], 35)) in (float, int)
        assert algorithms.getIndexToIns([10, 20, 30, 40, 50], 30) == 2
        assert type(algorithms.getIndexToIns([10, 20, 30, 40, 50], 30)) in (float, int)
        assert algorithms.getIndexToIns([40, 60], 50) == 1
        assert type(algorithms.getIndexToIns([40, 60], 50)) in (float, int)
        assert algorithms.getIndexToIns([3, 10, 5], 3) == 0
        assert type(algorithms.getIndexToIns([3, 10, 5], 3)) in (float, int)
        assert algorithms.getIndexToIns([5, 3, 20, 3], 5) == 3
        assert type(algorithms.getIndexToIns([5, 3, 20, 3], 5)) in (float, int)
        assert algorithms.getIndexToIns([2, 20, 10], 19) == 2
        assert type(algorithms.getIndexToIns([2, 20, 10], 19)) in (float, int)
        assert algorithms.getIndexToIns([2, 5, 10], 15) == 3
        assert type(algorithms.getIndexToIns([2, 5, 10], 15)) in (float, int)
        assert algorithms.getIndexToIns([], 1) == 0
        assert type(algorithms.getIndexToIns([], 1)) in (float, int)


class TestMutations:
    def tests(self):
        assert not algorithms.mutations(["hello", "hey"])
        assert algorithms.mutations(["hello", "Hello"])
        assert algorithms.mutations(["zyxwvutsrqponmlkjihgfedcba", "qrstu"])
        assert algorithms.mutations(["Mary", "Army"])
        assert algorithms.mutations(["Mary", "Aarmy"])
        assert algorithms.mutations(["Alien", "line"])
        assert algorithms.mutations(["floor", "for"])
        assert not algorithms.mutations(["hello", "neo"])
        assert not algorithms.mutations(["voodoo", "no"])
        assert not algorithms.mutations(["ate", "date"])
        assert not algorithms.mutations(["Tiger", "Zebra"])
        assert algorithms.mutations(["Noel", "Ole"])


class TestChunkyMonkey:
    def tests(self):
        assert algorithms.chunky_monkey(["a", "b", "c", "d"], 2) == [
            ["a", "b"],
            ["c", "d"],
        ]
        assert algorithms.chunky_monkey([0, 1, 2, 3, 4, 5], 3) == [[0, 1, 2], [3, 4, 5]]
        assert algorithms.chunky_monkey([0, 1, 2, 3, 4, 5], 2) == [
            [0, 1],
            [2, 3],
            [4, 5],
        ]
        assert algorithms.chunky_monkey([0, 1, 2, 3, 4, 5], 4) == [[0, 1, 2, 3], [4, 5]]
        assert algorithms.chunky_monkey([0, 1, 2, 3, 4, 5, 6], 3) == [
            [0, 1, 2],
            [3, 4, 5],
            [6],
        ]
        assert algorithms.chunky_monkey([0, 1, 2, 3, 4, 5, 6, 7, 8], 4) == [
            [0, 1, 2, 3],
            [4, 5, 6, 7],
            [8],
        ]
        assert algorithms.chunky_monkey([0, 1, 2, 3, 4, 5, 6, 7, 8], 2) == [
            [0, 1],
            [2, 3],
            [4, 5],
            [6, 7],
            [8],
        ]


class TestSumAllNumbers:
    def tests(self):
        assert type(algorithms.sum_all_numbers([1, 4])) in (int, float)
        assert algorithms.sum_all_numbers([1, 4]) == 10
        assert algorithms.sum_all_numbers([4, 1]) == 10
        assert algorithms.sum_all_numbers([5, 10]) == 45
        assert algorithms.sum_all_numbers([10, 5]) == 45


class TestDiffArrays:
    def tests(self):
        assert type(algorithms.diff_arrays([1, 2, 3, 5], [1, 2, 3, 4, 5])) == list
        assert algorithms.diff_arrays(
            ["diorite", "andesite", "grass", "dirt", "pink wool", "dead shrub"],
            ["diorite", "andesite", "grass", "dirt", "dead shrub"],
        ) == ["pink wool"]
        assert (
            type(
                algorithms.diff_arrays(
                    ["diorite", "andesite", "grass", "dirt", "pink wool", "dead shrub"],
                    ["diorite", "andesite", "grass", "dirt", "dead shrub"],
                )
            )
            == list
        )
        assert (
            len(
                algorithms.diff_arrays(
                    ["diorite", "andesite", "grass", "dirt", "pink wool", "dead shrub"],
                    ["diorite", "andesite", "grass", "dirt", "dead shrub"],
                )
            )
            == 1
        )
        assert algorithms.diff_arrays(
            ["andesite", "grass", "dirt", "pink wool", "dead shrub"],
            ["diorite", "andesite", "grass", "dirt", "dead shrub"],
        ) == ["pink wool", "diorite"]
        assert (
            type(
                algorithms.diff_arrays(
                    ["andesite", "grass", "dirt", "pink wool", "dead shrub"],
                    ["diorite", "andesite", "grass", "dirt", "dead shrub"],
                )
            )
            == list
        )
        assert (
            len(
                algorithms.diff_arrays(
                    ["andesite", "grass", "dirt", "pink wool", "dead shrub"],
                    ["diorite", "andesite", "grass", "dirt", "dead shrub"],
                )
            )
            == 2
        )
        assert (
            algorithms.diff_arrays(
                ["andesite", "grass", "dirt", "dead shrub"],
                ["andesite", "grass", "dirt", "dead shrub"],
            )
            == []
        )
        assert (
            algorithms.diff_arrays(
                ["andesite", "grass", "dirt", "dead shrub"],
                ["andesite", "grass", "dirt", "dead shrub"],
            )
            == []
        )
        assert algorithms.diff_arrays([1, 2, 3, 5], [1, 2, 3, 4, 5]) == [4]
        assert type(algorithms.diff_arrays([1, 2, 3, 5], [1, 2, 3, 4, 5])) == list
        assert len(algorithms.diff_arrays([1, 2, 3, 5], [1, 2, 3, 4, 5])) == 1
        assert algorithms.diff_arrays([1, "calf", 3, "piglet"], [1, "calf", 3, 4]) == [
            "piglet",
            4,
        ]
        assert (
            type(algorithms.diff_arrays([1, "calf", 3, "piglet"], [1, "calf", 3, 4]))
            == list
        )
        assert (
            len(algorithms.diff_arrays([1, "calf", 3, "piglet"], [1, "calf", 3, 4]))
            == 2
        )
        assert algorithms.diff_arrays(
            [], ["snuffleupagus", "cookie monster", "elmo"]
        ) == ["snuffleupagus", "cookie monster", "elmo"]
        assert (
            type(
                algorithms.diff_arrays([], ["snuffleupagus", "cookie monster", "elmo"])
            )
            == list
        )
        assert (
            len(algorithms.diff_arrays([], ["snuffleupagus", "cookie monster", "elmo"]))
            == 3
        )
        assert algorithms.diff_arrays([1, "calf", 3, "piglet"], [7, "filly"]) == [
            1,
            "calf",
            3,
            "piglet",
            7,
            "filly",
        ]
        assert (
            type(algorithms.diff_arrays([1, "calf", 3, "piglet"], [7, "filly"])) == list
        )
        assert len(algorithms.diff_arrays([1, "calf", 3, "piglet"], [7, "filly"])) == 6


class TestSeekAndDestroy:
    def tests(self):
        assert algorithms.seek_and_destroy([1, 2, 3, 1, 2, 3], 2, 3) == [1, 1]
        assert algorithms.seek_and_destroy([1, 2, 3, 5, 1, 2, 3], 2, 3) == [1, 5, 1]
        assert algorithms.seek_and_destroy([3, 5, 1, 2, 2], 2, 3, 5) == [1]
        assert algorithms.seek_and_destroy([2, 3, 2, 3], 2, 3) == []
        assert algorithms.seek_and_destroy(["tree", "hamburger", 53], "tree", 53) == [
            "hamburger"
        ]
        assert algorithms.seek_and_destroy(
            [
                "possum",
                "trollo",
                12,
                "safari",
                "hotdog",
                92,
                65,
                "grandma",
                "bugati",
                "trojan",
                "yacht",
            ],
            "yacht",
            "possum",
            "trollo",
            "safari",
            "hotdog",
            "grandma",
            "bugati",
            "trojan",
        ) == [12, 92, 65]


class TestWhereforeArtThou:
    def tests(self):
        assert algorithms.wherefore_art_thou(
            [
                {"first": "Romeo", "last": "Montague"},
                {"first": "Mercutio", "last": None},
                {"first": "Tybalt", "last": "Capulet"},
            ],
            {"last": "Capulet"},
        ) == [{"first": "Tybalt", "last": "Capulet"}]
        assert algorithms.wherefore_art_thou(
            [{"apple": 1}, {"apple": 1}, {"apple": 1, "bat": 2}], {"apple": 1}
        ) == [{"apple": 1}, {"apple": 1}, {"apple": 1, "bat": 2}]
        assert algorithms.wherefore_art_thou(
            [{"apple": 1, "bat": 2}, {"bat": 2}, {"apple": 1, "bat": 2, "cookie": 2}],
            {"apple": 1, "bat": 2},
        ) == [{"apple": 1, "bat": 2}, {"apple": 1, "bat": 2, "cookie": 2}]
        assert algorithms.wherefore_art_thou(
            [{"apple": 1, "bat": 2}, {"apple": 1}, {"apple": 1, "bat": 2, "cookie": 2}],
            {"apple": 1, "cookie": 2},
        ) == [{"apple": 1, "bat": 2, "cookie": 2}]
        assert algorithms.wherefore_art_thou(
            [
                {"apple": 1, "bat": 2},
                {"apple": 1},
                {"apple": 1, "bat": 2, "cookie": 2},
                {"bat": 2},
            ],
            {"apple": 1, "bat": 2},
        ) == [{"apple": 1, "bat": 2}, {"apple": 1, "bat": 2, "cookie": 2}]
        assert not (
            algorithms.wherefore_art_thou(
                [{"a": 1, "b": 2, "c": 3}], {"a": 1, "b": 9999, "c": 3}
            )
        )


class TestSpinalTapCase:
    def tests(self):
        assert algorithms.spinal_tap_case("This Is Spinal Tap") == "this-is-spinal-tap"
        assert algorithms.spinal_tap_case("thisIsSpinalTap") == "this-is-spinal-tap"
        assert (
            algorithms.spinal_tap_case("The_Andy_Griffith_Show")
            == "the-andy-griffith-show"
        )
        assert (
            algorithms.spinal_tap_case("Teletubbies say Eh-oh")
            == "teletubbies-say-eh-oh"
        )
        assert (
            algorithms.spinal_tap_case("AllThe-small Things") == "all-the-small-things"
        )


class TestPigLatin:
    def tests(self):
        assert algorithms.pig_latin("california") == "alifornia-cay"
        assert algorithms.pig_latin("paragraphs") == "aragraphs-pay"
        assert algorithms.pig_latin("glove") == "ove-glay"
        assert algorithms.pig_latin("algorithm") == "algorithm-way"
        assert algorithms.pig_latin("eight") == "eight-way"
        # Should handle words where the first vowel comes in the middle of the word.
        assert algorithms.pig_latin("schwartz") == "artz-schway"
        # Should handle words without vowels.
        assert algorithms.pig_latin("rhythm") == "rhythm-ay"


class TestMyReplace:
    def tests(self):
        assert (
            algorithms.myReplace("Let us go to the store", "store", "mall")
            == "Let us go to the mall"
        )
        assert (
            algorithms.myReplace("He is Sleeping on the couch", "Sleeping", "sitting")
            == "He is sitting on the couch"
        )
        assert (
            algorithms.myReplace("This has a spellngi error", "spellngi", "spelling")
            == "This has a spelling error"
        )
        assert (
            algorithms.myReplace("His name is Tom", "Tom", "John") == "His name is John"
        )
        assert (
            algorithms.myReplace(
                "Let us get back to more Coding", "Coding", "Algorithms"
            )
            == "Let us get back to more Algorithms"
        )


class TestDNAPairs:
    def tests(self):
        assert algorithms.dna_pairing("ATCGA") == [
            ["A", "T"],
            ["T", "A"],
            ["C", "G"],
            ["G", "C"],
            ["A", "T"],
        ]
        assert algorithms.dna_pairing("TTGAG") == [
            ["T", "A"],
            ["T", "A"],
            ["G", "C"],
            ["A", "T"],
            ["G", "C"],
        ]
        assert algorithms.dna_pairing("CTCTA") == [
            ["C", "G"],
            ["T", "A"],
            ["C", "G"],
            ["T", "A"],
            ["A", "T"],
        ]


class TestMissingLetters:
    def tests(self):
        assert algorithms.missing_letters("abce") == "d"
        assert algorithms.missing_letters("abcdefghjklmno") == "i"
        assert algorithms.missing_letters("stvwx") == "u"
        assert algorithms.missing_letters("bcdf") == "e"
        assert not algorithms.missing_letters("abcdefghijklmnopqrstuvwxyz")


class TestUniteUnique:
    def tests(self):
        assert algorithms.uniteUnique([1, 3, 2], [5, 2, 1, 4], [2, 1]) == [
            1,
            3,
            2,
            5,
            4,
        ]
        assert algorithms.uniteUnique([1, 2, 3], [5, 2, 1]) == [1, 2, 3, 5]
        assert algorithms.uniteUnique([1, 2, 3], [5, 2, 1, 4], [2, 1], [6, 7, 8]) == [
            1,
            2,
            3,
            5,
            4,
            6,
            7,
            8,
        ]


class TestConvertHTML:
    def tests(self):
        assert algorithms.convertHTML("Dolce & Gabbana") == "Dolce &amp; Gabbana"
        assert (
            algorithms.convertHTML("Hamburgers < Pizza < Tacos")
            == "Hamburgers &lt; Pizza &lt; Tacos"
        )
        assert algorithms.convertHTML("Sixty > twelve") == "Sixty &gt; twelve"
        assert (
            algorithms.convertHTML('Stuff in "quotation marks"')
            == "Stuff in &quot;quotation marks&quot;"
        )
        assert algorithms.convertHTML("Schindler's List") == "Schindler&#x27;s List"
        assert algorithms.convertHTML("<>") == "&lt;&gt;"
        assert algorithms.convertHTML("abc") == "abc"


class TestFibonacci:
    def tests(self):
        assert type(algorithms.sumFibs(1)) in (float, int)
        assert algorithms.sumFibs(1000) == 1785
        assert algorithms.sumFibs(4000000) == 4613732
        assert algorithms.sumFibs(4) == 5
        assert algorithms.sumFibs(75024) == 60696
        assert algorithms.sumFibs(75025) == 135721


class TestSumAllPrimes:
    def tests(self):
        assert type(algorithms.sum_all_primes(10)) in (float, int)
        assert algorithms.sum_all_primes(10) == 17
        assert algorithms.sum_all_primes(977) == 73156


class TestSCM:
    def tests(self):
        assert type(algorithms.smallest_common_multiple([1, 5])) in (float, int)
        assert algorithms.smallest_common_multiple([1, 5]) == 60
        assert algorithms.smallest_common_multiple([5, 1]) == 60
        assert algorithms.smallest_common_multiple([2, 10]) == 2520
        assert algorithms.smallest_common_multiple([1, 13]) == 360360
        assert algorithms.smallest_common_multiple([23, 18]) == 6056820


class TestDropIt:
    def tests(self):
        assert algorithms.drop_it([1, 2, 3, 4], lambda n: n >= 3) == [3, 4]
        assert algorithms.drop_it([0, 1, 0, 1], lambda n: n == 1) == [1, 1]
        assert algorithms.drop_it([1, 2, 3], lambda n: n > 0) == [1, 2, 3]
        assert algorithms.drop_it([1, 2, 3, 4], lambda n: n > 5) == []
        assert algorithms.drop_it([1, 2, 3, 7, 4], lambda n: n > 3) == [7, 4]
        assert algorithms.drop_it([1, 2, 3, 9, 2], lambda n: n >= 2) == [2, 3, 9, 2]


class TestSteamroller:
    def tests(self):
        assert algorithms.steamroller([[["a"]], [["b"]]]) == ["a", "b"]
        assert algorithms.steamroller([1, [2], [3, [[4]]]]) == [1, 2, 3, 4]
        assert algorithms.steamroller([1, [], [3, [[4]]]]) == [1, 3, 4]
        assert algorithms.steamroller([1, {}, [3, [[4]]]]) == [1, {}, 3, 4]


class TestBinaryTranslator:
    def tests(self):
        assert (
            algorithms.binary_translator(
                "01000001 01110010 01100101 01101110 00100111 01110100 00100000 01100010 01101111 01101110 01100110 01101001 01110010 01100101 01110011 00100000 01100110 01110101 01101110 00100001 00111111"
            )
            == "Aren't bonfires fun!?"
        )
        assert (
            algorithms.binary_translator(
                "01001001 00100000 01101100 01101111 01110110 01100101 00100000 01000110 01110010 01100101 01100101 01000011 01101111 01100100 01100101 01000011 01100001 01101101 01110000 00100001"
            )
            == "I love FreeCodeCamp!"
        )


class TestCaesar:
    def tests(self):
        assert algorithms.rot13("SERR PBQR PNZC") == "FREE CODE CAMP"
        assert algorithms.rot13("SERR CVMMN!") == "FREE PIZZA!"
        assert algorithms.rot13("SERR YBIR?") == "FREE LOVE?"
        assert (
            algorithms.rot13("GUR DHVPX OEBJA SBK WHZCF BIRE GUR YNML QBT.")
            == "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG."
        )


class TestPalindrome:
    def tests(self):
        assert type(algorithms.palindrome("eye")) == bool
        assert algorithms.palindrome("eye")
        assert algorithms.palindrome("_eye")
        assert algorithms.palindrome("race car")
        assert not algorithms.palindrome("not a palindrome")
        assert algorithms.palindrome("A man, a plan, a canal. Panama")
        assert algorithms.palindrome("never odd or even")
        assert not algorithms.palindrome("nope")
        assert not algorithms.palindrome("almostomla")
        assert algorithms.palindrome("My age is 0, 0 si ega ym.")
        assert not algorithms.palindrome("1 eye for of 1 eye.")
        assert algorithms.palindrome("0_0 (: - :) 0-0")
        assert not algorithms.palindrome("five|_|four")
