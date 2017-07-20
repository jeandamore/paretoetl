import petl as etl

def load_csv(file):
	return etl.fromcsv(file)

def rename_headers(table, mappings):
	return etl.rename(table, {'DONOR_ID':'URN', 'ADDRESS':'STREET', 'GENDER':'SEX'})

def map_values(table, column, mappings):
	return etl.convert(table, column, mappings)

def concat_columns(table, new_column, column_left, column_right):
	new_table = etl.addfield(table, new_column, lambda rec: rec[column_left]+', '+ rec[column_right], 1)
	return etl.cutout(new_table, column_left, column_right)