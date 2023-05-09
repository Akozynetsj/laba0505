def long_words(dictionary):
    result = []
    for word in dictionary:
        if len(word) >= 5:
            result.append(word)
    return result
