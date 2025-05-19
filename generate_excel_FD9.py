import pandas as pd

# Data for the spreadsheet
data = [
    [1, "Foreign Citizen’s Name (in English, Capital Letters)", "Yes", "Text", "Full name as per passport, in capital letters."],
    [2, "Passport Size Photo", "Yes", "File Upload", "Maximum 200 KB, PNG format. Recent photo required."],
    [3, "Passport Copy", "Yes", "File Upload", "Maximum 1 MB. Scanned copy of passport data page."],
    [4, "Father’s Name", "Yes", "Text", "Full name of the father."],
    [5, "Spouse’s Name", "Yes", "Text", "Full name of spouse; enter “N/A” if not applicable."],
    [6, "Mother’s Name", "Yes", "Text", "Full name of the mother."],
    [7, "Place and Date of Birth", "Yes", "Text/Date", "Format: Place (e.g., City, Country), Date (DD-MM-YYYY)."],
    [8, "Passport Number", "Yes", "Text", "Passport number as shown in the document."],
    [9, "Passport Issue Date", "Yes", "Date", "Format: DD-MM-YYYY."],
    [10, "Passport Expiry Date", "Yes", "Date", "Format: DD-MM-YYYY."],
    [11, "Identifying Mark in Passport", "Yes", "Text", "Any distinguishing mark noted in the passport (e.g., scar, tattoo)."],
    [12, "Gender", "Yes", "Dropdown", "Options: Male, Female."],
    [13, "Marital Status", "Yes", "Text/Dropdown", "Options: Married, Unmarried, Divorced, Widowed."],
    [14, "Nationality/Citizenship", "Yes", "Text/Dropdown", "Current nationality (e.g., USA, UK)."],
    [15, "Details of Multiple Citizenship (if any)", "No", "Text", "Specify if the individual holds multiple citizenships."],
    [16, "Reason for Termination of Previous Citizenship (if applicable)", "Yes", "Text", "Enter “N/A” if not applicable."],
    [17, "Current Address", "Yes", "Text", "Full address including city, country, and postal code."],
    [18, "Number of Family Members", "Yes", "Number", "Total number of family members accompanying the individual."],
    [19, "Names and Ages of Family Members (accompanying)", "Yes", "Table/Text", "List names and ages."],
    [20, "Academic Qualifications", "Yes", "Text/File Upload", "Details of degrees; attach certificate copies (Max 1 MB)."],
    [21, "Technical and Other Qualifications (if any)", "No", "Text/File Upload", "List certifications or skills; attach relevant certificates."],
    [22, "Past Experience and Expertise in Proposed Role", "Yes", "Text/File Upload", "Describe relevant work experience; attach proof (Max 1 MB)."],
    [23, "Countries Visited for Employment", "Yes", "Dropdown/Multi-select", "Select from provided list."],
    [24, "Designation Proposed for Appointment", "Yes", "Text", "Job title/role."],
    [25, "Appointment Letter", "Yes", "File Upload", "Copy of appointment letter (Max 1 MB)."],
    [26, "Contract Letter", "Yes", "File Upload", "Copy of employment contract (Max 1 MB)."],
    [27, "Project Name and Duration", "Yes", "Text/File Upload", "Name and duration; attach Bureau’s approval letter (Max 1 MB)."],
    [28, "Appointment Date and Type", "Yes", "Date/Dropdown", "Type: New, Replacement, Extension, Ongoing."],
    [29, "Extension Duration (if applicable)", "No", "Text", "Specify if appointment is an extension."],
    [30, "Number of Foreign Positions in Project", "Yes", "Number", "Total positions allocated."],
    [31, "Number of Foreigners Currently Employed in Project", "Yes", "Number", "Total number working now."],
    [32, "Previous Employment in Bangladesh (if any)", "No", "Text", "Leave blank if none."],
    [33, "Number of Foreign Citizens Currently Employed in Organization", "Yes", "Number", "Total foreign employees in the organization."],
    [34, "Additional Information (if any)", "No", "Text/File Upload", "Any other relevant details."],
    [35, "Chief Executive’s Name", "Yes", "Text", "Full name of the chief executive."],
    [36, "Chief Executive’s Designation", "Yes", "Text", "Job title of the chief executive (e.g., Director)."],
    [37, "Digital Signature", "Yes", "File Upload", "PNG format, 300x80 pixels, Max 60 KB."],
    [38, "Digital Seal", "Yes", "File Upload", "PNG format, 300x100 pixels, Max 80 KB."]
]

# Create DataFrame
df = pd.DataFrame(data, columns=["S. No", "Attribute Name", "Mandatory", "Component", "Notes"])

# Save to Excel
file_path = "D:/Dream71Project/FD9_Organization_Info.xlsx"
df.to_excel(file_path, index=False)

file_path
