import PyPDF2
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import PyInputPlus as pyip

def create_invoice_pdf(invoice_details):
    pdf_file = "invoice.pdf"
    pdf = canvas.Canvas(pdf_file, pagesize=letter)
    
    # Set up the title
    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawCentredString(300, 750, "Invoice")
    
    # Set up invoice details
    pdf.setFont("Helvetica", 12)
    height = 700
    for key, value in invoice_details.items():
        text = f"{key}: {value}"
        pdf.drawString(50, height, text)
        height -= 20
    
    pdf.save()
    print(f"Invoice saved as {pdf_file}")

def main():
    print("Please enter invoice details:")
    customer_name = pyip.inputStr("Customer Name: ")
    invoice_number = pyip.inputStr("Invoice Number: ")
    amount = pyip.inputFloat("Amount: $")
    
    invoice_details = {
        "Customer Name": customer_name,
        "Invoice Number": invoice_number,
        "Amount": f"${amount:.2f}"
    }
    
    create_invoice_pdf(invoice_details)

if __name__ == "__main__":
    main()
