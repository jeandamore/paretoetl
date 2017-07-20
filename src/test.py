import petl as etl
donors = etl.fromcsv('data/donors.csv')
print donors
donors_base = etl.rename(donors, {'DONOR_ID':'URN', 'ADDRESS':'STREET', 'GENDER':'SEX'})
donors_base = etl.convert(donors_base, 'SEX', {'Male':'M', 'Female':'F'})
donors_base = etl.addfield(donors_base, 'NAME', lambda rec: rec['LAST_NAME']+', '+ rec['FIRST_NAME'], 1)
donors_base = etl.cutout(donors_base, 'FIRST_NAME', 'LAST_NAME')

print donors_base