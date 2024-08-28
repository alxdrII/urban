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
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.participants = [
            Runner("Усэйн", 10),
            Runner("Андрей", 9),
            Runner("Ник", 3)
        ]

    def tearDownClass(cls):
        print("participant", "place", sep='\t')
        for participant, place in cls.all_results.items():
            print(participant, place, sep='\t')

    def test_tournament(self):
        tournament = Tournament(90, *self.participants)
        self.all_results = tournament.start()

        self.assertTrue(self.all_results(self.participants[2]) == "Ник")

if __name__ == "__main__":
    unittest.main()