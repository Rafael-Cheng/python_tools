import string

def Analysize(path, words):
    with open(path, 'r') as book:
        for line in book:
            depunc = line.translate(None, string.punctuation)
            despace = " ".join(depunc.split())
            for word in despace.split(' '):
                if words.has_key(word) == False:
                    words[word] = 1
                else:
                    words[word] += 1
    return words

def output(words):
    words = sorted(words.iteritems(), key=lambda d:d[1], reverse = True)
    out = ""
    for word in words:
        out += str(word) + '\n'
    with open('output.txt', 'w+') as f:
        f.write(out)
        f.close()

if __name__ == '__main__':
    words = {}
    path = raw_input('Input path of the books=>\n')
    words = Analysize(path, words)
    output(words)
