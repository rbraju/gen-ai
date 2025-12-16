# Simple Chat Bot

### Env Setup
1. Install below python and pip versions
```
[rajesh:~] which python
/Users/rbraju/venvs/langchain-python3.11.14/bin/python

[rbraju:~] python --version
Python 3.11.14

[rbraju:~] pip --version
pip 25.3 from /Users/rbraju/venvs/langchain-python3.11.14/lib/python3.11/site-packages/pip (python 3.11)
[rbraju:~] 
```

Create a new virtual env and activate it
```
[rbraju:~] python3 -m venv ~/venvs/langchain-python3.11.14
[rbraju:~] source ~/venvs/langchain-python3.11.14/bin/activate
(langchain-python3.11.14) [rbraju:~] 
```

## Sanity check
Run the below script to check the setup and imports are fine.
```
(langchain-python3.11.14) [rajesh:~/git/rbraju/gen-ai] python sanity-check.py 
3.11.14 (main, Oct  9 2025, 16:16:55) [Clang 17.0.0 (clang-1700.4.4.1)]
ALL IMPORTS OK
(langchain-python3.11.14) [rbraju:~/git/rbraju/gen-ai] 
```

## Run the app
```
(langchain-python3.11.14) [rajesh:~/git/rbraju/gen-ai] python -m streamlit run chatbot.py
  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.1.249:8501

  For better performance, install the Watchdog module:

  $ xcode-select --install
  $ pip install watchdog
(langchain-python3.11.14) [rbraju:~/git/rbraju/gen-ai] 
```
