import petl as etl
import pandas as pd
import cdata.azuretables as mod

cnxn = mod.connect("AccessKey=4vd+ucylSX+BIJs3O6/3DtDz4JOS9JlXp21yeFnNb7rX7i3vA4sQbmOI/PkaEgQMlfK+ZyvJ1+BH+AStZQJGhA==;Account=madhumlws981768029566;")

sql = "SELECT * FROM TestTextAnalytics'"

table1 = etl.fromdb(cnxn,sql)

# table2 = etl.sort(table1,'Price')

# etl.tocsv(table2,'northwindproducts_data.csv')

# table3 = [ ['Name','Price'], ['NewName1','NewPrice1'], ['NewName2','NewPrice2'], ['NewName3','NewPrice3'] ]

# etl.appenddb(table3, cnxn, 'NorthwindProducts')