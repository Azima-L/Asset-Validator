from PySide6.QtWidgets import QApplication, QWidget, QFileDialog, QLineEdit, QLabel, QListWidget, QListWidgetItem, QPushButton, QVBoxLayout
from PySide6.QtGui import QColor
import sys
import os

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Asset Validator")
        self.setFixedSize(400, 400)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.label = QLabel("Simply type in your custom prefixes and extensions below \nthen click Browse Folders\n")
        layout.addWidget(self.label)

        self.prefix_input = QLineEdit()
        self.prefix_input.setPlaceholderText("Prefixes: SM_, SK_, T_")
        layout.addWidget(self.prefix_input)

        self.extension_input = QLineEdit()
        self.extension_input.setPlaceholderText("Extensions: .blend, .fbx, .png")
        layout.addWidget(self.extension_input)

        self.label2 = QLabel("\nYour files:")
        layout.addWidget(self.label2)

        self.list_widget = QListWidget()
        layout.addWidget(self.list_widget)

        button = QPushButton("Browse Folders")
        button.clicked.connect(self.run_validator)
        layout.addWidget(button)

        button2 = QPushButton("Export Log")
        button2.clicked.connect(self.export_log)
        layout.addWidget(button2)

    def is_valid_asset_name(self, file_name):
        prefix_text = self.prefix_input.text()
        extension_text = self.extension_input.text()

        if not prefix_text or not extension_text:
            return False

        prefixes = tuple(p.strip() for p in prefix_text.split(","))
        extensions = tuple(e.strip() for e in extension_text.split(","))

        if not file_name.startswith(prefixes):
            return False
        if not file_name.endswith(extensions):
            return False
        return True

    def run_validator(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Asset Folder")

        if not folder:
            self.list_widget.clear()
            self.label.setText("No folder selected.\n")
            return

        self.files = os.listdir(folder)
        self.valid_counter = 0
        self.invalid_counter = 0
        assets = []

        for file in self.files:
            item = QListWidgetItem(file)
            assets.append(item)
            if self.is_valid_asset_name(file):
                item.setForeground(QColor("green"))
                self.valid_counter += 1
            else:
                item.setForeground(QColor("red"))
                self.invalid_counter += 1

        self.label.setText(f"{self.valid_counter} valid, {self.invalid_counter} invalid.\n")

        self.list_widget.clear()
        for asset in assets:
            self.list_widget.addItem(asset)

    def export_log(self):
        path, _ = QFileDialog.getSaveFileName(
            self,
            "Save Log File",
            "validation_log.txt",
            "Text Files (*.txt)"
        )

        if path:
            try:
                with open(path, "w") as f:
                    f.write("Asset Validation Report\n")
                    f.write("=======================\n")
                    for file in self.files:
                        if self.is_valid_asset_name(file):
                            f.write(f"{file} - VALID\n")
                        else:
                            f.write(f"{file} - INVALID\n")
                    f.write(f"\nSummary: {self.valid_counter} valid, {self.invalid_counter} invalid.")
                print("System Update: Asset Validation Report has been created.")
            except AttributeError:
                self.label.setText("Error: Run validation first\n")
                print("System Update: Error: Run validation first")


app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec()