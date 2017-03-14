import random
import nltk
from pattern.en import pluralize, singularize
from phrasedictionary import PhraseDictionary
import Tkinter as tk
from PIL import ImageTk as itk
from PIL import Image

class CaptionGenerator(object):

    def __init__(self, phrase_dictionary):
        self.phrase_dict = phrase_dictionary

    def get_phrase(self, keyword):
        # for now, random extraction
        phrases = self.phrase_dict.search(keyword)
        return phrases

    def create_caption(self, phrases, keyword):
        # given phrases, 1 keyword, generate caption
        # make sure to adapt to right type of noun
        # for now, assume keyword is a noun
        captions = []
        for p in phrases:
            tags = []
            tokens = nltk.word_tokenize(p)
            tags = [item[1] for item in nltk.pos_tag(tokens)]
            try:
                replace = max(i for i, tag in enumerate(tags) if tag == 'NN' or tag == 'NNS') # tag
            #last noun
            except ValueError: # no noun
                continue
            if tags[replace] == 'NN':
                keyword = singularize(keyword)
            else: # NNS
                keyword = pluralize(keyword)

            tokens[replace] = keyword
            captions.append((' '.join(tokens)))

        return captions

    def display_caption(self, captions, imagefile):
        # given list of captions and pictures display them together
        caption_list = '\n'.join(captions)
        root = tk.Tk()
        cartoon = itk.PhotoImage(file = imagefile)
        w1 = tk.Label(root, image=cartoon).pack(side="top")
        w2 = tk.Label(root, text=caption_list).pack(side="bottom")
        root.mainloop()

        return
