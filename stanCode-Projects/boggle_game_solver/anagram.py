"""
File: anagram.py
Name: Jasmine Tsai
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop

dict_lst = []
counter = 0
found = []


def main():
    read_dictionary()
    print('Welcome to stanCode \" Anagram Generator\" (or -1 to quit/)')
    while True:
        inp = input(str('Find anagrams for: '))  # user input
        inp = inp.lower()
        if inp == EXIT:
            break
        find_anagrams(inp)


def read_dictionary():
    with open(FILE, 'r') as f:
        for line in f:
            dict_lst.append(line.strip())


def find_anagrams(s):
    """
    :param s: user input
    :return: None
    """
    global counter
    print('Searching...')
    helper(s, found, '', [])
    print(f'{counter} anagrams: {found}')


def helper(s, current_lst, current_word, index):
    global counter
    if len(current_word) == len(s) and current_word in dict_lst:  # if the word in dictionary and length is len(s)
        if current_word not in current_lst:  # if the word not in list append
            current_lst.append(current_word)
            print('Found: ' + current_word)
            print('Searching...')
            counter += 1

    else:
        for i in range(len(s)):
            if i not in index:
                # choose
                current_word += s[i]
                index.append(i)
                # explore
                if has_prefix(current_word):
                    helper(s, current_lst, current_word, index)
                # un-choose
                current_word = current_word[:-1]
                index.pop()


def has_prefix(sub_s):
    """
    :param sub_s: the un-check combination
    :return: the combination is in the dictionary or not
    """
    for ch in dict_lst:
        if ch.startswith(sub_s):
            return ch.startswith(sub_s)


if __name__ == '__main__':
    main()
