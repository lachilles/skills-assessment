"""FIFO queues implemented as a list.

Warning: this is not the best way to implement a Queue."""


class Queue(object):
    """FIFO queue."""

    def __init__(self):
        self._list = []

    def __repr__(self):
        if not self._list:
            return "<Queue (empty)>"
        else:
            return "<Queue %s>" % self._list

    def dequeue(self):
        """Remove item from front of queue and return it."""

        return self._list.pop(0)

    def length(self):
        """Return length of queue."""

        return len(self._list)

    def empty(self):
        """Empty queue."""

        remaining = self._list
        self._list = []

        return remaining

    def is_empty(self):
        """Is queue empty?"""

        return not self._list

    def enqueue(self, item):
        """Add item to end of queue::

            >>> q = Queue()
            >>> q.enqueue("buy flight")
            >>> q.enqueue("pack")
            >>> q.enqueue("enjoy vacation")

            >>> q
            <Queue ['buy flight', 'pack', 'enjoy vacation']>

            >>> q.length
            3
        """

        return self._list.append(item)

        ## Did not get 3 returned for q.lenth. Instead I got:
        ## >>> q.length
        # <bound method Queue.length of <Queue ['buy flight', 'pack', 'enjoy vacation']>>

    def peek(self):
        """Return but don't remove the first item in the queue.

            >>> q = Queue()
            >>> q.enqueue("buy flight")
            >>> q.enqueue("pack")
            >>> q.enqueue("enjoy vacation")

            >>> q.peek()
            'buy flight'

            >>> q
            <Queue ['buy flight', 'pack', 'enjoy vacation']>
        """

        return self._list[0]
