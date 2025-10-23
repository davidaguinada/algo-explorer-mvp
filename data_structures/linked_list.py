"""Singly Linked List data structure implementation."""
from typing import Any, List, Optional
import copy


class Node:
    """
    Node for singly linked list.

    Attributes:
        data: Value stored in the node
        next: Reference to the next node
    """

    def __init__(self, data: Any):
        """
        Initialize a node with data.

        Args:
            data: Value to store in the node
        """
        self.data: Any = data
        self.next: Optional[Node] = None

    def __str__(self) -> str:
        """String representation of the node."""
        return f"Node({self.data})"

    def __repr__(self) -> str:
        """Detailed representation of the node."""
        return f"Node(data={self.data})"


class LinkedList:
    """
    Singly Linked List data structure.

    Attributes:
        head: Reference to the first node
        size_count: Number of nodes in the list
    """

    def __init__(self):
        """Initialize an empty linked list."""
        self.head: Optional[Node] = None
        self.size_count: int = 0

    def insert_at_head(self, data: Any) -> None:
        """
        Insert a new node at the beginning of the list.

        Args:
            data: Value to insert
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size_count += 1

    def insert_at_tail(self, data: Any) -> None:
        """
        Insert a new node at the end of the list.

        Args:
            data: Value to insert
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.size_count += 1

    def insert_at_position(self, data: Any, position: int) -> bool:
        """
        Insert a new node at a specific position.

        Args:
            data: Value to insert
            position: Zero-based index for insertion

        Returns:
            True if successful, False if position is invalid
        """
        if position < 0 or position > self.size_count:
            return False

        if position == 0:
            self.insert_at_head(data)
            return True

        new_node = Node(data)
        current = self.head
        for _ in range(position - 1):
            current = current.next

        new_node.next = current.next
        current.next = new_node
        self.size_count += 1
        return True

    def delete(self, data: Any) -> bool:
        """
        Delete the first occurrence of a value.

        Args:
            data: Value to delete

        Returns:
            True if deleted, False if not found
        """
        if self.head is None:
            return False

        if self.head.data == data:
            self.head = self.head.next
            self.size_count -= 1
            return True

        current = self.head
        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
                self.size_count -= 1
                return True
            current = current.next

        return False

    def delete_at_position(self, position: int) -> bool:
        """
        Delete node at a specific position.

        Args:
            position: Zero-based index for deletion

        Returns:
            True if successful, False if position is invalid
        """
        if position < 0 or position >= self.size_count or self.head is None:
            return False

        if position == 0:
            self.head = self.head.next
            self.size_count -= 1
            return True

        current = self.head
        for _ in range(position - 1):
            current = current.next

        if current.next is not None:
            current.next = current.next.next
            self.size_count -= 1
            return True

        return False

    def search(self, data: Any) -> Optional[int]:
        """
        Search for a value and return its position.

        Args:
            data: Value to search for

        Returns:
            Zero-based index of the value, or None if not found
        """
        current = self.head
        position = 0
        while current is not None:
            if current.data == data:
                return position
            current = current.next
            position += 1
        return None

    def find_middle(self) -> Optional[Any]:
        """
        Find the middle element using slow/fast pointer technique.
        Used for challenge mode.

        Returns:
            Data of the middle node, or None if list is empty
        """
        if self.head is None:
            return None

        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow.data

    def is_empty(self) -> bool:
        """Check if the list is empty."""
        return self.head is None

    def size(self) -> int:
        """Return the number of nodes in the list."""
        return self.size_count

    def clear(self) -> None:
        """Remove all nodes from the list."""
        self.head = None
        self.size_count = 0

    def to_list(self) -> List[Any]:
        """
        Convert the linked list to a Python list.

        Returns:
            List containing all values in order
        """
        result = []
        current = self.head
        while current is not None:
            result.append(current.data)
            current = current.next
        return result

    def get_state(self) -> dict:
        """
        Get the current state for serialization.

        Returns:
            Dictionary containing the list state
        """
        return {
            "items": self.to_list(),
            "size": self.size_count
        }

    def set_state(self, state: dict) -> None:
        """
        Restore the list from a saved state.

        Args:
            state: Dictionary containing the list state
        """
        self.clear()
        for item in state["items"]:
            self.insert_at_tail(item)

    def __str__(self) -> str:
        """String representation of the linked list."""
        return f"LinkedList({' -> '.join(str(x) for x in self.to_list())})"

    def __repr__(self) -> str:
        """Detailed representation of the linked list."""
        return f"LinkedList(size={self.size_count}, items={self.to_list()})"
