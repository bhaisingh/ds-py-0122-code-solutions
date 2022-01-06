first_name = 'Rakesh'
last_name = "Singh"
full_name = first_name + " " + last_name
print(full_name)
height_in_inches = 72
print('Height in inches:', height_in_inches , 'type:', type(height_in_inches))
height_in_inches_float = float(height_in_inches)
print('Height in inches float:', height_in_inches_float , 'type:', type(height_in_inches_float))
height_in_meters = (height_in_inches_float * 2.54) / 100.0
print('Height in meters:', height_in_meters)
eats_plants = True
eats_animals = False
is_animal = eats_animals or eats_plants
is_omnivore = eats_plants and eats_animals
is_plant = not is_animal
print('Is animal:', is_animal, 'Is omnivore:', is_omnivore, 'Is plant:', is_plant)
mean_height_in_meters = 1.7155
short_threshold_in_meters = 1.576
tall_threshold_in_meters = 1.860
is_mean_height = height_in_meters == mean_height_in_meters
is_short = height_in_meters < short_threshold_in_meters
is_tall = height_in_meters > tall_threshold_in_meters
is_normal_height = height_in_meters >= short_threshold_in_meters and height_in_meters < tall_threshold_in_meters
print('Is mean height:', is_mean_height, 'Is short:', is_short, 'Is tall:', is_tall, 'Is normal height:', is_normal_height)
nothing = None
print('Nothing:', nothing, 'type:', type(nothing))