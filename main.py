# Unit Conversion Program

print('1. Distance converter')
print('2. Amplitude converter')


choice = input('Enter if you want the first or second converter: ')

if choice == 'First':
    print('1. Kilometers to Meters')
    print('2. Meters to Kilometers')

    choose = input('First or second  unit converter? ')

    def km_meters():
        km = float(input('Enter a distance in Kilometers: '))
        meters = km * 1000
        print('Distance in meters: {0}'.format(meters))

    def meters_km():
        meters = float(input('Enter a distance in Meters: '))
        km = meters / 1000
        print('Distance in kilometers: {0}'.format(km))


    if choose == 'First':
        km_meters()

    elif choose == 'Second':
        meters_km()

if choice == 'Second':
    print('1. Centimeters to inches')
    print('2. Inches to Centimeters')

    choice2 = input('First or second unit converter? ')

    def cm_to_inc():
        centimeters = float(input('Enter a amplitude in Cm: '))
        inches = centimeters * 0.393701
        print('Amplitude in inches: {0}'.format(inches))

    def inc_to_cm():
        inches = float(input('Enter a amplitude in Inches: '))
        centimeters = inches / 0.393701
        print('Amplitude in Centimeters: {0}'.format(centimeters))

    if choice2 == 'First':
        cm_to_inc()

    elif choice2 == 'Second':
        inc_to_cm()

