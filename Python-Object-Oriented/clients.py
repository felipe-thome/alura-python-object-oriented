class Client:

    def __init__(self, name, surname):
        self._name = name
        self.surname = surname

    @property
    def name(self):
        return self._name.title()

    @name.setter
    def name(self, name):
        self._name = name
