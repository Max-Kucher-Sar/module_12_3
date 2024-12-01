import program_12_2
import unittest

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_runner1(self):
        runner1 = program_12_2.Runner('Usain', speed=10)
        runner1.run()
        self.assertEqual(runner1.distance, 20)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_runner2(self):
        runner2 = program_12_2.Runner('Andry', speed=9)
        runner2.run()
        self.assertEqual(runner2.distance, 18)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_runner3(self):
        runner3 = program_12_2.Runner('Nick', speed=3)
        runner3.run()
        self.assertEqual(runner3.distance, 6)



class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_result = []

    @classmethod
    def tearDownClass(cls):

        for dict_ in cls.all_result:
            print(dict_)



    def setUp(self):
        self.runner1 = program_12_2.Runner('Usain', speed=10)
        self.runner2 = program_12_2.Runner('Andry', speed=9)
        self.runner3 = program_12_2.Runner('Nick', speed=3)


    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run1(self):
        championship1 = program_12_2.Tournament(90, self.runner1, self.runner3)
        result1 = championship1.start()
        self.all_result.append({place: name for place, name in result1.items()})
        self.assertTrue(result1[2] == 'Nick')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run2(self):
        championship2 = program_12_2.Tournament(90, self.runner2, self.runner3)
        result2 = championship2.start()
        self.all_result.append({place: name for place, name in result2.items()})
        self.assertTrue(result2[2] == 'Nick')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run3(self):
        championship3 = program_12_2.Tournament(90, self.runner1, self.runner2, self.runner3)
        result3 = championship3.start()
        self.all_result.append({place: name for place, name in result3.items()})
        self.assertTrue(result3[3] == 'Nick')




if __name__ == '__main__':
    unittest.main()




