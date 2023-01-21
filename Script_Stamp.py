from pathlib import Path
from typing import Union, Literal, List
from pypdf import PdfWriter, PdfReader


def pageRamki(
    stamp_pdf,
    index
):
    reader = PdfReader(stamp_pdf)
    image_page = reader.pages[index]
    return image_page

def pageGOST(
    content_pdf,
    index
):
    reader = PdfReader(content_pdf)
    image_page = reader.pages[index]
    return image_page


def WritGost(
    pdf_result,
    writer
):
    with open(pdf_result, "wb") as fp:
        writer.write(fp)

def Merge(
    content_page,
    image_page
):
    mediabox_1 = image_page.mediabox
    mediabox_2 = content_page.mediabox
    content_page.merge_page(image_page, expand = False)
    content_page.mediabox = mediabox_2
    return content_page


def stamp(
    content_pdf: Path,
    stamp_pdf: Path,
    pdf_result: Path,
    page_indices = 0
):
    reader = PdfReader(content_pdf)
    Len_Content = len(reader.pages)
    reader = PdfReader(stamp_pdf)
    Len_Stamp = len(reader.pages)
    writer = PdfWriter()
    for index in range(0,page_indices):
        writer.add_page(pageGOST(content_pdf, index))
    Granica = Len_Stamp + page_indices
    for index in range(page_indices,Granica):
        List_page = Merge(pageGOST(content_pdf, index), pageRamki(stamp_pdf, index-page_indices))
        writer.add_page(List_page)
    for index in range(Granica,Len_Content):
        writer.add_page(pageGOST(content_pdf, index))
    WritGost(pdf_result, writer)

