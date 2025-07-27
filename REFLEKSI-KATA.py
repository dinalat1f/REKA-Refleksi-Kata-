import streamlit as st

st.set_page_config(page_title="REKA – Refleksi Kata", layout="centered")
st.title("REKA – Ruang Refleksi Karakter")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("Ketik di sini...")

if user_input:
    st.session_state.chat_history.append(("Kamu", user_input))
    
    # Respon sederhana berbasis keyword
    msg = user_input.lower()
    if "gak bisa" in msg or "bingung" in msg:
        balasan = "Aku paham kamu merasa kesulitan. Coba jelaskan lebih detail, ya."
    elif "capek" in msg:
        balasan = "Istirahat sejenak itu sama pentingnya dengan berusaha. Kamu boleh break dulu."
    else:
        balasan = "Terima kasih sudah berbagi. Kamu tidak sendiri dan aku di sini 😊"

    st.session_state.chat_history.append(("REKA", balasan))

# Tampilkan riwayat chat
for sender, msg in st.session_state.chat_history[::-1]:
    if sender == "Kamu":
        st.markdown(f"**🧍 {sender}:** {msg}")
    else:
        st.markdown(f"**🤖 {sender}:** {msg}")
