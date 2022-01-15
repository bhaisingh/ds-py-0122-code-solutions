# Data Set: Do Not Modify
columns = ("year", "unemployment_rate")
label_order = [
    2001, 2002, 2003, 2004, 2005,
    2006, 2007, 2008, 2009, 2010,
    2011, 2012, 2013, 2014, 2015,
    2016, 2017, 2018, 2019, 2020,
    2021
]
unemployment_rates = [
    (2005, 6),
    (2001, 5),
    (2013, 8),
    (2011, 10),
    (2017, 5),
    (2006, 5),
    (2009, 8),
    (2021, 7),
    (2002, 6),
    (2007, 5),
    (2012, 9),
    (2014, 7),
    (2003, 6),
    (2019, 4),
    (2016, 5),
    (2015, 6),
    (2018, 4),
    (2008, 5),
    (2010, 11),
    (2004, 6),
    (2020, 4)
]

# Write your code below this line:

def last_series_point(columns, unemployment_rates):
    return {columns[0]: unemployment_rates[-1][0], columns[1]: unemployment_rates[-1][1]}

print('last_series_point: ', last_series_point(columns, unemployment_rates))

def first_five_element_series(unemployment_rates):
    return unemployment_rates[:5]

print('first_five_element_series: ', first_five_element_series(unemployment_rates))

def check_include_2000(unemployment_rates):
    res_2000 = False
    for i in unemployment_rates:
        if 2000 == i[0]:
            res_2000 = True
    return res_2000

print('check_include_2000: ', check_include_2000(unemployment_rates))

def check_include_2010(unemployment_rates):
    res_2010 = False
    for i in unemployment_rates:
        if 2010 == i[0]:
            res_2010 = True
    return res_2010

print('check_include_2010: ', check_include_2010(unemployment_rates))

def unemployment_rate_latest_year(label_order, unemployment_rates):
  latest_year = label_order[-1]
  for element in unemployment_rates:
    if latest_year in element:
      return element[1]

print('unemployment_rate_latest_year: ', unemployment_rate_latest_year(label_order, unemployment_rates))

def unique_year_set(unemployment_rates):
    year_set = set()
    for element in unemployment_rates:
      year_set.add(element[0])
    return year_set

print('unique_year_set: ', unique_year_set(unemployment_rates))

def unemployment_rate_by_year(unemployment_rates, label_order):
  list_rate = []
  for year in label_order:
    for element in unemployment_rates:
      if year in element:
        list_rate.append(element[1])
  return list_rate

print('unemployment_rate_ord_by_year: ', unemployment_rate_by_year(unemployment_rates, label_order))

def largest_unemployment_rate(unemployment_rates):
  largest_rate = 0
  for element in unemployment_rates:
    if element[1] > largest_rate:
      largest_rate = element[1]
  return largest_rate

print('largest_unemployment_rate: ', largest_unemployment_rate(unemployment_rates))


def employment_rate_series(unemployment_rates):
    employment_rate = []
    for element in unemployment_rates:
      employment_rate.append(element)
    return employment_rate

print('employment_rate_series: ', employment_rate_series(unemployment_rates))

def unemployment_rate_atleast_7(unemployment_rates):
  unemployment_rate_atleast_7 = []
  for element in unemployment_rates:
    if element[1] >= 7:
      unemployment_rate_atleast_7.append(element)
  return unemployment_rate_atleast_7

print('unemployment_rate_atleast_7: ', unemployment_rate_atleast_7(unemployment_rates))

def rate_count(unemployment_rates):
  rate_count = {}
  for element in unemployment_rates:
    count = 0
    for element2 in unemployment_rates:
      if element[1] == element2[1]:
        count += 1
    rate_count[element[1]] = count
  return rate_count

print('rate_count: ', rate_count(unemployment_rates))
