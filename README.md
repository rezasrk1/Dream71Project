# Dream71Project

This project includes automation scripts to assist with NGO registration and renewal processes in Bangladesh. It generates structured Excel files based on FD-9 and other registration form requirements.

## 📁 Contents

- `generate_excel_FD9.py` - Script to generate an FD-9 Excel form.
- `Renew_Registration.py` - Script to generate a renewal registration form in Excel.
- `FD9_form.xlsx` - Auto-generated Excel file containing required FD-9 fields.
- `renewal_registration.xlsx` - Auto-generated Excel file for NGO renewal (optional, generated after running the script).

## 📌 Requirements

- Python 3.10+
- Required libraries:
  - `pandas`
  - `openpyxl`

You can install them using:


pip install pandas openpyxl
▶️ Usage
Clone the repository:

bash
Copy
Edit
git clone https://github.com/rezasrk1/Dream71Project.git
cd Dream71Project
Run a script to generate the Excel file:


python generate_excel_FD9.py
# or
python Renew_Registration.py
The generated Excel file will be saved in the root directory of the project.

🧾 Purpose
This project is intended to streamline form generation for NGOs in Bangladesh who require digital assistance for document submission, particularly with the NGO Affairs Bureau (NGOAB).

📬 Contact
Maintained by: Md Saiful Islam
Email: md.saiful.islam7@g.bracu.ac.bd
