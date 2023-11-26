import re
import pandas as pd

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

    return questions[1:]


def separate_question_elements(question: str) -> (str, [str]):
    """Separa a questão em seus elementos básicos, ou seja, enunciado
    e alternativas.

    Args:
        question (str): _description_

    Returns:
        str: enunciado
        [str]: lista de alternativas
    """
    
    # procura pelos delimitadores de alternativas (A-E no início de linha)
    enem_pattern = re.compile(r'^[A-E]\s[A-E] |^[A-E]\s', re.MULTILINE)
    match = re.split(enem_pattern, question)
    
    # considerando que os 5 últimos matches são as alternativas
    try:
        statement = ''.join(match[0:-5])
        alternatives = match[-5:]
    except:
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
    pattern = re.compile(r'^(\d+)\s+([A-E])', re.MULTILINE)

    answers = pattern.findall(text)

    gabarito = [(int(number), answer.upper()) for number, answer in answers]
    
    gabarito = sorted(gabarito, key=lambda x: x[0])
    
    # inglês e espanhol eu separei em 10 questões diferente
    # poderia também retornar o gabarito com 5 questões especiais ('1', 'A', 'B')
    pattern = re.compile(r'^(\d+)\s+([A-E])\s+([A-E])', re.MULTILINE)
    ing_esp = pattern.findall(text)
    esp = [(item[0], item[2]) for item in ing_esp]
    for answer in esp:
        gabarito.insert(int(answer[0])-1+5, answer)
    
    return gabarito
    

def scrappe_enem(year, day):
    exam_name = f'{year}_enem_{day}_dia'
    exam = get_raw_text(exam_name)
    raw_questions = separate_questions(exam)
    
    answer_sheet_name = f'{year}_enem_{day}_dia_gabarito'
    answer_sheet = get_raw_text(answer_sheet_name)
    answers = get_answers(answer_sheet)
    
    questions = []
    
    for question in raw_questions:
        statement, alternatives = separate_question_elements(question)
        statement, alternatives = format_question(statement, alternatives)
        
        questions.append([statement, alternatives])
    
    return questions, answers


def scrappe_enem_edition(year):
    first_day_questions, first_day_answers = scrappe_enem(year, 1)
    second_day_questions, second_day_answers = scrappe_enem(year, 2)
    
    all_questions = first_day_questions + second_day_questions
    all_answers = first_day_answers + second_day_answers
    
    return all_questions, all_answers

def generate_dataframe(edition):
    questions, answers = scrappe_enem_edition(edition)
    
    # cria os 2 dataframes
    df1 = pd.DataFrame(questions, columns=['enunciado', 'alternativas'])
    df2 = pd.DataFrame(answers, columns=['questao', 'gabarito'])

    # junta os 2 dataframes
    result_df = pd.concat([df2, df1], axis=1)

    return result_df
    

def test2():
    txt = get_raw_text("2023_enem_1_dia")
    questions = separate_questions(txt)
    
    question = questions[16]
    statement, alternatives = separate_question_elements(question)
    statement, alternatives = format_question(statement, alternatives)

    print(statement)
    print(alternatives)


def test():
    questions, answers = scrappe_enem_edition(2023)
    
    #print(questions[183][0])
    #print(questions[183][1])
    #print(questions[45][1:])
    print(answers)
    print(len(answers))
    #print(questions)

def main():
    print("MELVIN EXAM DATAFRAME GENERATOR")
    enem_editions = [2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]
    
    for enem_edition in enem_editions:
        df = generate_dataframe(enem_edition)
        print(f'\nEnem {enem_edition}')
        print(df)
        df.to_csv(f'../data/enem_{enem_edition}.csv', index=False)

if __name__ == "__main__":
    main()