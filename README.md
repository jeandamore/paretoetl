Demo Python ETL code for managing client datasets variations

This is a simplistic example to load donors' data.
It uses the Python PETL library.
The core code common to all client is in src/donors_etl.py
The client specific configuration is in config/<client>/donors.json
The ./go.sh script is a bootstrap script that also runs unit tests and an example transformation:
``python donors_etl.py fred-hollows``