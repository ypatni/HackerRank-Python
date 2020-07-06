favorite_languages = { 'jen': 'python',
'sarah': 'c', 'edward': 'ruby', 'phil': 'python', }
people = ['ryan', 'evan', 'scott','phil','jen']
language = favorite_languages['sarah'].title()

#1
for i in people:
    if i in sorted(favorite_languages.keys()):
        print(f"Thank you for taking the poll {i.title()}")
    else:
        print(f"Please take the poll {i.title()}")

#2

