from fpdf import FPDF
class Shirtificate(FPDF):
    def header(self):
        self.set_font("Helvetica", "B", 30)
        self.cell(0, 40, "CS50 Shirtificate", align="C", new_x="LMARGIN", new_y="NEXT")
def main():
    name = input("Name: ")
    pdf = Shirtificate(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    pdf.image("shirtificate.png", x=15, y=60, w=180)
    pdf.set_font("Helvetica", "B", 24)
    pdf.set_text_color(255, 255, 255)
    pdf.text(x=45, y=140, text=f"{name} took CS50")
    pdf.output("shirtificate.pdf")
if __name__ == "__main__":
    main()
