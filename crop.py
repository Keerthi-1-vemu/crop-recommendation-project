# Crop Recommendation Project
# Author: Keerthi

import csv

print("=== Crop Recommendation System ===")
print("Soil types: black, red, alluvial, sandy")
print("Rainfall: low, medium, high")
print("Temperature: hot, moderate")

soil = input("\nEnter soil type: ").lower()
rainfall = input("Enter rainfall: ").lower()
temperature = input("Enter temperature: ").lower()

found = False

with open('crops.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row['soil'] == soil and row['rainfall'] == rainfall and row['temperature'] == temperature:
            print(f"\n✅ Recommended Crop: {row['crop'].upper()}")
            print(f"Soil: {soil} | Rainfall: {rainfall} | Temperature: {temperature}")
            found = True
            break

if not found:
    print("\n❌ No exact match found. Try: black + high + hot = Cotton")

print("\nThank you! Project Completed.")