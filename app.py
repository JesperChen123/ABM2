import solara
from model import CultureModel
from mesa.visualization import (  
    SolaraViz,
    make_space_component,
    make_plot_component,
)
from mesa.visualization.components import AgentPortrayalStyle

# Define agent color
def agent_portrayal(agent):
    colors = [
        "red", "blue", "green", "orange", "purple", 
        "cyan", "magenta", "yellow", "brown", "pink",
        "darkblue", "darkgreen", "gray", "olive", "navy"
    ]
    
    color = colors[agent.culture[0] % len(colors)]
    
    return AgentPortrayalStyle(
        color=color,
        marker="s",
        size=85,
    )

# Model parameters
model_params = {
    "seed": {
        "type": "InputText",
        "value": 42,
        "label": "Random Seed",
    },
    "width": {
        "type": "SliderInt",
        "value": 12,
        "label": "Grid Width",
        "min": 5,
        "max": 20,
        "step": 1,
    },
    "height": {
        "type": "SliderInt",
        "value": 12,
        "label": "Grid Height",
        "min": 5,
        "max": 20,
        "step": 1,
    },
    "num_features": {
        "type": "SliderInt",
        "value": 5,
        "label": "Number of Features",
        "min": 2,
        "max": 10,
        "step": 1,
    },
    "num_traits": {
        "type": "SliderInt",
        "value": 10,
        "label": "Traits per Feature",
        "min": 2,
        "max": 15,
        "step": 1,
    },
}

# Create model
culture_model = CultureModel()

# Plots
RegionsPlot = make_plot_component(["Cultural_Regions"])
DiversityPlot = make_plot_component(["Average_Diversity"])

# Create space
SpaceGraph = make_space_component(agent_portrayal, draw_grid=True)

page = SolaraViz(
    culture_model,
    components=[SpaceGraph, RegionsPlot, DiversityPlot],
    model_params=model_params,
    name="Axelrod Culture Model",
)

page