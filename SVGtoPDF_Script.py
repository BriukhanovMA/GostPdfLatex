import cairosvg
import os
from pypdf import PdfWriter
from natsort import natsorted, ns


def SVGtoPDFConvector(Path_SVGform, Path_PDFform):
    arr = os.listdir(Path_SVGform)
    for page in arr:
        cairosvg.svg2pdf(file_obj=open(f"{Path_SVGform}\{page}", "rb"), write_to=f"{Path_PDFform}\{page.split('.')[0]}.pdf", parent_width = 297, parent_height = 210)





def CollectPage_PDF(Path_PDFform, Result_Name):
    arr = os.listdir(Path_PDFform)
    arr_sort = natsorted(arr, alg=ns.IGNORECASE)
    merger = PdfWriter()
    for pdf in arr_sort:
        merger.append(f"{Path_PDFform}\{pdf}")
    merger.write(f"{Result_Name}.pdf")
    merger.close()



def ClearForms(Path_SVGform, Path_PDFform):
    arr = os.listdir(Path_SVGform)
    arr_sort = natsorted(arr, alg=ns.IGNORECASE)
    for obj in arr_sort:
        os.remove(f"{Path_SVGform}\{obj}")
    arr = os.listdir(Path_PDFform)
    arr_sort = natsorted(arr, alg=ns.IGNORECASE)
    for obj in arr_sort:
        os.remove(f"{Path_PDFform}\{obj}")



def Result_skript(Path_SVGform, Path_PDFform, Result_Name):
    SVGtoPDFConvector(Path_SVGform, Path_PDFform)
    CollectPage_PDF(Path_PDFform, Result_Name)
    ClearForms(Path_SVGform, Path_PDFform)


