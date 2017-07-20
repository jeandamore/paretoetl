import paretoetl as petl

donors = petl.load_csv('data/donors.csv')
print donors

donors_base = petl.rename_headers(donors, {'DONOR_ID':'URN', 'ADDRESS':'STREET', 'GENDER':'SEX'})
donors_base = petl.map_values(donors_base, 'SEX', {'Male':'M', 'Female':'F'})
donors_base = petl.concat_columns(donors_base, 'NAME', 'LAST_NAME', 'FIRST_NAME')
print donors_base