print('multipleconditions')
country = input('What country do you live in? ')
if country.lower() == 'canada':
    province = input('What province do you live in? ')
    if province.lower() in('alberta','nunavat','yukon'):
        tax = 0.05
        print(tax)
    elif province.lower() == 'ontario':
        tax = 0.13
        print(tax)
    else:
        tax = 0.15
        print(tax)
else:
    tax = 0.00
    print(tax)
    