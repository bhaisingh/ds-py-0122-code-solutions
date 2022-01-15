# Data Set: Do Not Modify
columns = ("year", "unemployment_rate")
label_order = [
    2001, 2002, 2003, 2004, 2005,
    2006, 2007, 2008, 2009, 2010,
    2011, 2012, 2013, 2014, 2015,
    2016, 2017, 2018, 2019, 2020,
    2021
]
unemployment_rates = {
    'year': [
        2009, 2011, 2005, 2016, 2001,
        2012, 2019, 2007, 2021, 2018,
        2010, 2013, 2006, 2017, 2015,
        2014, 2008, 2004, 2003, 2020,
        2002
    ],
    'unemployment_rate': [
        8, 10, 6, 5, 5,
        9, 4, 5, 7, 4,
        11, 8, 5, 5, 6,
        7, 5, 6, 6, 4,
        6
    ]
}

# Write your code below this line:

print(unemployment_rates['year'][0])

def last_series_point(columns, unemployment_rates):
    return {columns[0]: unemployment_rates['year'][-1], columns[1]: unemployment_rates['unemployment_rate'][-1]}

print('last_series_point: ', last_series_point(columns, unemployment_rates))


def first_five_element_series(unemployment_rates):
    first_five_tuples = []
    for i in range(5):
      first_five_tuples.append((unemployment_rates['year'][i], unemployment_rates['unemployment_rate'][i]))
    return first_five_tuples

print('first_five_element_series: ', first_five_element_series(unemployment_rates))

def check_include_2000(unemployment_rates):
    res_2000 = False
    for i in unemployment_rates['year']:
        if 2000 == i:
            res_2000 = True
    return res_2000

print('check_include_2000: ', check_include_2000(unemployment_rates))

def check_include_2010(unemployment_rates):
    res_2010 = False
    for i in unemployment_rates['year']:
        if 2010 == i:
            res_2010 = True
    return res_2010

print('check_include_2010: ', check_include_2010(unemployment_rates))

def unemployment_rate_latest_year(label_order, unemployment_rates):
  latest_year = label_order[-1]
  index = unemployment_rates['year'].index(latest_year)
  return unemployment_rates['unemployment_rate'] [index]

print('unemployment_rate_latest_year: ', unemployment_rate_latest_year(label_order, unemployment_rates))


def unique_year_set(unemployment_rates):
    year_set = set()
    for element in unemployment_rates['year']:
      year_set.add(element)
    return year_set

print('unique_year_set: ', unique_year_set(unemployment_rates))

def unemployment_rate_by_year(unemployment_rates, label_order):
  list_rate = []
  for year in label_order:
    index = unemployment_rates['year'].index(year)
    list_rate.append(unemployment_rates['unemployment_rate'][index])
  return list_rate

print('unemployment_rate_ord_by_year: ', unemployment_rate_by_year(unemployment_rates, label_order))

def largest_unemployment_rate(unemployment_rates):
  largest_rate = 0
  for element in unemployment_rates['unemployment_rate']:
    if element > largest_rate:
      largest_rate = element
  return largest_rate

print('largest_unemployment_rate: ', largest_unemployment_rate(unemployment_rates))

def employment_rate_series(unemployment_rates):
    employment_rate = {}
    for keys, value in unemployment_rates.items():
      employment_rate[keys] = value
    return employment_rate

print('employment_rate_series: ', employment_rate_series(unemployment_rates))

def unemployment_rate_atleast_7(unemployment_rates):
  unemployment_rate_atleast_7 = {}
  year_list = []
  rate_list = []
  for element in unemployment_rates['unemployment_rate']:
    if element >= 7:
      index = unemployment_rates['unemployment_rate'].index(element)
      year_list.append(unemployment_rates['year'][index])
      rate_list.append(unemployment_rates['unemployment_rate'][index])
  unemployment_rate_atleast_7['year'] = year_list
  unemployment_rate_atleast_7['unemployment_rate'] = rate_list
  return unemployment_rate_atleast_7

print('unemployment_rate_atleast_7: ', unemployment_rate_atleast_7(unemployment_rates))

def rate_count(unemployment_rates):
  rate_count = {}
  for element in unemployment_rates['unemployment_rate']:
    count = 0
    for element2 in unemployment_rates['unemployment_rate']:
      if element == element2:
        count += 1
    rate_count[element] = count
  return rate_count

print('rate_count: ', rate_count(unemployment_rates))
