alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet = list(alphabet)
#encryption
def hash(word, key): #Key = step
    word=word.lower()
    for i in word:
        c=alphabet.index(i)
        s=c+key
        if s > len(alphabet) - 1:
            s = abs(len(alphabet) - s)
        print(alphabet[s], end='')

#decryption
def dehash(word, key): #Key = step
    word=word.lower()
    for i in word:
        c=alphabet.index(i)
        s=c-key
        if s < 0:
            s = len(alphabet) - abs(c - key)
        print(alphabet[s], end='')
