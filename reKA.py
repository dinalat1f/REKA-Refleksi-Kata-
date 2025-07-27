import streamlit as st

st.set_page_config(page_title="REKA Chat", layout="wide")
st.title("REKA – Ruang Refleksi Karakter")

# Chat Input
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("Ketik di sini...")

if user_input:
    st.session_state.chat_history.append(("Kamu", user_input))
    
    # Jawaban sederhana (simulasi)
    if "insecure" in user_input.lower():
        balasan = "Ingat ya, kamu berharga bukan karena pencapaianmu, tapi karena kamu adalah kamu."
    else:
        balasan = "Terima kasih sudah bercerita. Kamu tidak sendiri."

    st.session_state.chat_history.append(("REKA", balasan))

# Tampilkan riwayat chat
for sender, msg in st.session_state.chat_history:
    if sender == "Kamu":
        st.markdown(f"🧍 {sender}:** {msg}")
    else:
        st.markdown(f"🤖 {sender}:** {msg}")
