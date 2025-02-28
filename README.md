# Google Sheets Clone & Chatbot for CDPs

## Table of Contents
1. [Google Sheets Clone](#google-sheets-clone)
   - [Overview](#overview)
   - [Features](#features)
   - [Installation & Setup](#installation--setup)
   - [Deployment](#deployment)
   - [Technologies Used](#technologies-used)
   - [Contributing](#contributing)
   - [License](#license)
2. [Chatbot for "How-to" Questions on CDPs](#chatbot-for-how-to-questions-on-cdps)
   - [Overview](#overview-1)
   - [Features](#features-1)
   - [Installation & Setup](#installation--setup-1)
   - [Usage](#usage)
   - [Technologies Used](#technologies-used-1)
   - [Contributing](#contributing-1)
   - [License](#license-1)

---

# Google Sheets Clone

## Overview
This project is a simple **Google Sheets Clone** built using **React, TypeScript, RecoilJS, and MathJS**. It allows users to create spreadsheets, perform calculations, and manage data in a web-based environment.

## Features
✅ **Spreadsheet Interface** - Similar to Google Sheets with an interactive grid.  
✅ **Mathematical Operations** - Supports SUM, AVERAGE, MIN, MAX, COUNT.  
✅ **State Management** - Uses RecoilJS for efficient data handling.  
✅ **Lightweight & Fast** - Developed using Vite for fast builds.  
✅ **Dark Mode Support** - Includes a toggle for dark mode UI.  

## Installation & Setup

### Prerequisites
Make sure you have the following installed:
- [Node.js](https://nodejs.org/) (Latest LTS version recommended)
- npm (comes with Node.js) or yarn

### Steps
1. **Clone the repository:**  
   ```sh
   git clone <your-repo-link>
   cd sheets-clone
   ```
2. **Install dependencies:**  
   ```sh
   npm install
   ```
3. **Start the development server:**  
   ```sh
   npm run dev
   ```
   The app should now be running at `http://localhost:5173/`.

## Deployment

To build and deploy the application, use:
```sh
npm run build
```
This will generate an optimized production build inside the `dist/` folder.

## Technologies Used
- **React.js** - UI framework
- **TypeScript** - Type safety and scalability
- **RecoilJS** - State management
- **MathJS** - Mathematical operations
- **Vite** - Fast build tool

## Contributing
Feel free to submit pull requests or raise issues.

## License
This project is open-source under the MIT License.

---

# Chatbot for "How-to" Questions on CDPs

## Overview
This chatbot answers **"how-to" questions** about **Segment, mParticle, Lytics, and Zeotap** by extracting relevant information from their official documentation.

## Features
✅ **Extracts relevant content** from official CDP documentation.  
✅ **Understands platform-specific queries** (e.g., "How do I set up a new source in Segment?").  
✅ **Simple and lightweight** - Uses Flask and BeautifulSoup.  
✅ **Extensible** - Can be updated to support additional CDPs.  

## Installation & Setup

### Prerequisites
- [Python 3.x](https://www.python.org/downloads/)
- `pip` package manager

### Steps
1. **Clone the repository:**  
   ```sh
   git clone <your-repo-link>
   cd Assignment-2/chatbot
   ```
2. **Install dependencies:**  
   ```sh
   pip install -r requirements.txt
   ```
3. **Run the chatbot server:**  
   ```sh
   python chatbot.py
   ```
   The API should now be running at `http://127.0.0.1:5000/`.

## Usage

### 1️⃣ **Ask a question**
Send a **POST request** to `http://127.0.0.1:5000/ask` with the following JSON body:
```json
{
    "question": "How do I set up a new source in Segment?"
}
```
### 2️⃣ **Example Response**
```json
{
    "platform": "segment",
    "answer": "To set up a new source in Segment, go to the Sources page..."
}
```

## Technologies Used
- **Flask** - API framework
- **BeautifulSoup4** - Web scraping
- **Requests** - Fetching documentation

## Contributing
Feel free to submit pull requests or report issues.

## License
This project is open-source under the MIT License.

