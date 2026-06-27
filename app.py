import streamlit as st
import numpy as np
import plotly.graph_objects as go

def simulate_gbm(S0, mu, sigma, days, num_paths=200):
    dt = 1.0
    t = np.arange(days)
    Z = np.random.normal(0, 1, (num_paths, days))
    drift = (mu - 0.5 * sigma**2) * dt
    diffusion = sigma * np.sqrt(dt) * Z
    log_returns = drift + diffusion
    log_returns = np.cumsum(log_returns, axis=1)
    S = S0 * np.exp(log_returns)
    return S

st.set_page_config(page_title="Monte Carlo Stock Price Simulator", layout="wide", page_icon="📈")
st.markdown(
    """
    <style>
    .main {
        background-color: #0f1117;
    }
    .stSlider > div > div > div > div {
        background-color: #1e232e !important;
    }
    .stat-card {
        background-color: #1e232e;
        border-radius: 12px;
        padding: 20px;
        color: white;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Monte Carlo Stock Price Simulator")

with st.sidebar:
    st.header("Simulation Parameters")
    S0 = st.slider("Starting Price", min_value=10, max_value=1000, value=100, step=1)
    mu = st.slider("Daily Drift", min_value=-0.005, max_value=0.005, value=0.0005, step=0.0001, format="%.4f")
    sigma = st.slider("Volatility", min_value=0.005, max_value=0.10, value=0.02, step=0.001, format="%.3f")
    days = st.slider("Days", min_value=30, max_value=365, value=252, step=1)

S = simulate_gbm(S0, mu, sigma, days)

final_prices = S[:, -1]
median_final = np.median(final_prices)
p95 = np.percentile(final_prices, 95)
p05 = np.percentile(final_prices, 5)
pct_profit = np.mean(final_prices > S0) * 100

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown(f"""<div class="stat-card"><div style="font-size: 14px; color: #94a3b8; margin-bottom: 8px;">Median Final</div><div style="font-size: 24px; font-weight: 700;">${median_final:.2f}</div></div>""", unsafe_allow_html=True)
with col2:
    st.markdown(f"""<div class="stat-card"><div style="font-size: 14px; color: #94a3b8; margin-bottom: 8px;">95th Percentile</div><div style="font-size: 24px; font-weight: 700; color: #22c55e;">${p95:.2f}</div></div>""", unsafe_allow_html=True)
with col3:
    st.markdown(f"""<div class="stat-card"><div style="font-size: 14px; color: #94a3b8; margin-bottom: 8px;">5th Percentile</div><div style="font-size: 24px; font-weight: 700; color: #ef4444;">${p05:.2f}</div></div>""", unsafe_allow_html=True)
with col4:
    st.markdown(f"""<div class="stat-card"><div style="font-size: 14px; color: #94a3b8; margin-bottom: 8px;">% Paths Profit</div><div style="font-size: 24px; font-weight: 700;">{pct_profit:.1f}%</div></div>""", unsafe_allow_html=True)

fig = go.Figure()

for i in range(S.shape[0]):
    final = S[i, -1]
    if final > S0 * 1.3:
        color = "#22c55e"
    elif final < S0 * 0.7:
        color = "#ef4444"
    else:
        color = "#3b82f6"
    fig.add_trace(go.Scatter(x=np.arange(days), y=S[i, :], mode='lines', line=dict(width=1, color=color), opacity=0.3, showlegend=False))

fig.add_hline(y=S0, line_dash="dash", line_color="white", line_width=1, showlegend=False)

fig.update_layout(
    xaxis_title="Trading Days",
    yaxis_title="Stock Price",
    template="plotly_dark",
    height=600,
    margin=dict(l=0, r=0, t=40, b=0),
    plot_bgcolor="#0f1117",
    paper_bgcolor="#0f1117"
)

st.plotly_chart(fig, use_container_width=True)
