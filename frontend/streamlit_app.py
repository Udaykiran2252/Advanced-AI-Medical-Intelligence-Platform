import streamlit as st
import requests

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Advanced AI Medical Intelligence Platform",
    page_icon="🩺",
    layout="centered"
)

# -----------------------------
# Title
# -----------------------------
st.title("🩺 Advanced AI Medical Intelligence Platform")
st.markdown("### AI-Powered Chest X-ray Pneumonia Detection")

st.write(
    "Upload a Chest X-ray image to detect **Pneumonia** using the trained AI model."
)

# -----------------------------
# Upload Image
# -----------------------------
uploaded_file = st.file_uploader(
    "Choose a Chest X-ray Image",
    type=["jpg", "jpeg", "png"]
)

# -----------------------------
# Prediction
# -----------------------------
if uploaded_file is not None:

    st.image(
        uploaded_file,
        caption="Uploaded Chest X-ray",
        width="stretch"
    )

    st.write("")

    if st.button("🔍 Predict"):

        with st.spinner("Analyzing Chest X-ray..."):

            files = {
                "file": (
                    uploaded_file.name,
                    uploaded_file.getvalue(),
                    uploaded_file.type
                )
            }

            try:

                response = requests.post(
                    "http://127.0.0.1:8000/predict",
                    files=files,
                    timeout=60
                )

                if response.status_code == 200:

                    result = response.json()

                    st.success("✅ Prediction Completed Successfully")

                    # -----------------------------
                    # Prediction
                    # -----------------------------
                    st.subheader("🧠 Prediction")

                    if result["prediction"].upper() == "NORMAL":
                        st.success(result["prediction"])
                    else:
                        st.error(result["prediction"])

                    # -----------------------------
                    # Confidence
                    # -----------------------------
                    st.subheader("📊 Confidence")

                    confidence = float(result["confidence"])

                    st.progress(min(confidence / 100, 1.0))

                    st.write(f"**Confidence:** {confidence:.2f}%")

                    # -----------------------------
                    # AI Medical Report
                    # -----------------------------
                    st.subheader("🩺 AI Medical Report")

                    st.info(result["report"])

                    # -----------------------------
                    # Model Explainability
                    # -----------------------------
                    st.subheader("🧠 Model Explainability")

                    st.info(
                        "This version focuses on AI-powered pneumonia detection "
                        "and automated medical report generation."
                    )

                else:
                    st.error("❌ Prediction Failed")
                    st.code(response.text)

            except requests.exceptions.ConnectionError:
                st.error("❌ Cannot connect to FastAPI server.")
                st.info(
                    "Please start the FastAPI server first:\n\n"
                    "python -m uvicorn backend.app:app --reload"
                )

            except requests.exceptions.Timeout:
                st.error("❌ Request timed out.")

            except Exception as e:
                st.exception(e)

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")

st.caption(
    "⚠️ Disclaimer: This application is intended for educational and research purposes only. "
    "It is not a substitute for professional medical advice, diagnosis, or treatment."
)