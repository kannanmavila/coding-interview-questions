def reverse_word(sentence, start, end):
    word = sentence[start:end-1][::-1]
    return sentence[0:start] \
        + word \
        + sentence[end-1::]

def reverse_words(sentence):
    start = end = 0
    length = len(sentence)

    # Reverse the whole sentence
    sentence = sentence[::-1]

    # Reverse each word so that it gets back to
    # the original form.
    for i in sentence:
        end += 1
        if i == ' ' or end == length:
            if end == length: end += 1
            sentence = reverse_word(sentence, start, end)
            start = end
    return sentence
 
if __name__ == "__main__":
    print reverse_words("Do or do not, there is no try.")
