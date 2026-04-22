from abc import ABC, abstractmethod

class Screen(ABC):
    def __init__(self, assets, state):
        self.assets = assets
        self.state = state
    
    @abstractmethod
    def update(self, dt: float, events: list) -> None:
        """Handle input and logic."""
        pass
    
    @abstractmethod
    def draw(self, surface) -> None:
        """Draw everything to the given surface."""
        pass