from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, ListFlowable, ListItem
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch

def generate_report():
    pdf_filename = "iFarmAssist_Progress_Report_Phase1-4.pdf"
    document = SimpleDocTemplate(pdf_filename, pagesize=letter)
    styles = getSampleStyleSheet()
    
    # Custom Styles
    title_style = ParagraphStyle('Title', parent=styles['Title'], fontSize=24, spaceAfter=20, textColor=colors.darkgreen)
    h1_style = ParagraphStyle('Heading1', parent=styles['Heading1'], fontSize=18, spaceBefore=15, spaceAfter=10, textColor=colors.navy)
    h2_style = ParagraphStyle('Heading2', parent=styles['Heading2'], fontSize=14, spaceBefore=10, spaceAfter=6)
    normal_style = styles["BodyText"]
    bullet_style = ParagraphStyle('Bullet', parent=normal_style, leftIndent=20)

    story = []

    # Title Page
    story.append(Paragraph("iFarmAssist", title_style))
    story.append(Paragraph("Project Progress Report (Phase 1 - 4)", h2_style))
    story.append(Spacer(1, 12))
    story.append(Paragraph("<b>Status:</b> Completed & Verified", normal_style))
    story.append(Paragraph("<b>Date:</b> December 26, 2025", normal_style))
    story.append(Spacer(1, 24))

    # Executive Summary
    story.append(Paragraph("1. Executive Summary", h1_style))
    story.append(Paragraph("""
    The core foundation of the <b>iFarmAssist</b> system has been successfully implemented and verified. 
    The system now features a fully functional <b>Hybrid Architecture</b> connecting a React Native mobile application 
    to a Python FastAPI backend, integrated with Google's Gemini AI and a RAG (Retrieval-Augmented Generation) pipeline.
    """, normal_style))

    # Phase 1
    story.append(Paragraph("2. Phase 1: Environment & Backend Setup", h1_style))
    story.append(Paragraph("<b>Objective:</b> Establish a scalable project structure and backend server.", normal_style))
    p1_items = [
        ListItem(Paragraph("Established folder structure separating `mobile/` and `backend/`.", bullet_style)),
        ListItem(Paragraph("Initialized <b>FastAPI</b> server with virtual environment.", bullet_style)),
        ListItem(Paragraph("Configured `uvicorn` server binding to `0.0.0.0` for external access.", bullet_style)),
        ListItem(Paragraph("Implemented `.env` security for API keys.", bullet_style))
    ]
    story.append(ListFlowable(p1_items, bulletType='bullet'))

    # Phase 2
    story.append(Paragraph("3. Phase 2: Core Services & Database", h1_style))
    story.append(Paragraph("<b>Objective:</b> Enable data persistence and external integrations.", normal_style))
    p2_items = [
        ListItem(Paragraph("<b>Database:</b> Configured <b>SQLAlchemy</b> ORM with SQLite (Dev) / PostgreSQL (Prod) compatibility.", bullet_style)),
        ListItem(Paragraph("<b>Schema:</b> Designed models for `Users`, `Queries`, `Escalations`, and `Feedback`.", bullet_style)),
        ListItem(Paragraph("<b>Authentication:</b> Implemented JWT (JSON Web Token) infrastructure.", bullet_style)),
        ListItem(Paragraph("<b>Vector DB:</b> integrated <b>ChromaDB</b> for storing agricultural knowledge.", bullet_style))
    ]
    story.append(ListFlowable(p2_items, bulletType='bullet'))

    # Phase 3
    story.append(Paragraph("4. Phase 3: AI Engine Implementation", h1_style))
    story.append(Paragraph("<b>Objective:</b> Build the 'Brain' of the system using RAG.", normal_style))
    p3_items = [
        ListItem(Paragraph("<b>RAG Pipeline:</b> Created `vector_db.py` to ingest PDFs and retrieve relevant context based on user queries.", bullet_style)),
        ListItem(Paragraph("<b>Gemini Integration:</b> Integrated `gemini-2.0-flash-exp` model via Google GenAI SDK.", bullet_style)),
        ListItem(Paragraph("<b>Context Aggregator:</b> Implemented logic to inject <b>User Profile</b> (Location/Crops) and <b>Live Weather</b> (OpenWeatherMap API) into the AI prompt.", bullet_style)),
        ListItem(Paragraph("<b>Resilience:</b> Implemented 'Smart Retry' logic to handle API Rate Limits (429 Errors).", bullet_style))
    ]
    story.append(ListFlowable(p3_items, bulletType='bullet'))

    # Phase 4
    story.append(Paragraph("5. Phase 4: Mobile App Foundation", h1_style))
    story.append(Paragraph("<b>Objective:</b> Create the farmer-facing interface.", normal_style))
    p4_items = [
        ListItem(Paragraph("<b>Framework:</b> Initialized <b>React Native (Expo)</b> project.", bullet_style)),
        ListItem(Paragraph("<b>UI/UX:</b> Developed `LoginScreen` and `HomeScreen` with responsive layout.", bullet_style)),
        ListItem(Paragraph("<b>Networking:</b> Configured `axios` client with dynamic IP handling (auto-detects backend IP).", bullet_style)),
        ListItem(Paragraph("<b>Error Handling:</b> Implemented user-friendly error messages (e.g., 'Server Busy' instead of crash dumps).", bullet_style)),
        ListItem(Paragraph("<b>Result:</b> App successfully sends text queries and displays AI responses.", bullet_style))
    ]
    story.append(ListFlowable(p4_items, bulletType='bullet'))

    # Technical Architecture Table
    story.append(Paragraph("6. Technical Stack Summary", h1_style))
    data = [
        ["Component", "Technology Used"],
        ["Frontend", "React Native, Expo, Axios"],
        ["Backend", "FastAPI, Python, Uvicorn"],
        ["AI / LLM", "Google Gemini 2.0 Flash"],
        ["Vector Store", "ChromaDB, Sentence-Transformers"],
        ["Database", "SQLite (Dev) / PostgreSQL"]
    ]
    t = Table(data, colWidths=[150, 300])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.lightgrey),
        ('GRID', (0,0), (-1,-1), 1, colors.black),
        ('PADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t)
    story.append(Spacer(1, 12))
    
    # Conclusion
    story.append(Paragraph("Conclusion", h1_style))
    story.append(Paragraph("""
    The project is currently ahead of schedule with a stable, working prototype. 
    The core infrastructure is robust, handling real-world scenarios like network latency and API limits. 
    <b>Next Steps:</b> Phase 5 will introduce Multimodal features (Voice Input and Image Analysis) to complete the functional deliverables.
    """, normal_style))

    # Build
    document.build(story)
    print(f"Report generated successfully: {pdf_filename}")

if __name__ == "__main__":
    generate_report()
