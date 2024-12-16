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
st.markdown("<h2 style='text-align: center;'>BCPW Elevation Calc</h2>", unsafe_allow_html=True)


# Input fields
station_number = st.text_input("Station Number:")
benchmark = st.number_input("Benchmark Reading (ft)", value=0.0, step=0.01)
height_of_instrument = st.number_input("Height of Instrument (ft)", value=0.0, step=0.01)

# Calculate BM + HI
bm_plus_hi = benchmark + height_of_instrument
st.markdown(f"### BM + HI: {bm_plus_hi:.2f} ft")

proposed_elevation = st.number_input("Proposed Elevation (ft)", value=0.0, step=0.01)

# Dropdowns and inline thickness inputs for layers
layer_options = ["Pre Lime Subgrade", "Post Lime Subgrade", "Sand", "Dirt", "Rock", "Base", "Asphalt", "Concrete", "Curb", "Inlet"]
layer_thicknesses = []

st.markdown("### Layer Inputs")
for i in range(1, 6):
    cols = st.columns([3, 1])  # Adjust column widths for dropdown and input
    with cols[0]:
        layer_type = st.selectbox(f"Layer {i} Type:", options=["None"] + layer_options, key=f"layer_{i}_type")
    with cols[1]:
        thickness = st.number_input(f"Inches:", value=0, step=1, key=f"layer_{i}_thickness")
        layer_thicknesses.append(thickness)

# Calculate the results
if st.button("Calculate"):
    bm_plus_hi, total_in_inches, total_in_feet, rod_reading = calculate_set_length(
        benchmark, height_of_instrument, proposed_elevation, layer_thicknesses
    )

    st.markdown(f"### Total Layer Thickness: {total_in_inches:.2f} inches ({total_in_feet:.2f} ft)")
    st.markdown(f"### Rod Reading: {rod_reading:.2f} ft")
# Footer directly added at the end
st.markdown(
    """
    <div style="width: 100%; background-color: black; color: white; text-align: center; padding: 10px; margin-top: 20px;">
        Created by: NN <br>
        <a href="mailto:Nicholas.nabholz@bexar.org?subject=Feedback%20on%20BCPW%20Elevation%20Calc&body=Hello,%0A%0AI%20would%20like%20to%20provide%20feedback%20on%20the%20app.%0A%0A" 
           style="color: white; text-decoration: none;">
            For support, please email me. Thanks!
        </a>
    </div>
    """,
    unsafe_allow_html=True,
)
