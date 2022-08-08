from data import story
print(f'total char in nstory :{len(story)}')
a_count = story.count('a')
print(f'a occurs {a_count} times.')
the_count = story.lower().count('the')
print(f'a occurs {the_count} times.')
#replace
ustory = story.replace('of','on')
print(ustory)

#removing
ustory = story.replace('of','')
print (ustory)

#remove vowels
no_vowels_story = story.replace('a','').replace('e','').replace('i','').replace('o','').replace('u','')
print(no_vowels_story)

#retaining all vowels
only_vowel_story = ''
for char in story:
    if char in 'aeiouAEIOU':
        only_vowel_story +=char
print(only_vowel_story)


