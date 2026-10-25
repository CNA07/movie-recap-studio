


import streamlit as st

st.set_page_config(
    page_title="Movie Recap Studio",
    page_icon="🎬",
    layout="centered",
)

st.title("🎬 Movie Recap Studio")
st.write("Turn your movie into a recap video.")

st.divider()

st.subheader("Upload your movie")

video = st.file_uploader(
    "Choose a video",
    type=["mp4", "mov", "mkv", "avi", "webm"],
)

if video is not None:
    st.success(f"Video selected: {video.name}")
    st.video(video)

    if st.button("✨ Generate Recap", type="primary",
                  use_container_width=True):
        st.info(
            "Your video is ready for processing. "
            "The AI recap backend will be connected "
            "in the next step."
        )
else:
    st.caption("Upload a video to get started.")

st.divider()
st.caption("Movie Recap Studio · Your personal recap workspace")

