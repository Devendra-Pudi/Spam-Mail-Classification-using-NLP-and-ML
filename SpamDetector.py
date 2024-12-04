import streamlit as st
import pickle

model = pickle.load(open('spam.pkl','rb'))
cv = pickle.load(open('vec.pkl','rb'))

def main():
    st.title('Spam Email Classifier')
    st.write("Check the email is Spam Or Not Spam")
    st.subheader('Check For Spam')
    text = st.text_area("Enter an email to classify" ,height=150)
    if st.button("Classify"):
        if text:
            with st.spinner('Classifying...'):
                data=[text]
                print(data)
                vec=cv.transform(data).toarray()
                result=model.predict(vec)
                if result[0]==0:
                    st.success("This is Not a Spam Email")
                else:
                    st.error("This is a Spam Email")
    else:
        st.error("Please Enter an Email to Classify")
main()
