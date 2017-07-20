import unittest
import os
import pareto_etl as petl

class ParetoEtlTest(unittest.TestCase):

  def test_rename_headers(self):
    table = [['ME', 'YOU', 'HER']]
    new_table = petl.rename_headers(table, {'ME':'1', 'YOU':'2', 'HER':'3'})
    self.assertEqual(('1', '2', '3'), petl.headers(new_table))

  def test_read_json(self):
    test_file = open('test.json', 'w')
    test_file.write('{"key":"value"}')
    test_file.close()
    json_data = petl.read_json('test.json')
    self.assertEqual({'key':'value'}, json_data)
    os.remove('test.json')
