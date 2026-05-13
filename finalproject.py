import streamlit as st
import folium
from streamlit_folium import st_folium
import time
import requests

st.set_page_config(
    page_title="Human Evolution Timeline",
    page_icon="🦴",
    layout="wide"
)

st.markdown("""
<style>
.main {
    background-color: #f7f4ef;
}

h1, h2, h3 {
    color: #3b2f2f;
}

.species-card {
    background-color: white;
    padding: 25px;
    border-radius: 18px;
    box-shadow: 0px 4px 14px rgba(0,0,0,0.12);
    margin-top: 20px;
}

.timeline-label {
    background-color: #efe3d0;
    padding: 12px 18px;
    border-radius: 12px;
    font-size: 20px;
    font-weight: 600;
    color: #3b2f2f;
}

.info-box {
    background-color: #faf7f0;
    padding: 12px;
    border-radius: 10px;
    margin-bottom: 10px;
}
</style>
""", unsafe_allow_html=True)


st.markdown("""
# 🦴 Interactive Map of Human Evolution
Explore major hominin species across time and geography.
""")


lineages = [
    {
        "name": "Australopithecus afarensis",
        "time": 3900000,
        "location": "East Africa",
        "lat": 11.2,
        "lon": 40.6,
        "images": [
            "/workspaces/gened1029marielleandanita/images/australopithecus_afarensis.jpg",
            "/workspaces/gened1029marielleandanita/images/lucy.jpg",
        ],
        "details": "A. afarensis was a group of small-bodied and small-brained early hominin species. Based on fossils recovered to date, A. afarensus lived between 3.7 and 3 million years ago. Their diet included plants such as grasses, fruits, and leaves. Their brain size was about 385-550 cubic centimeters, and their body weight ranged from 25-64 kg, with females significantly smaller than males. This detail means that their brain was roughly 1.3% of their body weight. A. afarensis is so significant due to the recovered fossil named Lucy. Her skeleton was around 40% complete, which at the time was the most complete hominin skeleton known. The discovery of Lucy, along with A. africanus specimens, confirmed that our early relatives generally walked upright and did so before the evolution of a large brain. A. afarensis possessed human-like and ape-like qualities, with a slightly domed skull and a projecting face. The small skull and long arms were those of apes, but their spine, pelvis, and knees were more human-like.",
    },
    {
        "name": "Homo habilis",
        "time": 2300000,
        "location": "East Africa",
        "lat": -3.0,
        "lon": 36.0,
        "images": [
            "/workspaces/gened1029marielleandanita/images/homo_habilis1.jpg",
            "/workspaces/gened1029marielleandanita/images/homo_habilis2.jpg",
        ],
        "details": "H. habilis was the earliest of our ancestors found to show an increase in brain size and the first to be associated with stone tools. This species lived between 2.3 and 1.5 million years ago and is assigned to the same genus as modern humans. Chemical analysis suggests that this species was mainly vegetarian, but did include some meat in its diet. H. habilis' brain size was about 610 cubic centimeters, and their weights ranged from 20-37 kg, meaning it was roughly 1.7% of their body weight. Nicknamed the “handyman”, stone tools were found near fossil remains. The first crude stone tools, consisting of simple choppers, core tools, and scrapers, were made as early as 2.6 million years ago. These tools were a progression from the use of sticks and natural, unmodified stones that the earlier ancestors likely used. H. habilis had a reduced facial projection compared with earlier species, including a smaller jaw than australopithecines. While still having the ape-like leg and arm proportions, the finger bone proportions suggest the human-like ability to form a precision grip.",
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
        "details": "H. erectus was an ancient human with human-like body proportions, with shorter arms and longer legs relative to its torso. H. erectus lived for quite some time, ranging from about two million years ago until at least 250,000 years ago. Unlike some earlier relatives, they were meat-eaters and lived as hunter-gatherers. H. erectus had an average brain volume of roughly 900-950 cubic centimeters, which is smaller than that of modern humans but much larger than that of early hominins. Due to increased body size, brain size was roughly 1.8% of their body weight. H. erectus made an important milestone with the use of fire, where they gained access to light, warmth, protection from predators, and the ability to cook food. The species spread out of Africa into western Asia, then eventually to eastern Asia and Indonesia. Based on fossil findings, scientists have concluded that H. erectus walked and ran much the same way we do. They were also the first human species to make handaxes, which were likely used to butcher meat. "
    },
    {
        "name": "Neanderthals",
        "time": 400000,
        "location": "Europe and western Asia",
        "lat": 51.1,
        "lon": 6.6,
        "images": [
            "/workspaces/gened1029marielleandanita/images/neanderthal1.jpg",
            "/workspaces/gened1029marielleandanita/images/neanderthal2.jpg",
        ],
        "details": "Neanderthals are our closest ancient human relatives, with thousands of their artifacts and fossils found, including several nearly complete skeletons. With modern sequencing, their genomes were reconstructed from ancient DNA obtained from their fossils. Neanderthals lived from about 400,000 to 40,000 years ago, across Europe and southwest and central Asia. Their brain size was 1,200-1,750 cubic centimeters, and their weight ranged from 64 to 82 kg. This indicates that brain weight was likely accounting for 1.5-2% of their total body weight. Neanderthals lived alongside early modern humans for at least part of their existence, with encounters that were quite intimate. As a result, all those not completely composed of African DNA have inherited around 2% Neanderthal DNA. They had a long, low skull with a prominent brow ridge above their eyes. The central part of their face protruded forward, dominated by a very large, wide nose. Some scientists believe this feature may have been an adaptation to living in colder, drier climates, where the nose's volume would have helped moisten and warm the air they breathed.",
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
        "details": "The Denisovans are a population of extinct hominins who lived between 400,000 and 30,000 years ago. This time spread is when the Denisovans and Neanderthals split from the human lineage. For a long time, this species was known only from its teeth and mitochondrial DNA extracted from a finger bone. Other than that, only a few fragmentary fossils of this population have been found. There was evidence of interbreeding between modern humans and Denisovans, meaning that some groups of humans today have small amounts of Denisovan DNA, found in people from Southeast Asia. Denisovan brain size was up to 1,600 cubic centimeters, but their height and weight are unknown. They were likely stockier and more robust than Neanderthals, with sturdy jaws and a large cranium.",
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
        "details": "Homo heidelbergensis is known to have been the first early human species to live in colder climates and the first to routinely hunt large animals. They lived and worked in co-operative groups and made a variety of tools, such as wooden spears set with stone spearheads. This species lived between 300,000 and 600,000 years ago, and its fossils have been found scattered across Africa and Europe, with the African fossils tending to be older than those in Europe. It is believed that the European populations of Homo heidelbergensis evolved into the Neanderthals, while the separate population in Africa evolved into Homo sapiens. Fossil evidence regarding body shape and size is limited, however, leg bones indicate they were tall, and skulls suggest that they had a large brow ridge and large brain capacity.",
    },
    {
        "name": "Homo sapiens",
        "time": 300000,
        "location": "Africa",
        "lat": 31.8,
        "lon": -8.5,
        "images": [
            "/workspaces/gened1029marielleandanita/images/homo_sapien1.jpg",
            "/workspaces/gened1029marielleandanita/images/homo_sapien2.jpg",
        ],
        "details": "The only surviving member of the human species, and the one we all belong to, is Homo sapiens. Due to interbreeding between H. sapiens and Neanderthals, Neanderthals are known to contribute 1-4% of the genomes of non-African modern humans. H. sapiens first appeared around 300,000 years ago in Africa and eventually spread across every continent on Earth. Modern humans can generally be characterized by a lighter skeleton, a high, round braincase, a smaller bony brow ridge above the eyes, and a chin on the lower jaw. The complex brains of modern humans enabled them to interact with one another and their surroundings in new ways, leading to complex social structures and the ability to communicate and share knowledge."
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
        "details": "Paranthropus/Australopithecus robustus was an early human species that lived in southern Africa between about 1.8 and 1.2 million years ago. Similar to P. boisei, this species possessed large jaws and thick enamel adapted for chewing tough plant material. Their skulls had a broad face and a sagittal crest at the top that anchored the chewing muscles. Despite these features, studies of tooth wear suggest that they may have been more of a dietary generalist, eating a variety of other foods such as soft fruits, insects, and meat. Fossil evidence also suggests that they may have used simple bone and stone tools to dig for food or process materials. ",
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
        "details": "Nicknamed “Nutcracker Man,” P. boisei individuals had the thickest dental enamel of any known early human, with a wide, dish-shaped face that created a larger opening for larger jaw muscles to support massive cheek teeth. These features suggest they likely ate tough foods such as roots and nuts, but dental microwear patterns on P. boisei teeth are more similar to those of living fruit-eaters. It is possible that they only ate hard or tough foods during times when their preferred resources were scarce. Although it has long been thought that this species relied solely on its jaws for food, recent research has revealed that it was capable of toolmaking and use to some extent. ",
    },
    {
        "name": "Australopithecus africanus",
        "time": 3300000,
        "location": "South Africa",
        "lat": -27.3,
        "lon": 24.5,
        "images": [
            "/workspaces/gened1029marielleandanita/images/a_africanus1.jpg",
            "/workspaces/gened1029marielleandanita/images/a_africanus2.jpg",
        ],
        "details": "Australopithecus africanus was the first of our pre-human ancestors to be discovered, with the Taung Child skull, found in 1924, being the first to establish that early fossil humans occurred in Africa. The skull had a mixture of human-like and ape-like features, such as a spinal cord hole positioned towards the front of the skull, suggesting upright walking, and a low, sloping forehead. This species is believed to have lived between 3.2 and 2 million years ago, and analysis of tooth-wear patterns suggests that its diet consisted of fruit, leaves, and some meat. No stone tools have been discovered in the same sediments as their fossils, but they likely used simple tools such as sticks and scavenged animal bones. ",
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
        "details": "Ardipithecus is the earliest known genus of the zoological family Hominidae, having lived between 5.8 million and 4.4 million years ago. Although they had some ape-like features, they also had key human features, including smaller canines and some evidence of upright walking. In 2009, a partial skeleton nicknamed “Ardi” was announced, which has been considered the oldest known skeleton of a putative human ancestor. The scientists who found her argue that her skeleton reflects a human-African ape common ancestor that was not chimpanzee-like. This is due to the structure of her pelvis, which made it useful for both climbing and upright walking. Along with this, the bones of her palm were short, indicating that she did not knuckle-walk or swing beneath trees, but her long, curving fingers and opposable big toes suggest that she grasped tree branches. Through Ardi, researchers have been able to determine some of the anatomical changes that laid the foundation for upright walking. ",
    },
    {
        "name": "Homo floresiensis",
        "time": 100000,
        "location": "Asia - Indonesia",
        "lat": -8.6,
        "lon": 121.1,
        "images": [
            "/workspaces/gened1029marielleandanita/images/h_floresiensis1.jpg",
            "/workspaces/gened1029marielleandanita/images/h_floresiensis2.jpg",
        ],
        "details": "Nicknamed “the Hobbit,” H. floresiensis individuals were approximately 3 feet 6 inches tall. They had small brains, about a third of the size of ours, broad hipbones, shrugged-forward shoulders, and very large flat feet. They are one of the most recently discovered early human species, discovered in 2003 on the island of Flores, Indonesia. The last known trace of H. floresiensis dates to about 50,000 years ago, and their oldest known remains are at least 100,000 years old. When they were first discovered, scientists believed that the skeleton may have belonged to a modern human child, however, the presence of fully developed wisdom teeth and defined brow ridges indicated that this was not the case. There are multiple theories as to why they were so small, one being that it may have resulted from island dwarfism, the evolutionary process in which large animals isolated on islands evolve smaller bodies due to limited food resources and a lack of large predators.  ",
    },
]


lineages_sorted = sorted(lineages, key=lambda x: x["time"], reverse=True)

if "step" not in st.session_state:
    st.session_state.step = 0
if "running" not in st.session_state:
    st.session_state.running = False
if "selected" not in st.session_state:
    st.session_state.selected = None


st.markdown("### Timeline Controls")

col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    if st.button("▶ Play Timeline", use_container_width=True):
        st.session_state.running = True
        st.session_state.step = 0
        st.session_state.selected = None

with col2:
    if st.button("⏸ Pause", use_container_width=True):
        st.session_state.running = False

with col3:
    if st.button("↺ Reset", use_container_width=True):
        st.session_state.running = False
        st.session_state.step = 0
        st.session_state.selected = None


step = min(st.session_state.step, len(lineages_sorted))
current_lineages = lineages_sorted[:step]

st.progress(step / len(lineages_sorted))

if step == 0:
    st.markdown(
        '<div class="timeline-label">⏳ Press Play to begin</div>',
        unsafe_allow_html=True
    )
elif step < len(lineages_sorted):
    current = lineages_sorted[step - 1]
    st.markdown(
        f'<div class="timeline-label">🦴 {current["name"]} — {current["time"]:,} years ago</div>',
        unsafe_allow_html=True
    )
else:
    st.markdown(
        '<div class="timeline-label">🌍 Present day — all lineages shown</div>',
        unsafe_allow_html=True
    )


left_col, right_col = st.columns([2, 1])

with left_col:
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
            icon=folium.Icon(
                color="red" if st.session_state.selected == lineage["name"] else "blue",
                icon="info-sign"
            )
        ).add_to(m)

    map_data = st_folium(m, width=900, height=550, key=f"map_{step}")

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


with right_col:
    st.markdown("### How to Use")
    st.info(
        "Press Play to move through the timeline. "
        "Click a map marker to learn more about that lineage."
    )

    st.markdown("### Timeline Progress")
    st.write(f"Showing **{step}** out of **{len(lineages_sorted)}** lineages.")


if st.session_state.selected:
    match = next((l for l in lineages if l["name"] == st.session_state.selected), None)

    if match:
        st.markdown('<div class="species-card">', unsafe_allow_html=True)

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
                    st.image(img, use_container_width=True)

        st.markdown("### Information")

        st.write(f"📍 **Location:** {match['location']}")
        st.write(f"🕰 **Approximate time:** {match['time']:,} years ago")

        st.write(match["details"])

        st.markdown('</div>', unsafe_allow_html=True)


if st.session_state.running and step < len(lineages_sorted):
    time.sleep(3)
    st.session_state.step += 1
    st.rerun()

elif st.session_state.running and step >= len(lineages_sorted):
    st.session_state.running = False
