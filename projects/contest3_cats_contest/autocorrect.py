from utils import get_common_unique_words_from_corpus

PLAYER_NAME = ''  # Change this line!

def feline_flips(start, goal, limit):
    """A diff function for autocorrect that determines how many letters
    in START need to be substituted to create GOAL, then adds the difference in
    their lengths and returns the result.

    Arguments:
        start: a starting word
        goal: a string representing a desired goal word
        limit: a number representing an upper bound on the number of chars that must change

    >>> big_limit = 10
    >>> feline_flips("nice", "rice", big_limit)    # Substitute: n -> r
    1
    >>> feline_flips("range", "rungs", big_limit)  # Substitute: a -> u, e -> s
    2
    >>> feline_flips("pill", "pillage", big_limit) # Don't substitute anything, length difference of 3.
    3
    >>> feline_flips("roses", "arose", big_limit)  # Substitute: r -> a, o -> r, s -> o, e -> s, s -> e
    5
    >>> feline_flips("rose", "hello", big_limit)   # Substitute: r->h, o->e, s->l, e->l, length difference of 1.
    5
    """
    # BEGIN PROBLEM 6
    if limit == -1:
        return 1
    if start == goal: 
        return 0
    if start == '' and goal != '':
        return len(goal)
    if start != '' and goal == '':
        return len(start)
    if start[0] == goal[0]:
        return feline_flips(start[1:], goal[1:], limit)
    else:
        return 1+feline_flips(start[1:], goal[1:], limit-1)
    # END PROBLEM 6


def minimum_mewtations(start, goal, limit):
    """A diff function that computes the edit distance from START to GOAL.
    This function takes in a string START, a string GOAL, and a number LIMIT.

    Arguments:
        start: a starting word
        goal: a goal word
        limit: a number representing an upper bound on the number of edits

    >>> big_limit = 10
    >>> minimum_mewtations("cats", "scat", big_limit)       # cats -> scats -> scat
    2
    >>> minimum_mewtations("purng", "purring", big_limit)   # purng -> purrng -> purring
    2
    >>> minimum_mewtations("ckiteus", "kittens", big_limit) # ckiteus -> kiteus -> kitteus -> kittens
    3
    """
    if limit == -1:  # Fill in the condition
        # BEGIN
        return 1
        # END
    elif start == goal:
        return 0
    elif start == '' or goal == '':  # Feel free to remove or add additional cases
        # BEGIN
        return max(len(start), len(goal))
        # END
    elif start[0] == goal[0]:
        return minimum_mewtations(start[1:], goal[1:], limit)
    else:
        add = goal[0]+start  # Fill in these lines
        remove = start[1:]
        substitute = goal[0]+start[1:]
        # BEGIN
        return min(1+minimum_mewtations(add, goal, limit-1), 1+minimum_mewtations(remove, goal, limit-1),1+minimum_mewtations(substitute, goal, limit-1))
        # END


def final_diff(start, goal, limit):
    """A diff function that takes in a string START, a string GOAL, and a number LIMIT.
    If you implement this function, it will be used."""
    if limit == -1:  # Fill in the condition
        # BEGIN
        return 1
        # END
    elif start == goal:
        return 0
    elif start == '' or goal == '':  # Feel free to remove or add additional cases
        # BEGIN
        return max(len(start), len(goal))
        # END
    elif start[0] == goal[0]:
        return minimum_mewtations(start[1:], goal[1:], limit)
    else:
        add = goal[0]+start  # Fill in these lines
        remove = start[1:]
        substitute = goal[0]+start[1:]
        # BEGIN
        return min(1+minimum_mewtations(add, goal, limit-1), 1+minimum_mewtations(remove, goal, limit-1),1+minimum_mewtations(substitute, goal, limit-1))
        # END

global_dict = get_common_unique_words_from_corpus('the_adventures_of_sherlock_holmes.txt')
FINAL_DIFF_LIMIT = 6  # REPLACE THIS WITH YOUR LIMIT
def autocorrect(user_word, words_dict=global_dict):
    
    if user_word in words_dict.keys():
        return user_word

    ret = user_word
    minDif = FINAL_DIFF_LIMIT
    
    for word in words_dict.keys():
        diff = final_diff(user_word, word, FINAL_DIFF_LIMIT)
        if  diff <= minDif:
            if ret == user_word:
                ret = word
            elif diff == minDif and words_dict[ret] < words_dict[word]:
                ret = word
            elif diff < minDif:
                ret = word
            minDif = diff
        
    return ret  # Replace with your autocorrect implementation!
