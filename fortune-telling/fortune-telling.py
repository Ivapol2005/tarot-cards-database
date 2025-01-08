import random
import json

def generate_celtic_cross_readings(num_readings: int) -> list:
    readings = []
    
    for _ in range(num_readings):
        reading = {}
        
        # Assign a random tarot card (0-77) and if it's reversed or not
        for position in range(1, 11):  # Positions 1 to 10
            reading[str(position)] = {
                "cardNumber": random.randint(0, 77),
                "ifReversed": random.choice([True, False])  # 50% chance to be reversed
            }
        
        readings.append(reading)
    
    return readings

# Generate 77,777 readings
celtic_cross_readings = generate_celtic_cross_readings(77777)

# Save to JSON file
with open("celtic_cross_readings.json", "w") as json_file:
    json.dump(celtic_cross_readings, json_file, indent=4)

print("Celtic Cross readings saved to celtic_cross_readings.json successfully!")

