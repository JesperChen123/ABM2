# Axelrod Culture Dissemination Model

Implementation of Robert Axelrod's (1997) "The Dissemination of Culture" model using Mesa framework.

## Overview

This ABM explores how cultural differences persist despite tendencies toward convergence. The key insight is that local convergence can lead to global polarization - neighbors become similar while distinct cultural regions remain separated.

### The Model

- **Agents**: Placed on a fixed grid
- **Culture**: Each agent has multiple cultural features
- **Interaction Rule**: 
  - More similar neighbors are more likely to interact
  - When they interact, one copies a trait from the other
  - Result: Similar agents become even more similar

### Key Result
![Model Results](f4bc100434433342fd4c31da0de1cbb5e.png)