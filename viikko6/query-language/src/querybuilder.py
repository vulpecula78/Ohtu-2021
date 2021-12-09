from matchers import *

class QueryBuilder:
    def __init__(self, query = All()):
        self.query_obj = query
        
    def playsIn(self, team):
        return QueryBuilder(And(self.query_obj, PlaysIn(team)))
    
    def hasAtLeast(self, value, param):
        return QueryBuilder(And(self.query_obj, HasAtLeast(value, param)))
    
    def hasFewerThan(self, value, param):
        return QueryBuilder(And(self.query_obj, HasFewerThan(value, param)))
    
    def oneOf(self, *queries):
        return QueryBuilder(Or(*queries))
    
    def build(self):
        return self.query_obj
