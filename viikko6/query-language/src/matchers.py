class And:
    def __init__(self, *matchers):
        self._matchers = matchers
    
    def matches(self, player):
        for matcher in self._matchers:
            if not matcher.matches(player):
                return False
        
        return True
    
class All:
    def matches(self, player):
        return True

class Not:
    def __init__(self, metodi):
        self._metodi = metodi
        self._metodi
        
    def matches(self, player):
        return not self._metodi.matches(player)
    
class Or:
    def __init__(self, *matchers):
        self._matchers = matchers
        
    def matches(self, player):
        for matcher in self._matchers:
            if matcher.matches(player):
                return True
        return False
    
class PlaysIn:
    def __init__(self, team):
        self._team = team

    def matches(self, player):
        return player.team == self._team

class HasAtLeast:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def matches(self, player):
        player_value = getattr(player, self._attr)

        return player_value >= self._value
    
class HasFewerThan:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr
        
    def matches(self, player):
        player_value = getattr(player, self._attr)
        return player_value < self._value

