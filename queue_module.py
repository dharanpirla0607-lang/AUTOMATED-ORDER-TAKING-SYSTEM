# ============================================================
# MODULE 4: STACK  (Order Cancellation)
# ------------------------------------------------------------
# A LIFO stack tracks recently placed orders so customers can
# cancel within a 15-second window.
#
# Each entry pushed onto the stack is a dict:
#   { 'token': int, 'customer': str, 'timestamp': float }
#
# Operations:
#   push(info)           → push new cancellation record
#   cancel_token(token)  → pop & validate within time window
#   peek()               → inspect top without popping
#   is_empty()           → True when stack is empty
# ============================================================

import time

CANCEL_WINDOW_SECONDS = 15      # customer has 15 s to cancel


class CancelStack:
    """LIFO stack used to manage order cancellation requests."""

    def __init__(self):
        self._stack: list = []      # internal Python list used as a stack

    # ── PUSH ─────────────────────────────────────────────────
    def push(self, order_info: dict):
        """
        Push a new cancellation record onto the top of the stack.
        Automatically records the current time as the timestamp.
        """
        record = {
            'token':     order_info.get('token'),
            'customer':  order_info.get('customer', ''),
            'timestamp': time.time()          # epoch seconds at push time
        }
        self._stack.append(record)            # stack grows at the right (top)

    # ── CANCEL ───────────────────────────────────────────────
    def cancel_by_order_id(self, order_id: str) -> bool:
        """Cancel using unique order_id - always exact match."""
        import time
        for i in range(len(self._stack) - 1, -1, -1):
            if self._stack[i].get('order_id') == order_id:
                elapsed = time.time() - self._stack[i]['timestamp']
                if elapsed <= CANCEL_WINDOW_SECONDS:
                    self._stack.pop(i)
                    return True
                else:
                    return False
        return False

    def cancel_token(self, token: int) -> bool:
        """
        Search the stack for the given token and pop it if the
        15-second cancellation window has not expired.

        Returns True  → order cancelled successfully.
        Returns False → window expired or token not found.
        """
        # Search from top (most recent) downwards
        for i in range(len(self._stack) - 1, -1, -1):
            if self._stack[i]['token'] == token:
                elapsed = time.time() - self._stack[i]['timestamp']
                if elapsed <= CANCEL_WINDOW_SECONDS:
                    self._stack.pop(i)        # pop from stack
                    return True
                else:
                    return False              # window expired
        return False                          # token not in stack

    # ── PEEK ─────────────────────────────────────────────────
    def peek(self):
        """Return the top element without removing it."""
        return self._stack[-1] if self._stack else None

    # ── STATUS ───────────────────────────────────────────────
    def is_empty(self) -> bool:
        return len(self._stack) == 0

    def size(self) -> int:
        return len(self._stack)
