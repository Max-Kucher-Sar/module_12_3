import test_program_12_2
import unittest

test_ST = unittest.TestSuite()
test_ST.addTest(unittest.TestLoader().loadTestsFromTestCase(test_program_12_2.RunnerTest))
test_ST.addTest(unittest.TestLoader().loadTestsFromTestCase(test_program_12_2.TournamentTest))


runner = unittest.TextTestRunner(verbosity=2)
runner.run(test_ST)