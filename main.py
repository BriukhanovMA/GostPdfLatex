from GetForma_to_svg import GetoverPagedict
from SVGtoPDF_Script import Result_skript
from Script_Stamp import stamp

List_pole ={
    'contractor': 'Иванов В.В',
    'Numer_variant': "ДП 13.03.02.15",
    'Secton': "ЭЛЕКТРОТЕХНИЧЕСКАЯ ЧАСТЬ",
    'receiving': "Толстов А.В.",
    'Critic': "Гоголь В.А.",
    'N_control': "Дунай А.М.",
    'num_sec': 40,
    'Pole_group': "ЧПТК гр. Эз-13"
}



GetoverPagedict('page1.svg', 'page2.svg', List_pole, 'SVG_Form')
Result_skript('SVG_Form', 'PDF_Form', f'{List_pole["Secton"]} border')
stamp('Вторая.pdf', f'{List_pole["Secton"]} border.pdf', 'PDFGost.pdf', 0)
