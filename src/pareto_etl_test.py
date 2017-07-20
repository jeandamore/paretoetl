import unittest
import pareto_etl as petl

class ParetoEtlTest(unittest.TestCase):

  def test_rename_headers(self):
    table = [['ME', 'YOU', 'HER']]
    new_table = petl.rename_headers(table, {'ME':'1', 'YOU':'2', 'HER':'3'})
    self.assertEqual(('1', '2', '3'), petl.headers(new_table))