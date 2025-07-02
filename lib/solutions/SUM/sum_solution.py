
class SumSolution:
    
    def compute(self, x: int, y: int) -> int:
        """Add two numbers and return a total"""

        if x > 100 or x < 0 or y > 100 or y < 0:
            raise ValueError(f"Arguments must be between 0-100")

        return x + y 
