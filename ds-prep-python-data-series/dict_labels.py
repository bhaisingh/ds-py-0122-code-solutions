# Data Set: Do Not Modify
from itertools import count


columns = ("year", "unemployment_rate")
label_order = [
    2001, 2002, 2003, 2004, 2005,
    2006, 2007, 2008, 2009, 2010,
    2011, 2012, 2013, 2014, 2015,
    2016, 2017, 2018, 2019, 2020,
    2021
]
unemployment_rates = {
    2002: 6,
    2020: 4,
    2007: 5,
    2015: 6,
    2010: 11,
    2014: 7,
    2001: 5,
    2006: 5,
    2004: 6,
    2009: 8,
    2013: 8,
    2008: 5,
    2021: 7,
    2018: 4,
    2011: 10,
    2005: 6,
    2016: 5,
    2019: 4,
    2012: 9,
    2017: 5,
    2003: 6
}

# Write your code below this line:

def last_series_point(columns, unemployment_rates):
  dict_len = len(unemployment_rates)
  iter_count = 1
  for key, value in unemployment_rates.items():
    if iter_count == dict_len:
      print('return')
      return {columns[0]: key, columns[1]: value}
    else:
      iter_count += 1

print('last_series_point: ', last_series_point(columns, unemployment_rates))


def first_five_element_series(unemployment_rates):
    return list(unemployment_rates.items())[:5]

print('first_five_element_series: ', first_five_element_series(unemployment_rates))

def check_include_2000_2010(unemployment_rates):
    res_2000 = False
    res_2010 = False
    for i in unemployment_rates.keys():
        if 2000 == i:
            res_2000 = True
        if 2010 == i:
            res_2010 = True
    return res_2000, res_2010

res_2000, res_2010 = check_include_2000_2010(unemployment_rates)
print('check_include_2000: ', res_2000, 'check_include_2010: ', res_2010)


def unemployment_rate_latest_year(label_order, unemployment_rates):
  latest_year = label_order[-1]
  for key, value in unemployment_rates.items():
    if latest_year == key:
      return value

print('unemployment_rate_latest_year: ', unemployment_rate_latest_year(label_order, unemployment_rates))

def unique_year_set(unemployment_rates):
    year_set = set()
    for key in unemployment_rates.keys():
      year_set.add(key)
    return year_set

print('unique_year_set: ', unique_year_set(unemployment_rates))

def unemployment_rate_by_year(unemployment_rates, label_order):
  list_rate = []
  for year in label_order:
    for key, value in unemployment_rates.items():
      if year == key:
        list_rate.append(value)
  return list_rate

print('unemployment_rate_ord_by_year: ', unemployment_rate_by_year(unemployment_rates, label_order))

def largest_unemployment_rate(unemployment_rates):
  largest_rate = 0
  for value in unemployment_rates.values():
    if value > largest_rate:
      largest_rate = value
  return largest_rate

print('largest_unemployment_rate: ', largest_unemployment_rate(unemployment_rates))

def employment_rate_series(unemployment_rates):
    employment_rates = {}
    for key, value in unemployment_rates.items():
      employment_rates[key] = 100 - value
    return employment_rates

print('employment_rate_series: ', employment_rate_series(unemployment_rates))

def unemployment_rate_atleast_7(unemployment_rates):
  unemployment_rate_atleast_7 = {}
  for key, value in unemployment_rates.items():
    if value >= 7:
      unemployment_rate_atleast_7[key] = value
  return unemployment_rate_atleast_7

print('unemployment_rate_atleast_7: ', unemployment_rate_atleast_7(unemployment_rates))

def rate_count(unemployment_rates):
  rate_count = {}
  for element in unemployment_rates.values():
    count = 0
    for element2 in unemployment_rates.values():
      if element == element2:
        count += 1
    rate_count[element] = count
  return rate_count

print('rate_count: ', rate_count(unemployment_rates))
