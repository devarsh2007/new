from fpdf import FPDF

# Function to convert hex color to RGB
def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

# Example hex color
hex_color = '#FF4500'  # Example: Orange color

# Convert hex color to RGB
rgb_color = hex_to_rgb(hex_color)

# Create instance of FPDF class
pdf = FPDF()

# Add a page
pdf.add_page()

# Set font: Arial, bold, size 12
pdf.set_font("Arial", 'B', 12)

# Set text color (RGB format)
pdf.set_text_color(*rgb_color)

# Table data (example)
data = [
    ["product Name", "price", "contity"],
    ["Alice", "1000", "2"],
    ["Bob", "320", "3"],
    ["Charlie", "353", "5"]
]

# Set column width (arbitrary for this example)
col_width = 45

# Print header row
for row in data:
    for item in row:
        pdf.cell(col_width, 10, txt=item, border=1)
    pdf.ln()

# Save the pdf with name .pdf
pdf.output("table.pdf")
