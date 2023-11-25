import re

DEFAULT_RAW_TXT_PATH = '../raw_txts'

def get_raw_text(exam_name: str) -> str:
    """Obtém o texto bruto da prova, pelo arquivo txt da pasta /raw_txts

    Args:
        exam_name (str): nome do arquivo da prova

    Returns:
        str: texto bruto da prova
    """
    file_extension = ".txt"
    full_path = DEFAULT_RAW_TXT_PATH + '/' + exam_name + file_extension
    f = open(full_path, "r")
    
    return f.read()


def separate_questions(exam_raw_txt: str) -> [str]:
    """Separa questões do enem por 

    Args:
        exam_raw_txt (str): texto bruto da prova

    Returns:
        [str]: lista de questões (texto bruto, com enunciado e alternativas)
    """
    # padrão regex para pegar questões do enem
    enem_pattern = re.compile(r'QUESTÃO \d+', re.IGNORECASE)
    questions = re.split(enem_pattern, exam_raw_txt)

    # remover elementos vazios resultantes da divisão
    questions = [question.strip() for question in questions if question.strip()]

    return questions


def separate_question_elements(question: str) -> (str, [str]):
    """Separa a questão em seus elementos básicos, ou seja, enunciado
    e alternativas.

    Args:
        question (str): _description_

    Returns:
        str: enunciado
        [str]: lista de alternativas
    """
    
    # procura pelos delimitadores de alternativas
    enem_pattern = re.compile(r'A A |B B |C C |D D |E E ')
    match = re.split(enem_pattern, question)
    
    statement = match[0]
    alternatives = match[1:]
    
    return statement, alternatives


def format_question(statement: str, alternatives: [str]) -> (str, [str]):
    """Formata a questão para corrigir problemas de espaçamento, ortografia,
    formatação em geral, etc.

    Args:
        statement (str): enunciado original, não formatado
        alternatives ([str]): alternativas da questão, originais, não formatadas
        
    Returns:
        str: enunciado formatado
        [str]: alternativas formatadas
    """
    new_statement = normalize_white_spaces(statement)
    new_alternatives = [normalize_white_spaces(alternative) for alternative in alternatives]
    
    return new_statement, new_alternatives


def normalize_white_spaces(text: str) -> str:
    """Corrige problemas de espaçamento irregular no texto, trocando tabs por
    whitespaces padrão.

    Args:
        text (str): texto original não formatado

    Returns:
        str: texto formatado, com correção dos espaçamentos
    """
    corrected_text = re.sub(r'\s+', ' ', text)
    
    return corrected_text

def get_answers(text):
    pattern = re.compile(r'(\d+)\s+([A-Za-z])')

    answers = pattern.findall(text)

    gabarito = {int(number): answer.upper() for number, answer in answers}

    print(gabarito)


def test2():
    txt = get_raw_text("texto_bruto_enem")
    questions = separate_questions(txt)
    question = questions[21]
    statement, alternatives = separate_question_elements(question)
    statement, alternatives = format_question(statement, alternatives)
    
    print(statement)
    print(f'(A) {alternatives[0]}')
    print(f'(B) {alternatives[1]}')
    print(f'(C) {alternatives[2]}')
    print(f'(D) {alternatives[3]}')
    print(f'(E) {alternatives[4]}')


def test():
    txt = get_raw_text('2016_enem_1_dia_gabarito')
    get_answers(txt)
    
test()