from crewai import Agent, Task, Crew
#from langchain_ollama import OllamaLLM # pip install langchain-ollama
from langchain_openai import ChatOpenAI
#from langchain_anthropic import ChatAnthropic # pip install langchain_anthropic
from dotenv import load_dotenv
load_dotenv()


joao_fine_tunning = Agent(
    role='O seu papel é criar diálogos',
    goal='Fazer as melhores perguntas e repostas possiveis',
    backstory="""
    Você é um entrevistador profissional
""",
    verbose=False,
    allow_delegation=False,
    max_iter=10,
    # llm=ChatAnthropic(model='claude-3-haiku-20240307'),
    # llm=ChatOpenAI(model_name="gpt-4o", temperature=0.1),
    llm=ChatOpenAI(model_name="llama3.1", base_url = "http://localhost:11434/v1", api_key="nada", temperature=0.1),
    # llm=OllamaLLM(model="llama3.1", base_url = "http://localhost:11434", api_key="nada", temperature=0.1)
)


task1 = Task(
    description="""
    Baseado em um prompt recebido, criar cinco perguntas e respostas diferentes:
    
    {prompt}
    
    """,
    agent=joao_fine_tunning,
    expected_output="""
        Suas 5 respostas precisam ser em português no formato Json.

        Exemplo de 5 respostas:

        {exemplos}
        {exemplos}
        {exemplos}
        {exemplos}
        {exemplos}
    """
)


crew = Crew(
    agents=[joao_fine_tunning],
    tasks=[task1],
    verbose=2,
)

result = crew.kickoff(
    inputs={"prompt": "Diálogos hipotéticos entre um cachorro e um gato",
    #"exemplos": {"messages": '[{"role": "user", "content": "coloque a pergunta aqui"}, {"role": "assistant", "content": "coloque a resposta aqui"}]}'}})
    "exemplos": {"menssagens": '[{"cachorro": "coloque a pergunta aqui"}, {"gato": "coloque a resposta aqui"}]}'}})

print(result)
