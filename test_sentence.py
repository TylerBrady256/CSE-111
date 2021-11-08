from sentence import get_determiner, get_noun, get_verb, get_preposition, get_prepositional_phrase, a_to_an_conversion
import pytest

# def test_a_to_an_conversion():
    
#     determiner = "a"
#     vowels =["a","e","i","o","u","y"]
#     possible_outcomes = ["a","an"]

#     for _ in range (20):
#         noun = get_noun()
#         if determiner == "a" and noun[0] in vowels:
#                 determiner = "an"
        
        

#         assert determiner in possible_outcomes

     
    

def test_get_determiner():
    # 1. Test the single determiners.

    single_determiners = ["the", "one","a"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):
        word = get_determiner(1)

        # Verify that the word returned from get_determiner is
        # one of the words in the single_determiners list.
        assert word in single_determiners

    # 2. Test the plural determiners.

    plural_determiners = ["some", "many","the"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):
        word = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners

def test_get_noun():

    possible_single_nouns = ["adult","elephant","ant", "bird", "boy", "car", "cat",
        "child", "dog", "girl", "man", "woman"]

    for _ in range(20):
        noun = get_noun(1)

        assert noun in possible_single_nouns

    possible_plural_nouns = ["adults","elephants","birds", "boys", "cars", "cats",
        "children", "dogs", "girls", "men", "women"]
    
    for _ in range(20):
        noun = get_noun(2)

        assert noun in possible_plural_nouns

def test_get_verb():

    past_verbs =["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    for _ in range(20):
        verb = get_verb(1,"past")
        assert verb in past_verbs
        verb = get_verb(2,"past")
        assert verb in past_verbs
    present_single_verbs = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
    for _ in range(20):
        verb = get_verb(1,"present")
        assert verb in present_single_verbs
        
    present_plural_verbs =["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    for _ in range(20):
        verb = get_verb(2,"present")
        assert verb in present_plural_verbs
        
    future_verbs = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]
    for _ in range(20):
        verb = get_verb(1,"future")
        assert verb in future_verbs
        verb = get_verb(2,"future")
        assert verb in future_verbs

def test_get_prepositional():
    prepositional_words = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]

    for _ in range(20):
        preposition = get_preposition()
        assert preposition in prepositional_words

def test_get_prepositional_phrase():
    
    possible_nouns_singular = ["adult","elephant","ant", "bird", "boy", "car", "cat",
        "child", "dog", "girl", "man", "woman"]
    
    possible_nouns_plural =["adults","elephants", "birds", "boys", "cars", "cats",
        "children", "dogs", "girls", "men", "women"]

    possible_determiners_singular = ["the", "one","a"]

    possible_determiners_plural = ["some","many","the"]

    possible_prepositions = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]


    for _ in range(20):
        phrase = get_prepositional_phrase(1)
        split_phrase = phrase.split(" ")

        prepostion = split_phrase[0]
        determiner = split_phrase[1]
        noun = split_phrase[2]

        assert noun in possible_nouns_singular
        assert determiner in possible_determiners_singular
        assert prepostion in possible_prepositions

    for _ in range(20):
        phrase = get_prepositional_phrase(2)
        split_phrase = phrase.split(" ")

        prepostion = split_phrase[0]
        determiner = split_phrase[1]
        noun = split_phrase[2]

        assert noun in possible_nouns_plural
        assert determiner in possible_determiners_plural
        assert prepostion in possible_prepositions
    





    
        
pytest.main(["-v", "--tb=line", "-rN", "test_sentence.py"])