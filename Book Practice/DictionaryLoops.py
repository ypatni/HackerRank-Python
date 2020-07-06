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
users = { 'aeinstein': {
'first': 'albert',
'last': 'einstein', 'location': 'princeton', },
'mcurie': {
'first': 'marie', 'last': 'curie', 'location': 'paris', },
}
for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}" 
    location = user_info['location']
    print(f"\tFull name: {full_name.title()}") 
    print(f"\tLocation: {location.title()}")

#3
favorite_cities = {
    'evan' : ['london' , 'new york city'],
    'yash' : ['mumbai', 'philly']
}
for name in favorite_cities.keys():
    print(f"{name.title()}'s favorite cities are: ")
    for cities in favorite_cities[name]:
        print("\t" + cities.title())
