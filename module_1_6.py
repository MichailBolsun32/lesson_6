my_dict = {'Vova': 1975,
           'Anna': 1999,
           'Misha': 2002}

print(f'Dict: {my_dict}')
print(f'Existing value: {my_dict.get('Vova')}')
print(f'Not existing value: {my_dict.get('Pavel')}')

my_dict.update({'Peter': 1999,
                'Masha': 1989})

print(f'Deleted value: {my_dict.pop('Vova')}')
print(f'Modified dictionary: {my_dict}')

my_set = {1, 'Яблоко', 42.314, 'Апельсин', 'Яблоко', 1, 42.314, 'Яблоко'}

print(f'Set: {my_set}')

my_set.add(13)
my_set.add((5, 6, 1.6))
my_set.remove(1)
print(f'Modified set: {my_set}')