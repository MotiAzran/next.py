def translate(sentence):
    words = {'esta': 'is', 'la': 'the', 'en': 'in', 'gato': 'cat', 'casa': 'house', 'el': 'the'}
    translation_gen = (words.get(word, word) for word in sentence.split(' '))
    return ' '.join(translation_gen)
