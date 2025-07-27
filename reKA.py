import streamlit as st

st.set_page_config(page_title="REKA Chat Sederhana", layout="wide")
st.title("REKA – Ruang Refleksi Karakter")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("Ketik di sini...")

if user_input:
    st.session_state.chat_history.append(("Kamu", user_input))
    msg = user_input.lower()

    # Rule-based responses
    if any(k in msg for k in ["hai", "halo", "hei", "hi"]):
        balasan = "Hai! Senang ngobrol sama kamu 😊 Apa kabar hari ini?"
    elif any(k in msg for k in ["insecure", "gak cukup", "ragu", "tidak percaya diri"]):
        balasan = "Aku paham kamu merasa tidak percaya diri. Coba ingat kembali hal kecil yang sudah kamu capai."
    elif any(k in msg for k in ["bingung", "gimana", "tidak tahu", "bingung"]):
        balasan = "Jika kamu merasa bingung, coba tuliskan satu hal yang ingin kamu ketahui lebih jelas."
    elif any(k in msg for k in ["capek", "lelahan", "stress"]):
        balasan = "Istirahat itu penting. Apa yang bisa membuatmu rileks sekarang?"
    elif any(k in msg for k in ["sedih", "galau", "putus asa"]):
        balasan = "Sedih itu bagian dari proses. Kamu tidak sendiri. Ceritakan kalau kamu mau."
    else:
        balasan = "Terima kasih sudah berbagi. Ingat: kamu penting, kamu tidak sendiri."

    st.session_state.chat_history.append(("REKA", balasan))

# Tampilkan chat history terbaru di atas
for sender, msg in reversed(st.session_state.chat_history):
    if sender == "Kamu":
        st.markdown(f"**🧍 {sender}:** {msg}")
    else:
        st.markdown(f"**🤖 {sender}:** {msg}")
