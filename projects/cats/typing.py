"""Typing test implementation"""

from utils import *
from ucb import main, interact, trace
from datetime import datetime


###########
# Phase 1 #
###########


def choose(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns true. If there are fewer than K such paragraphs, return
    the empty string.
    """
    # BEGIN PROBLEM 1
    count = 0
    for i in range(len(paragraphs)):
        if count == k and select(paragraphs[i]):
            return paragraphs[i]
        if select(paragraphs[i]):
            count += 1
    return ""
    # END PROBLEM 1


def about(topic):
    """Return a select function that returns whether a paragraph contains one
    of the words in TOPIC.

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in topic]), 'topics should be lowercase.'
    # BEGIN PROBLEM 2
    def func(paragraph):
        words = paragraph.split(' ')
        for word in words:
            if remove_punctuation(lower(word)) in topic:
                return True
        return False
    return func
    # END PROBLEM 2


def accuracy(typed, reference):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of REFERENCE that was typed.

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    """
    typed = split(typed)
    reference = split(reference)
    # BEGIN PROBLEM 3
    correct = 0
    size = min(len(typed), len(reference))
    for words in range(size):
        if typed[words] == reference[words]:
            correct += 1
    div = len(typed) if len(typed) != 0 else 1
    return correct / div * 100
    # END PROBLEM 3


def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string."""
    assert elapsed > 0, 'Elapsed time must be positive'
    # BEGIN PROBLEM 4
    return len(typed)/ 5. * 60. / elapsed
    # END PROBLEM 4


def autocorrect(user_word, valid_words, diff_function, limit):
    """Returns the element of VALID_WORDS that has the smallest difference
    from USER_WORD. Instead returns USER_WORD if that difference is greater
    than LIMIT.
    """
    # BEGIN PROBLEM 5
    from sys import maxsize
    smallest = maxsize
    closest = ""
    for word in valid_words:
        if word == user_word:
            return user_word
        diff = diff_function(user_word, word, limit)
        if diff <= limit and diff < smallest:
            smallest = diff
            closest = word
    return user_word if closest == "" else closest
    # END PROBLEM 5


def swap_diff(start, goal, limit):
    """A diff function for autocorrect that determines how many letters
    in START need to be substituted to create GOAL, then adds the difference in
    their lengths.
    """
    # BEGIN PROBLEM 6
    minSize = len(start) if len(start) < len(goal) else len(goal)
    maxSize = len(start) if len(start) > len(goal) else len(goal)
    count = 0

    def helper(i):
        nonlocal minSize, maxSize, count
        if count > limit:
            return
        if i >= minSize:
            count += maxSize - i
            return
        if start[i] != goal[i]:
            count += 1
        helper(i+1)

    helper(0)
    return count if count <= limit else limit+1
    # END PROBLEM 6

def edit_diff(start, goal, limit):
    """A diff function that computes the edit distance from START to GOAL."""
    # BEGIN PROBLEM 7
    memory = {}
    def helper(i, j):
        if i >= len(start):
            return len(goal) - j
        if j >= len(goal):
            return len(start) - i

        if start[i] != goal[j]:
            if memory.get((i+1, j)) == None:
                memory[(i+1, j)] = helper(i+1, j)
            if memory.get((i, j+1)) == None:
                memory[(i, j+1)] = helper(i, j+1)
            if memory.get((i+1, j+1)) == None:
                memory[(i+1, j+1)] = helper(i+1, j+1)
            return min(memory[(i+1, j)], memory[(i, j+1)], memory[(i+1, j+1)]) + 1
        if memory.get((i+1, j+1)) == None:
            memory[(i+1, j+1)] = helper(i+1, j+1)
        return memory[(i+1, j+1)]

    if min(len(start), len(goal)) == 0: # Fill in the condition
        diff = max(len(start), len(goal))
    else:
        diff = helper(0, 0)
    return diff if diff <= limit else limit+1
    # END PROBLEM 7


def final_diff(start, goal, limit):
    """A diff function. If you implement this function, it will be used."""
    assert False, 'Remove this line to use your final_diff function'




###########
# Phase 3 #
###########


def report_progress(typed, prompt, id, send):
    """Send a report of your id and progress so far to the multiplayer server."""
    # BEGIN PROBLEM 8
    correct = 0.
    for i in range(min(len(typed), len(prompt))):
        if typed[i] != prompt[i]:
            break
        correct += 1.
    progress = correct / len(prompt)
    send({"id": id, "progress": progress})
    return progress
    # END PROBLEM 8


def fastest_words_report(word_times):
    """Return a text description of the fastest words typed by each player."""
    fastest = fastest_words(word_times)
    report = ''
    for i in range(len(fastest)):
        words = ','.join(fastest[i])
        report += 'Player {} typed these fastest: {}\n'.format(i + 1, words)
    return report


def fastest_words(word_times, margin=1e-5):
    """A list of which words each player typed fastest."""
    n_players = len(word_times)
    n_words = len(word_times[0]) - 1
    assert all(len(times) == n_words + 1 for times in word_times)
    assert margin > 0
    # BEGIN PROBLEM 9
    out = [[] for _ in range(n_players)]
    for wIndex in range(1, n_words+1, 1):
        fastest = min([elapsed_time(player[wIndex]) - elapsed_time(player[wIndex-1]) for player in word_times])
        for pIndex in range(n_players):
            if elapsed_time(word_times[pIndex][wIndex]) - elapsed_time(word_times[pIndex][wIndex-1]) - fastest < margin:
                out[pIndex] += [word(word_times[pIndex][wIndex])]
    return out
    # END PROBLEM 9


def word_time(word, elapsed_time):
    """A data abstrction for the elapsed time that a player finished a word."""
    return [word, elapsed_time]


def word(word_time):
    """An accessor function for the word of a word_time."""
    return word_time[0]


def elapsed_time(word_time):
    """An accessor function for the elapsed time of a word_time."""
    return word_time[1]


enable_multiplayer = False  # Change to True when you


##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file('data/sample_paragraphs.txt')
    select = lambda p: True
    if topics:
        select = about(topics)
    i = 0
    while True:
        reference = choose(paragraphs, select, i)
        if not reference:
            print('No more paragraphs about', topics, 'are available.')
            return
        print('Type the following paragraph and then press enter/return.')
        print('If you only type part of it, you will be scored only on that part.\n')
        print(reference)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print('Goodbye.')
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print('Words per minute:', wpm(typed, elapsed))
        print('Accuracy:        ', accuracy(typed, reference))

        print('\nPress enter/return for the next paragraph or type q to quit.')
        if input().strip() == 'q':
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument('topic', help="Topic word", nargs='*')
    parser.add_argument('-t', help="Run typing test", action='store_true')

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)