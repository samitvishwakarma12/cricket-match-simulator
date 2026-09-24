import random as rand;

class Team():

    def __init__(self, country: str):
        self.score = 0;
        self.country = country;
        self.players = [];
        self.create_team();

    class Player:

        def __init__(self):
            self.name = None;
            self.score = 0;

    def create_team(self):
        for i in range(11):
            self.players.append(self.Player());
            self.players[i].name = input("Enter Player name:");



class Match:

    def __init__(self, country1: str, country2: str):
        self.team1 = Team(country1);
        self.team2 = Team(country2);
    
        
    def play_inning(self, team):

        for i in range(len(team.players)):
            if rand.randint(1,15) == 1:
                print(f"The player {team.players[i]} is out.");
                continue;

            else:
                score = rand.randint(1,7);
                team.players[i].score += score;
                team.score += score;
                print(f"{team.players[i].name} has scored a {score}!");



    def display_result(self):

        if self.team1.score > self.team2.score:
            print(f"{self.team1.country} has won the match!");

        elif self.team1.score == self.team2.score:
            print(f"It's a miraculous tie between {self.team1.country} and {self.team2.country}");

        else:
            print(f"{self.team2.country} has won the match!");



    def generate_scorecard(self, team):

        print(f"{team.country.captalize()}'S SCORECARD");
        print("------------------------------------------");

        for player in team.players:
            print(f"{player.name}:\t{player.score}");

        print("------------------------------------------");
        print(f"Final Score:{team.score}");
        print("------------------------------------------");



    def main(self):
        self.play_inning(self.team1);
        self.play_inning(self.team2);
        self.display_result();

        if input("Enter 'y' to view the scorecard, enter any other key to continue.\n").capitalize() == 'Y':
            self.generate_scorecard(self.team1);
            self.generate_scorecard(self.team2);
        else:
            print("You opted out.");

        print("The game ends, thanks for watching.");

    

if __name__ == "__main__":

    game = Match("India", "Pakistan");
    game.main();
