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
    # procura pelo enunciado da questão
    statement_pattern = re.compile(r'^(.*?)(?=\sA\sA)', re.DOTALL)
    statement_match = re.search(statement_pattern, question)

    statement = statement_match.group(1).strip() if statement_match else ''

    # Find the alternatives (A to E)
    alternatives_pattern = re.compile(r'([A-E])\s\1\s\[(.*?)\]', re.DOTALL)
    alternatives = {match.group(1): match.group(2).strip() for match in re.finditer(alternatives_pattern, question)}
    
    # TODO n tá funfando; gepeto trolou
    return statement, alternatives


def test():
    txt = get_raw_text("texto_bruto_enem")
    questions = separate_questions(txt)
    question = questions[19]
    statement, alternatives = separate_question_elements(question)
    
    print(question)
    print(statement)
    print(alternatives)

test()