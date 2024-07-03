class MaxSizeList(object):
    """takes an integer and return a list with spicified
    number of integers
    params:
    list_size: max list size to return"""

    def __init__(self, list_size):
        self.list_size = list_size
        self.word_list = []

    def push(self, word):
        """insert words into the class word_list
        param
        ======
        word: word to be inserted into word word_list"""
        self.word_list.append(word)

    def get_list(self):
        """Returns list of inserted words of size as list_size(if list_size is greater than
        word_list functions returns list chopping of the first few words
        """
        return self.word_list[(len(self.word_list)-self.list_size):]


a = MaxSizeList(3)
a.push('hey')
a.push('hi')
a.push('let\'s')
a.push('go')
print(a.get_list())
b = MaxSizeList(1)
b.push('hi')
b.push('hey')
b.push('let\'s')
b.push('go')
print(b.get_list())

