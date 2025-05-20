import csv
import os

# Ensure the directory exists
output_dir = r"D:\Dream71Project"
os.makedirs(output_dir, exist_ok=True)

# Data for FD-9.1 form attributes
data = [
    ["S. No", "Attribute Name", "Mandatory", "Component", "Notes"],
    [1, "NGO Affairs Bureau Memo Number", "Yes", "Text", "Reference number of the NGO Affairs Bureau’s memo."],
    [2, "Memo Date", "Yes", "Date", "Date of the memo, format: DD-MM-YYYY."],
    [3, "Name of Organization", "Yes", "Text", "Full name of the NGO (e.g., as registered with NGOAB)."],
    [4, "Project Name", "Yes", "Text", "Name of the project under which the foreign expert/advisor/officer/volunteer is hired."],
    [5, "Designation of Foreign Expert/Advisor/Officer/Volunteer", "Yes", "Text", "Role (e.g., Expert, Advisor, Officer, Volunteer) of the foreign individual."],
    [6, "Name of Foreign Expert/Advisor/Officer/Volunteer", "Yes", "Text", "Full name of the foreign individual applying for the work permit."],
    [7, "Start Date of Appointment", "Yes", "Date", "Start date of employment, format: DD-MM-YYYY."],
    [8, "End Date of Appointment", "Yes", "Date", "End date of employment, format: DD-MM-YYYY."],
    [9, "Appointment Letter Verification Proof", "Yes", "File Upload", "Maximum 500 KB, proof of verified appointment letter."],
    [10, "Copy of FD-9 Form", "Yes", "File Upload", "Maximum 500 KB, copy of the submitted FD-9 form."],
    [11, "Photo", "Yes", "File Upload", "Maximum 200 KB, PNG format, recent passport-size photo."],
    [12, "N-Visa Arrival Date with Proof", "Yes", "Date/File Upload", "Date of arrival with N-Visa, proof document (max 500 KB)."],
    [13, "Head of the Organization Name", "Yes", "Text", "Full name of the organization’s chief executive."],
    [14, "Head of the Organization Title", "Yes", "Text", "Designation, e.g., Director, Deputy Project Manager."],
    [15, "Digital Signature", "Yes", "File Upload", "PNG format, 300x80 pixels, max 60 KB."],
    [16, "Digital Seal", "Yes", "File Upload", "PNG format, 300x100 pixels, max 80 KB."]
]

# Write to CSV file at specified path
output_path = os.path.join(output_dir, "fd9_1_form.csv")
with open(output_path, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f"CSV file 'fd9_1_form.csv' has been created successfully at {output_path}.")