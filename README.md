# 🎨 ComicCraft-AI – AI Comic Story Creator

## 📌 Project Overview

ComicCraft-AI is an AI-powered web application that helps users transform their creative story ideas into structured comic stories.

Users can provide a story idea, character name, setting, story tone, and art style. The application processes these inputs and creates a five-panel comic with scene descriptions, dialogues, and AI-generated images.

---

## 🎯 Project Goal

The goal of ComicCraft-AI is to provide a simple and user-friendly platform that converts creative ideas into engaging comic stories using generative AI technologies.

---

## ✨ Main Features

* AI-powered comic story generation
* User-defined story ideas
* Character name input
* Setting input
* Story tone selection
* Art style selection
* Five-panel comic generation
* Scene descriptions
* Character dialogues
* AI-generated comic images
* Dynamic comic preview
* Error handling
* Simple and user-friendly interface

---

## 🛠️ Technologies Used

* Python
* FastAPI
* HTML
* CSS
* Jinja2 Templates
* Hugging Face Inference API
* FLUX.1-schnell
* Pillow
* Uvicorn
* Git
* GitHub

---

## 🏗️ Project Architecture

```text
User
  ↓
HTML / CSS Interface
  ↓
FastAPI Backend
  ↓
Story Generation Logic
  ↓
AI Image Generation
  ↓
Generated Comic Panels
  ↓
Comic Preview
```

---

## 📁 Project Structure

```text
comic craft/
│
├── .env
├── README.md
├── requirements.txt
│
└── app/
    │
    ├── __init__.py
    ├── main.py
    ├── routes.py
    ├── schemas.py
    ├── image_generator.py
    │
    ├── ai/
    │   ├── __init__.py
    │   ├── config.py
    │   ├── gemini_flash.py
    │   └── gemini_pro.py
    │
    ├── templates/
    │   ├── index.html
    │   ├── comic_preview.html
    │   └── error.html
    │
    └── static/
        ├── style.css
        └── generated_images/
```

---

# 🚀 Installation and Setup

## 1. Install Python

Install Python 3.12 or a compatible Python version.

Check the installed version:

```bash
python --version
```

---

## 2. Install Required Packages

Open the terminal inside the project folder and run:

```bash
python -m pip install -r requirements.txt
```

---

## 3. Configure Environment Variables

Create a `.env` file in the project root directory.

Example:

```env
APP_NAME=ComicCraft
HF_API_KEY=YOUR_HUGGINGFACE_TOKEN
MAX_PANELS=5
IMAGE_MODEL=black-forest-labs/FLUX.1-schnell
```

Do not publish your API key on GitHub.

---

## 4. Run the Application

Start the FastAPI server:

```bash
python -m uvicorn app.main:app --reload
```

The application will be available at:

```text
http://127.0.0.1:8000
```

---

# 🖥️ How to Use

1. Open the ComicCraft application.
2. Enter a story idea.
3. Enter the character name.
4. Enter the story setting.
5. Select the story tone.
6. Select the art style.
7. Click **Generate Comic**.
8. The application generates five comic panels.
9. View the generated comic on the preview page.

---

# 📖 Example Input

### Story Idea

```text
A clever little fox gets lost in a magical forest and discovers a hidden golden tree.
```

### Character

```text
Foxy
```

### Setting

```text
Magical Forest
```

### Tone

```text
Adventurous
```

### Art Style

```text
Comic Book
```

---

# 📚 Expected Output

ComicCraft-AI produces a structured comic containing:

1. Story scenes
2. Scene descriptions
3. Character information
4. Character dialogues
5. Story progression
6. AI-generated comic images
7. A final comic preview

---

# 🔧 Backend

The application uses FastAPI to:

* Receive user input
* Validate form data
* Process comic generation
* Generate image prompts
* Generate AI images
* Return the generated comic to the frontend

---

# 🎨 Frontend

The frontend uses:

* HTML
* CSS
* Jinja2 templates

The interface contains:

* Story input form
* Character input
* Setting input
* Tone selection
* Art style selection
* Generate Comic button
* Comic preview page

---

# 🤖 AI Image Generation

The application uses Hugging Face Inference Providers with the FLUX.1-schnell model to generate comic images from text prompts.

The image generation process creates a separate image for each comic panel.

---

# 🧪 Testing

The application can be tested using different:

* Story ideas
* Characters
* Settings
* Story tones
* Art styles

Example story themes:

* Fantasy
* Adventure
* Mystery
* School life
* Science fiction
* Friendship
* Magical stories

---

# 🛡️ Error Handling

The application handles common errors such as:

* Missing API key
* Invalid user input
* Image generation errors
* Backend errors
* Invalid requests

A user-friendly error page is displayed when generation fails.

---

# 📌 Project Phases

## Phase 1 – Model Selection and Architecture

* Research generative AI models
* Select suitable AI technologies
* Design application architecture
* Set up the development environment

## Phase 2 – Core Functionality

* Create story generation logic
* Accept user inputs
* Create comic scenes
* Generate dialogues

## Phase 3 – Backend Development

* Develop FastAPI backend
* Create API routes
* Validate user input
* Implement error handling

## Phase 4 – AI Integration

* Integrate generative AI services
* Create image generation prompts
* Generate comic images
* Improve prompt quality

## Phase 5 – User Interface

* Create comic input form
* Design the application interface
* Connect frontend and backend

## Phase 6 – Dynamic Comic Presentation

* Create dynamic HTML templates
* Display comic panels
* Display scenes and dialogues
* Provide comic preview

## Phase 7 – Testing

* Test different story ideas
* Test different inputs
* Test backend routes
* Test image generation
* Fix application errors

## Phase 8 – Deployment and Submission

* Perform final testing
* Prepare project documentation
* Create README
* Upload project to GitHub
* Prepare project demonstration
* Submit the final project

---

# 👩‍💻 Project Information

**Project Name:** ComicCraft-AI

**Project Type:** AI-Powered Web Application

**Backend:** FastAPI

**Frontend:** HTML, CSS, Jinja2

**AI Image Generation:** Hugging Face Inference Providers

**Image Model:** FLUX.1-schnell

---

# 🎯 Conclusion

ComicCraft-AI provides a simple way for users to transform creative ideas into structured comic stories. The application combines a web-based interface, FastAPI backend, structured story generation, and AI image generation to create an interactive comic creation experience.
