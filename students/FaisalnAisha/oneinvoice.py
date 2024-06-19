import streamlit as st #python module to create framework/page
from fpdf import FPDF #python module to generate PDFs
import base64 #python module to convert binary data (of your code) to printable characters

Image1,Image2,Image3=st.columns([0.5,2.5,1])
with Image1:

    st.image("Logo.png",use_column_width=True)
col1,col2=st.columns(2)
with Image3:
    st.header(":blue[INVOICE]")
with col1:
    st.write(':blue[Faisaltech]')
    st.write(":blue[471, Camelia 7, Arabian Ranches 8]")
    st.write(':blue[Dubai, UAE]')
    st.write(" ")
    st.write(":blue[**Bill To:**]")


colb1,colb2,colb3=st.columns([2,1,1])


with colb1:
    customer = st.text_input('w',placeholder='Customer Name',label_visibility= 'collapsed')
    adress = st.text_input('w',placeholder='Enter Adress',label_visibility= 'collapsed')  


with colb2:
        st.write(":blue[**Invoice#:**]")
        st.write('')
        st.write(":blue[**Invoice Date:**]")
        st.write('')
        st.write(":blue[**Due Date:**]")
with colb3:
        Invoicenum = st.text_input('w',placeholder='Invoice Number',label_visibility= 'collapsed')
        Date=st.date_input("Enter Invoice Date",label_visibility='collapsed')
        due=st.date_input("Enter Due Date",label_visibility='collapsed')
st.write("")
st.write("")


colc1,colc2,colc3,colc4=st.columns(4)
with colc1:
    st.write(":blue[**Description**]")
    description=st.text_input("f",label_visibility='collapsed')
with colc2:
     st.write(":blue[**Quantity**]")
     quantity=st.number_input("y",0,label_visibility='collapsed')
with colc3:
     st.write(":blue[**Price|Unit**]")
     price=st.number_input("s",0,label_visibility='collapsed')
with colc4:
     st.write(":blue[**Total Price**]")
     total=st.text_input("g",value=quantity*price,label_visibility='collapsed',disabled=True)
     total=int(total)
st.divider()
cold1,cold2=st.columns(2)
with cold1:
    st.write(":blue[**Payment Info**]")
    st.write(":blue[Acc Name: Faisaltech]")
    st.write(":blue[Acc Number: 509 173 1594]")
    st.write(":blue[Bank Name: UAE Bank]")
with cold2:
     st.write(":blue[**Payment Due:**]")
     st.header(f":violet[**${total:,}**]")

#function to generate our PDF

def generate_pdf():
     pdf = FPDF()

     #Add a page
     pdf.add_page()

     #Set your default fonts
     pdf.set_font("Arial", size=12)

     #Set column1 x and y coord
     col1x = 10
     col1y = 100

     #Add image
     pdf.image("Logo.png",x=col1x, y=col1y)



     
     #Save the PDF
     pdf_file = 'invoice.pdf'
     pdf.output(pdf_file)
     return pdf_file

#Generate the PDF
pdf_func = generate_pdf()

#Read the PDF FUNCT as binary data
with open(pdf_func, 'rb') as binary:
     pdf_data = binary.read()

if st.button(":blue[View Invoice]"):
     #Write the PDF using base64
     pdf_base64 = base64.b64encode(pdf_data).decode('utf-8')

     #Generate the HTML to embed the PDF
     pdf_embed = f'<embed src="data:application/pdf;base64,{pdf_base64}" type="application/pdf" width="100%" height="600px" />'

     #Display the embedded pdf (Markdown helps us use HTML in streamlit)
     st.markdown(pdf_embed,unsafe_allow_html=True)


