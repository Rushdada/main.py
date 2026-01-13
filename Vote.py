import streamlit as st
import pandas as pd

# ------------------ DATA ------------------
df = pd.DataFrame({
    'name': ["rushi", 'shubham', 'tatyaso', 'pushpa', "Amit",
             'aniket', 'ankita', 'divya', 'akshy Ana', 'john'],
    'Voter_id': [12, 13, 14, 15, 16, 17, 18, 19, 11, 20]
})

st.title("🚨 CM Vote Poll")

st.subheader("Voter Information")
st.dataframe(df)

# ------------------ VOTING SECTION ------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.header("Ajit Pawar")
    st.image(
        r"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSew6jsEGaf5mx4d9kgQ0WviZBFUF8h7TtK5Dw3IM_D--jYOlU-c8SYQ9GkaFj2XO9q5FW3Cz6z_zsA88ioNAloVBqPWDVaqu3yuhDqFz8&s=10",
        width=200
    )
    vote1 = st.button("Vote Ajit Dada")

with col2:
    st.header("Eknath Shinde")
    st.image(
        r"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTCTr_lIr6Jm5GJXFqufxNRem_aypek3EtLtw&s",
        width=400
    )
    vote2 = st.button("Vote Eknath Shinde")

with col3:
    st.header("Deva Bhau")
    st.image(
        r"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSv6nRvWFvakIxVy1IuDxaB0WNR7VY-eMdVYw&s",
        width=200
    )
    vote3 = st.button("Vote Deva Bhau")

# ------------------ VOTE RESULT ------------------
if vote1:
    st.success("🙏 Thanks for Voting Ajit Pawar")
    st.feedback("stars")

elif vote2:
    st.success("🙏 Thanks for Voting Eknath Shinde")
    st.feedback("stars")

elif vote3:
    st.success("🙏 Thanks for Voting Deva Bhau")
    st.feedback("stars")

# ------------------ SIDEBAR ------------------
st.sidebar.header("Voter Verification")

df['name'] = df['name'].str.lower()

Name = st.sidebar.text_input("Enter Voter Name").strip().lower()
Voter_id = int(st.sidebar.number_input("Enter Voter ID", step=1))
Age = int(st.sidebar.number_input("Enter Your Age", step=1))

if Name in df['name'].values:
    fetched_voter_id = df.loc[df['name'] == Name, 'Voter_id'].values[0]
else:
    fetched_voter_id = None

if Age < 18:
    st.sidebar.error("You must be 18+ to vote ❌")

elif fetched_voter_id is None:
    st.sidebar.error("Name not found ❌")

elif Voter_id != fetched_voter_id:
    st.sidebar.error("Voter ID does not match Name ❌")

else:
    st.sidebar.success("Verified Voter ✅")
    st.sidebar.info(f"Your Voter ID is {fetched_voter_id}")

#------------------Show Result---------------------

if "votes" not in st.session_state:
    st.session_state.votes = {
        "Ajit Dada": 0,
        "Eknath Shinde": 0,
        "Deva Bhau": 0
    }

if vote1:
    st.session_state.votes["Ajit Dada"] += 1
    st.success("🙏 Thanks for Voting Ajit Dada")

elif vote2:
    st.session_state.votes["Eknath Shinde"] += 1
    st.success("🙏 Thanks for Eknath Shinde")

elif vote3:
    st.session_state.votes["Deva Bhau"] += 1
    st.success("🙏 Thanks for Voting Deva Bhau")

st.subheader("📊 Live Voting Results")

result_df = pd.DataFrame.from_dict(
    st.session_state.votes,
    orient="index",
    columns=["Votes"]
)

st.bar_chart(result_df)
st.dataframe(result_df)
st.text_area("feedback")
