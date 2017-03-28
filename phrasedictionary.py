from whoosh.index import create_in
from whoosh.fields import *
from whoosh.qparser import QueryParser
import pickle
import gensim

# files == list of .txt files, each line a phrase, separated by a new line
# min == min length of sentence
# max == max length of sentence
# model == word2vec model location
class PhraseDictionary(object):
    def __init__(self, filenames, min_len, max_len, model):
        # load the files into phrases
        self.phrases = set()
        for filename in filenames:
            with open(filename) as f:
                for line in f.read().splitlines():
                    words = line.split(' ')
                    if len(words) > min_len and len(words) < max_len:
                        self.phrases.add(line)

        # self.model = gensim.models.KeyedVectors.load_word2vec_format(model, binary = True)
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
        # similar_words = self.model.similar_by_word(keyword, topn=10, restrict_vocab=None)
        # similar_words.insert(0,keyword)
        # for word in similar_words:
        with self.ix.searcher() as searcher:
            query = QueryParser("content", schema=self.ix.schema).parse(keyword)
            result_indexes = searcher.search(query, limit=100)
            results = [ r['content'] for r in result_indexes ]
        return results

    def save(self, f):
        f = file(f, 'wb')
        pickle.dump(self, f)
        f.close()

    def del_model(self):
        del self.model
