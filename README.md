# Algo Explorer - Visual Data Structures Playground

An interactive Python GUI application for visualizing and learning core data structures with animations and challenges.

## Features

### Data Structures (Implemented from Scratch)
- **Stack** - LIFO structure with push, pop, peek operations
- **Queue** - FIFO structure with enqueue, dequeue operations
- **Singly Linked List** - Dynamic list with insert, delete, search
- **Binary Search Tree** - Hierarchical structure with insert, delete, traversals

### Visualization
- Real-time animations for all operations
- Clean academic color scheme (blue/white/black)
- Interactive canvas with zoom and pan
- Step-by-step operation display

### Challenge Mode
Built-in challenges to test understanding:
- **Stack**: Reverse using recursion
- **Queue**: Implement queue using two stacks
- **Linked List**: Find middle node in one pass
- **BST**: Build balanced BST from sorted array

### Additional Features
- **Undo/Redo** - Full command history with Ctrl+Z/Ctrl+Y support
- **Recursion Visualization** - Step through recursive calls
- **Multiple Traversals** - Inorder, preorder, postorder for BST
- **Interactive Controls** - Button-based operations with value input

## Installation

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Install Dependencies

```bash
pip install -r requirements.txt
```

Or manually install PyQt5:

```bash
pip install PyQt5
```

## Running the Application

From the project directory:

```bash
python main.py
```

## Project Structure

```
algo_explorer/
├── main.py                          # Application entry point
├── requirements.txt                 # Dependencies
├── data_structures/                 # Data structure implementations
│   ├── stack.py
│   ├── queue.py
│   ├── linked_list.py
│   └── binary_search_tree.py
├── visuals/                         # Visualization components
│   ├── base_visualizer.py
│   ├── stack_visualizer.py
│   ├── queue_visualizer.py
│   ├── linked_list_visualizer.py
│   └── bst_visualizer.py
├── challenges/                      # Challenge mode logic
│   ├── challenge_manager.py
│   ├── stack_challenges.py
│   ├── queue_challenges.py
│   ├── linked_list_challenges.py
│   └── bst_challenges.py
└── ui/                             # PyQt5 interface
    ├── main_window.py
    ├── control_panel.py
    ├── animation_canvas.py
    └── commands.py
```

## Usage Guide

### Basic Operations

1. **Select a Data Structure Tab** - Choose from Stack, Queue, Linked List, or BST
2. **Enter a Value** - Type a value in the input field
3. **Perform Operations** - Click operation buttons (Insert, Delete, Search, etc.)
4. **View Visualization** - Watch the animated updates on the canvas

### Keyboard Shortcuts

- `Ctrl+Z` - Undo last operation
- `Ctrl+Y` - Redo last undone operation
- `Ctrl+Q` - Quit application

### Challenge Mode

1. Click "Start Challenge" in any tab
2. Read the challenge description and goal
3. Perform operations to complete the challenge
4. Click "Validate Solution" to check your answer
5. Use "Show Hint" if you need help

### Canvas Controls

- **Scroll Wheel** - Zoom in/out
- **Click and Drag** - Pan around the canvas

## Data Structure Operations

### Stack
- **Push** - Add element to top
- **Pop** - Remove top element
- **Peek** - View top element
- **Reverse** - Reverse stack using recursion
- **Clear** - Remove all elements

### Queue
- **Enqueue** - Add element to rear
- **Dequeue** - Remove front element
- **Front** - View front element
- **Clear** - Remove all elements

### Linked List
- **Insert at Head** - Add element at beginning
- **Insert at Tail** - Add element at end
- **Delete** - Remove specific value
- **Search** - Find element position
- **Find Middle** - Find middle using slow/fast pointers
- **Clear** - Remove all elements

### Binary Search Tree
- **Insert** - Add value to tree
- **Delete** - Remove value from tree
- **Search** - Find value in tree
- **Inorder Traversal** - Left, Root, Right
- **Preorder Traversal** - Root, Left, Right
- **Postorder Traversal** - Left, Right, Root
- **Clear** - Remove all nodes

## Extending the Application

### Adding New Data Structures

1. Create implementation in `data_structures/`
2. Create visualizer in `visuals/` extending `BaseVisualizer`
3. Create challenges in `challenges/`
4. Add tab in `ui/main_window.py`

### Adding New Challenges

1. Create challenge class extending `Challenge` in appropriate file
2. Implement `setup()`, `validate()`, and `get_solution_steps()`
3. Register in `MainWindow._register_challenges()`

## Technical Details

### Architecture
- **MVC Pattern** - Separation of data structures, visualization, and UI
- **Command Pattern** - Undo/redo implementation
- **Observer Pattern** - Signal-slot communication in PyQt5

### Design Principles
- Clean, modular code with type hints
- Comprehensive docstrings for all classes and methods
- Academic color scheme for clarity
- Extensible architecture for future enhancements

## License

Educational project - free to use and modify.

## Credits

Built with Python and PyQt5 for educational purposes.
