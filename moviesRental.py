from faker import Faker
from numpy import size
from pandas import Series
from numpy import random

class Item:

    play_count = 0

    def __init__(self, name, year_of_publication, genre, play_count):
        self.name = name
        self.year_of_publication = year_of_publication
        self.genre = genre
        self.play_count = play_count

        
    def __str__(self):
        return f'{self.name} {self.year_of_publication} {self.genre} '

    def play(self):
        play_count = play_count + 1
        print("Liczba odtworzen" + play_count)

    def getPlay():
        print("Liczba odtworzen" + play_count)
        return self.play_count

    def getName(self):
        return self.name

class Movie(Item):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
       

    def __str__(self):
        return f'{self.name} ({self.year_of_publication}) '   

    def contact(self):
         print(" Wybieram numer ",self.businessPhone ," i dzwonie do ", self.firstName, " ", self.lastName)     

class Serie(Item):

    def __init__(self, episode, season, *args, **kwargs):
        super().__init__(*args, **kwargs)   
        self.episode = episode
        self.season = season      
    
    def __str__(self):
        return f'{self.name} S{self.season}E{self.episode} '      


    
pulpFiction = Movie('Pulp Fiction', 1999,'Dramat',0)
print(pulpFiction)

desperados = Movie('Desperados', 1992,'Kryminal',0)
print(desperados)

friends = Serie(0,1,'Friends', 1999,'Komedia',0)
print(friends)

twoAndHalf = Serie(1,2,'TwoAndHalf', 2010,'Komedia',0)
print(twoAndHalf)

gameOfThrone = Serie(1,2,'Game Of Thorne', 2020,'Thriller',0)
print(gameOfThrone)

allItems = [pulpFiction,desperados, friends, twoAndHalf, gameOfThrone]


def  getSeries():
    print("\ngetSeries\n")
    series = [print(i) for i in allItems if isinstance(i,Serie)]
    print("\n")
    return series

def getMovies():
    print("\ngetMovies\n")
    movies = [print(i) for i in allItems if isinstance(i, Movie)] 
    print("\n")   
    return movies  

serieList = getSeries()
movieList = getMovies()

       

def search(name):
    k=0
    for i in allItems:
        if allItems[k].getName()==name:
            break
        searchedElement = f'Item {name} has a index {k}'
        k=k+1    
    print(searchedElement)

search("Two And Half")

def play(self, count):
    self.play_count = self.play_count + count
    print(f"Liczba wywietlen dla wylosowanego elementu wynosi {self.play_count}")   

def generate_views():
    randomViewNumber = random.randint(1,100,size=1)[0]
    print(f"Liczba wywietlen wynosi {randomViewNumber}") 
    randomIndex = random.randint(0,len(allItems)-1,size=1)[0]
    print(f"Wylosowany indeks elementu wynosi {randomIndex}") 
    selectedItem = allItems[randomIndex]
    play(selectedItem,randomViewNumber)

def generateMassiveViews():
    for i in range (0,10):
        generate_views()

generateMassiveViews()

def myFunc(item):
    return Item.getPlay(item)


def topTitles(topNumbers):
    topTitles = sorted(allItems, key=lambda item: item.play_count)
    k=0
    for i in topTitles[-topNumbers:]:
        rank=topNumbers-k
        print(f"Na pozycji {rank} plasuje sie {i.getName()} z  liczba wyswietlen {i.play_count}") 
        k=k+1

topTitles(5)

