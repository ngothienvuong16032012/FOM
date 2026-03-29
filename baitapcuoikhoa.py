import streamlit as st
import time

# ===== CONFIG =====
st.set_page_config(
    page_title="Tự do âm nhạc",
    page_icon="🎵",
    layout="wide"
)

# ===== STATE =====
if "selected" not in st.session_state:
    st.session_state.selected = "🧒 Thiếu nhi"

if "effect" not in st.session_state:
    st.session_state.effect = ""

# ===== SIDEBAR =====
st.sidebar.title("🎧 Menu")
trang = st.sidebar.radio(
    "Chọn trang:",
    ["Trang chủ", "Khám phá nhạc", "Giới thiệu dự án"]
)

# ===== DATA (GIỮ NGUYÊN) =====
data = {
    "🧒 Thiếu nhi": ["1Ne1hqOXKKI"],
    "😢 Nhạc buồn": ["5OESzopq3dE", "MkTWK8Sg7g8", "sJEbO_CsVo8"],
    "💖 Tình cảm": ["GIDoQsQyS0s", "fLrW_TqTNs4"],
    "🎤 Nhạc trẻ": ["aJBsZgvAEmk"],
    "🔥 Chiến tranh": [
        "Y_AU7DWWKsE", "fQPlSoz_jSA", "1tgFZP4NxBo",
        "gn63Siphu3M", "bm9QJQqGm7A"
    ],
    "🏛️ Lịch sử": ["CMC2xquhRUo", "4tmq1rF2xBc"],
    "📸 Ghép ảnh": [
        "ICNYa1lzVqo", "b2AF5HXA9rs",
        "GMUR8V2rGPs", "hSZYtLRAUyI",
        "MYaKCrEN-Cw"
    ]
}

categories = list(data.keys())

# ===== TRANG CHỦ =====
if trang == "Trang chủ":
    st.title("🎵 TỰ DO ÂM NHẠC")
    st.write("Chào mừng bạn đến với thế giới âm nhạc!")

# ===== KHÁM PHÁ NHẠC =====
elif trang == "Khám phá nhạc":

    st.title("🎶 KHÁM PHÁ ÂM NHẠC")

    # ===== MOOD =====
    st.markdown("## 🎚️ Chọn mood của bạn")
    mood = st.slider("Mood:", 0, 100, 0)

    index = min(mood // 15, len(categories) - 1)
    auto_category = categories[index]

    st.success(f"🎧 Gợi ý theo mood: {auto_category}")

    # ===== BUTTON =====
    st.markdown("## 👉 Hoặc chọn thủ công")
    cols = st.columns(len(categories))

    for i, category in enumerate(categories):
        if cols[i].button(category):
            st.session_state.selected = category
            st.session_state.effect = category

    selected = st.session_state.selected

    st.markdown("---")

    # ===== EFFECT (ỔN ĐỊNH) =====
    effect = st.session_state.effect

    if effect == "🔥 Chiến tranh":
        st.warning("🚀 Đang tấn công...")
        progress = st.progress(0)
        for i in range(100):
            time.sleep(0.01)
            progress.progress(i + 1)
        st.error("💥 BOOM!!!")

    elif effect == "💖 Tình cảm":
        st.balloons()
        st.success("💖 Tình yêu đang lan tỏa!")

    elif effect == "😢 Nhạc buồn":
        st.snow()
        st.info("🌧️ Tâm trạng buồn...")

    elif effect == "🧒 Thiếu nhi":
        st.balloons()
        st.write("🧸 Vui nhộn, dễ thương!")

    elif effect == "🏛️ Lịch sử":
        st.warning("🏛️ Đang quay về quá khứ...")

    elif effect == "📸 Ghép ảnh":
        st.info("📸 Đang xử lý ảnh...")

    elif effect == "🎤 Nhạc trẻ":
        st.toast("🔥 Chill thôi!")

    # reset effect (tránh lặp)
    st.session_state.effect = ""

    # ===== VIDEO =====
    st.subheader(f"🎬 {selected}")

    cols = st.columns(2)
    for i, vid in enumerate(data[selected]):
        with cols[i % 2]:
            st.video(f"https://www.youtube.com/watch?v={vid}")

    # ===== MOOD TEXT =====
    st.markdown("---")

    if mood < 15:
        st.write("👶 Nhẹ nhàng, dễ thương")
    elif mood < 30:
        st.write("😢 Hơi buồn")
    elif mood < 45:
        st.write("💔 Sâu lắng")
    elif mood < 60:
        st.write("💖 Yêu đời")
    elif mood < 75:
        st.write("😎 Chill")
    elif mood < 90:
        st.write("🔥 Sung")
    else:
        st.write("💥 MAX năng lượng")

# ===== GIỚI THIỆU =====
else:
    st.title("📌 Giới thiệu")
    st.write("App khám phá âm nhạc theo cảm xúc ")
    st.write("bạn có thể cho tôi thêm một gợi ý để phát triển trong tương lai không")                                                                                                                                                
    user_input = st.text_input("Bạn đang cảm thấy thế nào?Có thể giúp tôi đưa ra hướng đi tương lai chứ")
    if user_input:
        st.write("cảm ơn vì những đóng góp của bạn cho dự án?Chúc bạn có một trải nghiệm tuyệt vời")
        
