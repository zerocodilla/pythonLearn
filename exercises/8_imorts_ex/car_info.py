def car_info(manufacturer, model, **car_profile):
    """Build dictionary with car info."""
    car_profile['manufacturer'] = manufacturer
    car_profile['model'] = model
    return car_profile
