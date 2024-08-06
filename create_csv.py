import csv

# Data for bedrooms
bedrooms = [
    {'bedroom_id': 1, 'title': "Lego Bedroom", 'description': "Dive into a world of creativity and fun in the Lego Bedroom! This vibrant and colorful room is adorned with Lego-themed decor, from bedding to wall art, perfect for any young builder. Whether you're constructing your next masterpiece or enjoying a good night's sleep, this bedroom sparks imagination and joy.", 'img_src': "images/lego.jpg"},
    {'bedroom_id': 2, 'title': "Princess Bedroom", 'description': "Enter a magical realm of elegance and charm in the Princess Bedroom. With soft pastel colors, fairy-tale decor, and luxurious bedding fit for royalty, this enchanting space is perfect for any little princess. Let dreams take flight in this regal sanctuary.", 'img_src': "images/princess.jpg"},
    {'bedroom_id': 3, 'title': "Racecar Bedroom", 'description': "Rev up the excitement in the Racecar Bedroom! Designed for speed enthusiasts, this room features racecar-themed decor, dynamic wall art, and a bed that resembles a sleek racecar. Perfect for young racers who dream of crossing the finish line in first place.", 'img_src': "images/racecar.jpg"},
    {'bedroom_id': 4, 'title': "Space Bedroom", 'description': "Blast off into an intergalactic adventure in the Space Bedroom! This cosmic room is adorned with space-themed decor, including stars, planets, and rockets, creating an out-of-this-world experience. Perfect for aspiring astronauts and space explorers.", 'img_src': "images/space.jpg"},
    {'bedroom_id': 5, 'title': "Y2K Bedroom", 'description': "Step back into the vibrant and quirky era of the early 2000s with the Y2K Bedroom. Featuring bold colors, funky patterns, and nostalgic decor, this room captures the essence of the turn-of-the-millennium style. With posters of iconic boy bands like *NSYNC and Backstreet Boys adorning the walls. Relive the Y2K craze in this trendy and nostalgic space.", 'img_src': "images/y2k.jpg"}
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