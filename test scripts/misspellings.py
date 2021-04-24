from spellchecker import SpellChecker

def misspelled_words(text):
    #Library for spell checking
    spell = SpellChecker()
    text = remove_symbols(text)
    #Regex for finding digits
    _digits = re.compile('\d')

    #List of misspelled words
    misspelled = spell.unknown(text.split())
    #Remove words, that start with capital letter (Likely names)
    no_names = [x for x in misspelled if x.title() not in text]
    #Remove words that contain digits (7th)
    no_digits = [x for x in no_names if not bool(_digits.search(x))]
    
    #Find corrections for misspelled words - if word is more than a single character.
    corrections = [spell.correction(x) for x in no_digits if len(x)>1]
    #Remove corrections, if they have no correction (likely misclassified spelling mistake)
    remove_no_correction = [x for x in corrections if x not in misspelled]
    return remove_no_correction

misspelled_words(corpus[1])
