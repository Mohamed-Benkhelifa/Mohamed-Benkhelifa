#The purpose of this program is to give the user 1 of 3 options every time the code is run to either find the definetion of a word, add a word to the dictionary, or remove a word
#The input from the user
#The result of the users choice, whether a definetion,adding, or removing a word from the dictionary

'''Welcome to my dictionary, what can I do for you?
1. Search for a word
2. Add a new word
3. Remove a word'''


import unittest 


# your code here

def printdict():
    print("Here is the current dictionary:")
    result = '\n'.join(f'{word}: {definition}' for word, definition  in dictionary.items())
    print(result)

print("""Welcome to My Dictionary! What can I do for you?
1. Search for a word
2. Add a new word
3. Remove a word""")

dictionary = {
"Variable": "a quantity or function that may assume any given value or set of values.", 
"Array": "an arrangement of a series of terms according to value, as from largest to smallest.",
"Function": "a set of ordered pairs in which none of the first elements of the pairs appears twice.",
}
printdict()
option = input("Please type your choice number: ")

match option:
    case '1':
        word = input("Enter a word you want to look up: ")
        try:
            print('{}: {}'.format(word, dictionary[word]))
        except KeyError:
            print("uh typo? I don’t have this word in my database")
    case '2':
        word = input("Enter a word that you want to add: ")
        definition = input("Please add a definition for it: ")
        dictionary[word] = definition
        printdict()
    case '3':
        print("Removing a word")
        try:
            word = input("Enter the word you want to remove: ")
            del dictionary[word]
            printdict()
        except KeyError:
            print("uh typo? I don’t have this word in my database")

    case other:
        print("Invalid Option, try again")

#Code for searching for a word that's already in the dictionary
def lookup_word(dictionary, wordLook):
    if wordLook in dictionary:
        print(f"{wordLook} : {dictionary[wordLook]}\n")
        print("Thanks for using MyDictionary")
        return(f'{dictionary[wordLook]}')
    if wordLook not in dictionary:
        print("uh typo? I don't have this word in my database")
        return "N/A"
    print("           ...")

#Code to add a word that isn't already in dictionary and has message if word is already defined
def add_word_to_dict(dictionary, addWord, definition):
    print("Here are all the words I have\n")
    if addWord in dictionary:
      newWord = addWord +'(2)'
      dictionary[newWord] = definition
      return dictionary
    else:
      dictionary[addWord] = definition
      return dictionary

#Code for deleting a word
def delete_in_dict(dictionary, wordDel):
    if wordDel in dictionary:
        del dictionary[wordDel]
        print("Here are the words I have: \n")
        for key, value in dictionary.items():
            print(f"{key} : {value}\n")
        return dictionary
    else:
        print("uh typo? I don't habe this word in my database\n")
        return dictionary
    print("             ...")

#Main function for the cases
def main():
  my_dict = {
    "Variable":
    "a quantity or function that may assume any given value or set of values.",
    "Array":
    "an arrangement of a series of terms according to value, as from largest to smallest.",
    "Function":
    "a set of ordered pairs in which none of the first elements of the pairs appears twice."
  }
  print("  ***   Dictionary   ***\n" )
  print("Welcome to My Dictionary, What can I do for you?\n")
  print("1. Search for a word")
  print("2. Add a new word")
  print("3. Remove a word\n")

  choice = int(input("Please type your option: "))
  #checks whether choice was within 1-3 and if it isn't it restarts
  if choice < 1 or choice > 3:
      choice = int(input("Your choice must be 1, 2, or 3. Type your choice again: "))
  #the result for choice 1
  if choice == 1:
      wordLook = str(input("Type the word you're looking for: "))
      lookup_word(my_dict, wordLook)
  #the result for choice 2
  elif choice == 2:
      wordAdd = str(input("Type the word you want to add: "))
      definition = str(input("define the word: "))
      for key, value in add_word_to_dict(my_dict, wordAdd, definition).items():
        print('{} : {}'.format(key,value))
  #The result for choice 3
  elif choice == 3:
      wordDel = str(input("What word do you want to delete: "))
      delete_in_dict(my_dict, wordDel)

# Testing code
class TestDictFunctions(unittest.TestCase):

  def test_search_word_success(self):
    test_dict = {
      "Variable":
      "a quantity or function that may assume any given value or set of values."
    }
    actual = test_dict["Variable"]
    expected = lookup_word(test_dict, "Variable")
    self.assertEqual(actual, expected)

  def test_search_word_no_result(self):
    test_dict = {
      "Variable":
      "a quantity or function that may assume any given value or set of values."
    }
    actual = "N/A"
    expected = lookup_word(test_dict, "Array")
    self.assertEqual(actual, expected)

  def test_add_word_sucess(self):
    test_dict = {
      "Variable":
      "a quantity or function that may assume any given value or set of values."
    }
    actual = {
      "Variable":
      "a quantity or function that may assume any given value or set of values.",
      "Array":
      "an arrangement of a series of terms according to value, as from largest to smallest.",
    }
    expected = add_word_to_dict(
      test_dict, "Array",
      "an arrangement of a series of terms according to value, as from largest to smallest."
    )

    self.assertEqual(actual, expected)

  def test_add_word_duplicate(self):
    test_dict = {
      "Variable":
      "a quantity or function that may assume any given value or set of values."
    }
    actual = {
      "Variable":
      "a quantity or function that may assume any given value or set of values.",
      "Variable(2)": "temporary value assignment"
    }
    expected = add_word_to_dict(test_dict, "Variable",
                                "temporary value assignment")
    self.assertEqual(actual, expected)

  def test_delete_word_sucess(self):
    test_dict = {
      "Variable":
      "a quantity or function that may assume any given value or set of values."
    }
    expected = {}
    actual = delete_in_dict(test_dict, "Variable")
    self.assertEqual(actual, expected)

  def test_delete_word_no_result(self):
    test_dict = {
      "Variable":
      "a quantity or function that may assume any given value or set of values."
    }
    expected = test_dict
    actual = delete_in_dict(test_dict, "Array")
    self.assertEqual(actual, expected)


#uncomment to run tests
#unittest.main()

main()
