import mesa
from mesa.space import SingleGrid
from agents import CultureAgent
from mesa.datacollection import DataCollector


class CultureModel(mesa.Model):
    """
    Axelrod's culture dissemination model.
    Agents will interact with similar neighbors and become more similar over time.
    """
    
    def __init__(self, width=10, height=10, num_features=5, num_traits=10, seed=None):
        super().__init__(seed=seed)
        # first define model parameters
        self.width = width
        self.height = height
        self.num_features = num_features
        self.num_traits = num_traits
        
        # Create grid
        self.grid = SingleGrid(width, height, torus=False)
        
        # Define data collector
        self.datacollector = DataCollector(
            model_reporters={
                "Cultural_Regions": self.count_regions,
                "Average_Diversity": self.measure_diversity
            }
        )
        
        # Place agents on grid
        for x in range(width):
            for y in range(height):
                agent = CultureAgent(self, num_features, num_traits)
                self.grid.place_agent(agent, (x, y))
        
        # Initialize data collection
        self.datacollector.collect(self)
        
        self.running = True
    
    def step(self):
        """all agents interact in random order, then collect data."""
        # All agents step in random order
        self.agents.shuffle_do("step")
        self.datacollector.collect(self)
    
    def count_regions(self):
        """Count number of distinct cultures."""
        unique_cultures = set()
        for agent in self.agents:
            culture_tuple = tuple(agent.culture)
            unique_cultures.add(culture_tuple)
        return len(unique_cultures)
    
    def measure_diversity(self):
        """Measure average cultural difference between neighbors."""
        total_diff = 0
        total_pairs = 0
        
        for agent in self.agents:
            neighbors = self.grid.get_neighbors(
                agent.pos,
                moore=False,
                include_center=False
            )
            
            for neighbor in neighbors:
                diff = sum(1 for i in range(self.num_features)
                          if agent.culture[i] != neighbor.culture[i])
                total_diff += diff
                total_pairs += 1
        
        return (total_diff / total_pairs) if total_pairs > 0 else 0