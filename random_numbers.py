import random

def main():
    randnum = [16.2, 75.1, 52.3]
    randword = ["burrito", "slime","belt"]
    print(randnum)
    append_random_number(randnum,)
    append_random_word(randword,)
    print(randword)
    print(randnum)
    append_random_number(randnum,2)
    append_random_word(randword,2)
    print(randword)
    print(randnum)

def append_random_number(numbers_list, quantity = 1):
    while quantity > 0:
        random_int = round(random.uniform(0,500),1)
        numbers_list.append(random_int)

        quantity-=1

def append_random_word(rand_word_list,quantity=1):
    rand_words = ["dog","yo","hi"]
    while quantity > 0:
        rand_word_list.append(random.choice(rand_words))

        quantity -=1
    

        

if __name__ == "__main__":
    main()