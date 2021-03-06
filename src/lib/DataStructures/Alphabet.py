
class Alphabet:

        """
        We use the conventions described here: https://meme-suite.org/meme/doc/alphabets.html
        to define alphabets.

        If you, the user, would like to define your own alphabet, please be sure it conforms
        to the rules described on our website here: INSERT TUTORIAL LINK

        """

        DNA = {"-": 0, "A":1, "C":2, "M":3, "G":4, "R":5, "S":6, "V":7, "T":8, "U":8, "W":9, "Y":9,
        "H":10, "K":11, "D":12, "B":13, "N":14, "X":14, ".":14}

        RNA = {"-": 0, "A":1, "C":2, "M":3, "G":4, "R":5, "S":6, "V":7, "T":8, "U":8, "W":9, "Y":9,
        "H":10, "K":11, "D":12, "B":13, "N":14, "X":14, ".":14}
        
        PROTEIN = {"-": 0, "A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7, "H":8, "I":9, "J":10,
        "K":11, "L":12, "M":13, "N": 14, "P": 15, "Q":16, "R":17, "S":18, "T":19, "V":20, "W":21, "X":22,
        "Y":23, "Z":24, ".":25}

        CODON = {"-": 0, "A":1, "C":2, "M":3, "G":4, "R":5, "S":6, "V":7, "T":8, "U":8, "W":9, "Y":9,
        "H":10, "K":11, "D":12, "B":13, "N":14, "X":14, ".":14}

        SNP = {"-": 0, "0": 1, "1": 2, "2": 3}

        BINARY = {"-": 0, "0": 1, "1": 2}

        def __init__(self, type, myAlphabet={}):

                self.type = type
                
                if type == "user":
                        self.alphabet = myAlphabet
                else:
                        if type == "DNA" or type == "RNA" or type == "CODON":
                                self.alphabet = self.DNA
                        elif type == "PROTEIN":
                                self.alphabet = self.PROTEIN
                        elif type == "SNP":
                                self.alphabet = self.SNP
                        elif type == "BINARY":
                                self.alphabet = self.BINARY
                        else:
                                #Other matrix type?
                                pass


        def map(self, char):
                return self.alphabet[char]
        
        def getType(self):
                return self.type

        def reverseMap(self, state):
                for key in self.alphabet.keys():
                        if self.alphabet[key] == state:
                                return key