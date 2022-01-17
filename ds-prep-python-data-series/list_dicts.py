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
    {"unemployment_rate": 8, "year": 2013},
    {"unemployment_rate": 5, "year": 2006},
    {"unemployment_rate": 5, "year": 2017},
    {"unemployment_rate": 6, "year": 2015},
    {"unemployment_rate": 6, "year": 2002},
    {"unemployment_rate": 4, "year": 2019},
    {"unemployment_rate": 9, "year": 2012},
    {"unemployment_rate": 4, "year": 2018},
    {"unemployment_rate": 6, "year": 2003},
    {"unemployment_rate": 5, "year": 2007},
    {"unemployment_rate": 11, "year": 2010},
    {"unemployment_rate": 7, "year": 2014},
    {"unemployment_rate": 6, "year": 2004},
    {"unemployment_rate": 5, "year": 2016},
    {"unemployment_rate": 6, "year": 2005},
    {"unemployment_rate": 7, "year": 2021},
    {"unemployment_rate": 5, "year": 2001},
    {"unemployment_rate": 4, "year": 2020},
    {"unemployment_rate": 10, "year": 2011},
    {"unemployment_rate": 8, "year": 2009},
    {"unemployment_rate": 5, "year": 2008}
]

# Write your code below this line:

def last_series_point(columns, unemployment_rates):
    return {columns[0]: unemployment_rates[-1]['year'], columns[1]: unemployment_rates[-1]['unemployment_rate']}

print('last_series_point: ', last_series_point(columns, unemployment_rates))

def first_five_element_series(unemployment_rates):
    return unemployment_rates[:5]

print('first_five_element_series: ', first_five_element_series(unemployment_rates))

def check_include_2000_2010(unemployment_rates):
    res_2000 = False
    res_2010 = False
    for i in unemployment_rates:
        if 2000 == i['year']:
            res_2000 = True
        if 2010 == i['year']:
            res_2010 = True
    return res_2000, res_2010

res_2000, res_2010 = check_include_2000_2010(unemployment_rates)
print('check_include_2000: ', res_2000, 'check_include_2010: ', res_2010)


def unemployment_rate_latest_year(label_order, unemployment_rates):
    for element in unemployment_rates:
      if element['year'] == label_order[-1]:
         return element['unemployment_rate']

print('unemployment_rate_latest_year: ', unemployment_rate_latest_year(label_order, unemployment_rates))

def unique_year_set(unemployment_rates):
    year_set = set()
    for element in unemployment_rates:
      year_set.add(element['year'])
    return year_set

print('unique_year_set: ', unique_year_set(unemployment_rates))

def unemployment_rate_by_year(unemployment_rates, label_order):
  list_rate = []
  for year in label_order:
    for element in unemployment_rates:
      if year == element['year']:
        list_rate.append(element['unemployment_rate'])
  return list_rate

print('unemployment_rate_ord_by_year: ', unemployment_rate_by_year(unemployment_rates, label_order))

def largest_unemployment_rate(unemployment_rates):
  largest_rate = 0
  for element in unemployment_rates:
    if element['unemployment_rate'] > largest_rate:
      largest_rate = element['unemployment_rate']
  return largest_rate

print('largest_unemployment_rate: ', largest_unemployment_rate(unemployment_rates))

def employment_rate_series(unemployment_rates):
    employment_rates = []
    for element in unemployment_rates:
      employment_rates.append({'employment_rate': 100 - element['unemployment_rate'], 'year': element['year']})
    return employment_rates

print('employment_rate_series: ', employment_rate_series(unemployment_rates))

def unemployment_rate_atleast_7(unemployment_rates):
  unemployment_rate_atleast_7 = []
  for element in unemployment_rates:
    if element['unemployment_rate'] >= 7:
      unemployment_rate_atleast_7.append(element)
  return unemployment_rate_atleast_7

print('unemployment_rate_atleast_7: ', unemployment_rate_atleast_7(unemployment_rates))

def rate_count(unemployment_rates):
  rate_count = {}
  for element in unemployment_rates:
    count = 0
    for element2 in unemployment_rates:
      if element['unemployment_rate'] == element2['unemployment_rate']:
        count += 1
    rate_count[element['unemployment_rate']] = count
  return rate_count

print('rate_count: ', rate_count(unemployment_rates))
