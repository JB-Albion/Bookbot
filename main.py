
def main():
    with open("Bookbot/books/frankenstein.txt") as f:
        text = f.read()
        num_words = num_of_words(text)
        print(f"There are {num_words} words in this text.")
        num_letters = num_of_letters(text)
        print(f"There are this amount of each letter; {num_letters} ")
        presentation(num_letters, num_words)


def num_of_words(text):
    words = text.split()
    return len(words)

def num_of_letters(text):
    my_dictionary = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}
    other_character_count = 0
    lowercase_text = text.lower()
    #print(my_dictionary)
    for letter in lowercase_text:
        if letter == ' ' or letter == "'" or letter == ',' or letter == '(' or letter == ')' or letter == '\n' or letter == '.' or letter == '-' or letter == ':' or letter == '1' or letter == '2' or letter == '3' or letter == '4' or letter == '5' or letter == '6' or letter == '7' or letter == '8' or letter == '9' or letter == '0' or letter == '[' or letter ==']' or letter == '#' or letter == '*' or letter == '?' or letter == ';' or letter == '!' or letter == '"' or letter == "_" or letter == '/' or letter == '%' or letter == '@' or letter == '$':
            other_character_count += 1
        #elif letter == "'":
        #    other_character_count += 1
        #elif letter == ',':
        #    other_character_count += 1
        #elif 
        else: 
            my_dictionary[letter] += 1
    #print(my_dictionary)
    return my_dictionary


def presentation(my_dictionary, num_of_letters):
    print("=========================================")
    print(f"There are {num_of_letters} words in this text.")
    print("\n")
    for letter in my_dictionary:
        print(f"The character {letter} occured {my_dictionary[letter]} times.")
    print("=========================================")










main()

