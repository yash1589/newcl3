from mrjob.job import MRJob

class CharCount(MRJob):
    def mapper(self, _, line):
        # Emit each character with a count of 1
        for char in line:
            if char.isalnum():  # Ignore non-alphanumeric characters
                yield (char, 1)
    
    def reducer(self, char, counts):
        # Sum the counts for each character
        yield (char, sum(counts))

if __name__ == '__main__':
    CharCount.run()