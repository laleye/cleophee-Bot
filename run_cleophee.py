#from nltk.stem.snowball import FrenchStemmer
#stemmer = FrenchStemmer()
from chatscript import ChatscriptInstance
#import spacy
#nlp = spacy.load('fr')


class Cleophee(object):
    def __init__(self):
        self.cs = ChatscriptInstance("cleophee", "user")
    def process(self, texte):
        return self.cs.chatscript(texte)
    

def main():
    cl = Cleophee()
    while True:
        texte = input('User> ')
        print('Cleophee> {}'.format(cl.process(texte)))
        
main()
        
