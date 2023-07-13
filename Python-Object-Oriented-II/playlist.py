# Programs
class Program:
    def __init__(self, name, year):
        self._name = name.title()
        self.year = year
        self._likes = 0

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name.title()

    @property
    def likes(self):
        return self._likes

    def like_it(self):
        self._likes += 1

    # textual representation
    def __str__(self):
        return f'{self.name}, {self.year} : {self.likes} likes'


class Movie(Program):
    def __init__(self, name, year, duration):
        super().__init__(name, year)
        self.duration = duration

    def __str__(self):
        return f'{self.name}, {self.year} - {self.duration} min : {self.likes} likes'


class Series(Program):
    def __init__(self, name, year, seasons):
        super().__init__(name, year)
        self.seasons = seasons

    def __str__(self):
        return f'{self.name}, {self.year} - {self.seasons} temporadas : {self.likes} likes'


# Playlist
class Playlist:
    def __init__(self, name, programs):
        self.name = name
        self._programs = programs

    def __getitem__(self, item):
        return self._programs[item]

    def __len__(self):
        return len(self._programs)

    def __add__(self, other):
        self._programs.append(other)

    def __sub__(self, other):
        self._programs.remove(other)


vingadores = Movie('vingadores', 2018, 160)
atlanta = Series('atlanta ', 2018, 3)
tmep = Movie('todo mundo em pãnico', 1999, 100)
demolidor = Series('demolidor', 2016, 2)
avatar2 = Movie('Avatar 2', 2022, 120)

vingadores.like_it()
atlanta.like_it()
atlanta.like_it()
tmep.like_it()
tmep.like_it()
tmep.like_it()
tmep.like_it()
tmep.like_it()
demolidor.like_it()
demolidor.like_it()
demolidor.like_it()

movies_and_series = [vingadores, atlanta, demolidor, tmep]
weekend_playlist = Playlist('Weekend', movies_and_series)

weekend_playlist + avatar2
weekend_playlist - demolidor

print(f'Tamanho da playlist: {len(weekend_playlist)} programas')

for program in weekend_playlist:
    print(program)
