def word_ladder(beginWord, endWord, wordList):
    word_list = set(wordList)
    queue = [(beginWord, 1, None)]
    parent_map = {beginWord: None}

    while queue:
        word, level, parent = queue.pop(0)
        if word == endWord:
            path = []
            while word:
                path.append(word)
                word = parent_map[word]
            return path[::-1]

        for i in range(len(word)):
            for char in 'abcdefghijklmnopqrstuvwxyz':
                new_word = word[:i] + char + word[i+1:]
                if new_word in word_list and new_word not in parent_map:
                    parent_map[new_word] = word
                    queue.append((new_word, level + 1, word))

    return []


beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

print(word_ladder(beginWord, endWord, wordList))
