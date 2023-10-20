












movies = [
{
"name": "Usual Suspects",
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]


#Write a function that takes a single movie and returns True if its IMDB score is above 5.5
def task1():
    for x in movies:
        if x["imdb"] >= 5.5:
            print(True)
        else:
            print(False)

#Write a function that returns a sublist of movies with an IMDB score above 5.5.
def task2():
    for x in movies:
        if x["imdb"] >= 5.5:
            print(x)
            print()

#Write a function that takes a category name and returns just those movies under that category.
def score(categ):
    for i in movies:
        if(i["category"] == categ):
            print(i)
            print()

categ = "Romance"
score(categ)

#Write a function that takes a list of movies and computes the average IMDB score.
def score(size):
    avg = 0
    for i in movies:
        avg = avg + i["imdb"]

    print(avg / size)


size = len(movies)
score(size)

#Write a function that takes a category and computes the average IMDB score.

def score(categ, size):
    avg = 0
    for i in movies:
        if (i["category"] == categ):
            avg = avg + i["imdb"]
    print(avg / size)


size = len(movies)
categ = 'Romance'
score(categ, size)