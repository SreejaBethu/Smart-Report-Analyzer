# 🧠 Smart Report Analyzer(Hugging Face + Streamlit)

Smart Report Analyzer is an LLM-powered web app built with **Streamlit**, powered by **Hugging Face models**, that intelligently summarizes and analyzes structured data (Excel/CSV) and unstructured text (PDF). It can also answer questions about the uploaded content using LLMs.

---

## 🚀 Features

- 📄 Upload **PDF**, **CSV**, or **Excel** files
- 🔍 Automatic **data preview** and **exploratory data analysis (EDA)**
- ✨ Generate smart **summaries** from structured or unstructured content
- 💬 Ask natural language questions and get answers powered by **Hugging Face LLMs**
- 📊 Dynamic visualizations with Plotly

---

## 🧰 Tech Stack

- [Streamlit](https://streamlit.io/)
- [Transformers (Hugging Face)](https://huggingface.co/docs/transformers/index)
- PyTorch
- Pandas, Plotly, PDFplumber, OpenPyXL

---

## 📁 Project Structure

 Smart-Report-Analyzer/ 
 ├── app.py # Main Streamlit app 
 
 ├── requirements.txt 
 
 ├── .env # Contains your Hugging Face token (not to be pushed) 
 
 ├── utils/ 
 
       ├── file_handler.py # Handles file upload and parsing 
       
       ├── eda.py # Data visualization (EDA) 
       
       └── llm_agent.py # LLM summarization and Q&A logic 
    
       ├── sample_sales_data.xlsx # Test Excel file (optional) 
        
       ├── sample_report.pdf # Test PDF file (optional) 
    
└── README.md


---

### 🛠️ Setup Instructions

##  1. Clone the Repository

git clone https://github.com/your-username/smart-report-analyzer.git

cd smart-report-analyzer


### 2. **Create and Activate Virtual Environment**

python -m venv venv
venv\Scripts\activate      # On Windows


### OR
source venv/bin/activate   # On Mac/Linux


### 3. Install Dependencies

pip install -r requirements.txt


### 4. Create .env File

Create a .env file in the root directory and add your Hugging Face token:

HUGGINGFACE_HUB_TOKEN=hf_xxxxxxxxxxxxxxxxxxxxxx

You can generate a free token from your Hugging Face account here:
👉 https://huggingface.co/settings/tokens


### ▶️ Run the App

streamlit run app.py

The app will open in your browser at http://localhost:8501.

--

### 📦 Sample Files

Use the included sample files to test:

    sample_sales_data.xlsx – Structured Excel data

    sample_report.pdf – Business-style unstructured report


### ✅ Models Used

Purpose	Model

Summarization	knkarthick/MEETING_SUMMARY

Table Q&A	google/tapas-large-finetuned-wtq

PDF/Text Q&A	google/flan-t5-small


### 🔐 Important Notes

Never commit your .env file or token to GitHub.

You can add .env to .gitignore:

.env

### 📌 TODOs / Future Improvements

Add support for larger files or chunked analysis

Upload multiple files for comparison

Deploy to Streamlit Cloud or HuggingFace Spaces

Improve accuracy using retrieval-augmented generation (RAG)


### 📄 License

MIT License – free to use and modify.


###💡 Author

Created by Sreeja Bethu
🔗 LinkedIn (linkedin.com/in/sreejabethu)


---

Would you like me to:

- Help write the `requirements.txt` from your current setup?
- Generate `.gitignore` for Python + Streamlit?
- Zip this project structure for upload?

Let’s get you live on GitHub and ready to showcase 💫
