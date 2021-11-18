class Song:

    def getSong(self, firstIndex=None, secondIndex=None):
        song = ("On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.\n\n"
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
                )
        dl = len(song.split("\n\n"))
        splitedSong = song.split("\n\n")
        if(firstIndex is None and secondIndex is None):
            return song
        elif(firstIndex is not None and secondIndex is None):
            if (type(firstIndex) == int):
                if firstIndex >= 1 and firstIndex <= dl:
                    return splitedSong[firstIndex-1]
                else:
                    raise Exception("Wrong Value of Verse")
            else:
                raise Exception("Wrong type")
        elif(firstIndex is not None and secondIndex is not None):
            if (type(firstIndex) == int and type(secondIndex) == int):
                if(firstIndex >= 1 and firstIndex <= dl and secondIndex <= dl and secondIndex >= 1 and firstIndex <= secondIndex):
                    if firstIndex == secondIndex:
                        return splitedSong[firstIndex-1]
                    else:
                        section = splitedSong[firstIndex-1:secondIndex]
                        result = ""
                        for verse in section:
                            result += verse + "\n\n"
                        return result
                else:
                    raise Exception("Wrong Values of Verses")
            else:
                raise Exception("Wrong type")
        elif(firstIndex is None and secondIndex is not None):
            raise Exception("You tricky")
