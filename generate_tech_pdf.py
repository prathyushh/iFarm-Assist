from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

def generate_pdf():
    pdf_filename = "iFarmAssist_Tech_Stack.pdf"
    document = SimpleDocTemplate(pdf_filename, pagesize=letter)
    styles = getSampleStyleSheet()
    
    # Custom Styles
    title_style = styles["Title"]
    heading_style = styles["Heading2"]
    normal_style = styles["BodyText"]
    code_style = ParagraphStyle('Code', parent=styles['BodyText'], fontName='Courier', fontSize=9, backColor=colors.lightgrey)

    story = []

    # Title
    story.append(Paragraph("iFarmAssist: Technical Architecture & Tech Stack", title_style))
    story.append(Spacer(1, 24))

    # Introduction
    intro_text = """
    This document provides a detailed breakdown of the technologies used in the iFarmAssist project. 
    The system is designed as a modern, scalable, AI-powered application for precision agriculture.
    """
    story.append(Paragraph(intro_text, normal_style))
    story.append(Spacer(1, 12))

    # --- Section 1: Mobile Frontend ---
    story.append(Paragraph("1. Mobile Frontend (The Farmer's Interface)", heading_style))
    story.append(Paragraph("<b>Framework: React Native (via Expo)</b>", normal_style))
    story.append(Paragraph("We chose React Native to build a truly native mobile experience using JavaScript. Expo was used to accelerate development and testing.", normal_style))
    
    frontend_details = [
        ["Technology", "Purpose"],
        ["React Native", "Cross-platform mobile UI framework."],
        ["Expo", "Build tool and runtime for easy testing."],
        ["Axios", "HTTP Client to communicate with the Backend API."],
        ["React Navigation", "Handling screen transitions (Login -> Home)."],
        ["Lucide React Native", "Modern, lightweight icon set."]
    ]
    t = Table(frontend_details, colWidths=[150, 300])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    story.append(t)
    story.append(Spacer(1, 12))

    # --- Section 2: Backend API ---
    story.append(Paragraph("2. Backend API (The Brain)", heading_style))
    story.append(Paragraph("<b>Framework: FastAPI (Python)</b>", normal_style))
    story.append(Paragraph("FastAPI was selected for its high performance and native support for asynchronous programming, which is crucial for handling AI requests without blocking.", normal_style))
    
    backend_details = [
        ["Technology", "Purpose"],
        ["Python 3.10+", "Primary programming language."],
        ["FastAPI", "High-performance web framework."],
        ["Uvicorn", "ASGI Server to run the application."],
        ["Pydantic", "Data validation and settings management."],
        ["Python-Dotenv", "Managing environment variables securely."]
    ]
    t = Table(backend_details, colWidths=[150, 300])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.darkblue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    story.append(t)
    story.append(Spacer(1, 12))

    # --- Section 3: AI & Machine Learning ---
    story.append(Paragraph("3. Artificial Intelligence Engine", heading_style))
    story.append(Paragraph("<b>Core Feature: RAG (Retrieval Augmented Generation)</b>", normal_style))
    story.append(Paragraph("The system combines Generative AI with a custom Knowledge Base to give accurate, context-aware answers.", normal_style))
    
    ai_details = [
        ["Technology", "Purpose"],
        ["Google Gemini 2.0", "Main LLM for reasoning and text generation."],
        ["LangChain / Direct SDK", "Orchestrating the AI workflow."],
        ["ChromaDB", "Vector Database to store agricultural manuals."],
        ["Sentence-Transformers", "Creating embeddings (all-MiniLM-L6-v2) for search."]
    ]
    t = Table(ai_details, colWidths=[150, 300])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.purple),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    story.append(t)
    story.append(Spacer(1, 12))

    # --- Section 4: Database & External Services ---
    story.append(Paragraph("4. Data Storage & External APIs", heading_style))
    
    db_details = [
        ["Technology", "Description"],
        ["SQLite (Dev)", "Lightweight, file-based SQL database for local testing."],
        ["PostgreSQL (Prod)", "Robust relational database for user data (Architecture ready)."],
        ["OpenWeatherMap API", "Real-time weather data fetching for context-awareness."]
    ]
    t = Table(db_details, colWidths=[150, 300])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.darkgreen),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    story.append(t)
    story.append(Spacer(1, 24))

    # Footer
    story.append(Paragraph("Generated automatically by iFarmAssist AI Agent.", normal_style))

    # Build
    document.build(story)
    print(f"PDF generated successfully: {pdf_filename}")

if __name__ == "__main__":
    generate_pdf()
