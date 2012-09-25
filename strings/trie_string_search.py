#!/usr/bin/python

"""
Author: TD
License: GPLv3
"""

class Trie(object):
    __debug = False

    """docstring for Trie"""
    def __init__(self):
        super(Trie, self).__init__()
        self.root = {}
        
    def create_sub_trie(self, word, i, l):
        result = {}
        node = result
        for x in xrange(i, l):
            new_node = {}
            node[word[x]] = new_node
            node = new_node
        return result

    def add(self, word):
        l = len(word)
        node = self.root
        for i in xrange(0, l):
            if word[i] in node:
                node = node[word[i]]
            else:
                node[word[i]] = self.create_sub_trie(word, i+1, l)
                break
        return self

    def disp(self, root):
        if root is None:
            if self.__debug:
                print "No root specified, using self.root"
            root = self.root

        print root

        if not root:
            return

        for k,v in root.items():
            print v
            self.disp(v)
                
    
    def contains(self, word):
        if self.__debug:
            print "Entering search for word", word
        l = len(word)
        node = self.root
        for i in xrange(0, l):
            if word[i] in node:
                node = node[word[i]]
            else:
                if self.__debug:
                    print "Exiting search at letter", word[i]
                return False
        return True
    

if __name__ == '__main__':
    try:
        print "Please enter the string we will be searching into."
        T = Trie()
        for w in raw_input().strip().split(" "):
            T.add(w)

        T.disp(None)

        print "Please enter space separated values of words you want to search in this string"
        for w in raw_input().strip().split(" "):
            print "Word", w, ", result:"
            print T.contains(w)
    except EOFError:
        pass
