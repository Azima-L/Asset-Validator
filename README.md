# Asset Validator

An **Asset Validation** tool built from scratch that validates 3D asset naming conventions with PySide6.

This project serves as my practical exploration of GUI programming in Python and foundational tool development for a **Pipeline / Tools Technical Artist** path.

---

## ✨ Features & Architecture

* **PySide6 GUI**: Implements a clean UI utilizing `QVBoxLayout`, responsive labels, and custom layout sizing.
* **Granular Validation Engine**: Programmatically enforces rule-based prefixes (`SM_`, `SK_`, `T_`), strict file extension matching (`.fbx`, `.png`), and character length constraints.
* **Dynamic UI Feedback**: Updates user labels on the fly with comprehensive test outcomes, detailing pass counts, failure counts, and naming violators.
* **Clean OOP Design**: Separates the GUI presentation code from the asset scanning validation rules for readability and future modularity.

---

## 📁 System Architecture

```text
├── asset_validator.py      # Primary PySide6 application containing UI and validation logic
├── README.md               # Project documentation and developer overview
└── LICENSE                 # MIT Licensing details
```

---

## Prerequisites
* Python 3.10+ installed on your machine.
* pip install PySide6

---

## 💻 How to Use

Simply launch the application script via your command line interface:

```bash
python asset_validator.py
```

1. The application window will open titled **Asset Validator**.
2. Click the **Run Validator** button.
3. The interface will instantly calculate and display the validation metric output directly in the app frame.

---

## License
Distributed under the MIT License. See `LICENSE` for details.