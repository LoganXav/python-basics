# from app import Planet


# hoth = Planet('Hoth', 200000, 5.5, 'hoth')               # instance 1
# print(f'the name is: {hoth.name}')
# print(f'the radius is: {hoth.radius}')
# print(f'the gravity is: {hoth.gravity}')
# print(hoth.orbit())

# naboo = Planet('Naboo', 500000, 5.5, 'hoth')             # instance 2              
# print(f'the name is {naboo.name}')
# print(f'the radius is: {naboo.radius}')
# print(f'the gravity is: {naboo.gravity}')
# print(naboo.orbit())
# print(Planet.commons())
# print(Planet.orbit())    # won't work because Planet doesn't not have access to it. Only the instances do(not globally scoped)
# print(naboo.commons())
# print(Planet.spin())
# print(naboo.spin('a very high speed'))