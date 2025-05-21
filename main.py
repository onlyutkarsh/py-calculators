import streamlit as st

def main():
    # st.markdown("# Main page 🎈")
    # st.sidebar.markdown("# Main page 🎈")
    aer_page = st.Page("pages/aer.py", title="AER calculator", icon=":material/payments:", default=True)
    mortgage_page = st.Page("pages/mortgage.py", title="Mortgage calculator", icon=":material/login:", default=False)
    pg = st.navigation({
        "Financial": [aer_page, mortgage_page],
    })
    pg.run()

if __name__ == "__main__":
    main()
