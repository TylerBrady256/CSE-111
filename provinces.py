# with open("provinces.txt") as

def main():
    text_list = read_list("provinces.txt")

    print(text_list)

def read_list(filename):
    text_list=[]

    with open(filename, "rt") as text_file:

        
        

        alberta_count = 0 
        for lines in text_file:


            #makes sure the words do not have spaces attached to them.
            clean_line = lines.strip()

            #adds elements to the list
        

            #if the abreviation AB is found it replaces it with Alberta
            if clean_line.upper() == "AB":
                text_list.append("Alberta")
            else:
                text_list.append(clean_line)

            if clean_line.upper() == "ALBERTA":
                alberta_count +=1

    #removes the first and last elements in the list.
        text_list.pop(0)
        text_list.pop() 
        
    print(alberta_count)
    return text_list




if __name__ == "__main__":
    main()