import random as rand
import tkinter as tk


class GUI:

    def __init__(self) -> None:
        self.runtime = self.Runtime()
        self.main()

    def main(self):
        self.runtime.main_menu_frame()
        self.runtime.root.mainloop()

    class Runtime:

        def __init__(self) -> None:
            self.width = 1000
            self.height = 300
            self.game: Match | None = None
            self.root = tk.Tk()
            self.root.title("Cricket Saga")
            self.root.geometry(str(self.width) + "x" + str(self.height))

        def main_menu_frame(self):
            frame = tk.Frame(self.root)
            super_heading = tk.Label(
                frame,
                text="Welcome To",
                font=("Times New Roman", 15)
            )
            heading = tk.Label(
                frame,
                text="Ultimate Cricket Saga",
                font=("Cursive", 25)
            )
            super_heading.pack()
            heading.pack()

            def onclick():
                frame.destroy()
                self.team_selection_frame()

            start_btn = tk.Button(frame, text="Start", command=onclick)
            start_btn.pack()
            frame.pack()

        def team_selection_frame(self):
            frame = tk.Frame(self.root)
            label = tk.Label(frame, text="Select two team for the match")
            country1_entry = tk.Entry(frame)
            country2_entry = tk.Entry(frame)

            def onclick():
                country1 = country1_entry.get()
                country2 = country2_entry.get()
                self.game = Match(country1, country2)
                frame.destroy()
                self.player_selection_frame()

            submit_btn = tk.Button(
                frame,
                text="Submit and Next",
                command=onclick
            )

            label.pack()
            country1_entry.pack()
            country2_entry.pack()
            submit_btn.pack()
            frame.pack()

        def player_selection_frame(self):
            frame = tk.Frame(self.root)
            player_entries_team1 = []
            player_entries_team2 = []

            label1 = tk.Label(
                frame,
                text="Enter the names off team 1 players"
            )
            label1.pack()

            for i in range(0, 11):
                player_entries_team1.append(tk.Entry(frame))
                player_entries_team1[i].pack()

            label2 = tk.Label(
                frame,
                text="Enter the names off team 2 players"
            )
            label2.pack()

            for i in range(0, 11):
                player_entries_team2.append(tk.Entry(frame))
                player_entries_team2[i].pack()

            def onclick():
                if self.game is not None:
                    for i in range(0, 11):
                        self.game.team1.players.append(
                            Team.Player(player_entries_team1[i].get())
                        )

                    for i in range(0, 11):
                        self.game.team2.players.append(
                            Team.Player(player_entries_team2[i].get())
                        )

                    frame.destroy()
                    self.game_loop_frame()

            submit = tk.Button(
                frame,
                text="Submit and Next",
                command=onclick
            )
            submit.pack()
            frame.pack()

        def game_loop_frame(self):

            frame = tk.Frame(self.root)
            score_label = tk.Label(frame, text="")
            event_label = tk.Label(frame, text="")

            score_label.pack()
            event_label.pack()

            def play_next(team, player_index):

                def onclick():
                    frame.destroy()
                    self.scorecard_frame()

                if self.game is not None:

                    result = self.game.play_ball(team, player_index)

                    event_label.config(text=result["event"])

                    score_label.config(
                        text=f"{self.game.team1.country}: {self.game.team1.score}  |  "
                             f"{self.game.team2.country}: {self.game.team2.score}"
                    )

                    if result["out"]:

                        if player_index + 1 < len(team.players):
                            frame.after(
                                500,
                                lambda: play_next(team, player_index + 1)
                            )

                        else:

                            if team == self.game.team1:
                                frame.after(
                                    500,
                                    lambda: play_next(self.game.team2, 0)
                                )

                            else:
                                continue_btn = tk.Button(
                                    frame,
                                    text="Continue to final scorecard?",
                                    command=onclick
                                )
                                continue_btn.pack()

                    else:
                        frame.after(
                            500,
                            lambda: play_next(team, player_index)
                        )

            frame.pack()

            if self.game is not None:
                play_next(self.game.team1, 0)

        def scorecard_frame(self):

            if self.game is not None:

                frame = tk.Frame(self.root)

                heading = tk.Label(
                    frame,
                    text="Final Scorecard",
                    font=("Times New Roman", 20)
                )
                heading.pack(pady=10)

                # *Team 1*

                team1_heading = tk.Label(
                    frame,
                    text=f"{self.game.team1.country}: {self.game.team1.score}",
                    font=("Times New Roman", 15)
                )
                team1_heading.pack()

                for player in self.game.team1.players:
                    player_label = tk.Label(
                        frame,
                        text=f"{player.name}: {player.score}"
                    )
                    player_label.pack()

                # *Team 2*

                team2_heading = tk.Label(
                    frame,
                    text=f"{self.game.team2.country}: {self.game.team2.score}",
                    font=("Times New Roman", 15)
                )
                team2_heading.pack(pady=10)

                for player in self.game.team2.players:
                    player_label = tk.Label(
                        frame,
                        text=f"{player.name}: {player.score}"
                    )
                    player_label.pack()

                # *Result*

                if self.game.team1.score > self.game.team2.score:
                    result = f"{self.game.team1.country} wins!"

                elif self.game.team2.score > self.game.team1.score:
                    result = f"{self.game.team2.country} wins!"

                else:
                    result = "It's a draw!"

                result_label = tk.Label(
                    frame,
                    text=result,
                    font=("Times New Roman", 18)
                )
                result_label.pack(pady=15)

                frame.pack()


class Team:

    def __init__(self, country: str):
        self.score = 0
        self.country = country
        self.players = []

    class Player:

        def __init__(self, name):
            self.name = name
            self.score = 0


class Match:

    def __init__(self, country1: str, country2: str):
        self.team1 = Team(country1)
        self.team2 = Team(country2)

    def play_ball(self, team, player_index):

        player = team.players[player_index]

        if rand.randint(1, 25) == 1:

            return {
                "out": True,
                "event": f"{player.name} is OUT!"
            }

        score = rand.choice(
            [0, 1, 1, 1, 2, 2, 2, 2, 3, 4, 4, 6]
        )

        player.score += score
        team.score += score

        return {
            "out": False,
            "event": f"{player.name} scored {score}!"
        }


if __name__ == "__main__":
    instance = GUI()
