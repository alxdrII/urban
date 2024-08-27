from unittest import TestCase, main


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(TestCase):
    def test_walk(self):
        runner = Runner("test_walk")
        for i in range(10): runner.walk()
        self.assertEqual(runner.distance, 50, "Test of the 'walk()' method")

    def test_run(self):
        runner = Runner("test_run")
        for i in range(10): runner.run()
        self.assertEqual(runner.distance, 100, "Test of the 'run()' method")

    def test_challenge(self):
        runner1 = Runner("test_challenge 1")
        runner2 = Runner("test_challenge 2")
        for i in range(10):
            runner1.walk()
            runner2.run()

        self.assertNotEqual(runner1.distance, runner2.distance)


if __name__ == "__main__":
    main()