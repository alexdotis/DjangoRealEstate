from typing import List, Tuple
ESTATE_CATEGORY: List[Tuple[str, str]] = [
    ('residential', 'Residential'),
    ('commercial', 'Commercial'),
    ('land', 'Land'),
    ('other', 'Other')
]
PROPERTY_STATUS: List[Tuple[str, str]] = [
    ('rent', 'Rent'),
    ('sale', 'Sale')
]
RESINDETIAL: List[Tuple[str, str]] = [
    ('apartment', 'Apartment'),
    ('studio', 'Studio'),
    ('maisonette', 'Maisonette'),
    ('detached', 'Detached house'),
    ('villa', 'Villa'),
    ('loft', 'Loft'),
    ('bungalow', 'Bungalow'),
    ('building', 'Building'),
    ('farm', 'Farm / Ranch'),
    ('houseboat', 'Houseboat'),
    ('other', 'Other Categories'),

]
COMMERCIAL: List[Tuple[str, str]] = [
    ('office', 'Office'),
    ('store', 'Store'),
    ('warehouse', 'Warehouse'),
    ('industrial', 'Industrial area'),
    ('craft', 'Craft space'),
    ('hotel', 'Hotel'),
    ('business', 'Business building'),
    ('room', 'Room'),
    ('gallery', 'Gallery'),
    ('other', 'Other Categories'),
]
LAND: List[Tuple[str, str]] = [
    ('plot', 'Plot'),
    ('plot', 'Plot of land'),
    ('island', 'Island'),
    ('other', 'Other Categories'),
]
OTHER: List[Tuple[str, str]] = [
    ('parking', 'Parking'),
    ('business', 'Business'),
    ('prefabricated', 'Prefabricated'),
    ('removable', 'Removable'),
    ('air', 'Air'),
    ('other', 'Other Property Categories')
]
SUBCATECORY = RESINDETIAL + COMMERCIAL + LAND + OTHER


def display_subcategory_dictionary() -> dict:
    global_list = {
        'residential': RESINDETIAL,
        'commercial': COMMERCIAL,
        'land': LAND,
        'other': OTHER
    }

    result = {}
    for key, values in global_list.items():
        result[key] = [{'obj': obj} for obj in values]
    return result
