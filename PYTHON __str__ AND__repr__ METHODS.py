#These codes give an idea on __str__ and __repr__ methods respectively
#BY: SHARMILA.V

#This __str__ method directly calls the object data and accepts only string formats
print("Government Library")
class Library:
    def __init__(self,name,author,genere):
        self.name = name
        self.author = author
        self.genere = genere
        
    def __str__(self):
        book = f"Name of the book:{self.name}\nAuthor:{self.author}\
        \nGenere:{self.genere}"
        return book
b = Library("ps","Kalki","Historical Novel")
print(b)


#This __repr__ method gives the data in the object in the form of list
print("Government Library")
class Library:
    retdt = 30
    def __init__(self,name,author,genere):
        self.name = name
        self.author = author
        self.genere = genere
        
    def __repr__(self):
        book = f"Library(Name of the book:{self.name}\nAuthor:{self.author}\
        \nGenere:{self.genere})"
        return book
b = Library("ps","Kalki","Historical Novel")
print([b])