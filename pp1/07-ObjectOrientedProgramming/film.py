class Film():
    
    cinema = "Multikino, Kraków"
    
    def __init__(self, title):
        self.title = title
    
    def __str__(self):
        return f"{self.title} ({Film.cinema})"
    
film1 = Film("The Shawshank Redemption")
print(film1)
film2 = Film("Pulp Fiction")
print(film2)

# zmiana nazwy kina (zmiana wartości zmiennej klasowej)
Film.cinema = "Kino Kijów, Kraków"
print(film1)
print(film2)

