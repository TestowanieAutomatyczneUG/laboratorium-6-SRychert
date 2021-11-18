import unittest
from song import Song


class SongTest(unittest.TestCase):

    def setUp(self):
        self.temp = Song()

    def test_Get_First_Verse(self):
        self.assertEqual(self.temp.getSong(1),
                         ("On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree."))

    def test_Get_One_Verse(self):
        self.assertEqual(self.temp.getSong(3),
                         "On the third day of Christmas my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.")

    def test_Get_Section(self):
        self.assertEqual(self.temp.getSong(2, 4),
                         ("On the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree.\n\n"
                          "On the third day of Christmas my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\n\n"
                          "On the fourth day of Christmas my true love gave to me: four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\n\n"))

    def test_Get_Whole_Song(self):
        self.assertEqual(self.temp.getSong(),
                         ("On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.\n\n"
                          "On the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree.\n\n"
                          "On the third day of Christmas my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\n\n"
                          "On the fourth day of Christmas my true love gave to me: four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\n\n"
                          "On the fifth day of Christmas my true love gave to me: five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\n\n"
                          "On the sixth day of Christmas my true love gave to me: six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\n\n"
                          "On the seventh day of Christmas my true love gave to me: seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\n\n"
                          "On the eighth day of Christmas my true love gave to me: eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\n\n"
                          "On the ninth day of Christmas my true love gave to me: nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\n\n"
                          "On the tenth day of Christmas my true love gave to me: ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\n\n"
                          "On the eleventh day of Christmas my true love gave to me: eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\n\n"
                          "On the twelfth day of Christmas my true love gave to me: twelve Drummers Drumming, eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree."
                          ))

    def test_Get_Wrong_Order(self):
        self.assertEqual(self.temp.getSong(6, 1), "")

    def test_Get_Same_Values(self):
        self.assertEqual(self.temp.getSong(5, 5),
                         "On the fifth day of Christmas my true love gave to me: five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.\n\n")

    def test_Get_Negative(self):
        self.assertRaises(Exception, self.temp.getSong, -5)

    def test_Get_Out_Of_Range(self):
        self.assertRaises(Exception, self.temp.getSong, 50)

    def test_Get_Wrong_Type(self):
        self.assertRaises(Exception, self.temp.getSong, "1")

    def test_Get_First_Negative(self):
        self.assertRaises(Exception, self.temp.getSong, -5, 5)

    def test_Get_Second_Negative(self):
        self.assertRaises(Exception, self.temp.getSong, 3, -5)

    def test_Get_First_Out_Of_Range(self):
        self.assertRaises(Exception, self.temp.getSong, 50, 8)

    def test_Get_Second_Out_Of_Range(self):
        self.assertRaises(Exception, self.temp.getSong, 50, 8)

    def test_Get_First_Wrong_Type(self):
        self.assertRaises(Exception, self.temp.getSong, "1", 7)

    def test_Get_Second_Wrong_Type(self):
        self.assertRaises(Exception, self.temp.getSong, 11, "12")

    def tearDown(self):
        self.temp = None


if __name__ == "__main__":
    unittest.main()
