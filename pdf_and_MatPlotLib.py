from fpdf import FPDF
import lorem  # Use this package to showcase long texts
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.DataFrame(
    {"feature 1": ["cat 1", "cat 2", "cat 3", "cat 4"],
     "feature 2": [400, 300, 200, 100]
     })

fig, ax = plt.subplots(1, 1, figsize=(6, 4))
sns.barplot(data=df, x="feature 1", y="feature 2")
plt.title("Chart")
plt.savefig("./example_chart.png",
            transparent=False,
            facecolor="white",
            bbox_inches="tight")

# cell height
ch = 8

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", "B", 24)
pdf.cell(w=0, h=20, txt="Title", ln=1)
pdf.set_font("Arial", "", 16)
pdf.cell(w=30, h=ch, txt="Date: ", ln=0)
pdf.cell(w=30, h=ch, txt="01/01/2022", ln=1)
pdf.cell(w=30, h=ch, txt="Author: ", ln=0)
pdf.cell(w=30, h=ch, txt="Max Mustermann", ln=1)
pdf.ln(ch)
pdf.multi_cell(w=0, h=5, txt=lorem.paragraph())
pdf.image("./example_chart.png",
          x=10, y=None, w=100, h=0, type="PNG")
pdf.ln(ch)
pdf.multi_cell(w=0, h=5, txt=lorem.paragraph())
pdf.output(f'./example.pdf', 'F')