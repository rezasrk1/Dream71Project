import pandas as pd

# Define the data for the new sheet again after reset
data = {
    "S. No": list(range(1, 21)),
    "Attribute Name": [
        "Name of Organization with Address",
        "Address",
        "Registration Number",
        "Address of the Principal/Head Office",
        "Telephone Number",
        "Mobile Number",
        "Email Address",
        "Website",
        "Name (Head of Organization)",
        "Whether Full-time or Part-time",
        "Address (Head of Organization)",
        "Nationality (Head of Organization)",
        "Telephone Number (Head of Organization)",
        "Mobile Number (Head of Organization)",
        "Email (Head of Organization)",
        "Citizenship (Head of Organization)",
        "Head of the Organization Name",
        "Head of the Organization Title",
        "Digital Signature",
        "Digital Seal"
    ],
    "Mandatory": ["Yes"] * 20,
    "Component": [
        "Text", "Text", "Text", "Text", "Text", "Text", "Text", "Text", "Text", "Dropdown",
        "Text", "Dropdown", "Text", "Text", "Text", "Dropdown", "Text", "Text", "File Upload", "File Upload"
    ],
    "Notes": [
        "Full name and address of the organization in Bangladesh.",
        "Detailed address, e.g., block, city, area (may be redundant with Name of Organization with Address).",
        "NGO registration number issued by the NGO Affairs Bureau (e.g., 5-digit format).",
        "Address of the main office, may differ from local office.",
        "Landline number, including country/area code.",
        "Mobile number, including country code.",
        "Official email address for communication.",
        "Organization’s website URL (e.g., www.abc.com); enter \"N/A\" if none.",
        "Full name of the head of the organization in Bangladesh.",
        "Options: Full Time, Part Time.",
        "Residential or official address of the head in Bangladesh.",
        "Select from extensive list of nationalities (e.g., Bangladeshi, American, etc.).",
        "Landline number, may be same as organization’s.",
        "Mobile number, may be same as organization’s.",
        "Personal or official email of the head.",
        "Select from extensive list of citizenships (over 190 options, e.g., Bangladeshi, Welsh, etc.).",
        "Full name of the organization’s chief executive (may overlap with Name in row 9).",
        "Designation, e.g., Deputy Project Manager, Director.",
        "PNG format, 300x80 pixels, max 60 KB.",
        "PNG format, 300x100 pixels, max 80 KB."
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to Excel file
file_path = "D:/Dream71Project/FD9_Organization_Info.xlsx"
df.to_excel(file_path, index=False)

file_path
