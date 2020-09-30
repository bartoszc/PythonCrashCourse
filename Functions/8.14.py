def make_car(make, model, **other_info):
    """Budowa słownika zawierającego wszelkie informacje    o użytkowniku."""
    car_profile = dict()
    car_profile['make'] = make
    car_profile['model'] = model
    for key, value in other_info.items():
        car_profile[key] = value
    return car_profile


car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)

