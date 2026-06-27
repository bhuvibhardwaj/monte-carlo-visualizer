# Monte Carlo Stock Price Simulator

An interactive Monte Carlo simulator that visualizes 200 possible future stock price trajectories using Geometric Brownian Motion (GBM).

## Features

- **200 Parallel Simulations**: Simulates 200 independent price paths simultaneously
- **Interactive Controls**: Adjust starting price, drift, volatility, and time horizon
- **Color-Coded Paths**:
  - Green: >30% gain
  - Red: >30% loss  
  - Blue: everything else
- **Statistics Dashboard**:
  - Median Final Price
  - 95th Percentile (optimistic outcome)
  - 5th Percentile (pessimistic outcome)
  - % of Paths in Profit
- **Modern Dark Theme**: Professional financial dashboard design

## Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the application:
```bash
streamlit run app.py
```

Then open http://localhost:8501 in your browser.

## Technologies

- **Streamlit**: Web framework
- **NumPy**: Numerical computations and GBM simulation
- **Plotly**: Interactive visualization
