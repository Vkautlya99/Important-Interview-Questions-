# Reverse Words in a StringYou are given a string of length N. You need to reverse the string word by word. There can be multiple spaces between two words and there can be leading or trailing spaces but in the output reversed string you need to put a single space between two words


def Reverse_Words_Of_A_String(string):
    words = string.strip().split()
    reverse_words = words[::-1]
    reversed_str = " ".join(reverse_words)
    return reversed_str

string = "  vikram  kautlya  "                            #TC :- O(n)
print(Reverse_Words_Of_A_String(string))                  #SC :- O(n)





