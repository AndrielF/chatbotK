
<div align="center">
<h1 align="center">
<img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
<br>Chatbot Personalizado!
</h1>
<h3>◦ Chat smarter, chat with FMF!</h3>
<h3>◦ Developed with the software and tools listed below.</h3>

<p align="center">
<img src="https://img.shields.io/badge/tqdm-FFC107.svg?style&logo=tqdm&logoColor=black" alt="tqdm" />
<img src="https://img.shields.io/badge/TensorFlow-FF6F00.svg?style&logo=TensorFlow&logoColor=white" alt="TensorFlow" />
<img src="https://img.shields.io/badge/precommit-FAB040.svg?style&logo=pre-commit&logoColor=black" alt="precommit" />
<img src="https://img.shields.io/badge/Keras-D00000.svg?style&logo=Keras&logoColor=white" alt="Keras" />
<img src="https://img.shields.io/badge/OpenAI-412991.svg?style&logo=OpenAI&logoColor=white" alt="OpenAI" />
<img src="https://img.shields.io/badge/Python-3776AB.svg?style&logo=Python&logoColor=white" alt="Python" />

<img src="https://img.shields.io/badge/AIOHTTP-2C5BB4.svg?style&logo=AIOHTTP&logoColor=white" alt="AIOHTTP" />
<img src="https://img.shields.io/badge/Pytest-0A9EDC.svg?style&logo=Pytest&logoColor=white" alt="Pytest" />
<img src="https://img.shields.io/badge/NumPy-013243.svg?style&logo=NumPy&logoColor=white" alt="NumPy" />
<img src="https://img.shields.io/badge/JSON-000000.svg?style&logo=JSON&logoColor=white" alt="JSON" />
<img src="https://img.shields.io/badge/Markdown-000000.svg?style&logo=Markdown&logoColor=white" alt="Markdown" />
<img src="https://img.shields.io/badge/Markdown-000000.svg?style&logo=Markdown&logoColor=white" alt="Markdown" />
</p>
</div>

---

## 📒 Table of Contents
- [📒 Table of Contents](#-table-of-contents)
- [📍 Overview](#-overview)
- [⚙️ Features](#-features)
- [📂 Project Structure](#project-structure)
- [🧩 Modules](#modules)
- [🚀 Getting Started](#-getting-started)
- [🗺 Roadmap](#-roadmap)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👏 Acknowledgments](#-acknowledgments)

---


## 📍 Overview

The project located at /Users/andriel/DevNew/PROJETO-FMF-chatbot is a chatbot implementation that utilizes natural language processing and AI models to generate responses. It includes a graphical user interface (GUI) for displaying the chatbot conversation and supports both text and voice input. Users can interact with the chatbot by asking questions, and the chatbot provides relevant responses based on predefined intents, an OpenAI language model, or a custom API. This project offers the value proposition of providing an interactive and user-friendly chatbot interface for easily obtaining information and assistance.

---

## ⚙️ Features

| Feature                | Description                           |
| ---------------------- | ------------------------------------- |
| **⚙️ Architecture**     | The codebase follows a modular architecture. It uses a chatbot implementation with various libraries and APIs for natural language processing and response generation. It incorporates a graphical user interface (GUI) using Tkinter to display the conversation. The system handles user input via text field or voice input using the microphone. Limit: 200 characters.    |
| **📖 Documentation**   | The codebase lacks comprehensive documentation. While some code comments and file summaries are present, there is room for improvement in providing detailed explanations and usage instructions. Limit: 200 characters.    |
| **🔗 Dependencies**    | The codebase depends on multiple external libraries and APIs, including keras, gtts, numpy, pickle, json, os, speech_recognition, requests, nltk, openai, dotenv, and tkinter. These dependencies are crucial for the functioning of the chatbot, NLP operations, GUI creation, and API integrations. Limit: 200 characters.    |
| **🧩 Modularity**      | The system exhibits modularity by organizing functionalities into separate files. There is a clear separation of concerns between the chat logic, GUI implementation, data processing, and model training. This organization allows for code reusability, maintainability, and extensibility. Limit: 200 characters.    |
| **✔️ Testing**          | The codebase lacks information on testing strategies and tools. There is no clear indication of automated tests, unit tests, or integration tests being implemented. Addition of a testing framework, like PyTest, and comprehensive test coverage would be beneficial. Limit: 200 characters.    |
| **⚡️ Performance**      | The performance of the codebase depends on the efficiency of the underlying libraries and APIs used. No specific benchmarks or performance metrics are available in the codebase. The use of neural networks for chatbot training and dependency on external services like OpenAI may impact performance. Limit: 200 characters.    |
| **🔐 Security**        | The codebase does not explicitly exhibit security measures beyond the use of standard libraries. It is essential to ensure secure handling of user data, input sanitization, and protection against potential vulnerabilities like injection attacks or unintended data leakage. Limit: 200 characters.    |
| **🔀 Version Control** | The codebase includes the Git version control system. However, details about specific version control strategies and tools used, such as branching strategies or continuous integration workflows, are not provided. There is a scope for enhancing the version control process by implementing best practices. Limit: 200 characters.    |
| **🔌 Integrations**    | The system interacts with various external systems and APIs. It involves integration with OpenAI's chat-based language model, an external custom API, and libraries like NLTK for data processing. These integrations allow the chatbot to generate responses and leverage external NLP capabilities. Limit: 200 characters.    |
| **📶 Scalability**     | The codebase's scalability depends on the underlying libraries, APIs, and infrastructure used. There is no explicit information or architectural considerations mentioned regarding scalability. To ensure scalability, the system may require optimizations

---


## 📂 Project Structure


```bash
repo
├── README.md
├── chatbot_model.h5
├── chatgui.py
├── classes.pkl
├── intents.json
├── requirements.txt
├── train_chatbot.py
└── words.pkl

1 directory, 8 files
```

---

## 🧩 Modules

<details closed><summary>Root</summary>

| File             | Summary                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ---              | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| chatgui.py       | The provided code snippet is a chatbot implementation that uses various libraries and APIs for natural language processing and generating responses.Here are the core functionalities of the code:-It imports necessary modules like `keras`, `gtts`, `numpy`, `pickle`, `json`, `os`, `speech_recognition`, `requests`, `nltk`, `openai`, `dotenv`, and `tkinter`.-It loads the required AI models, dataset, and other resources.-It defines functions for cleaning up sentences, converting them into bags of words (BOWs), and predicting classes based on the BOWs using a trained AI model.-It generates responses using predefined intents from a JSON file, randomly selecting appropriate responses from the matched intent.-It includes additional functions for interacting with OpenAI's chat-based language model and a custom API.-It provides options for getting user input via a text field or voice input using the microphone.-It incorporates a graphical user interface (GUI) using Tkinter, where the chatbot conversation is displayed.This code snippet demonstrates the implementation of a chatbot that can respond to user queries using predefined intents, OpenAI's language model, or a custom API. It incorporates both text and voice input and includes a simple GUI for displaying the conversation. |
| train_chatbot.py | The provided code snippet performs the following tasks: 1. Downloads and imports necessary packages and datasets from NLTK library2. Processes and cleans the text data, lemmatizes words, removes punctuation3. Creates a model and trains it using neural networks with Keras4. Saves the trained model to be used for chatbot applications.5. Prints out important information about the data and the created model.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

</details>

---

## 🚀 Getting Started

### ✔️ Prerequisites

Before you begin, ensure that you have the following prerequisites installed:
> - `ℹ️ Requirement 1`
> - `ℹ️ Requirement 2`
> - `ℹ️ ...`

### 📦 Installation

1. Clone the PROJETO-FMF-chatbot repository:
```sh
git clone /Users/andriel/DevNew/PROJETO-FMF-chatbot
```

2. Change to the project directory:
```sh
cd PROJETO-FMF-chatbot
```

3. Install the dependencies:
```sh
pip install -r requirements.txt
```

### 🎮 Using PROJETO-FMF-chatbot

```sh
python main.py
```

### 🧪 Running Tests
```sh
pytest
```

---


## 🗺 Roadmap

> - [X] `ℹ️  Task 1: Implement X`
> - [ ] `ℹ️  Task 2: Refactor Y`
> - [ ] `ℹ️ ...`


---

## 🤝 Contributing

Contributions are always welcome! Please follow these steps:
1. Fork the project repository. This creates a copy of the project on your account that you can modify without affecting the original project.
2. Clone the forked repository to your local machine using a Git client like Git or GitHub Desktop.
3. Create a new branch with a descriptive name (e.g., `new-feature-branch` or `bugfix-issue-123`).
```sh
git checkout -b new-feature-branch
```
4. Make changes to the project's codebase.
5. Commit your changes to your local branch with a clear commit message that explains the changes you've made.
```sh
git commit -m 'Implemented new feature.'
```
6. Push your changes to your forked repository on GitHub using the following command
```sh
git push origin new-feature-branch
```
7. Create a new pull request to the original project repository. In the pull request, describe the changes you've made and why they're necessary.
The project maintainers will review your changes and provide feedback or merge them into the main branch.

---

## 📄 License

This project is licensed under the `ℹ️  INSERT-LICENSE-TYPE` License. See the [LICENSE](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-license-to-a-repository) file for additional info.

---

## 👏 Acknowledgments

> - `ℹ️  List any resources, contributors, inspiration, etc.`

---
