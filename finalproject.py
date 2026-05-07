import streamlit as st
import folium
from streamlit_folium import st_folium

st.title("Interactive Map of Human Evolution")

lineages = [
    {
        "name": "Australopithecus afarensis",
        "time": 3900000,
        "location": "East Africa",
        "lat": 9.0,
        "lon": 40.0,
        "info": "Lived about 3.9–2.9 million years ago. Famous fossil: Lucy."
    },
    {
        "name": "Homo habilis",
        "time": 2400000,
        "location": "East Africa",
        "lat": -3.0,
        "lon": 36.0,
        "info": "Lived about 2.4–1.4 million years ago. Associated with early stone tools."
    },
    {
        "name": "Homo erectus",
        "time": 1900000,
        "location": "Africa and Eurasia",
        "lat": -1.3,
        "lon": 36.8,
        "info": "Lived about 1.9 million–110,000 years ago. One of the first hominins to spread out of Africa."
    },
    {
        "name": "Neanderthals",
        "time": 400000,
        "location": "Europe and western Asia",
        "lat": 48.0,
        "lon": 10.0,
        "info": "Lived about 400,000–40,000 years ago. Closely related to modern humans."
    },
    {
        "name": "Homo sapiens",
        "time": 300000,
        "location": "Africa",
        "lat": 31.8,
        "lon": -7.1,
        "info": "Modern humans appeared around 300,000 years ago in Africa."
    }
]

years_ago = st.slider(
    "Timeline: years ago",
    min_value=0,
    max_value=4000000,
    value=4000000,
    step=50000
)

st.write(f"Showing lineages that existed by about **{years_ago:,} years ago**.")

m = folium.Map(location=[15, 20], zoom_start=2)

for lineage in lineages:
    if lineage["time"] <= years_ago:
        folium.Marker(
            location=[lineage["lat"], lineage["lon"]],
            popup=f"""
            <b>{lineage['name']}</b><br>
            Location: {lineage['location']}<br><br>
            {lineage['info']}
            """,
            tooltip=lineage["name"]
        ).add_to(m)

st_folium(m, width=700, height=500)

st.subheader("Lineage Information")

for lineage in lineages:
    if lineage["time"] <= years_ago:
        with st.expander(lineage["name"]):
            st.write(f"**Location:** {lineage['location']}")
            st.write(f"**Approximate time:** {lineage['time']:,} years ago")
            st.write(lineage["info"])
