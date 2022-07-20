def pluralise(word):
    if not word.endswith("s"):
        newword = word + "s" 
        return newword
    return word