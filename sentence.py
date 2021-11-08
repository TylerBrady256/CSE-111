import random
def main():
    grammatical_number = random.randint(0,1)
    tenses = ["past","present","future"]
    tense = random.choice(tenses)
    
    noun= get_noun(grammatical_number)

    initiator = a_to_an_conversion(noun,get_determiner(grammatical_number))
    verb = get_verb(grammatical_number,tense)

    prepesitional_phrase = ""
    if random.randint(0,1) ==1:
        prepesitional_phrase = get_prepositional_phrase(grammatical_number)
    


    print(f"{initiator} {noun} {verb} {prepesitional_phrase}")

def a_to_an_conversion(noun,determiner):
    vowels =["a","e","i","o","u","y"]
    if determiner == "a" and noun[0] in vowels:
            determiner = "an"

    return determiner 

def get_determiner(grammatical_number):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "two", "some", "many".
    If grammatical_number == 1, this function will return
    either "the" or "one". Otherwise this function will
    return either "some" or "many".

    Parameter
        grammatical_number: an integer.
            If grammatical_number == 1, this function will return
            a determiner for a single noun. Otherwise this
            function will return a determiner for a plural noun.
    Return: a randomly chosen determiner.
    """
    if grammatical_number == 1:
        words = ["the", "one","a"]
    else:
        words = ["some", "many", "the"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

def get_noun(grammatical_number):
    """Return a randomly chosen noun.
    If grammatical_number == 1, this function will
    return one of these ten single nouns:
        "adult", "bird", "boy", "car", "cat",
        "child", "dog", "girl", "man", "woman"
    Otherwise, this function will return one of these
    ten plural nouns:
        "adults", "birds", "boys", "cars", "cats",
        "children", "dogs", "girls", "men", "women"

    Parameter
        grammatical_number: an integer that determines
            if the returned noun is single or plural.
    Return: a randomly chosen noun.
    """
    if grammatical_number ==1:
        nouns = ["adult","elephant", "ant","bird", "boy", "car", "cat",
        "child", "dog", "girl", "man", "woman"]
    else:
        nouns = [ "adults","elephants", "birds", "boys", "cars", "cats",
        "children", "dogs", "girls", "men", "women"]
    
    noun = random.choice(nouns)
    return noun


def get_verb(grammatical_number, tense):
    """Return a randomly chosen verb. If tense is "past", this
    function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and grammatical_number is 1, this
    function will return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and grammatical_number is NOT 1,
    this function will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of
    these ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"

    Parameter
        grammatical_number: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """
    if tense == "past":
        verbs = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    elif tense == "present" and grammatical_number ==1:
        verbs = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
    elif tense=="present" and grammatical_number != 1:
        verbs = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    elif tense =="future":
        verbs = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]

    verb = random.choice(verbs)

    return verb

def get_preposition():
    """Return a randomly chosen preposition
    from this list of prepositions:
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"

    Return: a randomly chosen preposition.
    """
    prepositions =["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]

    prep_word =random.choice(prepositions)
    return prep_word

def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed of three
    words: a preposition, a determiner, and a noun by calling the
    get_preposition, get_determiner, and get_noun functions.

    Parameter
        quantity: an integer that determines if the
            determiner and nouns are singular or plural.
    Return: a prepositional phrase.
    """



    noun = get_noun(quantity)
    preposition = get_preposition()
    determiner= get_determiner(quantity)

    prepostional_phrase = (f"{preposition} {determiner} {noun}")

    return prepostional_phrase


for _ in range(6):

    main()

#main function should not have any variables passed to it but this is for a test
# main(1,"past")
# main(2,"past")
# main(1,"present")
# main(2,"present")
# main(1,"future")
# main(2,"future")