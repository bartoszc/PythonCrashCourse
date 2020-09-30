def build_profile(first, last, **user_info):
    """Budowa słownika zawierającego wszelkie informacje    o użytkowniku."""
    profile = dict()
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('Bartosz', 'Chojnacki', location='Lublin', field='IT', job='Tester', company='JMMJ',
                             sport='Speedway')
print(user_profile)
