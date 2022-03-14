import sys

from bin.design_pdf import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
import PyPDF2
import os

class ok(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.setWindowTitle('Split and Merge PDF')
        self.setFixedSize(400, 500)


class SplitAndMergePdf(QMainWindow, Ui_MainWindow):  
    def __init__(self, parent=None, count=1, new_pdf=None):
        super().__init__(parent)
        super().setupUi(self)
        self.setWindowTitle('Split and Merge PDF')
        self.setFixedSize(400, 500)
        self.count = count
        self.btnAddArquivo.clicked.connect(self.add_pdf)
        self.btnSaida.clicked.connect(self.saida_pasta)
        self.btnUnir.clicked.connect(self.unir)
        self.btnEscolheArquivo.clicked.connect(self.open_pdf)
        self.btnUnir_.clicked.connect(self.dividir)


    def add_pdf(self):
        pdf, _ = QFileDialog.getOpenFileName(
            self.centralwidget,
            'Adicionar PDF',
            '/home/leandro/',
            options=QFileDialog.DontUseNativeDialog
            )

        if self.count == 1:
            self.unir1.setText(pdf)
            self.count += 1

        elif self.count == 2:
            self.unir2.setText(pdf)
            self.count += 1

        elif self.count == 3:
            self.unir3.setText(pdf)
            self.count += 1

        elif self.count == 4:
            self.unir4.setText(pdf)
            self.count += 1   

        elif self.count == 5:
            self.unir5.setText(pdf)
            self.count += 1  

        else:
            self.unir6.setText(pdf)
                             
    def saida_pasta(self):
        pasta = QFileDialog.getExistingDirectory(
            self.centralwidget,
            'Adicionar PDF',
            '/home/leandro/',
            options=QFileDialog.DontUseNativeDialog
            )
    
        self.saida.setText(pasta)


    def unir(self):
        new_pdf = PyPDF2.PdfFileMerger()

        try:
            new_pdf.append(self.unir1.text(), 'rb')
            new_pdf.append(self.unir2.text(), 'rb')
            new_pdf.append(self.unir3.text(), 'rb')
            new_pdf.append(self.unir4.text(), 'rb')
            new_pdf.append(self.unir5.text(), 'rb')
            new_pdf.append(self.unir6.text(), 'rb')

        except:
            pass    

        saida = self.saida.text()

        try: 
            with open(f'{saida}/merged.pdf', 'wb') as my_new_pdf:
                new_pdf.write(my_new_pdf)
                
        except:
            pass  
        
        try:
            if self.checkBoxDelUnir.isChecked() == True:
                os.remove(self.unir1.text())
                os.remove(self.unir2.text())
                os.remove(self.unir3.text())
                os.remove(self.unir4.text())
                os.remove(self.unir5.text())
                os.remove(self.unir5.text())   

        except:
            pass

        
    def open_pdf(self):
        pdf, _ = QFileDialog.getOpenFileName(
        self.centralwidget,
        'Escoolher PDF',
        '/home/leandro/',
        options=QFileDialog.DontUseNativeDialog
        )

        self.lineEdit_3.setText(pdf)


    def dividir(self):
        caminho = self.lineEdit_3.text()
        with open(f'{caminho}', 'rb') as pdf_file:
            reader = PyPDF2.PdfFileReader(pdf_file)
            pages_numb = reader.getNumPages()

            for pages_numb in range(pages_numb):
                writer = PyPDF2.PdfFileWriter()
                actual_page = reader.getPage(pages_numb)
                writer.addPage(actual_page)
                
                with open(f'splited_{pages_numb + 1}.pdf', 'wb') as new_pdf:
                    writer.write(new_pdf)

        try:
            if self.checkBoxDelDividir.isChecked() == True:
                os.remove(caminho)  

        except:
            pass
              

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    PDF = SplitAndMergePdf()
    PDF.show()
    qt.exec_()
