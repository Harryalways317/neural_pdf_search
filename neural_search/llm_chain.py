from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import AzureChatOpenAI

from neural_search.models.keyword_model import Keywords

from dotenv import load_dotenv
load_dotenv()

llm = AzureChatOpenAI(model="gpt-4", deployment_name="hom-gpt-4")

parser = JsonOutputParser(pydantic_object=Keywords)


def generate_chain():
    prompt = PromptTemplate(
        template="""
                get similar keywords related to the given keyword
                if the query is defense then keywords are like "Military Contracts", "Defense Contracts", "Government Contracts" "Force Modernization", "Military Upgrades", "Defense Revitalization" Defense Budget", "Military Spending", "Defense Expenditure" "Weapons Systems", "Armament See full mat Development", "Defense Platforms" "Strategic Partnerships", "Military Alliances", "Defense Collaboration" "Unmanned Vehicles", "Autonomous Systems", "Drone Technology" "Threat Assessment", "Risk Analysis", "Security Evaluation"
                {format_instructions}

                {keyword}
                """,
        input_variables=["query"],
        partial_variables={"format_instructions": parser.get_format_instructions()},
    )

    print(prompt.template)

    # Construct a Langchain Chain to connect the prompt template with the LLM and Pydantic parser
    chain = prompt | llm | parser

    return chain