import mesa
import random


class CultureAgent(mesa.Agent):
    """
    An agent with a culture represented by multiple features.
    Each feature can take on one of several trait values.
    """
    
    def __init__(self, model, num_features, num_traits):
        super().__init__(model)
        # Culture is a list of traits, one for each feature
        # For example: [3, 7, 2, 9, 1] means feature 1 has trait 3, feature 2 has trait 7, etc.
        self.culture = [random.randrange(num_traits) for _ in range(num_features)]
    
    def step(self):
        """
        Rule is more similar neighbors are more likely to influence you.
        
        Process:
        1. Pick a random neighbor
        2. Calculate similarity
        3. With probability = similarity, adopt one of their different traits
        """
        # Get neighbors (4 adjacent cells, no diagonals)
        neighbors = self.model.grid.get_neighbors(
            self.pos,
            moore=False,
            include_center=False
        )
        
        if not neighbors:
            return
        
        # Pick random neighbor
        neighbor = random.choice(neighbors)
        
        # Calculate similarity
        num_features = len(self.culture)
        matching = sum(1 for i in range(num_features) 
                      if self.culture[i] == neighbor.culture[i])
        similarity = matching / num_features
        
        # Interact with probability equal to similarity
        if random.random() < similarity:
            # Find features where we differ
            different = [i for i in range(num_features)
                        if self.culture[i] != neighbor.culture[i]]
            
            # If different, adopt one of neighbor's traits
            if different:
                feature = random.choice(different)
                self.culture[feature] = neighbor.culture[feature]