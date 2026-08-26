# Asset Validator

An **Asset Validation** tool built from scratch that validates asset naming conventions within a folder with PySide6.

This project serves as my practical exploration of GUI programming in Python and foundational tool development for a **Pipeline / Tools Technical Artist** path.

---

## Features & Architecture (v0.6)

* **PySide6 (Qt) GUI Framework**: Built a standalone GUI utilizing `QVBoxLayout` for structured element alignment. A clean, smooth, and easy interface allows the tool to dock inside a software like DCC and game engines (Maya, Blender, Houdini, or Unreal Engine).
* **Custom Validation Rules:** Allows users —— like TDs and artists —— to define custom naming conventions (prefixes and extensions) to match specific project needs.
* **Real-Time Visual Feedback:** Instantly colour-codes files (Green for valid, Red for invalid) within a GUI list view, enabling immediate identification of naming errors.
* **Production Log Exporting:** Generates structured `.txt` validation reports detailing compliant and non-compliant assets, crucial for pipeline tracking, automated ingestion prep, and team/department feedback.
* **Error Prevention:** Built-in safeguards with basic exception and attribute handling to prevent the app from crashing if users attempt to export a report before choosing a folder.

---

## Prerequisites

* Python 3.10+ installed on your machine.
* pip install PySide6

---

## System Architecture

```text
├── asset_validator.py      # Primary PySide6 application containing everything (UI and validation logic)
├── README.md               # Project documentation and developer overview
├── LICENSE                 # MIT Licensing details
└── .gitignore              # Python .gitignore details
```

---

## How to Use

Simply launch the application script via your command line interface:

```bash
python asset_validator.py
```
1. Open `asset_validator.py` file.
2. Run the program and the application window titled **Asset Validator** will pop up.
3. Fill in the required prefixes and file extensions you want to flag in the text input field.
4. Click the **Browse Folders** button.
5. The interface will instantly display and flag assets that do not meet your intended criteria in the app frame.
6. You can also create a report log of your files once you have validated your assets by clicking the **Export Log** button.

---

## License
Distributed under the MIT License. See `LICENSE` for details.