import unittest
from phrasedictionary import PhraseDictionary
import gensim
MODEL = 'GoogleNews-vectors-negative300.bin'
class TestPhraseDictionary(unittest.TestCase):


    def test_init(self):
        filename = 'temp.txt'
        # create a file
        outFile = open(filename, 'w')
        outFile.write('This is test sentence one\nThis is test sentence two\n')
        outFile.close()

        # load word2vecModel
        # model = gensim.models.KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True)

        phrase_dict = PhraseDictionary([filename],3,20,MODEL)

        # assert dicitonary right format
        result = len(phrase_dict.phrases)
        self.assertEqual(2, result)
        result = len(list(phrase_dict.phrases)[0].split(' '))
        self.assertEqual(5, result)
        self.assertFalse('\n' in list(phrase_dict.phrases)[1].split(' '))

        #phrase_dict.del_model()
        #self.assertTrue(phrase_dict.model is model)

    def test_create_index(self):
        filename = 'temp.txt'
        # create a file
        outFile = open(filename, 'w')
        outFile.write('This is test sentence one\nThis is test sentence two\n')
        outFile.close()

        # load word2vecModel
        # model = gensim.models.KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True)

        phrase_dict = PhraseDictionary([filename],3,20,MODEL)
        phrase_dict.create_index()

        #phrase_dict.del_model()
        # Need to add tests

    def test_search(self):
        filename = 'temp.txt'
        # create a file
        outFile = open(filename, 'w')
        outFile.write('This is test sentence one\nThis is test sentence two\n')
        outFile.close()

        # model = gensim.models.KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True)
        phrase_dict = PhraseDictionary([filename],3,20,MODEL)
        phrase_dict.create_index()

        results = phrase_dict.search("one")
        #phrase_dict.del_model()

        # gonna need gensims for this

    def test_save(self):
        # saving the latest model for TestCaptionGenerator
        phrase_dict = PhraseDictionary(['../phraseScrapers/cliches.txt', '../phraseScrapers/phrases.txt', '../phraseScrapers/proverbs_0.txt', '../phraseScrapers/quotes.txt', '../phraseScrapers/truisms_1.txt', '../phraseScrapers/truisms.txt'],5,25,MODEL)
        phrase_dict.create_index()
        phrase_dict.save('./phrases.model')
        print len(phrase_dict.phrases)




if __name__ == '__main__':
    unittest.main()
