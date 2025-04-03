import pandas as pd
import plotly.graph_objects as go

# Load the final.csv data file (adjust the path as needed)
final_df = pd.read_csv(r"plot\final.csv")

# Define the columns for density
density_columns = ["2 deg", "4 deg", "6 deg (Kepler)", "8 deg", "10 deg", 
                   "12 deg (TESS 1 detector)", "14 deg", "16 deg", "18 deg", "20 deg"]

# Create a figure
fig = go.Figure()

# Create one trace per density column with hover info showing name and value
for col in density_columns:
    fig.add_trace(go.Scatter(
        x=final_df["ra_j2000_formula"],
        y=final_df["dec_j2000_formula"],
        mode="markers",
        marker=dict(
            size=8,
            color=final_df[col],
            colorscale='Viridis',
            colorbar=dict(title=col),
            showscale=False  # only the visible trace will show the colorbar
        ),
        name=col,
        visible=(col == "10 deg"),
        text=[f"{name}<br>{col}: {val}" for name, val in zip(final_df["name"], final_df[col])],
        hoverinfo="text"
    ))

# Create buttons to toggle traces and colorbars
buttons = []
num_traces = len(density_columns)
for i, col in enumerate(density_columns):
    visibility = [False] * num_traces
    visibility[i] = True
    showscale_list = [False] * num_traces
    showscale_list[i] = True
    buttons.append(dict(
        label=col,
        method="update",
        args=[
            {"visible": visibility, "marker.showscale": showscale_list},
            {"title": f"Sky Map Density ({col})"}
        ]
    ))

# Update layout with dropdown moved to the right
fig.update_layout(
    updatemenus=[dict(
        active=density_columns.index("10 deg"),
        buttons=buttons,
        x=1.2,  # pushed further right
        xanchor="left",
        y=1,
        yanchor="top"
    )],
    title="Interactive Sky Map Density (10 deg shown initially)",
    xaxis_title="RA (deg)",
    yaxis_title="Dec (deg)",
    width=1000,
    height=600
)

# Ensure the visible trace shows its colorbar
fig.update_traces(marker=dict(showscale=True), selector=dict(name="10 deg"))

fig.show()
fig.write_html("sky_map_density.html", full_html=True, include_plotlyjs='cdn')
