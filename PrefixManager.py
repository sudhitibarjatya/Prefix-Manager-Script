import hou
from PySide2 import QtWidgets, QtCore

class PrefixManagerGui(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Prefix Manager")
        self.setMinimumWidth(700)
        self.setMinimumHeight(150)
        
        self.layout = QtWidgets.QVBoxLayout()
        self.action_layout = QtWidgets.QHBoxLayout()
        
        self.label = QtWidgets.QLabel("Enter Prefix")
        self.layout.addWidget(self.label)
        
        self.prefix_input = QtWidgets.QLineEdit()
        self.layout.addWidget(self.prefix_input)
        
        self.action_label = QtWidgets.QLabel("Select Action")
        self.action_layout.addWidget(self.action_label)
        
        self.action_dropdown = QtWidgets.QComboBox()
        self.action_dropdown.addItem("Assign New Prefix")
        self.action_dropdown.addItem("Change Prefix")
        self.action_layout.addWidget(self.action_dropdown)
        
        self.layout.addLayout(self.action_layout)
        
        self.add_button = QtWidgets.QPushButton("Add Prefix")
        self.layout.addWidget(self.add_button)
        
        self.undo_button = QtWidgets.QPushButton("Undo")
        self.undo_button.setEnabled(False)  
        self.layout.addWidget(self.undo_button)
        
        self.status_label = QtWidgets.QLabel("")
        self.layout.addWidget(self.status_label)
        
        self.add_button.clicked.connect(self.add_prefix_to_nodes)
        self.undo_button.clicked.connect(self.undo_changes)
        
        self.setLayout(self.layout)
        
        self.original_node_names = {}  
      
    def add_prefix_to_nodes(self):
        user_input = self.prefix_input.text()

        for char in user_input:
            if not (char.isalnum()):
                self.status_label.setText("Prefix should only contain alphanumeric characters and underscores.")
                return
        
        if not user_input.strip():
            self.status_label.setText("Error: Prefix cannot be empty!")
            return
        else:
            self.status_label.setText("")

        selected_nodes = hou.selectedNodes()
        
        if not selected_nodes:
            hou.ui.displayMessage("No Nodes Selected", title="Warning")
            return
            
        action = self.action_dropdown.currentText() 
        
        for node in selected_nodes:
            node_name = node.name()
            self.original_node_names[node] = node_name
        
        for node in selected_nodes:
            current_node_name = node.name()
            if action == "Assign New Prefix":
                new_name = user_input + "_" + current_node_name
                node.setName(new_name)
            else:
                parts = current_node_name.split("_", 1)
                part = parts[1]
                new_name = user_input + "_" + part
                node.setName(new_name)
        
        self.undo_button.setEnabled(True)  
    
    def undo_changes(self):
        for node, original_name in self.original_node_names.items():
            node.setName(original_name)
        
        self.status_label.setText("Undo completed.")
        self.undo_button.setEnabled(False)  

window = PrefixManagerGui()
window.show()