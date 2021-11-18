class HammingDistance:
    def distance(self, dna1, dna2):
        if len(dna1) != len(dna2):
            raise ValueError("DNA must be same length")
        distance = 0
        for i in range(len(dna1)):
            if dna1[i] != dna2[i]:
                distance += 1
        return distance
