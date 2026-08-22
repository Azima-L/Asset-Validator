# Asset Validator

An **Asset Validation** tool built from scratch that validates 3D asset naming conventions with PySide6.

This project serves as my practical exploration of GUI programming in Python and foundational tool development for a **Pipeline / Tools Technical Artist** path.

---

## Features & Architecture (v0.3)

* **PySide6 GUI**: Implements a clean UI utilizing `QVBoxLayout`, responsive labels, and custom layout sizing.
* **Asset/File Naming Validation**: Programmatically enforces rule-based prefixes (`SM_`, `SK_`, `T_`), strict file extension matching (`.fbx`, `.png`), and character length constraints.
* **Dynamic UI Feedback**: Updates user labels on the fly with comprehensive test outcomes, detailing pass counts, failure counts, and naming violators.
* **Clean OOP Design**: Separates the GUI presentation code from the asset scanning validation rules for readability and future modularity.

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
3. Click the **Browse Folders** button.
4. The interface will instantly calculate and display the validation metric output directly in the app frame.

---

## License
Distributed under the MIT License. See `LICENSE` for details.