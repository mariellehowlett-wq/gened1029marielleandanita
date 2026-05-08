import streamlit as st
import folium
from streamlit_folium import st_folium
import time
import requests

st.title("Interactive Map of Human Evolution")

lineages = [
    {
        "name": "Australopithecus afarensis",
        "time": 3900000,
        "location": "East Africa",
        "lat": 9.0,
        "lon": 40.0,
        "images": [
            "/workspaces/gened1029marielleandanita/images/australopithecus_afarensis.jpg",
            "/workspaces/gened1029marielleandanita/images/lucy.jpg",
        ],
        "info": "Lived about 3.9–2.9 million years ago. Famous fossil: Lucy.",
        "details": "A. afarensis walked upright but still had ape-like features including a small brain and long arms. The famous fossil 'Lucy', discovered in Ethiopia in 1974, is one of the most complete early hominin skeletons ever found."
    },
    {
        "name": "Homo habilis",
        "time": 2400000,
        "location": "East Africa",
        "lat": -3.0,
        "lon": 36.0,
        "images": [
            "/workspaces/gened1029marielleandanita/images/homo_habilis1.jpg",
            "/workspaces/gened1029marielleandanita/images/homo_habilis2.jpg",
        ],
        "info": "Lived about 2.4–1.4 million years ago. Associated with early stone tools.",
        "details": "H. habilis, meaning 'handy man', is the earliest species assigned to the genus Homo. They created the Oldowan toolkit — simple sharp-edged flakes struck from stone — marking a major leap in cognitive ability."
    },
    {
        "name": "Homo erectus",
        "time": 1900000,
        "location": "Africa and Eurasia",
        "lat": -1.3,
        "lon": 36.8,
        "images": [ 
            "/workspaces/gened1029marielleandanita/images/homo_erectus1.jpg",
            "/workspaces/gened1029marielleandanita/images/homo_erectus2.jpg",
        ],
        "info": "Lived about 1.9 million–110,000 years ago. First hominin to leave Africa.",
        "details": "H. erectus had a much larger brain than earlier hominins and was the first to master fire. They spread from Africa into Asia and Europe, surviving for nearly 2 million years — longer than any other Homo species."
    },
    {
        "name": "Neanderthals",
        "time": 400000,
        "location": "Europe and western Asia",
        "lat": 48.0,
        "lon": 10.0,
        "images": [
            "/workspaces/gened1029marielleandanita/images/neanderthal1.jpg",
            "/workspaces/gened1029marielleandanita/images/neanderthal2.jpg",
        ],
        "info": "Lived about 400,000–40,000 years ago. Closely related to modern humans.",
        "details": "Neanderthals had large brains, buried their dead, and created tools and art. Genetic evidence shows they interbred with H. sapiens — most non-African people today carry 1–4% Neanderthal DNA."
    },
    {
        "name": "Denisovans",
        "time": 400000,
        "location": "Denisova Cave - Altai Krai, Russia",
        "lat": 52.5,
        "lon": 82.5, 
        "images": [
            "/workspaces/gened1029marielleandanita/images/denisovan1.jpg",
            "/workspaces/gened1029marielleandanita/images/denisovan2.jpg",
        ],
        "info": "", 
        "details": "", 
    },
    {
        "name": "Homo heidelbergensis", 
        "time": 700000,
        "location": "Africa, Europe, and possibly Asia", 
        "lat": 49.4,
        "lon": 8.67,
        "images": [
            "/workspaces/gened1029marielleandanita/images/homo_heidelbergensis1.jpg",
            "/workspaces/gened1029marielleandanita/images/homo_heidelbergensis2.jpg",
        ],
        "info": "", 
        "details": "", 
    },
    {
        "name": "Homo sapiens",
        "time": 300000,
        "location": "Africa",
        "lat": 31.8,
        "lon": -7.1,
        "images": [
            "/workspaces/gened1029marielleandanita/images/homo_sapien1.jpg",
            "/workspaces/gened1029marielleandanita/images/homo_sapien2.jpg",
        ],
        "info": "Modern humans appeared around 300,000 years ago in Africa.",
        "details": "H. sapiens developed complex language, abstract thinking, and culture. Starting around 70,000 years ago, they spread out of Africa and eventually colonized every continent, becoming the last surviving hominin species."
    },
    {
        "name": "Paranthropus/Australopithecus robustus", 
        "time": 1800000, 
        "location": "South Africa",
        "lat": -26.0,
        "lon": 27.7, 
        "images": [
            "/workspaces/gened1029marielleandanita/images/a_robustus1.jpg",
            "/workspaces/gened1029marielleandanita/images/a_robustus2.jpg",
        ],
        "info": "",
        "details":"",
    },
    {
        "name": "Paranthropus/Australopithecus boisei", 
        "time": 2300000, 
        "location": "East Africa", 
        "lat": -3.0,
        "lon": 35.35,
        "images": [
            "/workspaces/gened1029marielleandanita/images/a_boisei1.jpg",
            "/workspaces/gened1029marielleandanita/images/a_boisei2.jpg",
        ], 
        "info": "", 
        "details": "ethiopia, malawi, kenya, tanzania",
    }, 
    {
        "name": "Australopithecus africanus", 
        "time": 3300000, 
        "location": "South Africa", 
        "lat": -27.3 , 
        "lon": 24.5, 
        "images": [
            "/workspaces/gened1029marielleandanita/images/a_africanus1.jpg", 
            "/workspaces/gened1029marielleandanita/images/a_africanus2.jpg",
        ], 
        "info": "", 
        "details": "",
    },
    {
        "name": "Ardipithecus", 
        "time": 4400000, 
        "location": "Eastern Africa", 
        "lat": 12.0, 
        "lon": 41.5, 
        "images": [
            "/workspaces/gened1029marielleandanita/images/ardipithecus1.jpg", 
            "/workspaces/gened1029marielleandanita/images/ardipithecus2.jpg",
        ],
        "details": "",
    },
    {
        "name": "Homo floresiensis", 
        "time": 100000, 
        "location": "Asia - Indonesia", 
        "lat": -8.6, 
        "lon": 121.1, 
        "images": [
            "/workspaces/gened1029marielleandanita/images/h_florensiensis1.jpg",
            "/workspaces/gened1029marielleandanita/images/h_florensiensis2.jpg",
        ],
        "details": "",
    }, 
]


lineages_sorted = sorted(lineages, key=lambda x: x["time"], reverse=True)

if "step" not in st.session_state:
    st.session_state.step = 0
if "running" not in st.session_state:
    st.session_state.running = False
if "selected" not in st.session_state:
    st.session_state.selected = None

col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    if st.button("▶ Play"):
        st.session_state.running = True
        st.session_state.step = 0
        st.session_state.selected = None
with col2:
    if st.button("⏸ Pause"):
        st.session_state.running = False
with col3:
    if st.button("↺ Reset"):
        st.session_state.running = False
        st.session_state.step = 0
        st.session_state.selected = None

step = min(st.session_state.step, len(lineages_sorted))
current_lineages = lineages_sorted[:step]

st.progress(step / len(lineages_sorted))

if step == 0:
    st.markdown("### ⏳ Press Play to begin")
elif step < len(lineages_sorted):
    current = lineages_sorted[step - 1]
    st.markdown(f"### 🦴 {current['name']} — {current['time']:,} years ago")
else:
    st.markdown("### 🌍 Present day — all lineages shown")

m = folium.Map(location=[15, 20], zoom_start=2, tiles=None)
folium.TileLayer(
    tiles="https://mt1.google.com/vt/lyrs=r&x={x}&y={y}&z={z}&hl=en",
    attr="Google Maps",
    name="Google Maps EN"
).add_to(m)

for lineage in current_lineages:
    folium.Marker(
        location=[lineage["lat"], lineage["lon"]],
        tooltip=lineage["name"],
        icon=folium.Icon(color="red" if st.session_state.selected == lineage["name"] else "blue")
    ).add_to(m)

map_data = st_folium(m, width=700, height=500, key=f"map_{step}")

if map_data and map_data.get("last_object_clicked"):
    clicked = map_data["last_object_clicked"]
    for lineage in current_lineages:
        if (
            abs(lineage["lat"] - clicked["lat"]) < 0.01
            and abs(lineage["lon"] - clicked["lng"]) < 0.01
        ):
            st.session_state.selected = lineage["name"]
            st.session_state.running = False
            break

# Info popup with image
if st.session_state.selected:
    match = next((l for l in lineages if l["name"] == st.session_state.selected), None)
    if match:
        with st.container(border=True):
            col_a, col_b = st.columns([9, 1])
            with col_a:
                st.markdown(f"## 🦴 {match['name']}")
            with col_b:
                if st.button("✕"):
                    st.session_state.selected = None
                    st.rerun()

            if match.get("images"):
                cols = st.columns(len(match["images"]))
                for col, img in zip(cols, match["images"]):
                    with col:
                        st.image(img, width=300)

            st.markdown(f"**📍 Location:** {match['location']}")
            st.markdown(f"**🕰 Approximate time:** {match['time']:,} years ago")
            st.divider()
            st.write(match["info"])
            st.write(match["details"])

if st.session_state.running and step < len(lineages_sorted):
    time.sleep(3)
    st.session_state.step += 1
    st.rerun()
elif st.session_state.running and step >= len(lineages_sorted):
    st.session_state.running = False
