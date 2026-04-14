import streamlit as st

st.title("Mini-Calculator",anchor=False)

Num1= st.number_input("enter first number:",value=None,placeholder="type first number......")
Num2=st.number_input("enter second number:",value=None,placeholder="type second number......")

operation=st.selectbox("choose operation",
                       ["+", "-", "*", "/"])

calculate=st.button("calculate")

if calculate:
    try:
       if operation=="+":
        result=Num1+Num2
       elif operation=="-":
        result=Num1-Num2
       elif operation=="*":
        result=Num1*Num2
       elif operation=="/":

        if Num2!=0:           
            result=Num1-Num2
        else:
            result = "❌ Cannot divide by zero"
       st.success(f"Result: {result}")
    except Exception as e:
      st.error(f"error:{e}")
