"""Binary Search Tree data structure implementation."""
from typing import Any, List, Optional
import copy


class TreeNode:
    """
    Node for binary search tree.

    Attributes:
        data: Value stored in the node
        left: Reference to left child
        right: Reference to right child
    """

    def __init__(self, data: Any):
        """
        Initialize a tree node with data.

        Args:
            data: Value to store in the node
        """
        self.data: Any = data
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None

    def __str__(self) -> str:
        """String representation of the node."""
        return f"TreeNode({self.data})"

    def __repr__(self) -> str:
        """Detailed representation of the node."""
        return f"TreeNode(data={self.data})"


class BinarySearchTree:
    """
    Binary Search Tree data structure.

    Attributes:
        root: Reference to the root node
        size_count: Number of nodes in the tree
    """

    def __init__(self):
        """Initialize an empty binary search tree."""
        self.root: Optional[TreeNode] = None
        self.size_count: int = 0

    def insert(self, data: Any) -> None:
        """
        Insert a value into the tree.

        Args:
            data: Value to insert
        """
        if self.root is None:
            self.root = TreeNode(data)
            self.size_count += 1
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, node: TreeNode, data: Any) -> None:
        """
        Recursively insert a value into the tree.

        Args:
            node: Current node in the recursion
            data: Value to insert
        """
        if data < node.data:
            if node.left is None:
                node.left = TreeNode(data)
                self.size_count += 1
            else:
                self._insert_recursive(node.left, data)
        elif data > node.data:
            if node.right is None:
                node.right = TreeNode(data)
                self.size_count += 1
            else:
                self._insert_recursive(node.right, data)
        # If data == node.data, ignore (no duplicates)

    def search(self, data: Any) -> bool:
        """
        Search for a value in the tree.

        Args:
            data: Value to search for

        Returns:
            True if found, False otherwise
        """
        return self._search_recursive(self.root, data)

    def _search_recursive(self, node: Optional[TreeNode], data: Any) -> bool:
        """
        Recursively search for a value.

        Args:
            node: Current node in the recursion
            data: Value to search for

        Returns:
            True if found, False otherwise
        """
        if node is None:
            return False
        if data == node.data:
            return True
        elif data < node.data:
            return self._search_recursive(node.left, data)
        else:
            return self._search_recursive(node.right, data)

    def delete(self, data: Any) -> bool:
        """
        Delete a value from the tree.

        Args:
            data: Value to delete

        Returns:
            True if deleted, False if not found
        """
        if not self.search(data):
            return False
        self.root = self._delete_recursive(self.root, data)
        return True

    def _delete_recursive(self, node: Optional[TreeNode], data: Any) -> Optional[TreeNode]:
        """
        Recursively delete a value from the tree.

        Args:
            node: Current node in the recursion
            data: Value to delete

        Returns:
            Updated node after deletion
        """
        if node is None:
            return None

        if data < node.data:
            node.left = self._delete_recursive(node.left, data)
        elif data > node.data:
            node.right = self._delete_recursive(node.right, data)
        else:
            # Node with only one child or no child
            if node.left is None:
                self.size_count -= 1
                return node.right
            elif node.right is None:
                self.size_count -= 1
                return node.left

            # Node with two children: get inorder successor
            min_larger_node = self._find_min(node.right)
            node.data = min_larger_node.data
            node.right = self._delete_recursive(node.right, min_larger_node.data)

        return node

    def _find_min(self, node: TreeNode) -> TreeNode:
        """
        Find the minimum value node in a subtree.

        Args:
            node: Root of the subtree

        Returns:
            Node with minimum value
        """
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder_traversal(self) -> List[Any]:
        """
        Perform inorder traversal (left, root, right).

        Returns:
            List of values in inorder sequence
        """
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node: Optional[TreeNode], result: List[Any]) -> None:
        """Helper for inorder traversal."""
        if node is not None:
            self._inorder_recursive(node.left, result)
            result.append(node.data)
            self._inorder_recursive(node.right, result)

    def preorder_traversal(self) -> List[Any]:
        """
        Perform preorder traversal (root, left, right).

        Returns:
            List of values in preorder sequence
        """
        result = []
        self._preorder_recursive(self.root, result)
        return result

    def _preorder_recursive(self, node: Optional[TreeNode], result: List[Any]) -> None:
        """Helper for preorder traversal."""
        if node is not None:
            result.append(node.data)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)

    def postorder_traversal(self) -> List[Any]:
        """
        Perform postorder traversal (left, right, root).

        Returns:
            List of values in postorder sequence
        """
        result = []
        self._postorder_recursive(self.root, result)
        return result

    def _postorder_recursive(self, node: Optional[TreeNode], result: List[Any]) -> None:
        """Helper for postorder traversal."""
        if node is not None:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.data)

    def is_empty(self) -> bool:
        """Check if the tree is empty."""
        return self.root is None

    def size(self) -> int:
        """Return the number of nodes in the tree."""
        return self.size_count

    def clear(self) -> None:
        """Remove all nodes from the tree."""
        self.root = None
        self.size_count = 0

    def get_state(self) -> dict:
        """
        Get the current state for serialization.

        Returns:
            Dictionary containing the tree state
        """
        return {
            "items": self.preorder_traversal(),
            "size": self.size_count
        }

    def set_state(self, state: dict) -> None:
        """
        Restore the tree from a saved state.

        Args:
            state: Dictionary containing the tree state
        """
        self.clear()
        for item in state["items"]:
            self.insert(item)

    @staticmethod
    def build_balanced_from_sorted(sorted_array: List[Any]) -> 'BinarySearchTree':
        """
        Build a balanced BST from a sorted array.
        Used for challenge mode.

        Args:
            sorted_array: Sorted list of values

        Returns:
            Balanced binary search tree
        """
        bst = BinarySearchTree()
        bst.root = BinarySearchTree._build_balanced_recursive(sorted_array, 0, len(sorted_array) - 1)
        bst.size_count = len(sorted_array)
        return bst

    @staticmethod
    def _build_balanced_recursive(arr: List[Any], start: int, end: int) -> Optional[TreeNode]:
        """
        Recursively build balanced tree from sorted array.

        Args:
            arr: Sorted array
            start: Start index
            end: End index

        Returns:
            Root node of the balanced subtree
        """
        if start > end:
            return None

        mid = (start + end) // 2
        node = TreeNode(arr[mid])
        node.left = BinarySearchTree._build_balanced_recursive(arr, start, mid - 1)
        node.right = BinarySearchTree._build_balanced_recursive(arr, mid + 1, end)
        return node

    def __str__(self) -> str:
        """String representation of the tree."""
        return f"BST(inorder={self.inorder_traversal()})"

    def __repr__(self) -> str:
        """Detailed representation of the tree."""
        return f"BinarySearchTree(size={self.size_count}, inorder={self.inorder_traversal()})"
