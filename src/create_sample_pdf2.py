#!/usr/bin/env python3
"""
Create a second sample PDF file for testing the PDF Document Processor
"""

import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph

def create_sample_pdf():
    """Create a sample PDF file with machine learning content."""
    # Get the Document directory
    document_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "Document")
    
    # Create the Document directory if it doesn't exist
    if not os.path.exists(document_dir):
        os.makedirs(document_dir)
    
    # Path to the sample PDF file
    pdf_path = os.path.join(document_dir, "Machine_Learning_Guide.pdf")
    
    # Create the PDF
    doc = SimpleDocTemplate(pdf_path, pagesize=letter)
    styles = getSampleStyleSheet()
    
    # Content
    content = []
    
    # Title
    title = Paragraph("Introduction to Machine Learning", styles["Title"])
    content.append(title)
    
    # Sections
    sections = [
        ("What is Machine Learning?", """
        Machine Learning is a subset of artificial intelligence that provides systems the ability 
        to automatically learn and improve from experience without being explicitly programmed. 
        It focuses on the development of computer programs that can access data and use it to 
        learn for themselves.
        
        The process of learning begins with observations or data, such as examples, direct 
        experience, or instruction, in order to look for patterns in data and make better 
        decisions in the future based on the examples that we provide. The primary aim is to 
        allow the computers to learn automatically without human intervention or assistance 
        and adjust actions accordingly.
        """),
        
        ("Types of Machine Learning", """
        There are three main types of machine learning:
        
        1. Supervised Learning: The algorithm is trained on a labeled dataset, which means that 
        each training example is paired with an output label. The algorithm learns to predict 
        the output from the input data. Examples include classification and regression.
        
        2. Unsupervised Learning: The algorithm is trained on an unlabeled dataset, which means 
        that the input data does not come with any output labels. The algorithm must find 
        structure in the input data on its own. Examples include clustering and dimensionality 
        reduction.
        
        3. Reinforcement Learning: The algorithm learns by interacting with an environment. It 
        receives rewards for performing correctly and penalties for performing incorrectly. The 
        algorithm learns to maximize the total reward. Examples include game playing and robotics.
        """),
        
        ("Common Machine Learning Algorithms", """
        There are many machine learning algorithms, each with its own strengths and weaknesses. 
        Some common ones include:
        
        1. Linear Regression: Used for predicting a continuous value.
        
        2. Logistic Regression: Used for binary classification problems.
        
        3. Decision Trees: Used for both classification and regression problems.
        
        4. Random Forests: An ensemble method that uses multiple decision trees.
        
        5. Support Vector Machines (SVM): Used for classification, regression, and outlier detection.
        
        6. K-Nearest Neighbors (KNN): Used for classification and regression.
        
        7. K-Means: Used for clustering.
        
        8. Neural Networks: Used for complex pattern recognition tasks.
        """),
        
        ("Neural Networks", """
        Neural networks are a set of algorithms, modeled loosely after the human brain, that are 
        designed to recognize patterns. They interpret sensory data through a kind of machine 
        perception, labeling or clustering raw input. The patterns they recognize are numerical, 
        contained in vectors, into which all real-world data, be it images, sound, text or time 
        series, must be translated.
        
        Neural networks help us cluster and classify. You can think of them as a clustering and 
        classification layer on top of the data you store and manage. They help to group unlabeled 
        data according to similarities among the example inputs, and they classify data when they 
        have a labeled dataset to train on.
        """),
        
        ("Deep Learning", """
        Deep Learning is a subfield of machine learning concerned with algorithms inspired by the 
        structure and function of the brain called artificial neural networks. Deep learning is 
        part of a broader family of machine learning methods based on artificial neural networks 
        with representation learning.
        
        Deep learning architectures such as deep neural networks, deep belief networks, recurrent 
        neural networks and convolutional neural networks have been applied to fields including 
        computer vision, speech recognition, natural language processing, audio recognition, 
        social network filtering, machine translation, bioinformatics, drug design, medical image 
        analysis, material inspection and board game programs, where they have produced results 
        comparable to and in some cases surpassing human expert performance.
        """),
        
        ("Applications of Machine Learning", """
        Machine learning is used in a wide range of applications:
        
        1. Image and Speech Recognition: Used in applications like face detection, voice 
        assistants, and automatic speech recognition.
        
        2. Medical Diagnosis: Used to diagnose diseases based on symptoms and medical history.
        
        3. Predictive Analytics: Used to predict future trends based on historical data.
        
        4. Recommendation Systems: Used by companies like Netflix and Amazon to recommend 
        products or content to users.
        
        5. Natural Language Processing: Used in applications like chatbots, sentiment analysis, 
        and language translation.
        
        6. Autonomous Vehicles: Used to help vehicles navigate and make decisions.
        """),
        
        ("Challenges in Machine Learning", """
        Despite its potential, machine learning also faces several challenges:
        
        1. Data Quality: Machine learning algorithms require high-quality, diverse data to learn 
        effectively.
        
        2. Interpretability: Many machine learning models, especially deep learning models, are 
        often seen as "black boxes" because it's difficult to understand how they make decisions.
        
        3. Overfitting: This occurs when a model learns the detail and noise in the training data 
        to the extent that it negatively impacts the performance of the model on new data.
        
        4. Underfitting: This occurs when a model is too simple to capture the underlying pattern 
        of the data.
        
        5. Computational Resources: Training complex models, especially deep learning models, 
        requires significant computational resources.
        """),
        
        ("Future of Machine Learning", """
        The future of machine learning is likely to involve continued advancements in algorithms, 
        hardware, and applications. We may see more integration of machine learning into everyday 
        life, with smart homes, autonomous vehicles, and personalized healthcare becoming more common.
        
        However, the development of machine learning will also require careful consideration of 
        ethical and societal implications. It will be important to ensure that machine learning is 
        developed and used in ways that benefit humanity and respect human rights and values.
        """)
    ]
    
    # Add sections to content
    for title, text in sections:
        heading = Paragraph(title, styles["Heading1"])
        content.append(heading)
        
        paragraphs = text.strip().split("\n\n")
        for p in paragraphs:
            para = Paragraph(p.strip(), styles["Normal"])
            content.append(para)
    
    # Build the PDF
    doc.build(content)
    
    print(f"Sample PDF created at: {pdf_path}")

if __name__ == "__main__":
    create_sample_pdf()