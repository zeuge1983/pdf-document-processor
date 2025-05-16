#!/usr/bin/env python3
"""
Create a sample PDF file for testing the PDF Document Processor
"""

import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph

def create_sample_pdf():
    """Create a sample PDF file with AI content."""
    # Get the Document directory
    document_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "Document")
    
    # Create the Document directory if it doesn't exist
    if not os.path.exists(document_dir):
        os.makedirs(document_dir)
    
    # Path to the sample PDF file
    pdf_path = os.path.join(document_dir, "AI_Overview.pdf")
    
    # Create the PDF
    doc = SimpleDocTemplate(pdf_path, pagesize=letter)
    styles = getSampleStyleSheet()
    
    # Content
    content = []
    
    # Title
    title = Paragraph("Introduction to Artificial Intelligence", styles["Title"])
    content.append(title)
    
    # Sections
    sections = [
        ("What is Artificial Intelligence?", """
        Artificial Intelligence (AI) refers to the simulation of human intelligence in machines 
        that are programmed to think like humans and mimic their actions. The term may also be 
        applied to any machine that exhibits traits associated with a human mind such as learning 
        and problem-solving.
        
        The ideal characteristic of artificial intelligence is its ability to rationalize and take 
        actions that have the best chance of achieving a specific goal. A subset of artificial 
        intelligence is machine learning, which refers to the concept that computer programs can 
        automatically learn from and adapt to new data without being assisted by humans.
        """),
        
        ("Types of AI", """
        AI can be categorized in several ways, but one common distinction is between narrow AI and 
        general AI:
        
        1. Narrow AI (or Weak AI): Designed and trained for a particular task. Virtual personal 
        assistants, such as Apple's Siri, are a form of narrow AI.
        
        2. General AI (or Strong AI): AI systems with generalized human cognitive abilities. When 
        presented with an unfamiliar task, a strong AI system can find a solution without human 
        intervention.
        
        Another categorization is based on functionality:
        
        1. Reactive Machines: These AI systems do not store memories or use past experiences to 
        determine future actions. They simply perceive the world and react to it.
        
        2. Limited Memory: These AI systems can use past experiences to inform future decisions. 
        Self-driving cars use this type of AI.
        
        3. Theory of Mind: This is a more advanced type of AI that can understand human emotions, 
        beliefs, and thoughts.
        
        4. Self-Aware: This is the most advanced form of AI, which has its own consciousness and 
        self-awareness.
        """),
        
        ("Applications of AI", """
        AI is being used across different industries and fields:
        
        1. Healthcare: AI is being used for disease identification, personalized treatment, and 
        drug discovery.
        
        2. Finance: AI is used for fraud detection, algorithmic trading, and customer service.
        
        3. Transportation: Self-driving cars and traffic management systems use AI.
        
        4. Manufacturing: AI is used for predictive maintenance, quality control, and supply chain 
        optimization.
        
        5. Education: AI is used for personalized learning, automated grading, and intelligent 
        tutoring systems.
        
        6. Customer Service: Chatbots and virtual assistants use AI to provide customer support.
        """),
        
        ("Challenges and Ethical Considerations", """
        Despite its potential benefits, AI also presents several challenges and ethical considerations:
        
        1. Job Displacement: As AI automates more tasks, there is concern about job displacement.
        
        2. Privacy: AI systems often require large amounts of data, raising concerns about privacy.
        
        3. Bias: AI systems can inherit biases from their training data, leading to unfair outcomes.
        
        4. Security: AI systems can be vulnerable to attacks or manipulation.
        
        5. Accountability: It can be difficult to determine who is responsible when AI systems make 
        mistakes.
        
        6. Existential Risk: Some experts worry about the potential risks of advanced AI systems 
        that could act in ways harmful to humanity.
        """),
        
        ("Future of AI", """
        The future of AI is likely to involve continued advancements in machine learning, natural 
        language processing, and robotics. We may see more integration of AI into everyday life, 
        with smart homes, autonomous vehicles, and AI-powered healthcare becoming more common.
        
        However, the development of AI will also require careful consideration of ethical and 
        societal implications. It will be important to ensure that AI is developed and used in 
        ways that benefit humanity and respect human rights and values.
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