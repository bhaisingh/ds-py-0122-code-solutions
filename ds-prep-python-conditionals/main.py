day_of_week = 'Monday'
if day_of_week == 'Saturday' or day_of_week == 'Sunday':
    print('It is the weekend')
else:
    print('It is a weekday')


student_1_score = 50
if student_1_score >= 70:
    pass_or_fail = 'You passed!'
else:
    pass_or_fail = 'You failed!'

print('Student_1_score:', student_1_score, 'Pass_or_fail:', pass_or_fail)

student_2_score = 50
if student_2_score < 60:
  letter_grade = 'F'
elif student_2_score >= 60 and student_2_score < 70:
    letter_grade = 'D'
elif student_2_score >= 70 and student_2_score < 80:
    letter_grade = 'C'
elif student_2_score >= 80 and student_2_score < 90:
    letter_grade = 'B'
elif student_2_score >= 90 and student_2_score < 100:
    letter_grade = 'A'
elif student_2_score >= 100:
    letter_grade = 'A+'
else:
  letter_grade = 'Invalid'

print('Student_2_score:', student_2_score, 'Letter_grade:', letter_grade)

def get_season_info(value):
  if value == 'summer':
    return 'Statistically, it\'s likely to be hotter today than in 6 months from now. Don\'t sweat it, though.'
  elif value == 'spring':
    return 'The flowers are blooming while it\'s spring, but that correlation, not causation.'
  elif value == 'autumn':
    return 'The leaves seem to regress to warmer colors as autumn approaches its end.'
  elif value == 'winter':
    return "There may only be a high likelihood of it being cold today, but there's a 100 percent chance of me wanting that sweater."
  else:
    return "That's not a season. Most likely."

print('Season summer:', get_season_info('summer'))
print('Season spring:', get_season_info('spring'))
print('Season autumn:', get_season_info('autumn'))
print('Season winter:', get_season_info('winter'))
print('Season invalid:', get_season_info('invalid'))

age = 42
print('Age: 42', 'adult' if age >= 18 else 'child')
