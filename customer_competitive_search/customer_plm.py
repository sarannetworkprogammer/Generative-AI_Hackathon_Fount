"""
Logic of this program is like, whenever competitior word is in search query that indicates they are comparing against,
Immediately this triggered to particular point of contact and win the deal.

How this is implemented.

Currently we are searching keywords of competitors [cisco, juniper, arista,exterme]
But going forward we integerate with ML algorithms and we use here and logic of both 
Traditional and ML algorithms


"""

import streamlit as st


def customer_future_requirements(user_query, key_words):
    count = 0
    for each in key_words:
        if each in user_query:
            count = count+1
    return count



def front_end():
    
    st.set_page_config(layout="wide")
    st.title("Customer Future requirements based on search query")
  



def main():
    front_end()

    f = open("future.txt","a")
    #user_sentence = input("enter customer query")

    st.write("we fetch authentication from SSO")
    cust = st.selectbox("Select customer",["customer1","customer2","customer3","customer4", "customer5"])



    plm_mapping = {"customer1":"plm_contact1",
                         "customer2":"plm_contact2",
                         "customer3":"plm_contact3",
                         "customer4":"plm_contact4",
                         "customer5":"plm_contact5",
                        }
                    
    

    user_query = st.text_input("Enter the user query")

    user_query = user_query.lower().strip()           # converting lowercase 
    
    #print(user_query)
   
    key_words = ["feature","cisco","juniper","arista","equivalent", "extreme", "nokia", "competitor"]

    if st.button("search"):
    
        score = customer_future_requirements(user_query, key_words)

        if score >=1: # This can be interchangable used to set threshold value
            f.write("\n" + cust + " : " + user_query + " : " + plm_mapping[cust])


if __name__ =="__main__":
    main()
   



