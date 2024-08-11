superHeroes={
    'Tony Stark': 'IronMan',
    'Peter Parker': 'SpiderMan'
}

print(superHeroes['Tony Stark'])

superHeroes['Bruce Wayne']='Batman'

print(superHeroes['Bruce Wayne'])


# This line doesn't error out if dictionary item doesn't exist. 
superman = superHeroes.get("Clark Kent")

print(superman)  # None

if superman:
    print('This superhero exists')
else: 
    print("this superhero doesn't exist")