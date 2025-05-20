import csv
import os

# Ensure the directory exists
output_dir = r"D:\Dream71Project\Product_traceability"
os.makedirs(output_dir, exist_ok=True)

# Data for Crop Farm Create Form attributes
data = [
    ["S. No", "Attribute Name", "Mandatory", "Component", "Notes"],
    [1, "Farm Type", "Yes", "Dropdown", "Select from predefined farm types (e.g., crop, livestock)."],
    [2, "Farm Name", "Yes", "Text", "English name of the farm."],
    [3, "Farm Name Bangla", "Yes", "Text", "Bangla name of the farm."],
    [4, "Farmer Name", "Yes", "Dropdown", "Select from a list of registered farmers."],
    [5, "Producer Group", "Yes", "Dropdown", "Select from a list of producer groups."],
    [6, "Date of Establishment", "Yes", "Date", "Date the farm was established, format: DD-MM-YYYY."],
    [7, "Manpower Involved", "Yes", "Text/Number", "Number or description of personnel involved in farm operations."],
    [8, "Area of Farm", "Yes", "Text/Number", "Farm size (e.g., in acres or hectares)."],
    [9, "Service Provider Type", "Yes", "Dropdown", "Select from predefined service provider types (e.g., agricultural, technical)."],
    [10, "Service Provider", "No", "Text/Dropdown", "Name or selection of the service provider; may be optional if not specified."],
    [11, "Farming System", "No", "Dropdown", "Select from predefined farming systems (e.g., organic, conventional)."],
    [12, "Cultivation Method", "No", "Dropdown", "Select from predefined cultivation methods (e.g., traditional, modern)."],
    [13, "Latitude", "Yes", "Text/Number", "Geographic latitude of the farm (e.g., decimal degrees)."],
    [14, "Longitude", "Yes", "Text/Number", "Geographic longitude of the farm (e.g., decimal degrees)."],
    [15, "Division", "No", "Dropdown", "Select from administrative divisions (e.g., Dhaka, Chittagong)."],
    [16, "District", "No", "Dropdown", "Select from districts within the chosen division."],
    [17, "Upazila", "No", "Dropdown", "Select from upazilas within the chosen district."],
    [18, "Union", "No", "Dropdown", "Select from unions within the chosen upazila."],
    [19, "Trade License Image", "Yes", "File Upload", "Image of trade license, max size not specified, assume standard formats (e.g., PNG, JPG)."],
    [20, "Farm Image", "Yes", "File Upload", "Image of the farm, max size not specified, assume standard formats (e.g., PNG, JPG)."]
]

# Write to CSV file at specified path
output_path = os.path.join(output_dir, "crop_farm_form.csv")
with open(output_path, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f"CSV file 'crop_farm_form.csv' has been created successfully at {output_path}.")