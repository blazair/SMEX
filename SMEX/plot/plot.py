import plotly.express as px
import pandas as pd

# Load your CSVs
target_list = pd.read_csv(r"plot\final.csv").dropna()


# Label each list
target_list["source"] = "List 1"


# Create the interactive scatter plot
fig = px.scatter(
    target_list,
    x="ra_j2000_formula",
    y="dec_j2000_formula",
    color="source",
    hover_name="name",
    labels={
        "ra_j2000_formula": "RA (deg)",
        "dec_j2000_formula": "Dec (deg)",
        "source": "List"
    },
    title="Interactive Sky Plot of Target Stars (RA/Dec)"
)

fig.update_layout(
    xaxis_title="Right Ascension (deg)",
    yaxis_title="Declination (deg)",
    height=600,
    width=900
)

fig.show()
