from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import AzureChatOpenAI

from neural_search.models.keyword_model import Keywords

from dotenv import load_dotenv

from neural_search.models.summary_model import Summary

load_dotenv()

llm = AzureChatOpenAI(model="gpt-4", deployment_name="hom-gpt-4")

parser = JsonOutputParser(pydantic_object=Keywords)

summary_parser = JsonOutputParser(pydantic_object=Summary)


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

def generate_summary_chain():
    # Define the new prompt template for summarization
    prompt_template = PromptTemplate(
        template="""
            Given the context: "{context}"
            and the specific interest in the search query: "{search_query}" related to the ticker symbol "{ticker}",
            the search query is just for reference dont directly check that, understand the query, any related items to the search query should also be considered,
            You are writing this for report, so be good at summarizing, dont say they have firect relation and all
            summarize the key points and implications in multiple paragraphs, focusing on:
            1. The overall impact of the search query topic on the company represented by the ticker.
            2. Key financial aspects related to the search query and ticker.
            3. Future outlook and strategic moves in response to the search query topic.
            4. Potential risks and opportunities for investors.
            
            {format_instructions}

            Ensure the summary is comprehensive and provides valuable insights for stakeholders.
            """,
        input_variables=["context", "search_query", "ticker"],
        partial_variables={"format_instructions": summary_parser.get_format_instructions()},
    )

    chain = prompt_template | llm | summary_parser

    return chain