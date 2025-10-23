"""
Algo Explorer - Visual Data Structures Playground

Main entry point for the application.

Features:
- Stack, Queue, Linked List, Binary Search Tree implementations
- Interactive visualizations with animations
- Challenge mode with built-in problems
- Undo/Redo functionality
- Recursion step-through visualization

Usage:
    python main.py
"""

import sys
from PyQt5.QtWidgets import QApplication
from ui.main_window import MainWindow


def main():
    """Main entry point for Algo Explorer."""
    # Create application
    app = QApplication(sys.argv)
    app.setApplicationName("Algo Explorer")

    # Create and show main window
    window = MainWindow()
    window.show()

    # Run event loop
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
