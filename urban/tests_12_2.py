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

    def __repr__(self):
        return self.__str__()

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

    @classmethod
    def tearDownClass(cls):
        for res in cls.all_results.values():
            print(res)

    def setUp(self):
        self.distance = 90
        self.participants = {
            "Усэйн": Runner("Усэйн", 10),
            "Андрей": Runner("Андрей", 9),
            "Ник": Runner("Ник", 3)
        }

    def test_speed(self):
        max_speed = max([part.speed for part in self.participants.values()])
        TournamentTest.all_results["Тест_0"] = {"dictance": self.distance, "max_speed": max_speed}
        self.assertTrue(max_speed < self.distance, "Дистанция меньше, чем скорость самого быстрого участника. "
                                                   "Результаты могугут быть неверными")

    def test_tournament_1(self):
        p = self.participants
        tournament = Tournament(self.distance, p["Усэйн"], p["Ник"])
        result = tournament.start()
        TournamentTest.all_results["Тест_1"] = result
        self.assertTrue(result[2] == "Ник")

    def test_tournament_2(self):
        p = self.participants
        tournament = Tournament(self.distance, p["Андрей"], p["Ник"])
        result = tournament.start()
        TournamentTest.all_results["Тест_2"] = result
        self.assertTrue(result[2] == "Ник")

    def test_tournament_3(self):
        p = self.participants
        tournament = Tournament(self.distance, *self.participants.values())
        result = tournament.start()
        TournamentTest.all_results["Тест_3"] = result
        self.assertTrue(result[3] == "Ник")


if __name__ == "__main__":
    unittest.main()
