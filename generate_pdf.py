from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
import re

def parse_markdown_to_pdf(md_file, pdf_file):
    try:
        doc = SimpleDocTemplate(pdf_file, pagesize=letter)
        styles = getSampleStyleSheet()
        story = []

        # Ensure we have a set of styles
        if 'Title' not in styles: styles.add(ParagraphStyle(name='Title', fontSize=18))
        if 'Heading2' not in styles: styles.add(ParagraphStyle(name='Heading2', fontSize=14))
        
        with open(md_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        table_buffer = []
        
        def flush_table():
            if table_buffer:
                data = []
                for row in table_buffer:
                    # Remove outer pipes and split
                    cols = [c.strip() for c in row.strip().strip('|').split('|')]
                    if any(cols): # Ensure not empty
                         data.append(cols)
                
                if data:
                    # Dynamically calculate col widths if possible, or let auto
                    t = Table(data)
                    t.setStyle(TableStyle([
                        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
                        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
                        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                        ('BOTTOMPADDING', (0, 0), (-1, 0), 6),
                        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
                        ('VALIGN', (0,0), (-1,-1), 'TOP'), 
                        ('WORD_WRAP', (0,0), (-1,-1), True)
                    ]))
                    story.append(t)
                    story.append(Spacer(1, 12))
                table_buffer.clear()

        for line in lines:
            line = line.strip()
            
            # Handle Table Rows
            if line.startswith('|'):
                table_buffer.append(line)
                continue
            else:
                flush_table()

            if not line:
                continue

            # Convert Bold
            line = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', line)
            
            # Headers
            if line.startswith('# '):
                story.append(Paragraph(line[2:], styles['Title']))
                story.append(Spacer(1, 12))
            elif line.startswith('## '):
                # Check for existing style
                s = styles['Heading2'] if 'Heading2' in styles else styles['Normal']
                story.append(Paragraph(line[3:], s))
                story.append(Spacer(1, 10))
            elif line.startswith('### '):
                s = styles['Heading3'] if 'Heading3' in styles else styles['Normal']
                story.append(Paragraph(line[4:], s))
                story.append(Spacer(1, 8))
            elif line.startswith('- ') or line.startswith('* '):
                 story.append(Paragraph(f'&bull; {line[2:]}', styles['Normal']))
                 story.append(Spacer(1, 4))
            else:
                story.append(Paragraph(line, styles['Normal']))
                story.append(Spacer(1, 6))

        flush_table() # Flush any remaining table
        
        doc.build(story)
        print(f"PDF generated: {pdf_file}")
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    parse_markdown_to_pdf("Implementation_Plan.md", "Implementation_Plan.pdf")
