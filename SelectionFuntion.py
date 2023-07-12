# This is the most important function, because
# the ability to select or choose something for ourselves
# is what is called intelligence, the more effienct solution to the
# situetion, better the intelligence, but also,
# what is true intelligence?

from RelationValueManipulationFunctions import *

# This function below allows only two relations to be selected
def two_rel_func(relation):
    """I think we will only need two choices, because
    even when it will have to make various choices, we can compare two at a time
    Exemple: ordering number array in acending order
    so, whenever, there are multiple chioce compare one on one, last one standing is selected"""
    if(relation == "choice"):
        print("two_rel_func() running")
        relOne = input("Give me option one: ")
        relTwo = input("Give me option two: ")
        if(get_rel_value(relOne) > get_rel_value(relTwo)):
            print(f"I want { relOne }")
        if(get_rel_value(relOne) < get_rel_value(relTwo)):
            print(f"I want { relTwo }")
        if(get_rel_value(relOne) == get_rel_value(relTwo)):
            print("Is it possible to have to relations with exact same values?")
            print("Not in this small version, but humans are always making judgements")
            print("Can be based on anything, but let this == if statement be here")
            print("Because, one day... this might be become a reality")
            print("Only people with absolute and universally big reality will understand")
            print("what truly means to have something with same value")
            print("UPDATE: read Theory of cat and dog, to reconsider this")