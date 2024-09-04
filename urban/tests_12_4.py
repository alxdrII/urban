import logging
import unittest
from runner_and_tournament import Runner


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        try:
            runner = Runner("test_walk", -5)
            for i in range(10): runner.walk()
            self.assertEqual(runner.distance, 50, "Test of the 'walk()' method")
            logging.info('"test_walk" выполнен успешно')

        except ValueError:
            logging.warning("Неверная скорость для Runner")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        try:
            runner = Runner("test_run")
            for i in range(10): runner.run()
            self.assertEqual(runner.distance, 100, "Test of the 'run()' method")
            logging.info('"test_run" выполнен успешно')

        except TypeError:
            logging.warning("Неверный тип данных для объекта Runner")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        runner1 = Runner("test_challenge 1")
        runner2 = Runner("test_challenge 2")
        for i in range(10):
            runner1.walk()
            runner2.run()

        self.assertNotEqual(runner1.distance, runner2.distance)


logging.basicConfig(
    level=logging.INFO,
    filemode="w",
    filename="runner_tests.log",
    encoding="utf-8",
    format="%(asctime)s | %(levelname)s | %(message)s")

# ---------------------------- TestSuite ---------------------------------
testRT = unittest.TestSuite()
testRT.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))

runner_test = unittest.TextTestRunner(verbosity=2)
runner_test.run(testRT)