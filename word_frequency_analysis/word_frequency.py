import string

def Analysize(path, words):
    with open(path, 'r') as book:
        for line in book:
            # delete punctuations
            depunc = line.translate(None, string.punctuation)
            # delete spcaces and spilt
            despace = depunc.strip().split()
            # count
            for word in despace:
                if True == word.isdigit() or '' == word:
                    continue
                word = word.lower()
                if False == words.has_key(word):
                    words[word] = 1
                else:
                    words[word] += 1
    return words

def output(path, words):
    words = sorted(words.iteritems(), key=lambda d:d[1], reverse = True)
    out = ""
    out_path = "word_frequency_of_" + path.split('/')[-1]
    for word in words:
        out += str(word) + '\n'
    with open(out_path, 'w+') as f:
        f.write(out)
        f.close()

if __name__ == '__main__':
    # frequency dictionary
    words = {} 
    path = raw_input('Input path of the books=>\n')
    words = Analysize(path, words)
    output(path, words)
