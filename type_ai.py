import tkinter as tk
import re
"""
Training content: https://statmt.org/wmt11/translation-task.html#download
"""

class Train():
    def __init__(self):
        

        #initialize the dic
        self.dictionary = {}

        #reading the training content
        with open("training_content.txt", "r", encoding="utf-8") as f:
            self.text = f.read()


        #a list
        self.sentences = re.split(r"[\n]", self.text)
        for i in self.sentences:
            words = re.split(r"[ ,;.!?()]", i)
            for x in range(len(words) - 1):
                word = words[x]
                next_word = words[x + 1]

                if word not in self.dictionary:
                    self.dictionary[word] = {}

                if next_word not in self.dictionary[word]:
                    self.dictionary[word][next_word] = 0

                self.dictionary[word][next_word] += 1




       

