from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

OPENAI_API_KEY = "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"

def quiz_Questions(quizTopic, qtionsNumbers):
    my_llm = OpenAI(api_key= OPENAI_API_KEY ,temperature=0.7)

    my_template = PromptTemplate(
        input_variables=["quizTopic", "qtionsNumbers"],
        template='''The user wants to take the quiz to check if he understood his subject well before his final exam. 
        The user will choose to take the quiz upon his interest {quizTopic} and will choose how many numbers of {qtionsNumbers} 
        he wants to be shown once the quiz starts. Generate MCQs based on the user's interest topic and how many
        questions he wants, after that show the correct answers.'''
    )

    my_chain = LLMChain(llm=my_llm, prompt=my_template, output_key='qtionsNumbers')
    response = my_chain({'quizTopic': quizTopic, 'qtionsNumbers': qtionsNumbers})

    return response

