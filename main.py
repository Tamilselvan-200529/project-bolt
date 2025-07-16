import streamlit as st
from openai import OpenAI

# Page setup
st.set_page_config(
    page_title="CodeAI",
    page_icon="💻",
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>
    .main-title {
        text-align: center;
        color: #2E86AB;
        font-size: 2.5rem;
        font-weight: bold;
        margin-bottom: 0.5rem;
    }
    .subtitle {
        text-align: center;
        color: #666;
        font-size: 1.1rem;
        margin-bottom: 2rem;
    }
    .stTextArea > div > div > textarea {
        border-radius: 8px;
        border: 2px solid #e0e0e0;
        font-size: 1rem;
    }
    .stButton > button {
        background-color: #2E86AB;
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.6rem 1.5rem;
        font-size: 1rem;
        font-weight: 600;
        width: 100%;
        transition: background-color 0.3s ease;
    }
    .stButton > button:hover {
        background-color: #1F5F7A;
    }
    .error-box {
        background-color: #ffebee;
        color: #c62828;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #f44336;
        margin: 1rem 0;
    }
    .success-box {
        background-color: #e8f5e8;
        color: #2e7d32;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #4caf50;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Init client with NVIDIA Qwen model
def initialize_client():
    api_key = st.secrets["NVIDIA_API_KEY"]
    if not api_key:
        st.markdown('<div class="error-box">🔑 <strong>Error:</strong> NVIDIA API key not found! Please set it in Streamlit secrets.</div>', unsafe_allow_html=True)
        st.stop()
    return OpenAI(
        base_url="https://integrate.api.nvidia.com/v1",
        api_key=api_key
    )

# Generate code using Qwen model
def generate_code(client, prompt):
    try:
        formatted_prompt = f"""
        Provide only the Python code (no explanation) to complete the following task:

        {prompt}

        - Only return Python code
        - Do not include any text before or after the code
        """

        completion = client.chat.completions.create(
            model="qwen/qwq-32b",
            messages=[{"role": "user", "content": formatted_prompt}],
            temperature=0.6,
            top_p=0.7,
            max_tokens=2048,
            stream=True
        )

        generated_code = ""
        code_placeholder = st.empty()

        for chunk in completion:
            delta = chunk.choices[0].delta
            if hasattr(delta, "content") and delta.content:
                generated_code += delta.content
                code_placeholder.code(generated_code, language='python')

        if not generated_code.strip():
            return "⚠️ No output received. Try rephrasing the prompt."

        return generated_code

    except Exception as e:
        st.markdown(f'<div class="error-box">❌ <strong>Error:</strong> {str(e)}</div>', unsafe_allow_html=True)
        return None

# Main app
def main():
    st.markdown('<h1 class="main-title">💻 CodeAI</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">⚡ Powered by NVIDIA Qwen 32B - Streamed Python Code Generation</p>', unsafe_allow_html=True)

    client = initialize_client()

    st.markdown("### 💬 What code do you need?")
    user_prompt = st.text_area(
        "",
        placeholder="Example: Create a function to reverse a string",
        height=120,
        help="Clearly describe the code or function you want."
    )

    if st.button("🚀 Generate Code"):
        if not user_prompt.strip():
            st.warning("⚠️ Please enter a description!")
            return

        with st.spinner("🧠 Generating code..."):
            st.markdown("---")
            st.markdown("### 📋 Output Code:")
            generated_code = generate_code(client, user_prompt)

            if generated_code:
                st.markdown('<div class="success-box">✅ <strong>Code generated successfully!</strong></div>', unsafe_allow_html=True)

                st.download_button(
                    label="💾 Download Code",
                    data=generated_code,
                    file_name="generated_code.py",
                    mime="text/python"
                )

    st.markdown("---")
    st.markdown(
        "<p style='text-align: center; color: #888; font-size: 0.9rem;'>"
        "Powered by <strong>Qwen 32B</strong> • Streamed by NVIDIA • Built with Streamlit"
        "</p>",
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
