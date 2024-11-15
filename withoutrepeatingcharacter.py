# print string without taking repeating characters. eg helper - helpr

def character_without_repeating(string):
    seen = set()
    res = []
    for char in string :
       if char not in seen :
          seen.add(char)
          res.append(char)
    return "".join(res)

string = input().lower()                                          #TC = O(n)
print(character_without_repeating(string))                        #SC = O(n)





