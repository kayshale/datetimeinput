from datetime import datetime
userdt = input('Enter Date and Time \n (Ex. 05/14/1998 14:50:21) \n')

expectedformat = '%m/%d/%Y %H:%M:%S'
#validates datetime
try:
    dt = datetime.strptime(userdt, expectedformat)
except Exception as e:
    print('Invalid. '+str(e))

#checks if year is between 1900 and 2020 limit
year = dt.year
if int(dt.year) > 1900 and int(dt.year) < 2020:
    print("Year is valid")
else:
    print("Invalid. Year is not valid")

#converts datetime timestamp to unix format
unix = dt.timestamp()
print(unix)
