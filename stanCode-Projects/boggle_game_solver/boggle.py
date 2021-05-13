"""
File: boggle.py
Name: Jasmine Tsai
----------------------------------------
TODO:
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'

dict_lst = []
counter = 0
found = []
num_of_words = 0
printed_words = []


def main():
	"""
	TODO: Find the possible words among the 16 letters of the 4x4 square.
	"""
	global counter
	read_dictionary()

	line = input('1 row of letters: ')
	line = line.lower()
	count = 1
	alphabet = []

	# while loop check whether the input letter is correct, if it is wrong, must re-enter it
	while True:

		if line is not None and len(line) == 7 and line[0].isalpha() and line[1] == " " and line[2].isalpha() and line[3] == " " and line[4].isalpha() and line[5] == " " and line[6].isalpha():
			if count < 4:
				alphabet.append(line)
				count += 1
				line = input(f'{count} row of letters: ')

			else:
				# last input
				if count == 4:
					alphabet.append(line)
					break

		else:
			# re-enter input
			print('IIllegal input')
			line = input(f'{count} row of letters: ')

	line1 = alphabet[0]
	line1 = line1.split()
	line2 = alphabet[1]
	line2 = line2.split()
	line3 = alphabet[2]
	line3 = line3.split()
	line4 = alphabet[3]
	line4 = line4.split()

	# put all the letters on the board
	board = [line1, line2, line3, line4]

	for y in range(4):
		for x in range(4):
			maybe_word = board[x][y]  # the start position to find a word
			found_word(board, x, y, maybe_word, [(x, y)])
	print(f'There are {num_of_words} words in total.')


def found_word(board, x, y, maybe_word, index_lst):
	global num_of_words
	if maybe_word in dict_lst and len(maybe_word) >= 4:  # if the word in dictionary and len(maybe_word) >= 4
		# base case
		if maybe_word not in printed_words:  # if the word not in printed_words append
			printed_words.append(maybe_word)
			print(f'Found \"{maybe_word}\"')
			num_of_words += 1

	if has_prefix(maybe_word):
		for i in range(-1, 2):
			for j in range(-1, 2):
				if 0 <= x + i < 4 and 0 <= y + j < 4:
					if (x + i, y + j) not in index_lst:
						# choose
						index_lst.append((x + i, y + j))
						maybe_word += board[x + i][y + j]
						# explore
						found_word(board, x + i, y + j, maybe_word, index_lst)
						# un-choose
						maybe_word = maybe_word[:len(maybe_word) - 1]
						index_lst.pop()


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	with open(FILE, 'r') as f:
		for line in f:
			dict_lst.append(line.strip())


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for ch in dict_lst:
		if ch.startswith(sub_s):
			return ch.startswith(sub_s)


if __name__ == '__main__':
	main()
