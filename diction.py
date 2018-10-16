
words = ["CAR", "CAT", "DOG", "SNOW", "SNOWBALL"]

# def get_stems(word):
#     stems = []
#     for i in range(1, len(word)):
#         stems.append(word[:i])
#     return stems
    
def get_stems(word):
    return [word[:i] for i in range(1, len(word))]





print(get_stems(words))
    
    
