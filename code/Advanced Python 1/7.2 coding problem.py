# Create a sentence class as iterator


class Sentence:
    def __init__(self, text):
        self.text = text
        self.value = 0
        self.items = self.text.split()

    def __iter__(self):
        return self

    def __next__(self):
        self.end = len(self.items)
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1
        return self.items[current]


my_sentence = Sentence("Hello World Banaglore")

for word in my_sentence:
    print(word)
