# 💻 CodeAI

**Lightweight AI-Powered Python Code Generator**

CodeAI is a lightweight, interactive chatbot application built using Streamlit that generates Python code from natural language prompts using NVIDIA's Mistral AI model via OpenAI-compatible API integration.

It allows users to describe what they want in plain English — such as "Create a binary search function" — and get syntactically correct, AI-generated Python code in real-time.

## 🚀 Features

- 💬 **Prompt-based code generation chatbot**
- 🔗 **Integrated with NVIDIA's Mistral model** using OpenAI SDK
- 🔐 **Uses .env for secure API key management**
- ⚡ **Real-time streaming code output**
- 📋 **Clean and interactive Streamlit interface**
- ⛔ **Error handling** for bad input or missing API keys
- ✅ **Minimal setup** and easy to extend

## 🧠 Tech Stack

- **Python 3.10+**
- **Streamlit** – UI Framework
- **OpenAI SDK** (NVIDIA-compatible)
- **python-dotenv** – for API key security

## 📁 Folder Structure

```
codeai/
├── main.py               # Main Streamlit chatbot app
├── .env                  # Secure API key storage
├── requirements.txt      # Dependencies
└── README.md             # Project documentation
```

## 🔐 NVIDIA API Integration

- **Endpoint**: `https://integrate.api.nvidia.com/v1`
- **Model**: `mistralai/mistral-large`
- **API key** is loaded from `.env` as:

```env
NVIDIA_API_KEY=your-api-key-here
```

## 🧪 Example Usage

**Input Prompt:**
```
Write a Python function to sort a list using bubble sort
```

**Output:** AI-generated Python code in a clean syntax-highlighted box.

## 💻 How to Run

1. **Clone or download** the repo
2. **Install requirements:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Create a .env file** and paste your NVIDIA API key:
   ```env
   NVIDIA_API_KEY=your-api-key-here
   ```
4. **Run the app:**
   ```bash
   streamlit run main.py
   ```

## 🎯 Example Prompts

Try these prompts to get started:

- `Write a function to check if a number is prime`
- `Create a binary search algorithm`
- `Build a class for managing a to-do list`
- `Generate code to read a CSV file and calculate averages`
- `Write a function to validate email addresses using regex`

## 🔧 Troubleshooting

### Windows PowerShell Issues
If you're on Windows and getting file path errors with spaces:

```powershell
# Use quotes around the command
streamlit run "main.py"
```

### Common Issues

- **"NVIDIA API key not found"**: Make sure you created a `.env` file with your API key
- **Module not found errors**: Run `pip install -r requirements.txt`
- **API connection issues**: Check your internet connection and verify your API key is valid

## 🤝 Contributing

Feel free to submit issues and enhancement requests!

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

**Made with ❤️ and AI** • Powered by NVIDIA Mistral AI