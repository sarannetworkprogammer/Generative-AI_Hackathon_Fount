import streamlit as st    


def customer_cfd(user_query, key_words):
    count = 0
    for each in key_words:
        if each in user_query:
            count = count+1
    return count



def display_cfd(user_query,score):
    with st.container():
        if st.button("Process"):
            if score >= 1:
                st.write(user_query)


def front_end():
    st.set_page_config(layout="wide")
    st.title("CFD Predictive Analysis")



def main():

    front_end()
    f = open("future_cfd.txt","a")

    st.write("we fetch authentication from SSO")
    cust = st.selectbox("Select customer",["customer1","customer2","customer3","customer4", "customer5","All"])


    customer_mapping = {"customer1":"point_of_contact1",
                        "customer2":"point_of_contact2",
                        "customer3":"point_of_contact3",
                        "customer4":"point_of_contact4",
                        "customer5":"point_of_contact5",
                        }
                    



    #user_query = st.text_input("Enter the user query")

    #print(f"user_query ={user_query}")
    
    key_words =["crash", "core-dump","flap", "in-active", "notup", "reboot"]

    if st.button("search"):


        st.write("Predictive_CFD.csv file generated")
        






if __name__ == "__main__":
    main()
