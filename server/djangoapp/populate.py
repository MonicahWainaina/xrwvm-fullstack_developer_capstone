from .models import CarMake, CarModel, Dealer  # Import the Dealer model

def initiate():
    car_make_data = [
        {"name": "NISSAN", "description": "Great cars. Japanese technology"},
        {"name": "Mercedes", "description": "Great cars. German technology"},
        {"name": "Audi", "description": "Great cars. German technology"},
        {"name": "Kia", "description": "Great cars. Korean technology"},
        {"name": "Toyota", "description": "Great cars. Japanese technology"},
    ]

    car_make_instances = []
    for data in car_make_data:
        car_make_instances.append(CarMake.objects.create(name=data['name'], description=data['description']))

    # Get or create a default dealer (you might need to adjust this logic)
    default_dealer, created = Dealer.objects.get_or_create(
        id=1,  # Assuming you want a dealer with ID 1
        defaults={'city': 'Default City', 'state': 'Default State', 'address': 'Default Address', 'zip': '00000', 'lat': '0.0', 'long': '0.0', 'short_name': 'Default', 'full_name': 'Default Dealership'}
    )

    # Create CarModel instances with the corresponding CarMake instances and the default dealer
    car_model_data = [
        {"name": "Pathfinder", "type": "SUV", "year": 2023, "car_make": car_make_instances[0], "dealer": default_dealer},
        {"name": "Qashqai", "type": "SUV", "year": 2023, "car_make": car_make_instances[0], "dealer": default_dealer},
        {"name": "XTRAIL", "type": "SUV", "year": 2023, "car_make": car_make_instances[0], "dealer": default_dealer},
        {"name": "A-Class", "type": "SUV", "year": 2023, "car_make": car_make_instances[1], "dealer": default_dealer},
        {"name": "C-Class", "type": "SUV", "year": 2023, "car_make": car_make_instances[1], "dealer": default_dealer},
        {"name": "E-Class", "type": "SUV", "year": 2023, "car_make": car_make_instances[1], "dealer": default_dealer},
        {"name": "A4", "type": "SUV", "year": 2023, "car_make": car_make_instances[2], "dealer": default_dealer},
        {"name": "A5", "type": "SUV", "year": 2023, "car_make": car_make_instances[2], "dealer": default_dealer},
        {"name": "A6", "type": "SUV", "year": 2023, "car_make": car_make_instances[2], "dealer": default_dealer},
        {"name": "Sorrento", "type": "SUV", "year": 2023, "car_make": car_make_instances[3], "dealer": default_dealer},
        {"name": "Carnival", "type": "SUV", "year": 2023, "car_make": car_make_instances[3], "dealer": default_dealer},
        {"name": "Cerato", "type": "Sedan", "year": 2023, "car_make": car_make_instances[3], "dealer": default_dealer},
        {"name": "Corolla", "type": "Sedan", "year": 2023, "car_make": car_make_instances[4], "dealer": default_dealer},
        {"name": "Camry", "type": "Sedan", "year": 2023, "car_make": car_make_instances[4], "dealer": default_dealer},
        {"name": "Kluger", "type": "SUV", "year": 2023, "car_make": car_make_instances[4], "dealer": default_dealer},
        # Add more CarModel instances as needed
    ]

    for data in car_model_data:
        CarModel.objects.create(name=data['name'], car_make=data['car_make'], type=data['type'], year=data['year'], dealer=data['dealer'])