import streamlit as st


def front_end():
    st.set_page_config(layout="wide")
    st.title("Customer Support and diagnostics through LLM")


def steps():
    with st.container():
        st.write("First check the configuration is intact ")
        st.write("Here are some show commands to validate")
        st.write("Here are some source documents")


def similar_tickets():
    with st.container():
        st.subheader("Similar Reported tickets")

def cli_commands():
    with st.container():
        st.write("Here are the cli commands")


def main():
    front_end()
    customer_issue = st.text_input("Enter the troubleshooting question")
    st.button("Submit")
    st.subheader("Diagnostic steps")
    steps()
    cli_commands()
    similar_tickets()
    




if __name__ == "__main__":
    main()

