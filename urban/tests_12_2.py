import unittest

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.participants = (
            Runner("Усэйн", 10),
            Runner("Андрей", 9),
            Runner("Ник", 3)
        )

    @classmethod
    def tearDownClass(cls):
        for participant, place in cls.all_results.items():
            print(participant, place, sep='\t')

    def test_tournament_1(self):
        tournament = Tournament(90, self.participants[0], self.participants[2])
        TournamentTest.all_results = tournament.start()
        self.assertTrue(TournamentTest.all_results[2] == "Ник")

    def test_tournament_2(self):
        tournament = Tournament(90, self.participants[1], self.participants[2])
        TournamentTest.all_results = tournament.start()
        self.assertTrue(TournamentTest.all_results[2] == "Ник")

    def test_tournament_3(self):
        tournament = Tournament(90, *self.participants)
        TournamentTest.all_results = tournament.start()
        self.assertTrue(TournamentTest.all_results[3] == "Ник")


if __name__ == "__main__":
    unittest.main()
