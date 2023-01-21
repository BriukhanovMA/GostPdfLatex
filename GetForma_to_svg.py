from jinja2 import Environment, FileSystemLoader
from pathlib import Path

List_pole ={
    'contractor': 'Иванов В.В',
    'Numer_variant': "ДП 13.03.02.15",
    'Secton': "ЭЛЕКТРОТЕХНИЧЕСКАЯ ЧАСТЬ",
    'receiving': "Толстов А.В.",
    'Critic': "Гоголь В.А.",
    'N_control': "Дунай А.М.",
    'num_sec': 11,
    'Pole_group': "ЧПТК гр. Эз-13"
}


def getForma_to_svg_Frontpage(File, List_pole, Name_file, flag = True):
    """"
    Заполняет форму svg файла титульного листа, данные получает из dict
    """
    lr = FileSystemLoader("templates", followlinks=True)
    env = Environment(loader = lr)
    tm = env.get_template(File)
    msg = tm.render(List_pole)
    if flag:
        OpenSvg(Name_file, msg)
        return print(f'Выполнено, file {Name_file} создан')
    return msg

def getForma_to_svg_Otherpage(File, List_pole, page_i, Name_file, flag = True):
    """"
    Заполняет форму svg файла основных страниц , данные получает из dict
    """
    lr = FileSystemLoader("templates", followlinks=True)
    env = Environment(loader = lr)
    tm = env.get_template(File)
    msg = tm.render(List_pole, num_sec_i = page_i)
    if flag:
        OpenSvg(Name_file, msg)
        return print(f'Выполнено, file {Name_file} создан')
    return msg

def OpenSvg(Name_file, msg):
    """"
    Заполняет форму svg файла , данные получает из dict
    """
    with open(Name_file, mode="w", encoding="utf-8") as message:
        message.write(msg)


def GetoverPagedict(
    NameForm_1: Path,
    NameForm_2: Path,
    List_pole: dict,
    PathSaveFile: Path
):
    getForma_to_svg_Frontpage(NameForm_1, List_pole, f'{PathSaveFile}/Ferstpage1.svg')
    for i in range(2, List_pole['num_sec']+1):
        getForma_to_svg_Otherpage(NameForm_2, List_pole, i, f'{PathSaveFile}/Otherpage{i}.svg')

# GetoverPagedict('page1.svg', 'page2.svg', List_pole, 'SVG_Form')