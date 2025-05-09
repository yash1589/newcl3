from mrjob.job import MRJob

class WordCount(MRJob):
    def mapper(self, _, line):
        # Split line into words and emit each word with a count of 1
        words = line.split()
        for word in words:
            yield (word.lower(), 1)  # Convert to lowercase to count "Word" and "word" as the same

    def reducer(self, word, counts):
        # Sum the counts for each word
        yield (word, sum(counts))

if __name__ == '__main__':
    WordCount.run()
