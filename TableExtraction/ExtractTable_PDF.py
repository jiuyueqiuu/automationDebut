import camelot

tables = camelot.read_pdf('../foo.pdf', pages ='1')
print(tables) # Will output <TableList n=1>, meaning there is only one table

tables.export('foo.csv', f = 'csv', compress = True)

"""
The command above will creat a foo.zip containing all tables in tables
"""

tables[0].to_csv('foo.csv') # Exports only the frst one (index 0)
