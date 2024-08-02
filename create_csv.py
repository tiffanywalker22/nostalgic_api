import csv

# Data for bedrooms
bedrooms = [
    {'bedroom_id': 1, 'title': "My 90s Bedroom", 'description': "A room filled with 90s nostalgia items", 'img_src': "img/bedroom_1.jpg"},
    {'bedroom_id': 2, 'title': "Classic Kids Room", 'description': "A classic kids room with timeless toys", 'img_src': "img/bedroom_2.jpg"},
    # Add more bedrooms as needed
]

# Data for objects
objects = [
    {'object_id': 1, 'name': "Tamagotchi", 'description': "An electronic pet", 'img_src': "img/tamagotchi.jpg"},
    {'object_id': 2, 'name': "Beanie Baby", 'description': "A small stuffed animal", 'img_src': "img/beanie_baby.jpg"},
    # Add more objects as needed
]

# Data for bedroom-object associations
bedrooms_objects = [
    {'bedroom_id': 1, 'object_id': 1},
    {'bedroom_id': 1, 'object_id': 2},
    {'bedroom_id': 2, 'object_id': 2},
    # Add more associations as needed
]

# Function to write data to CSV
def write_csv(file_path, fieldnames, data):
    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

# Writing data to CSV files
write_csv('bedrooms.csv', ['bedroom_id', 'title', 'description', 'img_src'], bedrooms)
write_csv('objects.csv', ['object_id', 'name', 'description', 'img_src'], objects)
write_csv('bedrooms_objects.csv', ['bedroom_id', 'object_id'], bedrooms_objects)