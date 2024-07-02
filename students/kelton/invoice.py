import streamlit as st
from fpdf import FPDF #python module to generate PDFs
import base64 #python module to convert binary data (code) to printable character (PDF)

cola1, cola2, cola3, cola4 = st.columns(4)
with cola1:
    st.image('kfclogo.png',use_column_width=True)
with cola4:
    st.write('')
    st.header(':blue[INVOICE]')
colb1,colb2,colb3, = st.columns(3)
with colb1:
    st.write(':blue[KFC Foods]')
    st.write(':blue[564, Chicken wings street]')
    st.write(':blue[Manchester, UK]')
colc1,colc2= st.columns(2)
with colc1:
    name = st.text_input(':blue[Bill to:]',placeholder='Name of Bill Receiver')
    email = st.text_input(':blue[Email Address:]',label_visibility='collapsed',placeholder='Email Address')
with colc2:
    colc2a,colc2b = st.columns(2)
    with colc2a:
       
        st.write(':blue[Invoice:]')
        st.write('')
        st.write(':blue[Invoice Date:]')
        st.write('')
        st.write(':blue[Due Date:]')
    with colc2b:
        invoice = st.text_input('sdsd',label_visibility='collapsed')
        indate = st.date_input('fgfgf',label_visibility='collapsed')
        duedate = st.date_input('hjhjh',label_visibility="collapsed")
st.write('')
cold1,cold2,cold3,cold4 = st.columns(4)
with cold1:
    Describtion = st.text_input(':blue[Description]')
with cold2:
    quantity = st.number_input(':blue[Quantity]',0)
with cold3:
    PriceUnit = st.number_input(':blue[Price|Unit]',0)
with cold4:
    price = quantity*PriceUnit
    totalPrice = st.text_input(':blue[Total Price]',value=price,disabled=True)
st.write('----------')
cole1,cole2 = st.columns(2)
with cole1:
    st.write(':blue[Payment Info]')
    st.write(':blue[Acc name: KFC Foods]')
    st.write(':blue[Acc Number: 509 173 1594]')
    st.write(':blue[Bank Name: England Bank]')
    view = st.button(':blue[View Invoice]')
with cole2:
    st.write(':blue[Payment Due:]')
    st.header(f':green[${price:,}]')


#function to generate your PDF

def generate_pdf():
    pdf = FPDF()

    #add a page
    pdf.add_page()

    #set your default fonts
    pdf.set_font('Arial',size=12)

    colx = 20
    coly = 20
    colw= 90

    pdf.image('kfclogo.png',x=colx,y=coly,w=40)

#FONTS: Courier, Arial, Times, Symbol
    #INVOICE
    pdf.set_font(family='Times',size=30,style='B')
    pdf.set_xy(colx+120,coly+12)
    pdf.cell(w=colw,txt='INVOICE',ln=True,align='L')

    #KFC
    pdf.set_font(family='Courier',size=12,style='B')
    pdf.set_xy(colx+10,coly+30)
    pdf.cell(w=colw,txt='KFC',ln=True,align='L')

    #ADDRESS
    pdf.set_font(family='Courier',size=12,style='B')
    pdf.set_xy(colx+10,coly+40)
    pdf.cell(w=colw,txt='564, Chicken wings street',ln=True,align='L')

    #COUNTRY
    pdf.set_font(family='Courier',size=12,style='B')
    pdf.set_xy(colx+10,coly+50)
    pdf.cell(w=colw,txt='Manchester, UK',ln=True,align='L')

    #BILL TO
    pdf.set_font(family='Courier',size=12,style='B')
    pdf.set_xy(colx+10,coly+70)
    pdf.cell(w=colw,txt='BILL TO:',ln=True,align='L')

    #NAME
    pdf.set_font(family='Courier',size=12,style='B')
    pdf.set_xy(colx+10,coly+80)
    pdf.cell(w=colw,txt=f'{name}',ln=True,align='L')

    #EMAIL
    pdf.set_font(family='Courier',size=12,style='B')
    pdf.set_xy(colx+10,coly+90)
    pdf.cell(w=colw,txt=f'{email}',ln=True,align='L')





    #save the PDF
    pdf_file = 'invoice.pdf' #create the file name
    pdf.output(pdf_file)
    return pdf_file


#store the function in a variable
pdf_func = generate_pdf()

#read the PDF func as binary data
with open(pdf_func,'rb') as binary:
    pdf_data = binary.read()

if view:
    #write the PDF using base64
    pdf_base64 = base64.b64encode(pdf_data).decode('utf-8')

    #Generate the HTML to embed the PDF
    pdf_embed = f'<embed src="data:application/pdf;base64, {pdf_base64}" type="application/pdf" width="100%" height="600px" />'

    #display the embedded PDF (Markdown helps us to use HTML on streamlit)
    st.markdown(pdf_embed,unsafe_allow_html=True)

