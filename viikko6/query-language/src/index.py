from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, Or, HasAtLeast, PlaysIn, All, HasFewerThan, Not
from querybuilder import *

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    matcher = And(
        HasAtLeast(5, "goals"),
        HasAtLeast(5, "assists"),
        PlaysIn("PHI")
    )

    for player in stats.matches(matcher):
        print(player)

    matcher = All()
    
    print("-----------")
    matcher = Or(
        HasAtLeast(30, "goals"),
        HasAtLeast(50, "assists")
    )
    print("******************")
    query = QueryBuilder()
    matcher = (
      query  
        .playsIn("NYR")  
        .hasAtLeast(5, "goals")  
        .hasFewerThan(10, "goals")  
        .build()
    )

    #matcher = query.build()
    '''
    m1 = (
        query
        .playsIn("PHI")
        .hasAtLeast(10, "assists")
        .hasFewerThan(5, "goals")
        .build()
    )

    m2 = (
        query
        .playsIn("EDM")
        .hasAtLeast(40, "points")
        .build()
    )
    '''
    matcher = (
        query
        .oneOf(
            query.playsIn("PHI")
            .hasAtLeast(10, "assists")
            .hasFewerThan(5, "goals")
            .build(),
        query.playsIn("EDM")
            .hasAtLeast(40, "points")
            .build(),
        query.hasAtLeast(45, "assists")
            .playsIn("TOR")
            .build()
            
        )
        .build()
    )

    #matcher = query.oneOf(m1, m2).build()
    matcher = All()
    
    for player in stats.matches(matcher):
        print(player)
    

if __name__ == "__main__":
    main()
