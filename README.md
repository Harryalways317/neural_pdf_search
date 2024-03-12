# Neural Search

First The Chunks needs to be generated with the pdfs
using ingest/preprocess.py and create chunks.json file

this will use sentence transformer model for chunking and then  uses spacy's model en_core_web_lg to get the organization names, which we can filter and stored under tickers on each doc, can be used for matching




a chunks.json file is created, diving the pdfs to chunks and then it has 
the format of 
```json
{
    "text": "Date: - 24th June, 2023 SUBJECT: - SUBMISSION OF ANNUAL REPORT Dear Sir / Madam, Pursuant to Regulation 34(1) of the SEBI (LODR) Regulations, 2015, we are pleased to enclose herewith copy of the Annual Report of the Company for the year financial year 2022-23. This is for your information and record. Thanking you, For SONA BLW PRECISION FORGINGS LIMITED Ajay Pratap Singh Vice President (Legal), Company Secretary and Compliance Officer Encl: As above BSE Ltd. Regd. Office: Floor - 25, Phiroze Jeejeebhoy Towers, Dalal Street, Mumbai-400 001. National Stock Exchange of India Ltd. Listing Deptt., Exchange Plaza, Bandra Kurla Complex, Bandra (East), Mumbai - 400 051 BSE Scrip Code: 543300 NSE Scrip: SONACOMS AJAY PRATAP SINGH Digitally signed by AJAY PRATAP SINGH Date: 2023.06.24 18:48:59 +05'30'  Annual Report 2022-23 Annual Report 2022-23  The future of mobility is E.P.I.C. Mobility as we know it, is undergoing a structural",
    "tickers": [
      "Regd",
      "National Stock Exchange of India Ltd.",
      "AJAY PRATAP SINGH Digitally",
      "BSE Ltd.",
      "SEBI",
      "AJAY PRATAP SINGH Date",
      "SONA",
      "Deptt"
    ],
    "pdf_name": "AR_22066_SONACOMS_2022_2023_24062023190637.pdf",
    "page_number": 3
  }
```

using the chunks.json file ingest them to qdrant db using ingest.py


once data in ingested we can search the data.

we can filter the data to only show the data which has the ticker we want
the search function uses llm to generate similar keywords and append them to a string and searches with the string to get nearest rests, then we can filter with the ticker for further more filtering, the filter will convert everything to lowercase with no spaces and check so that TATA MOTORS PVT LTD can match TATA MOTORS (tried fuzzy but it adds a lot latency)



TODO:

then the retrived contexts are sent to llm for summary generation