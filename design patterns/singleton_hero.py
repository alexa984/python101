class Hero:
    _shared_state = {} #attribute dictionary
    _possible_attr = {'name', 'title', 'health', 'mana', 'mana_regeneration_rate'}
    def __init__(self):
        self.__dict__ = self._shared_state

    def known_as(self):
        return "{} the {}".format(self.name, self.title)

    def is_alive(self):
        if self.health > 0:
            return True
        return False

    def take_damage(self, dmg_points):
        self.health-=dmg_points
        if self.health < 0:
            self.health = 0

    def take_healing(self, healing_points):
        self.health+=healing_points
        if self.health > self.__max_health:
            self.health = self.__max_health


class SingletonHero(Hero):
    def __init__(self, **kwargs):
        Hero.__init__(self)
        for k, v in kwargs.items():
            self.__dict__[k] = v

        #only want to manage objects with all the required attributes and no others
        if  all(el in self.__dict__ for el in self._possible_attr) and all(el in self._possible_attr for el in self.__dict__):
            self._shared_state.update(self.__dict__)
        else:
            raise TypeError

    def __str__(self):
        return str(self._shared_state)

