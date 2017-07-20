import petl as etl
donors = etl.fromcsv('data/donors.csv')
print donors
donors_base = etl.rename(donors, {'DONOR_ID':'URN', 'ADDRESS':'STREET', 'GENDER':'SEX'})
donors_base = etl.convert(donors_base, 'SEX', {'Male':'M', 'Female':'F'})
print donors_base