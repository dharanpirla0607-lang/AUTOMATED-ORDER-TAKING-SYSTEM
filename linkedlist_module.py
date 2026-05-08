# ============================================================
# MODULE 3: QUEUE  (Token Management)
# ------------------------------------------------------------
# A FIFO circular queue manages customer tokens (1 – 10).
# At most 10 customers can have active orders simultaneously.
# When a customer's order is served / cancelled the token is
# returned to the rear of the queue so it can be reused.
#
# Operations:
#   get_token()        → dequeue front token; None if full
#   return_token(t)    → enqueue used token back at rear
#   is_full()          → True when no tokens are available
#   available_count()  → number of free tokens
# ============================================================

from collections import deque


class TokenQueue:
    """FIFO queue of re-usable integer tokens (1 … max_tokens)."""

    def __init__(self, max_tokens: int = 10):
        self.max_tokens = max_tokens
        # Initialise queue with all tokens available (1 to max_tokens)
        self._available: deque = deque(range(1, max_tokens + 1))
        self._active: set = set()          # tokens currently in use

    # ── ENQUEUE / DEQUEUE ────────────────────────────────────
    def get_token(self):
        """
        Dequeue the next available token from the front.
        Returns None when all tokens are in use (queue is empty).
        """
        if not self._available:            # queue empty → all tokens busy
            return None
        token = self._available.popleft()  # FIFO: remove from front
        self._active.add(token)
        return token

    def return_token(self, token: int) -> bool:
        """
        Return a token back to the queue (enqueue at FRONT).
        Placing it at the front means the just-freed token is the
        very next one assigned, satisfying the requirement that
        token 1 is reused as soon as customer 1 collects their order.
        """
        if token in self._active:
            self._active.discard(token)
            self._available.appendleft(token)  # enqueue at front → reused immediately
            return True
        return False

    # ── STATUS ───────────────────────────────────────────────
    def is_full(self) -> bool:
        """True when all tokens are currently assigned."""
        return len(self._available) == 0

    def available_count(self) -> int:
        """Number of tokens not yet assigned."""
        return len(self._available)

    def active_tokens(self) -> set:
        """Snapshot of tokens currently in use."""
        return set(self._active)
