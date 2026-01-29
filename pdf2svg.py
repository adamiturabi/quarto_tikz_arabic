import pymupdf
import sys

pdf_file = sys.argv[1]
svg_file = sys.argv[2]

doc = pymupdf.open(pdf_file)
page = doc[0]

# Convert page to SVG
svg_content = page.get_svg_image()

# Save to file
with open(svg_file, "w", encoding="utf-8") as f:
    f.write(svg_content)

doc.close()

