from collections import deque


def compare_two_words(w1, w2):
    are_match = True

    if abs(len(w1) - len(w2)) > 1:
        are_match = False

    # Boolean indicating if one edit apart
    if len(w1) == len(w2):
        i1 = 0
        i2 = 0
        mismatches = 0  # E.g comapre put and pot
        while i1 < len(w1):
            if w1[i1] != w2[i2]:
                mismatches += 1

            if mismatches > 1:
                are_match= False
            i1 += 1
            i2 += 1

    else:
        # Swap so len(w1) <len(w2)
        if len(w1) > len(w2):
            w1, w2 = w2, w1

        i1 = 0
        i2 = 0
        mismatches = 0
        added_in_larger = False

        while i1 < len(w1):
            if w1[i1] != w2[i2]:
                if not added_in_larger:
                    i1 -= 1
                    added_in_larger = True
                else:
                    mismatches += 1

            if mismatches > 1:
                are_match = False

            i1 += 1
            i2 += 1
    
    # print(f"Comparing {w1} and {w2} ? {are_match}")
    return are_match

def get_candidates(word, word_set):
    return filter(lambda other_word: compare_two_words(word, other_word), word_set)


def shortestWordEditPath(source, target, words):

    seen_words = set()
    word_set = set(words)

    if target not in word_set or len(target) != len(source):
        return -1

    stack = deque()

    stack.append((source, 0))
    while stack:
        word_now, depth_now = stack.popleft()
        # print(f"Word now {word_now} and depth {depth_now}")
        seen_words.add(word_now)
        

        if word_now == target:
            return depth_now
        else:
            for related_word in get_candidates(word_now, word_set - seen_words):
                # print(f"Related word {related_word}")
                stack.append((related_word, depth_now+1))

    return -1


source = "bit"
target = "dog"
words = ["but", "put", "big", "pot", "pog", "dog", "lot"]

print(shortestWordEditPath(source, target, words))


# s="aa" t="aaaa"
# [aaa]

# aa -> aaa -> aaaa
# 2


# at one word, for all other words, check if maching after changing one ltter

# pairwise compare all words, get related candidates
# keep a counter in both words, go though letters and tolerate one mistach


# You want to do bfs and opposed to dfs
# If do bfs, return first solution

# explore those words, and if at the final word, stop
# if at end word stop
# To determine minimum, keep current words traversed, if at end, compare if curent minimum

# Keep a list of seen words
