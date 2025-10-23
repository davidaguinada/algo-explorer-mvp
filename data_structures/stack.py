"""Stack data structure implementation."""
from typing import Any, List, Optional
import copy


class Stack:
    """
    Stack data structure with LIFO (Last In First Out) behavior.

    Attributes:
        items: List storing stack elements
    """

    def __init__(self):
        """Initialize an empty stack."""
        self.items: List[Any] = []

    def push(self, item: Any) -> None:
        """
        Push an item onto the top of the stack.

        Args:
            item: Element to add to the stack
        """
        self.items.append(item)

    def pop(self) -> Optional[Any]:
        """
        Remove and return the top item from the stack.

        Returns:
            The top item, or None if stack is empty
        """
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self) -> Optional[Any]:
        """
        Return the top item without removing it.

        Returns:
            The top item, or None if stack is empty
        """
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self) -> bool:
        """Check if the stack is empty."""
        return len(self.items) == 0

    def size(self) -> int:
        """Return the number of items in the stack."""
        return len(self.items)

    def clear(self) -> None:
        """Remove all items from the stack."""
        self.items.clear()

    def to_list(self) -> List[Any]:
        """Return a copy of the stack as a list (bottom to top)."""
        return copy.copy(self.items)

    def get_state(self) -> dict:
        """
        Get the current state for serialization.

        Returns:
            Dictionary containing the stack state
        """
        return {"items": copy.deepcopy(self.items)}

    def set_state(self, state: dict) -> None:
        """
        Restore the stack from a saved state.

        Args:
            state: Dictionary containing the stack state
        """
        self.items = copy.deepcopy(state["items"])

    def reverse_recursive(self) -> None:
        """
        Reverse the stack using recursion.
        Used for challenge mode and recursion visualization.
        """
        if not self.is_empty():
            temp = self.pop()
            self.reverse_recursive()
            self._insert_at_bottom(temp)

    def _insert_at_bottom(self, item: Any) -> None:
        """
        Helper method to insert item at the bottom of the stack.

        Args:
            item: Element to insert at bottom
        """
        if self.is_empty():
            self.push(item)
        else:
            temp = self.pop()
            self._insert_at_bottom(item)
            self.push(temp)

    def __str__(self) -> str:
        """String representation of the stack."""
        return f"Stack({self.items})"

    def __repr__(self) -> str:
        """Detailed representation of the stack."""
        return f"Stack(items={self.items})"
