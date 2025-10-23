"""Queue data structure implementation."""
from typing import Any, List, Optional
import copy


class Queue:
    """
    Queue data structure with FIFO (First In First Out) behavior.

    Attributes:
        items: List storing queue elements
    """

    def __init__(self):
        """Initialize an empty queue."""
        self.items: List[Any] = []

    def enqueue(self, item: Any) -> None:
        """
        Add an item to the rear of the queue.

        Args:
            item: Element to add to the queue
        """
        self.items.append(item)

    def dequeue(self) -> Optional[Any]:
        """
        Remove and return the front item from the queue.

        Returns:
            The front item, or None if queue is empty
        """
        if self.is_empty():
            return None
        return self.items.pop(0)

    def front(self) -> Optional[Any]:
        """
        Return the front item without removing it.

        Returns:
            The front item, or None if queue is empty
        """
        if self.is_empty():
            return None
        return self.items[0]

    def is_empty(self) -> bool:
        """Check if the queue is empty."""
        return len(self.items) == 0

    def size(self) -> int:
        """Return the number of items in the queue."""
        return len(self.items)

    def clear(self) -> None:
        """Remove all items from the queue."""
        self.items.clear()

    def to_list(self) -> List[Any]:
        """Return a copy of the queue as a list (front to rear)."""
        return copy.copy(self.items)

    def get_state(self) -> dict:
        """
        Get the current state for serialization.

        Returns:
            Dictionary containing the queue state
        """
        return {"items": copy.deepcopy(self.items)}

    def set_state(self, state: dict) -> None:
        """
        Restore the queue from a saved state.

        Args:
            state: Dictionary containing the queue state
        """
        self.items = copy.deepcopy(state["items"])

    def __str__(self) -> str:
        """String representation of the queue."""
        return f"Queue({self.items})"

    def __repr__(self) -> str:
        """Detailed representation of the queue."""
        return f"Queue(items={self.items})"


class QueueFromStacks:
    """
    Queue implementation using two stacks.
    Used for challenge mode.
    """

    def __init__(self):
        """Initialize queue with two empty stacks."""
        self.stack1: List[Any] = []  # For enqueue
        self.stack2: List[Any] = []  # For dequeue

    def enqueue(self, item: Any) -> None:
        """Add item to queue using stack operations."""
        self.stack1.append(item)

    def dequeue(self) -> Optional[Any]:
        """Remove and return front item using stack operations."""
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if not self.stack2:
            return None
        return self.stack2.pop()

    def is_empty(self) -> bool:
        """Check if queue is empty."""
        return len(self.stack1) == 0 and len(self.stack2) == 0

    def size(self) -> int:
        """Return number of items in queue."""
        return len(self.stack1) + len(self.stack2)
