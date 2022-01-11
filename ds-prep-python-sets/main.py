trail_mix = {'m&ms', 'peanuts', 'raisins'}
print('trail_mix:', trail_mix)

print('Check cashews in trail_mix:', 'cashews' in trail_mix)
print('Check peanuts in trail_mix:', 'peanuts' in trail_mix)

trail_mix.add('pretzels')
trail_mix.update({'peanuts', 'banana chips', 'bits of jerky'})
print('trail_mix:', trail_mix)

trail_mix.remove('m&ms')
trail_mix.discard('raisins')
trail_mix.discard('rat poison')
print('trail_mix:', trail_mix)

nuts = {'peanuts', 'cashews', 'almonds', 'walnuts', 'pecans'}
print('In nuts, trail_mix or both:', nuts.union(trail_mix))
print('In nuts that are in trail_mix:', nuts.intersection(trail_mix))
print('Trail_mix items that are not nuts:', trail_mix.difference(nuts))
print('Nuts items that are not trail_mix:', nuts.difference(trail_mix))
