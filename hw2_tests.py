import data
import hw2
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_create_rectangle_1(self):
        input1 = data.Point(0, 0)
        input2 = data.Point(2, 4)
        result = hw2.create_rectangle(input1, input2)
        expected = data.Rectangle(data.Point(0, 4), data.Point(2, 0))
        self.assertEqual(expected, result)

    def test_create_rectangle_2(self):
        input1 = data.Point(10, 8)
        input2 = data.Point(-2, -6)
        result = hw2.create_rectangle(input1, input2)
        expected = data.Rectangle(data.Point(-2, 8), data.Point(10, -6))
        self.assertEqual(expected, result)

    # Part 2
    def test_shorter_duration_than_1(self):
        input1 = data.Duration(3, 55)
        input2 = data.Duration(3, 51)
        result = hw2.shorter_duration_than(input1, input2)
        expected = False
        self.assertEqual(expected, result)

    def test_shorter_duration_than_2(self):
        input1 = data.Duration(1, 21)
        input2 = data.Duration(5, 19)
        result = hw2.shorter_duration_than(input1, input2)
        expected = True
        self.assertEqual(expected, result)

    # Part 3
    def test_songs_shorter_than_1(self):
        input1 = [data.Song("Kali Uchis", "After The Storm", data.Duration(3, 27)),
                  data.Song("Sugar", "Maroon 5", data.Duration(3, 55)),
                  data.Song("Pink + White", "Frank Ocean", data.Duration(3, 5))]
        input2 = data.Duration(3, 30)
        result = hw2.songs_shorter_than(input1, input2)
        expected = [data.Song("Kali Uchis", "After The Storm", data.Duration(3, 27)),
                    data.Song("Pink + White", "Frank Ocean", data.Duration(3, 5))]
        self.assertEqual(expected, result)

    def test_songs_shorter_than_2(self):
        input1 = [data.Song("Lady Gaga", "Judas", data.Duration(4, 9)),
                  data.Song("Sugar", "Maroon 5", data.Duration(3, 55))]
        input2 = data.Duration(4,0)
        result = hw2.songs_shorter_than(input1, input2)
        expected = [data.Song("Sugar", "Maroon 5", data.Duration(3, 55))]
        self.assertEqual(expected, result)

    # Part 4
    def test_running_time_1(self):
        input1 = [data.Song("Kali Uchis", "After The Storm", data.Duration(3, 27)),
                  data.Song("Sugar", "Maroon 5", data.Duration(3, 55)),
                  data.Song("Pink + White", "Frank Ocean", data.Duration(3, 5)),
                  data.Song("Lady Gaga", "Judas", data.Duration(4, 9))]
        input2 = [2, 1 ,3]
        result = hw2.running_time(input1, input2)
        expected = data.Duration(11, 9)
        self.assertEqual(expected, result)

    def test_running_time_2(self):
        input1 = [data.Song("Kali Uchis", "After The Storm", data.Duration(3, 27)),
                  data.Song("Sugar", "Maroon 5", data.Duration(3, 55)),
                  data.Song("Pink + White", "Frank Ocean", data.Duration(3, 5)),
                  data.Song("Lady Gaga", "Judas", data.Duration(4, 9))]
        input2 = [0, 2, 3, 0, 2]
        result = hw2.running_time(input1, input2)
        expected = data.Duration(17, 13)
        self.assertEqual(expected, result)

    # Part 5
    def test_validate_route_1(self):
        input1 =  [
    ['san luis obispo', 'santa margarita'],
    ['san luis obispo', 'pismo beach'],
    ['atascadero', 'santa margarita'],
    ['atascadero', 'creston']
   ]
        input2 = ['san luis obispo', 'santa margarita', 'atascadero']
        result = hw2.validate_route(input1, input2)
        expected = True
        self.assertEqual(expected, result)

    def test_validate_route_2(self):
        input1 = [
            ['san luis obispo', 'santa margarita'],
            ['san luis obispo', 'pismo beach'],
            ['atascadero', 'santa margarita'],
            ['atascadero', 'creston']
        ]
        input2 = ['san luis obispo', 'santa margarita', 'creston']
        result = hw2.validate_route(input1, input2)
        expected = False
        self.assertEqual(expected, result)

    # Part 6
    def test_largest_repetition_1(self):
        input = [2,4, 4, 3, 5, 5, 5, 6,6, 9,9,9,9]
        result = hw2.largest_repetition(input)
        expected = 9
        self.assertEqual(expected, result)

    def test_largest_repetition_2(self):
        input = [6,6,6,4,2,3,3,5,5,5]
        result = hw2.largest_repetition(input)
        expected = 0
        self.assertEqual(expected, result)

    def test_largest_repetition_3(self):
        input = []
        result = hw2.largest_repetition(input)
        expected = None
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
