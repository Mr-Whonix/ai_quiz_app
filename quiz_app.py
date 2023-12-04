from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

OPENAI_API_KEY = "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"

def quiz_Questions(quizTopic, qtionsNumbers):
    my_llm = OpenAI(api_key= OPENAI_API_KEY ,temperature=0.7)

    my_template = PromptTemplate(
        input_variables=["quizTopic", "qtionsNumbers"],
        template='''The user wants to take the quiz to check if he understood his subject well before his final exam. 
        The user will choose to take the quiz upon his interest {quizTopic} and 
        number of questions will be {qtionsNumbers}, Generate MCQs questions.'''
    )

    my_chain = LLMChain(llm=my_llm, prompt=my_template, output_key='qtionsNumbers')
    response = my_chain({'quizTopic': quizTopic, 'qtionsNumbers': qtionsNumbers})

    return response

