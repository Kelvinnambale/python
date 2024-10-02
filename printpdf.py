# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 12:16:39 2024

@author: ADMIN
"""

from fpdf import FPDF

# Create PDF object
pdf = FPDF()

# Add a page
pdf.add_page()

# Set title
pdf.set_font("Arial", 'B', 16)
pdf.cell(200, 10, "Advanced Python Projects for Final Year", ln=True, align='C')

# Add subtitle
pdf.set_font("Arial", 'B', 12)
pdf.cell(200, 10, "30 Project Ideas with Steps, Requirements, and Images", ln=True, align='C')
pdf.ln(10)

# Project details with steps and requirements
projects_with_steps = [
    {
        "title": "AI-Based Chatbot",
        "description": "Build a chatbot that can interact with users using natural language processing.",
        "requirements": ["Python", "NLTK/Spacy", "Rasa"],
        "steps": [
            "1. Implement NLP using libraries like NLTK or SpaCy.",
            "2. Train the model using a chatbot framework (e.g., Rasa).",
            "3. Integrate a dialogue system and fine-tune the responses."
        ]
    },
    {
        "title": "Face Recognition System",
        "description": "Develop a real-time face recognition system using OpenCV and deep learning.",
        "requirements": ["Python", "OpenCV", "TensorFlow/Keras"],
        "steps": [
            "1. Use OpenCV to capture and process images.",
            "2. Implement face detection using Haar cascades.",
            "3. Train a model for face recognition using CNNs."
        ]
    },
    {
        "title": "Real-Time Traffic Analysis System",
        "description": "Build a system to analyze live traffic video feeds for congestion analysis.",
        "requirements": ["Python", "OpenCV", "Image Processing Libraries"],
        "steps": [
            "1. Capture video streams using OpenCV.",
            "2. Use image processing for vehicle detection.",
            "3. Implement traffic density measurement and analytics."
        ]
    },
    # More projects...
]

# Iterate through the project list and add them to the PDF
for i, project in enumerate(projects_with_steps, 1):
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, f"{i}. {project['title']}", ln=True)
    
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, f"Description: {project['description']}", align="L")
    
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, "Requirements:", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, ", ".join(project['requirements']), align="L")
    
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, "Steps:", ln=True)
    pdf.set_font("Arial", size=12)
    for step in project["steps"]:
        pdf.multi_cell(0, 10, step, align="L")
    
    pdf.ln(5)

# Save the file
pdf_file = "/mnt/data/Advanced_Python_Projects_With_Steps_Requirements.pdf"
pdf.output(pdf_file)

pdf_file