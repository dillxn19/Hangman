import random
superheroes = ["batman", "superman", "ironman", "spiderman", "captainamerica", "hulk", "hawkeye", "blackpanther"]
fruits = ["apple", "banana", "raspberry", "blueberries", "blackberry", "mango", "dragonfruit", "kiwi"]
places = ["paris", "tokyo", "newyork", "venice", "egypt", "malaysia", "india", "china"]
movies = ["toystory", "cars", "insideout", "minions", "despicableme", "kungfupanda", "findingnemo", "coco"]
themes = [superheroes, fruits, places, movies]
theme = input("What theme would you like to pick. Options: Superheros, Fruits, Places, Movies: ")
themeindex = 0
if theme == "superheroes":
    themeindex = 0
elif theme == "fruits":
    themeindex = 1
elif theme == "places":
    themeindex = 2
elif theme == "movies":
    themeindex = 3
word = random.choice(themes[themeindex])
chances = len(word)
print()
wordlist = []
for n in word:
    wordlist.append("_")
for a in wordlist:
    print(a, end = " ")
while "_" in wordlist:
    letter = input("What letter would you like to try: ")
    flag = False
    for n in range(0, len(word), 1):
        if word[n] == letter:
            wordlist[n] = letter
            flag = True                                                                                                     
    if flag == False:
        chances -=  1
    for a in wordlist:
        print(a, end = " ")
    print("   Lives:", chances)
    if chances == 0:
        break
if chances == 0:
    print("Game Over, your word was", word)
else:
    print("Congrats! You win")