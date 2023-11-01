import pickle
import streamlit as st
# import sklearn
import urllib.request
import numpy as np


st.markdown(
    """
    <style>
    body {
        background-color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Set the header color to light blue
st.markdown(
    """
    <style>
    h1 {
        color: #01EDF4;
    }
    </style>
    """,
    unsafe_allow_html=True
)

model_url = "https://github.com/BlackHole3344/DataScienceApp/blob/main/trainedINSURANCE.sav"
model_file = urllib.request.urlopen(model_url)
#
# st.markdown(f'<style>{custom_css}</style>', unsafe_allow_html=True)
load_model = pickle.load(open(model_file , "rb"))
# function for prediction

image_url = "https://www.bajajfinserv.in/marketplace/insurance/health-insurance/health-insurance-premium-calculator/assets/img/MedicalImage.png"
st.image(image_url, caption=" ", use_column_width=True)
def insurance_predction(input):
    INPUT = np.array(input).reshape(1,-1)
    charge_prediction = load_model.predict(INPUT)
    rounded_charge = round(charge_prediction[0] , 2)
    return rounded_charge



def main():
    st.title("Insurance Charge Prediction")

    age = st.slider("Age", min_value = 18 , max_value = 60 , value= 18)

    sex = st.radio("Gender" , ("Male" , "Female"))
    bmi = st.number_input("BMI (Body Mass index)" , min_value=10 , max_value= 50 , value = 20)
    smokers = st.selectbox("Smoker" , ("No" , "Yes"))
    children = st.number_input("Enter no of childrens" , min_value = 0 , max_value= 5 , value = 0 )

    # regions
    st.subheader("Select Region")
    selected_region = st.radio("Select Your Region" , ('northeast', 'northwest', 'southeast', 'southwest'))
    regions = {"northeast": 0 , "northwest": 0 , "southwest": 0 , "southeast": 0}
    regions[selected_region] = 1

    if st.button("Predict The Charges") :
        sex_num = 0 if sex == "Male" else 1
        smoke_bin = 0 if smokers == "No" else 1
        # input_type = ["age" , "bmi" , "smoker_bin" , "children" , "sex_cat" , 'northeast', 'northwest', 'southeast', 'southwest' ]
        input_list = [age , bmi , smoke_bin , children , sex_num , regions["northeast"] , regions["northeast"] , regions["southwest"] , regions["southwest"]]
        predd = insurance_predction(input_list)

        st.write(f"Your insurance charge will be: ${predd:.2f}")


if __name__ == "__main__":
    main()









