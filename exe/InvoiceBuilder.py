import streamlit as st
import pandas as pd
import pdfkit

def generate_invoice(data):
    # Generate DataFrame
    df = pd.DataFrame(data)

    # Calculate total amount
    total_amount = df["Amount"].sum()

    # Display DataFrame in Streamlit
    st.write(df)

    # Display total amount
    st.write(f"Total Amount: ${total_amount:.2f}")

    # Convert DataFrame to HTML
    html = df.to_html()

    # Write HTML to a temporary file
    with open("temp.html", "w") as f:
        f.write(html)

    # Convert HTML to PDF
    pdfkit.from_file("temp.html", "invoice.pdf")
    
    st.success("Invoice generated successfully as PDF!")

def main():
    st.title("Invoice Generator")
    
    # Logo column
    logo_col,logo_col2 = st.columns([1,0.5])
    with logo_col:
        st.image("employee.png", width=200)

    # Input fields for invoice data
    col1, col2, col3, col4, col5, col6, col7 = st.columns([1, 1, 1, 1, 1, 1, 1])
    with col1:
        customer_name = st.text_input("Customer Name")
    with col2:
        customer_address = st.text_area("Customer Address")
    with col3:
        invoice_number = st.text_input("Invoice Number")
    with col4:
        description = st.text_area("Invoice Description")
    with col5:
        quantity = st.number_input("Quantity", min_value=1, value=1)
    with col6:
        unit_price = st.number_input("Unit Price")
    with col7:
        invoice_date = st.date_input("Invoice Date")

    amount = quantity * unit_price

    if st.button("Add Item"):
        st.session_state.invoice_data.append({
            "Customer Name": customer_name,
            "Customer Address": customer_address,
            "Invoice Number": invoice_number,
            "Invoice Description": description,
            "Quantity": quantity,
            "Unit Price": unit_price,
            "Amount": amount,
            "Invoice Date": invoice_date,
        })

    if st.button("Generate Invoice"):
        generate_invoice(st.session_state.invoice_data)

if __name__ == "__main__":
    if "invoice_data" not in st.session_state:
        st.session_state.invoice_data = []
    main()
