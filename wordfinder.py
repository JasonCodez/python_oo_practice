from random import choice


"""Word Finder: finds random words from a dictionary."""


class WordFinder:

   def __init__(self, file):
      self.file = file

      dict_file = open(file)
   
   def word_count(self):
      f = open(self.file, 'r')
      return f"{len(f.readlines())} words read"

   def rand_word(self):
      f = open(self.file, 'r')
      return choice(f.readlines()).strip()

class SpecialWordFinder(WordFinder):

   def parse(self, dict_file):
      return [w.strip() for w in dict_file if w.strip() and not w.startswith("#")]
      

         
         
      


      


   
       
