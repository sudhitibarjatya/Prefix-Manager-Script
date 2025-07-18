# Prefix-Manager-Script
A user-friendly PySide2-based tool for managing node prefixes in Houdini.

**Features**:
- Assign new prefixes to selected nodes.
- Change an existing prefix while keeping the rest of the node name intact.
- Undo recent changes to revert node names.
- Input validation for alphanumeric characters and underscores.
- Real-time status feedback for successful or failed operations.

#### **Usage**:
1. Select the nodes in Houdini.
2. Enter the desired prefix.
3. Choose the action: assign or change prefix.
4. Click "Add Prefix" to apply changes.
5. Use "Undo" to revert changes if needed.

#### **Installation**:
1. Download the script file from the repository.
2. Create a new shelf tool in Houdini.
3. Edit the new tool and add the script in the python module under the script tab.

## Prerequisites
- **Houdini** (with Karma rendering support for relevant tools).
- **PySide2** (for GUI-based scripts).

## Contribution
Contributions are welcome! Feel free to submit pull requests or raise issues for any suggestions or bugs.

## Acknowledgments
- **PolyHaven** for their open-access library and public API.
- The Houdini community for inspiring innovative tools and workflows.
