#!/usr/bin/env python3
"""
Dinosaur Speed Calculator

This script solves the "dinosaur CSV" problem by:
1. Reading dinosaur data from two CSV files
2. Calculating speed for each dinosaur using the formula:
   speed = ((stride_length / leg_length) - 1) * sqrt(leg_length * g)
   where g = 9.8 m/s^2
3. Filtering for bipedal dinosaurs only
4. Sorting by speed from fastest to slowest

Expected CSV format:
- dataset1.csv: NAME, LEG_LENGTH, DIET
- dataset2.csv: NAME, STRIDE_LENGTH, STANCE
"""

import csv
import math
import sys
from typing import Dict, List, Tuple, Optional


class DinosaurData:
    """Container for dinosaur information"""
    
    def __init__(self, name: str, leg_length: float, stride_length: float, 
                 diet: str, stance: str):
        self.name = name
        self.leg_length = leg_length
        self.stride_length = stride_length
        self.diet = diet
        self.stance = stance
        self._speed: Optional[float] = None
    
    @property
    def speed(self) -> float:
        """Calculate and cache dinosaur speed using the given formula"""
        if self._speed is None:
            g = 9.8  # gravitational constant
            if self.leg_length <= 0:
                raise ValueError(f"Invalid leg length for {self.name}: {self.leg_length}")
            
            # speed = ((stride_length / leg_length) - 1) * sqrt(leg_length * g)
            stride_ratio = self.stride_length / self.leg_length
            self._speed = (stride_ratio - 1) * math.sqrt(self.leg_length * g)
        
        return self._speed
    
    @property
    def is_bipedal(self) -> bool:
        """Check if dinosaur is bipedal"""
        return self.stance.lower() == 'bipedal'
    
    def __repr__(self) -> str:
        return (f"DinosaurData(name='{self.name}', speed={self.speed:.2f}, "
                f"stance='{self.stance}')")


class DinosaurSpeedCalculator:
    """Main class for processing dinosaur CSV data and calculating speeds"""
    
    def __init__(self):
        self.dinosaurs: Dict[str, DinosaurData] = {}
    
    def load_dataset1(self, filepath: str) -> None:
        """
        Load dataset1.csv containing: NAME, LEG_LENGTH, DIET
        """
        try:
            with open(filepath, 'r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                
                # Handle different possible column names
                for row in reader:
                    # Normalize column names (remove spaces, convert to uppercase)
                    normalized_row = {k.strip().upper(): v.strip() for k, v in row.items()}
                    
                    # Try different possible column name variations
                    name_key = self._find_column(normalized_row, ['NAME', 'DINOSAUR', 'SPECIES'])
                    leg_key = self._find_column(normalized_row, ['LEG_LENGTH', 'LEG LENGTH', 'LGLENGTH'])
                    diet_key = self._find_column(normalized_row, ['DIET', 'FOOD', 'EATING'])
                    
                    if not all([name_key, leg_key, diet_key]):
                        print(f"Warning: Could not find required columns in row: {row}")
                        continue
                    
                    name = normalized_row[name_key]
                    try:
                        leg_length = float(normalized_row[leg_key])
                    except ValueError:
                        print(f"Warning: Invalid leg length for {name}: {normalized_row[leg_key]}")
                        continue
                    
                    diet = normalized_row[diet_key]
                    
                    # Store partial dinosaur data
                    if name not in self.dinosaurs:
                        self.dinosaurs[name] = {
                            'name': name,
                            'leg_length': leg_length,
                            'diet': diet
                        }
                    else:
                        self.dinosaurs[name].update({
                            'leg_length': leg_length,
                            'diet': diet
                        })
                        
        except FileNotFoundError:
            raise FileNotFoundError(f"Could not find dataset1 file: {filepath}")
        except Exception as e:
            raise Exception(f"Error reading dataset1: {e}")
    
    def load_dataset2(self, filepath: str) -> None:
        """
        Load dataset2.csv containing: NAME, STRIDE_LENGTH, STANCE
        """
        try:
            with open(filepath, 'r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                
                for row in reader:
                    # Normalize column names
                    normalized_row = {k.strip().upper(): v.strip() for k, v in row.items()}
                    
                    # Try different possible column name variations
                    name_key = self._find_column(normalized_row, ['NAME', 'DINOSAUR', 'SPECIES'])
                    stride_key = self._find_column(normalized_row, ['STRIDE_LENGTH', 'STRIDE LENGTH', 'STRIDE'])
                    stance_key = self._find_column(normalized_row, ['STANCE', 'POSTURE', 'POSITION'])
                    
                    if not all([name_key, stride_key, stance_key]):
                        print(f"Warning: Could not find required columns in row: {row}")
                        continue
                    
                    name = normalized_row[name_key]
                    try:
                        stride_length = float(normalized_row[stride_key])
                    except ValueError:
                        print(f"Warning: Invalid stride length for {name}: {normalized_row[stride_key]}")
                        continue
                    
                    stance = normalized_row[stance_key]
                    
                    # Store or update dinosaur data
                    if name not in self.dinosaurs:
                        self.dinosaurs[name] = {
                            'name': name,
                            'stride_length': stride_length,
                            'stance': stance
                        }
                    else:
                        self.dinosaurs[name].update({
                            'stride_length': stride_length,
                            'stance': stance
                        })
                        
        except FileNotFoundError:
            raise FileNotFoundError(f"Could not find dataset2 file: {filepath}")
        except Exception as e:
            raise Exception(f"Error reading dataset2: {e}")
    
    def _find_column(self, row: Dict[str, str], possible_names: List[str]) -> Optional[str]:
        """Find a column by trying multiple possible names"""
        for name in possible_names:
            if name in row:
                return name
        return None
    
    def create_dinosaur_objects(self) -> List[DinosaurData]:
        """
        Create DinosaurData objects from loaded data
        Only include dinosaurs that have all required fields
        """
        complete_dinosaurs = []
        
        for name, data in self.dinosaurs.items():
            required_fields = ['name', 'leg_length', 'stride_length', 'diet', 'stance']
            
            if all(field in data for field in required_fields):
                try:
                    dinosaur = DinosaurData(
                        name=data['name'],
                        leg_length=data['leg_length'],
                        stride_length=data['stride_length'],
                        diet=data['diet'],
                        stance=data['stance']
                    )
                    complete_dinosaurs.append(dinosaur)
                except Exception as e:
                    print(f"Warning: Could not create dinosaur object for {name}: {e}")
            else:
                missing = [f for f in required_fields if f not in data]
                print(f"Warning: Incomplete data for {name}, missing: {missing}")
        
        return complete_dinosaurs
    
    def get_bipedal_dinosaurs_by_speed(self) -> List[DinosaurData]:
        """
        Get bipedal dinosaurs sorted by speed (fastest to slowest)
        """
        all_dinosaurs = self.create_dinosaur_objects()
        
        # Filter for bipedal dinosaurs only
        bipedal_dinosaurs = [d for d in all_dinosaurs if d.is_bipedal]
        
        if not bipedal_dinosaurs:
            print("Warning: No bipedal dinosaurs found in the data")
            return []
        
        # Sort by speed (descending - fastest first)
        try:
            bipedal_dinosaurs.sort(key=lambda d: d.speed, reverse=True)
        except Exception as e:
            print(f"Error calculating speeds: {e}")
            return []
        
        return bipedal_dinosaurs
    
    def print_results(self, dinosaurs: List[DinosaurData], show_details: bool = False) -> None:
        """Print the results in a formatted way"""
        if not dinosaurs:
            print("No bipedal dinosaurs found.")
            return
        
        print(f"\nBipedal Dinosaurs Sorted by Speed (Fastest to Slowest):")
        print("=" * 60)
        
        for i, dinosaur in enumerate(dinosaurs, 1):
            if show_details:
                print(f"{i:2d}. {dinosaur.name:<20} | Speed: {dinosaur.speed:8.2f} m/s | "
                      f"Leg: {dinosaur.leg_length:6.2f}m | Stride: {dinosaur.stride_length:6.2f}m")
            else:
                print(f"{i:2d}. {dinosaur.name}")
        
        print("=" * 60)
        print(f"Total bipedal dinosaurs: {len(dinosaurs)}")


def create_sample_data() -> None:
    """Create sample CSV files for testing"""
    
    # Sample dataset1.csv
    dataset1_data = [
        ["NAME", "LEG_LENGTH", "DIET"],
        ["Tyrannosaurus", "6.5", "Carnivore"],
        ["Triceratops", "3.2", "Herbivore"],
        ["Velociraptor", "1.8", "Carnivore"],
        ["Stegosaurus", "2.1", "Herbivore"],
        ["Allosaurus", "5.2", "Carnivore"],
        ["Brachiosaurus", "8.1", "Herbivore"]
    ]
    
    # Sample dataset2.csv
    dataset2_data = [
        ["NAME", "STRIDE_LENGTH", "STANCE"],
        ["Tyrannosaurus", "12.3", "Bipedal"],
        ["Triceratops", "8.7", "Quadrupedal"],
        ["Velociraptor", "4.1", "Bipedal"],
        ["Stegosaurus", "6.2", "Quadrupedal"],
        ["Allosaurus", "9.8", "Bipedal"],
        ["Brachiosaurus", "15.2", "Quadrupedal"]
    ]
    
    # Write sample files
    with open('dataset1.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(dataset1_data)
    
    with open('dataset2.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(dataset2_data)
    
    print("Sample CSV files created: dataset1.csv and dataset2.csv")


def main():
    """Main function to run the dinosaur speed calculator"""
    
    # Parse command line arguments
    if len(sys.argv) == 1:
        print("No CSV files provided. Creating sample data...")
        create_sample_data()
        dataset1_file = "dataset1.csv"
        dataset2_file = "dataset2.csv"
    elif len(sys.argv) == 3:
        dataset1_file = sys.argv[1]
        dataset2_file = sys.argv[2]
    else:
        print("Usage: python dinosaur.py [dataset1.csv] [dataset2.csv]")
        print("Or run without arguments to use sample data")
        sys.exit(1)
    
    # Process the data
    try:
        calculator = DinosaurSpeedCalculator()
        
        print(f"Loading dataset1 from: {dataset1_file}")
        calculator.load_dataset1(dataset1_file)
        
        print(f"Loading dataset2 from: {dataset2_file}")
        calculator.load_dataset2(dataset2_file)
        
        # Get bipedal dinosaurs sorted by speed
        bipedal_dinosaurs = calculator.get_bipedal_dinosaurs_by_speed()
        
        # Print results
        calculator.print_results(bipedal_dinosaurs, show_details=True)
        
        # Also print just the names (as requested in the problem)
        print("\nJust the names (fastest to slowest):")
        for dinosaur in bipedal_dinosaurs:
            print(dinosaur.name)
            
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

