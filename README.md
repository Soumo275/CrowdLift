# CrowdLift

**"Fuel Innovation, Crowdfund Your Success with CrowdLift"**

CrowdLift is an open-source crowdfunding platform designed to support open-source projects, products, and startups. This repository contains separate modules for the Frontend, Backend, Payment Gateway integration, and an ML Chatbot.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Setup](#setup)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contributors](#contributors)

## Introduction
CrowdLift is a platform where innovators can raise funds for their open-source projects, products, and startups. The platform is built with a modular approach to ensure scalability and ease of maintenance.

## Features
- **Frontend**: Built using HTML, CSS, and JavaScript for a responsive and interactive user interface.
- **Backend**: Developed with FastAPI and MongoDB to handle API requests and manage data efficiently.
- **Payment Gateway**: Integrated RazorPay for handling transactions securely.
- **ML Chatbot**: Trained using the RAG (Retrieval-Augmented Generation) technique to assist users with queries and support.

## Tech Stack
### Frontend
- HTML
- CSS
- JavaScript

### Backend
- FastAPI
- MongoDB

### Payment Gateway
- Using Razorpay PaymentSDK

### Machine Learning Chatbot
- RAG (Retrieval-Augmented Generation) technique
- Jupyter Notebook for training and testing

## Setup
### Prerequisites
- Python 3.8+
- Node.js
- MongoDB

### Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/Soumo275/CrowdLift.git
   cd CrowdLift
   ```

2. **Frontend Setup:**
   Navigate to the `frontend` directory and open `index.html` in your browser.
   ```bash
   cd frontend
   ```

3. **Backend Setup:**
   Create a virtual environment and install the required dependencies.
   ```bash
   cd backend
   python3 -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   pip install -r requirements.txt
   ```

   Start the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```

4. **Payment Gateway Setup:**
   Follow the instructions in the `payment_gateway` directory to set up and configure the payment gateway.

5. **ML Chatbot Setup:**
   Navigate to the `chatbot` directory and run the Jupyter Notebook to train and test the chatbot.
   ```bash
   cd chatbot
   jupyter notebook Chatbot.ipynb
   ```

## Usage
- Access the frontend via `index.html` to interact with the platform.
- Use the FastAPI backend to handle API requests for the platform.
- Process payments securely through the integrated payment gateway.
- Get assistance through the ML Chatbot integrated into the platform.

## Contributing
We welcome contributions! Please follow these steps to contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add YourFeature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributors
- [Soumo275](https://github.com/Soumo275)
- [MrigankaDebnath03](https://github.com/MrigankaDebnath03)
- [Prabuddha747](https://github.com/Prabuddha747)
- [Sainy-Mishra](https://github.com/Sainy-Mishra)
