import pickle as pkl
import streamlit as st
import numpy as np


model = pkl.load(open("rd_clf.pkl","rb"))

st.title("Survival Prediction")

p = st.selectbox("Select your Passenger Class ",options = ["PClass 1",'PClass 2',"PClass 3"])
pclass = ["PClass 1",'PClass 2',"PClass 3"].index(p)

g = st.selectbox("Gender ",options=["Female","Male"])
gender = ["Female","Male"].index(g)

ag = st.slider("Age ",min_value = 1,max_value = 100,step=1,value=35)
age = np.log(ag)

sp =st.slider("Number of siblings/spouse aboard the Titanic ",min_value = 0,max_value = 10,value = 4,step=1)

pa = st.slider("Number of parents/children aboard the Titanic ",min_value = 0,max_value = 10,value = 2,step=1)

f = st.slider("Ticket Fare ",min_value = 0.0,max_value = 513.0,value = 300.0,step=0.5)
fare = np.log(f)

e = st.selectbox("Port of Embarkation ",options = ["Cherbourg","Queenstone","Southampton"])
embarked = ["Cherbourg","Queenstone","Southampton"].index(e)


if st.button("Predict Your Chances ?"):
    x = model.predict(np.array([[pclass,gender,age,sp,pa,fare,embarked]]))[0]
    
    if x == 1:
        st.image("Survived image.jpg")
        st.write("***congratulation !!!....*** **You probably would have made it!**")
    elif x == 0:
        st.image("rip_last.png")
        st.write("***Better Luck Next time !!!!...*** **you're probably Ended up like 'Jack'**")
