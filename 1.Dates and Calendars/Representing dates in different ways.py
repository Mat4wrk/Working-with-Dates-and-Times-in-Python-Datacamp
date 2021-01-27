"""Print andrew in the format 'YYYY-MM'."""
# Import date
from datetime import date

# Create a date object
andrew = date(1992, 8, 26)

# Print the date in the format 'YYYY-MM'
print(andrew.strftime('%Y-%m'))


"""Print andrew in the format 'MONTH (YYYY)', using %B for the month's full name, which in this case will be August."""
# Import date
from datetime import date

# Create a date object
andrew = date(1992, 8, 26)

# Print the date in the format 'MONTH (YYYY)'
print(andrew.strftime('%B (%Y)'))


"""Print andrew in the format 'YYYY-DDD' (where DDD is the day of the year) using %j."""
# Import date
from datetime import date

# Create a date object
andrew = date(1992, 8, 26)

# Print the date in the format 'YYYY-DDD'
print(andrew.strftime('%Y-%j'))
