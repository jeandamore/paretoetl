import sys
import pareto_etl as petl

def load_donors(client):
	return petl.read_csv('../data/'+client+'/donors.csv')

def transform_donors(client):
	donors_base = petl.rename_headers(donors, {'DONOR_ID':'URN', 'ADDRESS':'STREET', 'GENDER':'SEX'})
	donors_base = petl.map_values(donors_base, 'SEX', {'Male':'M', 'Female':'F'})
	donors_base = petl.concat_columns(donors_base, 'NAME', 'LAST_NAME', 'FIRST_NAME')
	return donors_base

def save_donors_base(client, table):
	return petl.write_csv(table, '../data/'+client+'/donors_base.csv')


client = sys.argv[1]
donors = load_donors(client)
donors_base = transform_donors(client)
save_donors_base(client, donors_base)

print donors
print donors_base