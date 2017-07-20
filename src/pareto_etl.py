import json
import numpy
import petl as etl

def read_csv(file):
	return etl.fromcsv(file)

def write_csv(table, file):
	return etl.tocsv(table, file)

def read_json(file):
	json_file = open(file)
	json_str = json_file.read()
	json_data = json.loads(json_str)
	return json_data

def headers(table):
	return etl.header(table)

def rename_headers(table, mappings):
	return etl.rename(table, mappings)

def map_values(table, column, mappings):
	return etl.convert(table, column, mappings)

def concat_columns(table, new_column, column_left, column_right):
	new_table = etl.addfield(table, new_column, lambda rec: rec[column_left]+', '+ rec[column_right], 1)
	return etl.cutout(new_table, column_left, column_right)