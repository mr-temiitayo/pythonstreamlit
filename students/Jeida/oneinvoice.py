import streamlit as st
from fpdf import FPDF #python module to generate PDFs
import base64 #python module to convert binary data (code) to printable character (PDF)

cl,cl2,cl3 = st.columns([2,1,1])
with cl3:
    st.header(':blue[**INVOICE**]')


with cl:
    img,img2,img3 = st.columns(3)
    with img:
        st.image('Logobiz.png',use_column_width=True) #to use full width
    
    st.write('')
    st.write(':blue[Deloitz Ventures]')
    st.write(':blue[1 Hacker Way, Menlo Park, CA 94025]')
    st.write(':blue[California, USA]')


st.header('')
st.header('')


ft,ft2,ft3 = st.columns([2,0.7,1])


with ft:
    name = st.text_input(':blue[**Bill To:**]',placeholder='Customer Name')
    st.write('')
    email = st.text_input('Enter email address',placeholder='Enter Email Address',label_visibility='collapsed')


with ft2:
    st.write(':blue[**INVOICE #**]')
    st.write('')
    st.write(':blue[**Invoice Date**]')
    st.write('')
    st.write(':blue[**Due Date**]')


with ft3:
   inv = st.text_input('invoice',label_visibility='collapsed')
   invdt = st.date_input('invoice date',label_visibility='collapsed')
   duedt = st.date_input('due date',label_visibility='collapsed')


st.header('')




st.divider()
st.header('')


c,c2,c3,c4 = st.columns([3,3,3,3])


with c:
    desc = st.text_input(':blue[**Description**]',placeholder='Enter Description')
with c2:
    qua = st.number_input(':blue[**Quantity**]',value=0,step=1)
with c3:
    pri = st.number_input(':blue[**Price | Item**]',value=0,step=1)
with c4:
    total = qua * pri
    amo = st.text_input(':blue[**Amount**]',placeholder=0, disabled=True, value=total)






st.header('')
st.divider()


py,py2 = st.columns([2,2])


with py:
    st.write(':blue[**Payment Info**]')
    st.write('Account Name: FaceBook')
    st.write('Account Number: 00919900001')
    st.write('Bank Name: Meta Pay')


with py2:
    ppy,ppy2 = st.columns([1,5])
    with ppy2:
     st.write(':blue[**Payment Due:**]')


     st.subheader(f'{total:,} AED')



#function to generate our PDF

def generate_pdf():
    pdf = FPDF() #create a var to rep our FPDF module

    #Add a page
    pdf.add_page()

    #s=Set your default fonts
    pdf.set_font('Arial', size=12)

    #Set column1 x and y coord

    col1x = 20
    col1y = 25

    #Set column width
    colw = 90
    colh = 10

    #Add Logo
    pdf.image('Logobiz.png',x=col1x,y=col1y,w=20)

    # FONTS TO USE: Courier, Helvetica/Arial,  Times, Symbol, ZapfDingbats
    #INVOICE
    # pdf.set_text_color(50,168,125)
    pdf.set_font(family='Times',size=30,style='B')
    pdf.set_xy(col1x+120,col1y+5)
    pdf.cell(colw,colh,txt='INVOICE',ln=True,align='L')


    # #Deloitz Ventures
    # pdf.set_font(family='Courier',size=12,style='B')
    # pdf.set_xy(col1x,col1y+25)
    # pdf.cell(colw,colh,txt='Deloitz Ventures',ln=True,align='L')   


    # #Address
    # pdf.set_font(family='Courier',size=12,style='B')
    # pdf.set_xy(col1x,col1y+35)
    # pdf.cell(colw,colh,txt='1 Hacker Way, Menlo Park, CA 94025',ln=True,align='L')  


    # # California, USA
    # pdf.set_font(family='Courier',size=12,style='B')
    # pdf.set_xy(col1x,col1y+45)
    # pdf.cell(colw,colh,txt='California, USA',ln=True,align='L') 


    #Bill to
    pdf.set_font(family='Courier',size=12,style='B')
    pdf.set_xy(col1x,col1y+25)
    pdf.cell(colw,colh,txt='BILLED TO:',ln=True,align='L') 


    #Invoice Number
    pdf.set_font(family='Courier',size=12,style='B')
    pdf.set_xy(col1x+120,col1y+25)
    pdf.cell(colw,colh,txt=f'Invoice No: {inv}',ln=True,align='L') 

    #Date
    pdf.set_font(family='Courier',size=12,style='B')
    pdf.set_xy(col1x+120,col1y+35)
    pdf.cell(colw,colh,txt=f'{invdt}',ln=True,align='L') 


    #Name
    pdf.set_font(family='Courier',size=12,style='B')
    pdf.set_xy(col1x,col1y+35)
    pdf.cell(colw,colh,txt=f'{name}',ln=True,align='L') 


    #Email
    pdf.set_font(family='Courier',size=12,style='B')
    pdf.set_xy(col1x,col1y+45)
    pdf.cell(colw,colh,txt=f'{email}',ln=True,align='L') 


    #Line
    pdf.set_line_width(0.5) #set the width of the line
    pdf.line(col1x,col1y+70,col1x+170,col1y+70) #startxy and stopxy

    #Item
    pdf.set_font(family='Courier',size=12,style='B')
    pdf.set_xy(col1x,col1y+75)
    pdf.cell(colw,colh,txt='ITEM',ln=True,align='L') 


    #Quantity
    pdf.set_font(family='Courier',size=12,style='B')
    pdf.set_xy(col1x+70,col1y+75)
    pdf.cell(colw,colh,txt='QUANTITY',ln=True,align='L') 

    #Unit Price
    pdf.set_font(family='Courier',size=12,style='B')
    pdf.set_xy(col1x+85,col1y+75)
    pdf.cell(colw,colh,txt='UNIT PRICE',ln=True,align='L') 


    #Total 
    pdf.set_font(family='Courier',size=12,style='B')
    pdf.set_xy(col1x+120,col1y+75)
    pdf.cell(colw,colh,txt='TOTAL',ln=True,align='L') 

    #Save the PDF
    pdf_file = 'invoice.pdf' #create the file name
    pdf.output(pdf_file) 
    return pdf_file

#Store the function in a variable
pdf_func = generate_pdf()

#Read the PDF Func as binary data
with open(pdf_func, 'rb') as binary:
    pdf_data = binary.read()


if st.button(":blue[View Inovice]"):
    #Write the PDF using base64
    pdf_base64 = base64.b64encode(pdf_data).decode('utf-8')

    #Generate the HTML to embed the PDF
    pdf_embed = f'<embed src="data:application/pdf;base64,{pdf_base64}" type="application/pdf" width="100%" height = "600px" />'

    #Display the embedded pdf (markdown helps us to use HTML on streamlit)
    st.markdown(pdf_embed,unsafe_allow_html=True)



