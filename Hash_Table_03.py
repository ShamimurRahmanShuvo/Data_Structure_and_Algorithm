# Count the words in a poem

class Poem:
    def poem_show(self):
        with open("poem.txt","r") as f:
            for line in f:
                print(line)

    def word_count(self):
        word_c = {}
        with open("poem.txt","r") as f:
            for line in f:
                tokens = line.split(' ')
                for token in tokens:
                    token = token.replace('\n', '')
                    if token in word_c:
                        word_c[token] +=1
                    else:
                        word_c[token] = 1
            return word_c


if __name__ == '__main__':
    p = Poem()
    p.poem_show()
    print(p.word_count())