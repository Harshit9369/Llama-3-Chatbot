# Llama-3-Chatbot
Streamlit Chatbot with Llama-3 chat


## Prerequisites

Before running the Streamlit Chatbot with Memory, you need to have the following installed:

1. Python (version 3.6 or higher)
2. Ollama (llama3 model - 4.7 GB) 

## Installation

To set up the chatbot locally, follow these steps:

1. Clone this repository to your local machine using Git and cd into the folder:

```bash
git clone https://github.com/Harshit9369/Llama-3-Chatbot.git
```

2. Create a virtual environment (optional but recommended) and activate it:

```bash
python -m venv venv
source venv/bin/activate  
```

3. Install the required Python packages:

```bash
pip install -r requirements.txt
```

## Usage

To run the Streamlit Chatbot with Memory, execute the following command:

```bash
streamlit run app.py
```

This will start the Streamlit server, and you can access the chatbot interface by opening your web browser and navigating to `http://localhost:8501`.

Simply type your messages in the input box and press "Enter" to send them to the chatbot. The chatbot will respond based on the context of the conversation, thanks to its memory capabilities.
