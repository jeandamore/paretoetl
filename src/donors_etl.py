import sys
import pareto_etl as petl

def load_donors(client):
	return petl.read_csv('../data/'+client+'/donors.csv')

def load_donors_config(client):
	return petl.read_json('../config/'+client+'/donors.json')

def transform_donors(client, donors):
	donors_config = load_donors_config(client)
	donors_base = petl.rename_headers(donors, donors_config['headers'])
	for mapping in donors_config['mappings']:
		donors_base = petl.map_values(donors_base, mapping['field'], mapping['values'])
	for concat in donors_config['concats']:
		donors_base = petl.concat_columns(donors_base, concat['new_field'], concat['old_field_left'], concat['old_field_right'])
	return donors_base

def save_donors_base(client, table):
	return petl.write_csv(table, '../data/'+client+'/donors_base.csv')


client = sys.argv[1]
donors = load_donors(client)
donors_base = transform_donors(client, donors)
save_donors_base(client, donors_base)

print donors
print donors_base