#!/usr/bin/env python3
"""
Dinosaur Speed Calculator - Interview Version

Problem: Read two CSV files and calculate speeds of bipedal dinosaurs,
then sort them from fastest to slowest.

Formula: speed = ((stride_length / leg_length) - 1) * sqrt(leg_length * g)
where g = 9.8 m/s^2
"""

import csv
import math


def read_csv_to_dict(filename, key_column):
    """Read CSV file and return dictionary keyed by specified column"""
    data = {}
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            key = row[key_column]
            data[key] = row
    return data


def calculate_speed(leg_length, stride_length):
    """Calculate dinosaur speed using given formula"""
    g = 9.8  # gravitational constant
    return ((stride_length / leg_length) - 1) * math.sqrt(leg_length * g)


def solve_dinosaur_problem(dataset1_file, dataset2_file):
    """Main function to solve the dinosaur speed problem"""
    
    # Read both datasets
    dataset1 = read_csv_to_dict(dataset1_file, 'NAME')  # NAME, LEG_LENGTH, DIET
    dataset2 = read_csv_to_dict(dataset2_file, 'NAME')  # NAME, STRIDE_LENGTH, STANCE
    
    bipedal_speeds = []
    
    # Process each dinosaur that appears in both datasets
    for name in dataset1:
        if name in dataset2:
            # Get data from both datasets
            leg_length = float(dataset1[name]['LEG_LENGTH'])
            stride_length = float(dataset2[name]['STRIDE_LENGTH'])
            stance = dataset2[name]['STANCE']
            
            # Only process bipedal dinosaurs
            if stance.lower() == 'bipedal':
                speed = calculate_speed(leg_length, stride_length)
                bipedal_speeds.append((name, speed))
    
    # Sort by speed (descending - fastest first)
    bipedal_speeds.sort(key=lambda x: x[1], reverse=True)
    
    # Return just the names in order
    return [name for name, speed in bipedal_speeds]





if __name__ == "__main__":
    # Solve the problem
    result = solve_dinosaur_problem('dataset1.csv', 'dataset2.csv')
    
    print("Bipedal dinosaurs sorted by speed (fastest to slowest):")
    for i, name in enumerate(result, 1):
        print(f"{i}. {name}")


# Interview walkthrough version - step by step
def interview_solution():
    """
    Interview version with step-by-step explanation
    """
    print("=== Interview Solution Walkthrough ===")
    
    # Step 1: Read the data
    print("\n1. Reading CSV files...")
    dataset1 = read_csv_to_dict('dataset1.csv', 'NAME')
    dataset2 = read_csv_to_dict('dataset2.csv', 'NAME')
    print(f"   Dataset1 has {len(dataset1)} dinosaurs")
    print(f"   Dataset2 has {len(dataset2)} dinosaurs")
    
    # Step 2: Process and calculate speeds
    print("\n2. Processing dinosaurs...")
    results = []
    
    for name in dataset1:
        if name in dataset2:
            leg_length = float(dataset1[name]['LEG_LENGTH'])
            stride_length = float(dataset2[name]['STRIDE_LENGTH'])
            stance = dataset2[name]['STANCE']
            
            print(f"   {name}: leg={leg_length}m, stride={stride_length}m, stance={stance}")
            
            if stance.lower() == 'bipedal':
                speed = calculate_speed(leg_length, stride_length)
                results.append((name, speed))
                print(f"      -> Bipedal! Speed = {speed:.2f} m/s")
            else:
                print(f"      -> Quadrupedal, skipping")
    
    # Step 3: Sort by speed
    print("\n3. Sorting by speed (fastest first)...")
    results.sort(key=lambda x: x[1], reverse=True)
    
    print("\nFinal result:")
    for i, (name, speed) in enumerate(results, 1):
        print(f"{i}. {name} - {speed:.2f} m/s")
    
    return [name for name, speed in results]


# Uncomment to run interview walkthrough
# interview_solution()
