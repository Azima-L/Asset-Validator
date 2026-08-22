from PySide6.QtWidgets import QApplication, QWidget, QFileDialog, QLabel, QListWidget, QPushButton, QVBoxLayout
import sys
import os

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Asset Validator")
        self.setFixedSize(400, 200)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.label = QLabel("Press Browse Folders to validate assets")
        layout.addWidget(self.label)

        self.list_widget = QListWidget()
        layout.addWidget(self.list_widget)

        button = QPushButton("Browse Folders")
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
        folder = QFileDialog.getExistingDirectory(self, "Select Asset Folder")

        if not folder:
            self.list_widget.clear()
            self.label.setText("No folder selected.")
            return

        files = os.listdir(folder)
        valid_counter = 0
        invalid_counter = 0
        failed_files = []

        for file in files:
            if self.is_valid_asset_name(file):
                valid_counter += 1
            else:
                failed_files.append(file)
                invalid_counter += 1

        self.label.setText(f"{valid_counter} valid, {invalid_counter} invalid.\n"
                           "\nInvalid files:")

        self.list_widget.clear()
        for failed_file in failed_files:
            self.list_widget.addItem(failed_file)
    

app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec()