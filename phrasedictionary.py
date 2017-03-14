from whoosh.index import create_in
from whoosh.fields import *
from whoosh.qparser import QueryParser
import pickle

class PhraseDictionary(object):
    def __init__(self, filenames):
        # files == list of .txt files, each line a phrase, separated by a new line
        # min == min length of sentence / not implemented
        # max == max length of sentence / not implemented
        # model == word2vec model / omitted for now

        # load the files into phrases
        self.phrases = []
        for filename in filenames:
            with open(filename) as f:
                self.phrases = f.read().splitlines()

        #self.model = model
        self.ix = None

        # self.vector_dict = {}
        # self.phrases_vectors = []

    # call this on the init? 
    def create_index(self):
        schema = Schema(index = ID(stored = True), content = TEXT(stored = True))
        self.ix = create_in("indexdir", schema)
        writer = self.ix.writer()
        for i, p in enumerate(self.phrases):
            writer.add_document(index = str(i).decode('utf-8'), content = p.decode('utf-8'))
        writer.commit()
        return

    def search(self, keyword):
        with self.ix.searcher() as searcher:
            query = QueryParser("content", schema=self.ix.schema).parse(keyword)
            result_indexes = searcher.search(query)
            results = [ r['content'] for r in result_indexes ]
        return results

    def save(self, f):
        f = file(f, 'wb')
        pickle.dump(self, f)
        f.close()
