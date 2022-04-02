import datetime
from fpdf import FPDF
class pdf_converter:
    def generate_pdf():
        pdf = FPDF('P', 'in', 'A5')
        font_height = 0.16

        pdf.add_page()
        pdf.set_margins(1.0, 1.0)
        pdf.set_auto_page_break(True, margin = 0.25)

        pdf.set_font('Courier', "", 10)
        pdf.set_xy(1.0, 1.0)

        f = open('doc.txt')
        for line in f:
            pdf.write(font_height, line)
        f.close()

        #Hash function to generate unique file name using datetime module
    
        uniq_filename = 'Jarvis_'+str(datetime.datetime.now().date())
        uniq_filename=uniq_filename+'_' + str(datetime.datetime.now().time()).replace(':', '_')[0:8]
        uniq_filename=uniq_filename+'.pdf'
        with open("name.txt","w") as f:
            f.write(uniq_filename)
        pdf.output(uniq_filename)

        
