from PySide6.QtWidgets import QApplication, QWidget, QLabel, QListWidget, QPushButton, QVBoxLayout
import sys

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Asset Validator")
        self.setFixedSize(400, 200)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.label = QLabel("Press Run to validate assets")
        layout.addWidget(self.label)

        self.list_widget = QListWidget()
        layout.addWidget(self.list_widget)

        button = QPushButton("Run Validator")
        button.clicked.connect(self.run_validator)
        layout.addWidget(button)

    def is_valid_asset_name(self, file_name):
        if not file_name.startswith(("SM_", "SK_", "T_")):
            return False
        if not file_name.endswith((".fbx", ".png")):
            return False
        if len(file_name) < 9:
            return False
        return True

    def run_validator(self):
        assets = [
            "SM_Rock.fbx",
            "rock.fbx",
            "T_.png",
            "SK_Hero.png",
            "SM_Tree.obj"
            ]

        valid_counter = 0
        invalid_counter = 0
        failed_files = []

        for asset in assets:
            if self.is_valid_asset_name(asset):
                valid_counter += 1
            else:
                failed_files.append(asset)
                invalid_counter += 1

        self.label.setText(f"{valid_counter} valid, {invalid_counter} invalid:\n"
                           "\nInvalid files:")

        self.list_widget.clear()
        for failed_file in failed_files:
            self.list_widget.addItem(failed_file)
    

app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec()