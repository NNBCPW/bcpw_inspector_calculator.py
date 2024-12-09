import streamlit as st

def calculate_set_length(benchmark, height_of_instrument, proposed_elevation, layers):
    # Calculate BM + HI
    bm_plus_hi = benchmark + height_of_instrument

    # Filter valid layers and convert inches to feet
    total_layer_thickness_in_inches = sum(layers)
    total_layer_thickness_in_feet = total_layer_thickness_in_inches / 12

    # Calculate Rod Reading
    rod_reading = bm_plus_hi - (proposed_elevation + total_layer_thickness_in_feet)
    return bm_plus_hi, total_layer_thickness_in_inches, total_layer_thickness_in_feet, rod_reading

# Streamlit app
st.title("BCPW CONST INSPECTOR ELEVATIONS CALCULATOR")

# Input fields
station_number = st.text_input("Station Number:")
benchmark = st.number_input("Benchmark Reading (ft)", value=0.0, step=0.01)
height_of_instrument = st.number_input("Height of Instrument (ft)", value=0.0, step=0.01)

# Calculate BM + HI
bm_plus_hi = benchmark + height_of_instrument
st.markdown(f"### BM + HI: {bm_plus_hi:.2f} ft")

proposed_elevation = st.number_input("Proposed Elevation (ft)", value=0.0, step=0.01)

# Dropdowns for street section cuts (C16-C20 equivalent)
layer_options = ["", "Pre Lime Subgrade", "Post Lime Subgrade", "Sand", "Dirt", "Rock", "Base", "Asphalt", "Concrete", "Curb", "Inlet"]
layer_thicknesses = [
    st.selectbox(f"Layer {i+1} Type (inches)", options=layer_options, index=0, format_func=lambda x: x or "None")
    for i in range(5)
]

# Convert dropdowns to thickness values (assuming all dropdown options give integer thickness; adjust logic as needed)
layer_values = [
    st.number_input(f"Thickness of {layer} (inches)", value=0, step=1) if layer else 0
    for layer in layer_thicknesses
]

# Calculate the results
if st.button("Calculate"):
    bm_plus_hi, total_in_inches, total_in_feet, rod_reading = calculate_set_length(
        benchmark, height_of_instrument, proposed_elevation, layer_values
    )

    st.markdown(f"### Total Layer Thickness: {total_in_inches:.2f} inches ({total_in_feet:.2f} ft)")
    st.markdown(f"### Rod Reading: {rod_reading:.2f} ft")
