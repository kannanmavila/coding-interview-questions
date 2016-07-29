#! /usr/bin/env python
# -*- coding: utf-8 -*-

class TrieNode(object):
	def __init__(self, alphabet_size, offset_char):
		self.is_leaf = False
		self.children = [None] * alphabet_size
		self.offset_char = offset_char

	def get_child(self, char):
		return self.children[self.get_pos(char)]

	def get_pos(self, char):
		return ord(char) - ord(self.offset_char)

	def get_char(self, i):
		return chr(ord(self.offset_char)+i)

	def set_child(self, char):
		self.children[self.get_pos(char)] = TrieNode(self.alphabet_size,
				self.offset_char)
		return self.get_child(char)

	@property
	def alphabet_size(self):
		return len(self.children)


class Trie(object):
	def __init__(self, alphabet_size=26, offset_char='a'):
		self.root = TrieNode(alphabet_size, offset_char)

	def add(self, string):
		node = self.root
		for c in string:
			next = node.get_child(c)
			if next is None:
				next = node.set_child(c)
			node = next
		node.is_leaf = True

	def search(self, string, prefix=False):
		node = self.root
		for c in string:
			node = node.get_child(c)
			if node is None:
				return False
		if node.is_leaf or prefix:
			return True
		return False

	def print_all(self):
		self._print_all(self.root)

	@staticmethod
	def _print_all(node, string=''):
		if node.is_leaf:
			print string
		for i in xrange(len(node.children)):
			if node.children[i] is not None:
				Trie._print_all(node.children[i], string+node.get_char(i))


if __name__ == "__main__":
	trie = Trie(26, 'a')
	trie.add('asdf')
	trie.add('asdfa')
	trie.add('bcde')
	print trie.search('asdf')
	print trie.search('asd')
	print trie.search('asd', prefix=True)
