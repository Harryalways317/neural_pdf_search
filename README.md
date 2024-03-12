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



## Sample Output
```json
{
    "summary": {
        "content": "1. Overall Impact on the Company: Tata Advanced Systems (TAS), a subsidiary of Tata Motors, appears to be heavily involved in the defense sector, manifesting in various collaborations, projects, and defense contracts. The company is engaged in the manufacturing of armored vehicles and defense systems, demonstrating a strong presence in the defense and military industry. The sale of certain assets related to its defense business to Tata Advanced Systems Limited (TASL) indicates an operational realignment within the group's defense entities. This strategic decision could potentially streamline its operations and enhance its focus on its core defense-related activities. Importantly, the company's involvement in the force modernization and military upgrades aligns with the global trend towards the modernization of defense equipment and could further strengthen its market position.\n\n2. Key Financial Aspects: Financially, the sale of defense assets to TASL amounted to `234.09 crores, contributing to the company's revenue stream. However, no specific financial details related to its defense contracts or military projects were disclosed. The company's sustained investment and involvement in defense-related projects underscore its commitment to this sector and indicate a significant portion of its revenue and expenditure might be linked to defense-related activities.\n\n3. Future Outlook and Strategic Moves: Tata Advanced Systems Limited (TAS) seems well-positioned for future growth in the defense sector, given its established presence and ongoing projects. The company's focus on autonomous systems and drone technology aligns with the industry's shift towards unmanned vehicles, suggesting potential future growth areas. The company's engagement in the development of advanced defense systems, including the integration of digital technologies, underpins its innovation-driven approach and could provide a competitive edge in the evolving defense landscape.\n\n4. Risks and Opportunities: While the defense sector offers substantial growth opportunities, it is also subject to various risks, including regulatory changes and geopolitical tensions. The company's significant involvement in this sector could expose it to these uncertainties. However, rising global defense budgets and increasing demand for advanced defense systems could present significant opportunities. For investors, the company's strong position in the defense sector, coupled with its innovative capabilities, could offer potential growth prospects. However, they should also consider the inherent risks associated with this sector.",
        "additional_kwargs": {},
        "type": "ai",
        "name": null,
        "id": null,
        "example": false
    },
    "search_result": [
        {
            "document": "No. Name of the entity 147 PT Mahindra Accelo Steel Indonesia 148 Mahindra Defence Systems Limited 149 Mahindra Emirates Vehicle Armouring FZ-LLC 150 Mahindra Armored Vehicles Jordan, LLC. 151 Mahindra Telephonics Integrated Systems Limited (w.e.f. 17th June, 2022) 152 Mahindra Aerospace Private Limited (w.e.f 29th March, 2023) 153 Mahindra Aerostructures Private Limited (w.e.f 29th March, 2023) 154 Mahindra Aerospace Australia Pty Ltd (w.e.f 29th March, 2023) 155 Gipps Aero Pty Ltd (w.e.f 29th March, 2023) 156 Airvan Flight Services Pty Ltd (w.e.f 29th March, 2023) 157 GA8 Airvan Pty Ltd (w.e.f 29th March, 2023) 158 GA200 Pty Ltd (w.e.f 29th March, 2023) 159 Nomad Tc Pty Ltd (w.e.f 29th March, 2023) 160 Airvan 10 Pty Ltd (w.e.f 29th March, 2023) 161 Mahindra Consulting Engineers Limited (upto 16th March, 2023) 162 Mahindra Consulting Engineers Limited ESOP Trust (upto 16th March, 2023) 163 Mahindra Namaste Limited (upto 16th March, 2023) 164 Mahindra",
            "page_number": 342,
            "pdf_name": "AR_22135_M&M_2022_2023_03072023013854.pdf"
        },
        {
            "document": "Guarantee/ security etc., in connection with loans provided and Interest, commission and other related income / expenses; 500 0.50% d) Sharing or usage of each other’s resources like employees, infrastructure including IT assets, cloud, IOT and digital engineering, digital transformation, analytics, cyber security, manpower, management and management support services, owned / third party services and reimbursements; 100 0.10% e) Purchase / sale / transfer / exchange / lease of business assets including property, plant and equipment, Intangible assets, transfer of technology to meet the business objectives and requirements; 25 0.025% f) Any transfer of resources, services or obligations to meet its objectives/ requirements. 25 0.025% Note: The value of corporate actions, if any, from CLPL including receipt of dividends, tendering securities as a part of buyback offer, receipt of bonus securities, subscribing to rights issue, etc. by the Company that are uniformly offered/applicable to all shareholders in proportion to their",
            "page_number": 33,
            "pdf_name": "AR_22135_M&M_2022_2023_03072023013854.pdf"
        },
        {
            "document": "Security CoP was formed and initial work started Set up an external SP advisory body External ESG advisory body with two global experts Annual human rights assessment across all the businesses Aim 2 Empowering over 2.5 million families with enhanced skillsets key performance indicators FY 2025 Goals FY 2030 Goals FY 2023 performance Material matters UN SDGs Skilling (Number of families to be impacted through skill development and training) 1.5 million 2.5 million families 0.6 million families skilled Community Development 2.3, 2.4, 4.4, 8.3 Aim 3 Uplifting over 100 million women and children through Education, Nutrition, Healthcare and Welfare key performance indicators FY 2025 Goals FY 2030 Goals FY 2023 performance Material matters UN SDGs Nand Ghar (Number of Nand Ghars to be completed) 29,000 29,000 4,533+ Nand Ghars built till 31 March 2023 Community Development 2.1, 2.2, 4.1, 4.2 2.3, 2.4, 4.4, 8.3 Education, Nutrition, Healthcare and Welfare (No.",
            "page_number": 117,
            "pdf_name": "AR_22033_VEDL_2022_2023_19062023161652.pdf"
        },
        {
            "document": "and safety, we communicate relevant information regarding 100% of our products and services through safety signs placed in and around substations within customer premises and public areas. We also diligently provide necessary information on regulations, laws and codes for appropriate product labeling and marketing. Notably, during FY23, we maintained complete compliance with regulations and voluntary codes pertaining to product information, labeling and marketing communication. Enhancing Customer Experience Service reliability To ensure uninterrupted power supply to our customers, we continuously monitor our vast distribution networks. Few of the initiatives we undertook include: ¥ Preventive maintenance: Preparation and execution of Annual Patrolling Programme as per IMS criteria ¥ Utilisation of new technologies to strengthen the operations, such as: − Drone patrolling for operational excellence − Voice assisted switchgear for safe RMU operation − Network management application SPINe-Spatial Patrolling Interface − Tower patrolling app deployment across all sites for centralised monitoring and digitalisation",
            "page_number": 79,
            "pdf_name": "AR_2022_2023.pdf"
        },
        {
            "document": "specified under the Consolidated FDI Policy, including sectoral limits, approval requirements and pricing guidelines, as may be applicable. Furthermore, as part of our automotive business, we supply, and have in the past supplied, vehicles to Indian military and paramilitary forces and in the course of such activities have obtained an industrial license from the Department of Industrial Policy. The Consolidated FDI policy applies different foreign investment restrictions to companies based upon the sector in which they operate. While we believe we are an automobile company by virtue of the significance of our automobile operations, in the event that foreign investment regulations applicable to the defense sector (including under the Consolidated FDI Policy) are made applicable to us, we may face more stringent foreign investment restrictions and other compliance requirements compared to those applicable to us presently, which, in turn, could materially affect our business, prospects, financial condition and results of",
            "page_number": 201,
            "pdf_name": "AR_22007_TATAMOTORS_2022_2023_12062023215502.pdf"
        },
        {
            "document": "for data centres. This helps filter out malicious traffic before it impacts the network and servers. DDoS (Distributed Denial of Service) Protection We have deployed a drone-based solution that accurately geotags vehicles in the yard against their unique identification numbers, thereby enabling accurate vehicle tracking, quick navigation and saving significant time and efforts of drivers. Drone-based vehicle inventory management Paint Defect Inspection using computer vision A SMART machine learning model was built and deployed across various plants to bring down hot firing and load testing to 10% and leading to savings of around INR 200 per engine. Smart Engine testing using AI Extensive use of digital manufacturing technologies such as simulations, analytics, 3D factory and collaboration to design and setup world class facilities and deliver best in class products. Digital manufacturing A programme institutionalised to expedite our digital transformation efforts and become a technology leader leveraging advanced analytics and automation",
            "page_number": 85,
            "pdf_name": "AR_22135_M&M_2022_2023_03072023013854.pdf"
        },
        {
            "document": "20,222 units in FY 2022-23 compared to 34,791 units in FY 2021-22. A major drop was witnessed in SAARC region (down by 62%) driven by total industry volumes softening, forex shortages and liquidity crunch in the latter half of the year. MENA and ASEAN regions witnessed 6% year on year growth in shipments. Non-SAARC markets contributed to 57% of total shipments in FY 2022-23 as compared to 34% in  Integrated Report / 2022-23 211 142-304 Statutory Reports 305-551 Financial Statements 1-141 Integrated Report FY 2021-22. Democratic Republic of Congo achieved highest ever shipments of 1,005 units in FY 2022-23; Saudi Arabia hits highest ever shipments of 1,292 units and retails of 1,401 units in FY 2022-23; Vietnam achieves highest ever retails of 998 units in FY 2022-23. TDCV, a subsidiary company engaged in the manufacturing of MHCVs and LCVs, reported an increase of 0.4%, with total units sold reaching",
            "page_number": 143,
            "pdf_name": "AR_22007_TATAMOTORS_2022_2023_12062023215502.pdf"
        },
        {
            "document": "to CPI. (b) During the year ended March 31, 2022, Jaguar Land Rover has created a provision of `428.66 crores (£43 million) in relation to customer liabilities arising from sanctions imposed against Russia by many countries, preventing the shipment of vehicles and certain parts to the market. (c) In April 2021, the Company has completed the sale of certain assets related to defence business to Tata Advanced Systems Limited (TASL) for sale consideration of `234.09 crores against the Net Assets of `231.57 crores resulting in a gain of `2.52 crores recorded as an exceptional item in the Consolidated Statement of Profit and Loss for the year ended March 31, 2023. In terms of our report attached For and on behalf of the Board For B S R & Co. LLP N CHANDRASEKARAN [DIN: 00121863] P B BALAJI Chartered Accountants Chairman Group Chief Financial Officer Firm's Registration No: 101248W/W-100022 SHIRAZ VASTANI",
            "page_number": 472,
            "pdf_name": "AR_22007_TATAMOTORS_2022_2023_12062023215502.pdf"
        },
        {
            "document": "31,515 542 (660) 1.1% (2.1%) JLR 2,22,860 1,87,697 3,482 (439) 1.6% (0.2%) Financing 4,595 4,585 1,499 2,466 32.6% 53.8% Unallocable 360 314 (158) (62) (43.8%) (19.9%) Inter-Segment eliminations (3,858) (618) (18) (90) 0.5% 14.6% Total 3,42,641 2,75,780 9,041 1,424 2.6% 0.5% In FY 2022-23, Jaguar Land Rover contributed 64% of our total automotive revenue compared to 68% in FY 2021-22 (before intra-segment elimination) and the remaining 36% was contributed by Tata and other brand vehicles and Vehicle Financing in FY 2022-23, compared to 32% in FY 2021-22. This is reflecting higher growth of Tata branded vehicles as compared to Jaguar Land Rover. Other operations Our other operations business segment mainly includes information technology services, machine tools and factory automation solutions. The following table sets forth selected data regarding our other operations for the periods indicated and the percentage change from period to period (before inter-segment eliminations). Particulars FY 2022- 23",
            "page_number": 147,
            "pdf_name": "AR_22007_TATAMOTORS_2022_2023_12062023215502.pdf"
        },
        {
            "document": "tooling resulting in superior products compared to competition. c. Development of inhouse capabilities in latest technologies for Hardware, Software, Motor, Validation, Systems Engineering, Functional Safety (A/B), Cybersecurity (L1), etc. d. Implementation of robust design processes to launch products which are safe, robust and technologically relevant such as IS26262 (A/B). e. Ability to co-develop with OEMs and continually improve products to meet changing market needs. 3. In case of imported technology (imported during the last 3 years reckoned from the beginning of the financial year) The Company has not imported technology during the last three years and therefore details including the details of technology imported, the year of import, whether the technology been fully absorbed and if not fully absorbed, areas where absorption has not taken place, and the reasons thereof are not applicable. 4. The expenditure incurred on Research and Development S. No. Particulars Amount (INR in Million) 1. Revenue",
            "page_number": 94,
            "pdf_name": "AR_22066_SONACOMS_2022_2023_24062023190637.pdf"
        },
        {
            "document": "lose the ability to remain flexible in a dynamic automotive industry, which is key to delivering innovative products and services. The loss of the services of one or more key personnel could impair our ability to implement our business strategy. Any prolonged inability to continue to attract, retain or motivate our workforce could materially and adversely affect our business, financial condition, results of operations and prospects. Any shortages of labor could lead to demands for higher wages, which could increase the labor costs of our business. We may be adversely impacted by terrorism, natural disasters and epidemics. Our products are exported to a number of geographical markets, and we plan to further expand our international operations in the future. Consequently, we are subject to various risks associated with conducting our business both within and outside our domestic market and our operations in markets abroad may be subject to terrorism, natural",
            "page_number": 193,
            "pdf_name": "AR_22007_TATAMOTORS_2022_2023_12062023215502.pdf"
        },
        {
            "document": "project management & development and operating of commercial complexes. Hospitality: This segment comprises of sale of timeshare and vacation ownership. Others: This segment mainly comprises of IT Services, after-market, defence, steel trading and processing, logistics, solar, powerol, agri business, two-wheelers, etc. The Chief Operating Decision Maker (“CODM”) evaluates the companies performance and allocates resources based on an analysis of various performance indicators by operating segments. The CODM reviews revenue and gross profit as the performance indicator for all of the operating segments. The measurement of each segment’s revenues, expenses, assets and liabilities is consistent with the accounting policies that are used in preparation of the consolidated financial statements. Segment result represents the profit before interest and tax without allocation of central administration costs, share of profit /(loss) of associates and joint ventures. 41. Related party disclosures (contd.) (b) The related party transactions are as under: (contd.)  392 MAHINDRA &",
            "page_number": 447,
            "pdf_name": "AR_22135_M&M_2022_2023_03072023013854.pdf"
        },
        {
            "document": "Securities 0.85 3.51 Interest Accrued on Finance Lease Receivable 5.90 6.29 Interest Accrued on Loans to Related Parties 8.36 8.27 Unsecured, considered doubtful Interest Accrued on Inter-corporate/Bank Deposits 1.31 1.40 105.81 90.55 Less: Provision for Doubtful Interest 1.31 1.40 104.50 89.15 (iii) Receivables under Service Concession Agreement 4.66 4.43 (iv) Others Unsecured, considered good Dividend Receivable 1.65 1.78 Derivative Contract (at FVTPL) 115.07 5.06 Receivable on sale of Property, Plant and Equipments 0.78 2.69 Insurance Claims Receivable 0.03 1.55 Government Grants Receivables 16.67 41.70 Recoverable from consumers 27.41 98.68 Other Advances 232.52 216.47 Balances with Banks: (Refer Note below) In Deposit Accounts (with remaining maturity of less than twelve months) 151.00 1.62 Unsecured, considered doubtful Other Receivables 3.58 3.45 548.77 373.00 Less: Allowances for Doubtful Receivables 3.58 3.45 545.19 369.55 Total 688.30 501.45 Note: Balances with Banks held as Margin Money Deposits against Guarantees. 13. Tax Assets As at March",
            "page_number": 443,
            "pdf_name": "AR_2022_2023.pdf"
        },
        {
            "document": "FY 2021-22. Compared to the prior year, wholesale volumes were higher in all markets led by Overseas 14.2%, Europe 14.1%, UK 8.7%, China 8.5% and North America 2.9%. This increase was driven by the gradual improvement in the supply of semiconductor during the year though constraints on the supply of commercial semiconductor was not completely removed. Given these restrictions on availability of [our products], we have been able to increase our revenue per unit reflecting the prioritisation of higher margin products giving us a strong mix, particularly in the Range Rover and Defender families. Jaguar Land Rover’s performance on a retail basis: Retail sales for FY 2022-23 were 3,54,662 down 5.8% compared to FY 2021-22. Compared to the prior year, retail volumes were higher in the UK 0.9% and down in North America 15.1%, Europe 0.5%, China 5.0% and Overseas 6.3%. This reduction reflected the impact of the chip shortages",
            "page_number": 145,
            "pdf_name": "AR_22007_TATAMOTORS_2022_2023_12062023215502.pdf"
        },
        {
            "document": "constraints that impact on Agile squads’ ability to deliver value. Our focus has been on simplifying governance, decision‑making processes, as well as increasing the speed with which impediments are resolved to streamline our products’ time to market. In Delivered Cost per Car, we have continued building on successful cost reduction initiatives across key vehicle programmes. Through technical and feature optimisation, we have driven material cost reduction changes without disrupting programme delivery. The delivery of cost initiatives approved in FY 2022‑23 will continue in FY 2023‑24 to mitigate a reduction in returns on legacy carlines. In Supply Chain, we have continued to deliver end‑to‑end efficiencies and increased operating stability. Throughout FY 2022‑23, we significantly improved our semiconductor supply, with intensive efforts on risk identification and mitigation. Throughout next year, our focus will be on improving operating transparency, stability, and resilience through new technologies with our external partners. In Customer and Market",
            "page_number": 37,
            "pdf_name": "AR_22007_TATAMOTORS_2022_2023_12062023215502.pdf"
        },
        {
            "document": "9,222.83 10,042.76 Fixed rate Borrowings (including current maturities) 13,021.98 15,152.63 13,056.36 15,169.26 Derivative Contracts (Net) 17.43 13.12 17.43 13.12 Other Financial Liabilities 4,418.78 2,274.39 4,418.78 2,274.39 28,666.04 31,562.79 28,700.42 31,579.42 # other than investments in subsidiaries, associates and joint ventures accounted at cost in accordance with Ind AS 27 ‘Separate Financial Statements’. Note: Certain unquoted investments are not held for trading, instead they are held for medium or long term strategic purpose. Upon the application of Ind AS 109 'Financial Instruments', the Company has chosen to designate these investments in equity instruments as at FVTOCI as the management believe this provides more meaningful presentation for medium and long term strategic investments, then reflecting changes in fair value immediately in profit or loss. The management assessed that the fair value of cash and cash equivalents, other balances with banks, trade receivables, derivative contracts, loans, unbilled revenues, trade payables, other financial assets",
            "page_number": 367,
            "pdf_name": "AR_2022_2023.pdf"
        },
        {
            "document": "2,378.48 3,397.18 74.92 18.31 56.61 56.61 - - 100.00 72 Jaguar Land Rover North America, LLC. (subsidiary w.e.f June 2, 2008) USA USD 82.18 328.73 5,081.56 14,835.93 9,425.64 54,531.92 1,003.12 257.89 745.23 745.23 (4.00) - 100.00 73 Jaguar Land Rover Japan Limited (subsidiary w.e.f October 1, 2008) Japan JPY 0.62 29.67 312.73 1,780.31 1,437.91 3,327.70 68.81 (1.62) 70.43 70.43 - - 100.00 74 Jaguar Land Rover Canada, ULC (subsidiary w.e.f June 2, 2008) Canada CAD 60.67 - 262.75 1,646.21 1,383.46 4,999.59 71.73 27.07 44.66 44.66 - - 100.00  Integrated Report / 2022-23 550 (` in crores) Sr. No Subsidiary Country Reporting currency Exchange Rate Share capital (incl. advances towards capital where applicable) Reserves and Surplus Total Assets Total Liabilities Turnover Profit/ (Loss) Before Tax Tax Expense/ (Credit) Profit/(Loss) after tax Profit/ (Loss) for the period/ year * Proposed dividend and tax thereon Investments (except in case of investment in",
            "page_number": 482,
            "pdf_name": "AR_22007_TATAMOTORS_2022_2023_12062023215502.pdf"
        },
        {
            "document": "and loss (Charged) / credited to other compre- hensive income Exchange gain/ (loss) on translation of foreign operations As at 31 March, 2022 Provision for employee benefits (including Voluntary Retirement Scheme) 35.96 (35.85) 0.09 (0.07) - 0.13 Allowance for receivables, loans and advances 96.23 (77.92) 7.02 - - 25.33 Provision for contingencies and claims 8.55 (8.04) - - - 0.51 Unpaid statutory liabilities 3.31 (3.31) - - - - Government Grant 1.70 (1.70) - - - - Estimated Loss on Projects 1.15 (0.98) 0.79 - - 0.96 Unutilised brought forward loss and unabsorbed depreciation 6.79 - (6.41) - - 0.38 MAT credit entitlement 13.58 - 2.73 - - 16.31 Free Maintenance services 6.06 (6.06) - - - - Others 0.91 (0.86) 0.33 - - 0.38 Deferred Tax Assets 174.24 (134.72) 4.55 (0.07) - 44.00 12. DEFERRED TAX (Contd.)  CORPORATE OVERVIEW STATUTORY REPORTS FINANCIAL STATEMENTS Annual Report 2022-23 247 `",
            "page_number": 250,
            "pdf_name": "AR_21928_VOLTAS_2022_2023_26052023210412.pdf"
        },
        {
            "document": "it is derecognised.  Integrated Report / 2022-23 440 Notes forming part of Consolidated Financial Statements (B) Property, plant and equipment (` in crores) Owned assets Given on lease Land Buildings Plant and equipment Furniture and fixtures Vehicles Computers Heritage Assets Land Buildings Plant and equipment Vehicles Total Cost as at April 1, 2022 7,456.81 28,644.08 147,024.91 1,815.70 411.18 2,933.15 301.66 21.58 35.60 5.16 142.13 188,791.96 Additions - 721.02 5,265.88 72.56 30.84 333.07 - - - 0.77 24.17 6,448.31 Additions on account of Ford plant acquisition (refer note below) 331.92 176.25 - - - - - 45.08 74.46 - - 627.71 Assets classified as held for sale (95.57) (520.13) - - - - (18.65) - - - - (634.35) Disposal/Adjustments - (146.78) (2,864.76) (18.48) (74.65) (19.64) (37.97) - (4.02) (0.19) (37.63) (3,204.12) Currency translation differences 63.80 696.92 2,781.32 39.51 4.18 62.85 0.24 - - - - 3,648.82 Cost as at",
            "page_number": 372,
            "pdf_name": "AR_22007_TATAMOTORS_2022_2023_12062023215502.pdf"
        },
        {
            "document": "(29.55) (29.55) - - 100.00 56 Jaguar Land Rover Ireland (Services) Limited Ireland GBP 101.64 0.00 252.59 288.53 35.94 392.81 85.99 8.45 77.54 77.54 - - 100.00 57 Limited Liability Company Jaguar Land Rover (Russia) (incorporated on 25-5-2008) (subsidiary w.e.f May 15, 2009) Russia RUB 1.06 5.13 430.29 746.18 310.76 274.61 (74.94) 49.19 (124.13) (124.13) - - 100.00 58 Jaguar Land Rover (China) Investment Co Ltd (previously Jaguar Land Rover Automotive Trading (Shanghai) Co. Ltd ) (subsidiary w.e.f June 2, 2008) China CNY 11.96 80.15 17,614.75 23,968.23 6,273.32 32,067.56 4,008.51 962.90 3,045.61 3,045.61 - - 100.00 59 Shanghai Jaguar Land Rover Automotive Service Co. Ltd (subsidiary w.e.f March 10, 2014) China CNY 11.96 19.14 (26.34) 13.44 20.64 13.77 0.99 0.05 0.94 0.94 - - 100.00 60 Jaguar Land Rover Colombia SAS (subsidiary w.e.f August 22, 2016) Columbia COP 0.02 39.78 (7.45) 32.39 0.06 - 5.46 - 5.46 5.46 - -",
            "page_number": 481,
            "pdf_name": "AR_22007_TATAMOTORS_2022_2023_12062023215502.pdf"
        },
        {
            "document": "5,159.74 2,041.51 983.43 2,496.48 5,521.42 5,521.42 Financial liabilities Borrowings - - 285.28 285.28 285.28 - - 126.04 126.04 126.04 Lease Liabilities - - 29.73 29.73 29.73 - - 13.75 13.75 13.75 Trade payables - - 2,209.79 2,209.79 2,209.79 - - 2,682.02 2,682.02 2,682.02 Other financial liabilities 0.25 - 128.98 129.23 129.23 0.33 - 117.79 118.12 118.12 0.25 - 2,653.78 2,654.03 2,654.03 0.33 - 2,939.60 2,939.93 2,939.93 *The above Investments does not include equity investments in subsidiaries, associates and joint ventures which are carried at costs and hence are not required to be disclosed as per Ind AS 107 “Financial Instruments Disclosures”. Management has assessed that Cash and cash equivalents, Other balances with banks, Loans, Trade receivables, Other financial assets, Borrowings, Lease liabilities, Trade payables and Other financial liabilities carried at amortised cost approximate their carrying amounts largely due to the short-term maturities of these instruments. Abbreviations : FVTPL - Fair",
            "page_number": 383,
            "pdf_name": "AR_21928_VOLTAS_2022_2023_26052023210412.pdf"
        },
        {
            "document": "/ services for execution of contracts 77.30 - 6.85 - 0.03 - - - 84.18 2021-22 113.32 - 19.59 - - - - - 132.91 16 2022-23 Deputation Charges paid 4.07 - 3.38 - - - - - 7.45 2021-22 - - - - - - - - - 17 2022-23 Impairment in value of investment - - - - - - - - - 2021-22 - - 0.25 - - - - - 0.25 18 2022-23 Security Deposit Refunded - - - - - - - - - 2021-22 - - - - 4.48 - - - 4.48 19 2022-23 Other Expenses- Recovery of expenses 21.39 - 39.44 - 0.28 - - - 61.11 2021-22 13.11 - 36.30 0.15 1.13 - - - 50.69 20 2022-23 Other Expenses- Reimbursement of expenses 3.08 - 8.20 0.13 18.08 - - - 29.49 2021-22 1.84 - 0.20 - 14.82 - - -",
            "page_number": 380,
            "pdf_name": "AR_21928_VOLTAS_2022_2023_26052023210412.pdf"
        },
        {
            "document": "tools and technologies developed by the Digital team have underpinned critical operations in FY 2022‑23. Notable examples include a suite of tools to support the launch of our vehicles built on the modular longitudinal architecture (MLA), as well as enabling data‑driven decision making. Our focus remains on modernising our digital infrastructure, as well as staying safe from cyber‑attacks. In Agile Organisation and Culture, our priority has been on unfolding our Purpose and Creators’ Code across the organisation. We launched our “Reimagine Leadership” programme which offered numerous learning interventions such as practical empowerment and team engagement to support our cultural transformation. To enable delivery of our products on time, to cost and quality, we also transitioned six programme delivery portfolios into agile ways of working whereby 8,000 people are working in empowered squads and have adopted core Agile procedures. Commitment to carbon net zero In Sustainability, in FY 2022‑23, we successfully",
            "page_number": 38,
            "pdf_name": "AR_22007_TATAMOTORS_2022_2023_12062023215502.pdf"
        },
        {
            "document": "to check the safety and quality of services/design/actual physical work • Use of a reputed international agency for Geotech modelling and technical support, wherever required Access to capital Impact: The Group may be unable to meet its payment obligations when due or may be unable to borrow funds in the market at an acceptable price to fund actual or proposed commitments. A sustained adverse economic downturn and/or suspension of its operations in any business, affecting revenue and free cash flow generation, may cause stress on the Company's ability to raise financing at competitive terms. • Focussed team continues to work on proactive refinancing initiatives with an objective to contain cost and extend tenure • Team is actively building the pipeline for long-term funds for near-to-medium term requirements, both for refinancing and growth capex • Track record of good relations with banks, and of raising borrowings in the last few years",
            "page_number": 97,
            "pdf_name": "AR_22033_VEDL_2022_2023_19062023161652.pdf"
        },
        {
            "document": "2022-23 FY 2021-22 Processing charges 1,786 1,406 27.0% 0.5% 0.5% Stores, spare parts and tools consumed 1,610 1,446 11.3% 0.5% 0.5% Freight, transportation, port charges, etc. 7,548 6,278 20.2% 2.2% 2.3% Power and fuel 2,513 2,178 15.4% 0.7% 0.8% Warranty charges and Product Liabilities 10,497 8,775 19.6% 3.0% 3.2% Publicity 6,035 4,864 24.1% 1.7% 1.7% Information technology/computer expenses 3,970 3,544 12.0% 1.1% 1.3% Provision and write off of sundry debtors, vehicle loans and advances (net) 2,086 1,427 46.2% 0.6% 0.5% Engineering expenses 4,401 3,031 45.2% 1.3% 1.1% MTM (gain)/loss on commodity derivatives 1,415 (1,371) (203.2%) 0.4% (0.5%) Works operation and other expenses 19,926 15,556 27.9% 5.8% 5.6% Other Expenses 61,786 47,134 31.0% 17.9% 16.9% 1. Freight and transportation expenses increased by 20.2% to `7,548 crores in FY 2022-23. This is partially offset favourable currency translation of `313 crores from GBP to INR. At Jaguar Land Rover freight and transportation expenses",
            "page_number": 151,
            "pdf_name": "AR_22007_TATAMOTORS_2022_2023_12062023215502.pdf"
        },
        {
            "document": "Government authorities and capital advances. Contract assets represent contract revenues recognized in Projects business, in excess of certified bills. In Projects business, revenues are recognized on the basis of the percentage of completion method, in line with the accounting standards.  corporate overview statutory reports financial statements Annual Report 2022-23 109 (f) LiAbiLitiEs AnD ProVisions ` in crores 2022-23 2021-22 change change% Current liabilities 4,620 4,056 564 14 Non-current liabilities 166 153 13 8 Current liabilities include contract liabilities, borrowings, trade payables, short-term provisions, income tax liabilities and other current liabilities. Non-current liabilities consist of long-term provisions, trade payables and deferred tax liabilities. Provisions (long-term and short-term) are towards employee benefits – gratuity, pension, medical benefits and compensated absences, trade guarantees and contingencies, among others. finAnciAL PErformAncE: stAnDALonE financial performance as a measure of operational performance: (A) Gross sALEs/incomE from oPErAtions (sEGmEnt rEVEnUEs) ` in crores 2022-23 2021-22 change change%",
            "page_number": 112,
            "pdf_name": "AR_21928_VOLTAS_2022_2023_26052023210412.pdf"
        },
        {
            "document": "be reclassified subsequently to statement of profit and loss.  CORPORATE OVERVIEW STATUTORY REPORTS FINANCIAL STATEMENTS Annual Report 2022-23 357 Equity instruments fair value through other comprehensive income : The Company has elected to recognise changes in the fair value of certain investments in equity securities in other comprehensive income. These changes are accumulated within the FVTOCI equity investments reserve within equity. The Company transfers amounts from this reserve to retained earnings when the relevant equity securities are derecognised. Retained Earnings : The balance in the Retained Earnings primarily represents the surplus after payment of dividend and transfer to reserves. 23 CONTRACT LIABILITIES (NON-CURRENT) ` in crores As at 31 March, 2023 As at 31 March, 2022 Unexpired service contracts 6.33 3.51 Total Contract liabilities (Non-Current) 6.33 3.51 24 BORROWINGS (AT AMORTISED COST) (NON-CURRENT) ` in crores As at 31 March, 2023 As at 31 March, 2022 Unsecured Term Loans",
            "page_number": 360,
            "pdf_name": "AR_21928_VOLTAS_2022_2023_26052023210412.pdf"
        },
        {
            "document": "the subsidiaries) % of shareholding 75 Jaguar e Land Rover Brasil Indústria e Comércio de Veículos LTDA (subsidiary w.e.f June 2, 2008) Brazil BRL 16.25 1,001.82 (499.72) 2,150.00 1,647.91 3,053.58 133.15 4.02 129.12 129.12 - - 100.00 76 Jaguar Land Rover Belux N.V. (subsidiary w.e.f June 2, 2008) Belgium EUR 89.47 11.18 148.56 1,482.26 1,322.52 4,116.75 43.82 12.02 31.80 31.80 1.85 - 100.00 77 Jaguar Land Rover Nederland BV (subsidiary w.e.f June 2, 2008) Netherlands EUR 89.47 0.41 82.62 824.91 741.88 2,112.65 25.58 6.46 19.11 19.11 (3.30) - 100.00 78 Jaguar Land Rover (South Africa) (Pty) Limited (subsidiary w.e.f June 2, 2008) South Africa ZAR 4.62 0.00 249.91 1,290.03 1,040.12 2,151.39 131.22 37.76 93.46 93.46 - - 100.00 79 Jaguar Land Rover Singapore Pte. Ltd (incorporated w.e.f November 25,2015) (subsidiary w.e.f November 25, 2015) Singapore SGD 61.81 4.64 40.47 146.63 101.53 242.54 17.82 3.78 14.03 14.03 - - 100.00 80",
            "page_number": 482,
            "pdf_name": "AR_22007_TATAMOTORS_2022_2023_12062023215502.pdf"
        },
        {
            "document": "40% Market share 39.4% Q4F20 40.7% Q4F23 l Leadership, Asset quality, Tech and Data l Transformation underway l Early wins in large deals l Succession plan in place l Margin transformation to commence in F24 GNPA* 8.4% Q4F20 4.5% Q4F23 * Refers to gross stage 3 delinquent contracts Transform 14 MeraKisan  COMPANY OVERVIEW RISE TO CREATE VALUE RISE TO BE FUTURE READY RISE FOR A MORE EQUAL WORLD CORPORATE INFORMATION STATUTORY REPORTS FINANCIAL STATEMENTS ESTABLISHING THE GROWTH GEMS þ Robust launch pipeline with 9 launches; 4,000+ Crs GDV acquired þ Customer & inventory adds, curated customer experience þ Integrated logistics play with multiple acquisitions Progress made so far Valuation¹ ($ Min) FY20 FY23 Revenue ($ Mn) Unlock Emerging Growth Gems þ 67% market share in 3W EV; IFC investment þ OTPPF investment to accelerate scale-up Growth Mindset þ Pivot to decarbonising of Mobility and Energy þ Retail scale-up across",
            "page_number": 70,
            "pdf_name": "AR_22135_M&M_2022_2023_03072023013854.pdf"
        },
        {
            "document": "also help ensure that: i. All social incidents are investigated and closed in a systematic manner ii. The site takes mitigative and pre-emptive action on any operational elements that may cause harm to the community iii. There are strategies in place to ensure local procurement and local employment iv. There is a coordinated stakeholder engagement strategy that involves the relevant internal teams such as CSR, External Affairs, and Security among others v. All social incidents are investigated and closed in a systematic manner To further enhance our performance and governance on security matters, we have established a security Community of Practice (CoP). This CoP has been tasked to implement the recommendations of the Voluntary Principles on Security and Human Rights (VPSHR), which are recognised as global best practices for managing private and public security forces. Highlights for FY 2023: • Local procurement1 improved to 40% from 35% YoY • Social",
            "page_number": 122,
            "pdf_name": "AR_22033_VEDL_2022_2023_19062023161652.pdf"
        },
        {
            "document": "258.50 254.50 Prepaid taxes* 258.50 254.50 * Includes amount paid under protest of ` 24.48 million (31 March 2022: ` 24.48 million) 8 OTHER ASSETS As at 31st March 2023 As at 31st March 2022 Non current Prepaid expenses 1.69 1.01 Un-adjusted consideration for revenue contract 33.40 41.83 Capital advances 357.67 506.98 Total other assets- non current 392.76 549.82 Current Prepaid expenses 97.62 85.77 Loans and advances to employees 4.06 2.94 Advance to suppliers for goods and services 172.75 82.10 Balance with government authorities 225.26 338.65 Un-adjusted consideration for revenue contract 11.21 14.24 Other assets 99.41 139.46 Less: Allowance for doubtful advances (20.38) (20.38) Total other assets- current 589.93 642.78 FINANCIAL STATEMENTS STATUTORY REPORTS CORPORATE OVERVIEW 197  (Figures in Million `, unless stated otherwise) Notes Summary of significant accounting policies and other explanatory information to the standalone financial statements for the year ended 31st March 2023 9 INVENTORIES As",
            "page_number": 170,
            "pdf_name": "AR_22066_SONACOMS_2022_2023_24062023190637.pdf"
        },
        {
            "document": "multiple formats þ New launches, distribution scale up and exports Emerging <100G 734 +630 Mn <200 290 +90 Mn 120 670 +550 Mn 230 660 +430 Mn 200 320 +120 Mn 182 514 +332 Mn 50 141 +91 Mn 56 84 +28 Mn 1. Closing value as of 31>? March for corresponding years; 2. F20 Valuation based on rough estimate of Jeeto and 3 Wheelers ICE portfolio; 3. Investment by a wholly owned subsidiary of Ontario Teachers’ Pension Plan Board “OTPP” Note: For FY20: $1 = INR 74.1; For FY23: $1 = INR 81.7 On track to achieve target Through our commitment to Reigniting Value Creation, we successfully steered the Group to reach an ROE of 19.9% in F23. The PAT at consolidated level has seen a significant growth as can be seen from the following chart. 66 4,667 FY02 FY14 FY21 +43% -5% FY23 +75% 10,282 ^ 3,347 *",
            "page_number": 70,
            "pdf_name": "AR_22135_M&M_2022_2023_03072023013854.pdf"
        },
        {
            "document": "Adjustments for: Depreciation and amortisation expense 24,860.36 24,835.69 Allowances for finance receivables 2,039.15 1,307.59 Provision for trade and other receivables 80.63 151.26 Inventory write-down (net) 723.21 125.34 Reversal for costs of closure of operations of a subsidiary company - (3.32) Discounting of warranty and other provisions (140.76) - Write off/provision for tangible/intangible assets (including under development) (net) 229.95 - Reversal of Impairment in subsidiaries (214.39) (104.42) Reversal for onerous contracts and related supplier claims (61.03) - Defined benefit pension plan amendment past service credit (1,495.07) - Other exceptional items (61.99) - Accrual for share-based payments 30.03 18.05 Marked-to-market gain on investments measured at fair value through profit or loss (93.27) - Loss on sale of assets (including assets scrapped/written off) (net) 354.96 94.19 Profit on sale of investments (net) (303.44) (266.56) Share of (profit)/loss of joint ventures and associates (net) (336.38) 74.06 Tax expense (net) 704.06 4,231.29 Finance costs and",
            "page_number": 358,
            "pdf_name": "AR_22007_TATAMOTORS_2022_2023_12062023215502.pdf"
        },
        {
            "document": "2022-23 336 Notes forming part of Financial Statements (` in crores) As at March 31, 2022 Up to 1 year 1-2 years 2-3 years More than 3 years Total Projects in progress Project 1 97.81 - - - 97.81 Other Projects* 18.76 - - - 18.76 Projects temporarily suspended Project 1 - - - 61.31 61.31 Project 2 - - - 209.04 209.04 116.57 - - 270.35 386.92 *Individual projects less than ` 50 crores have been clubbed together in other projects. Original plan is considered as that plan which is approved and on the basis of which implementation progress is evaluated. Such original plan includes management’s estimates and assumptions w.r.t future business, economy / industry and regulatory environments. 6. Investments in subsidiaries, joint ventures and associates measured at cost - non-current (a) Accounting policy Investments in Subsidiaries, Joint ventures and Associates are carried at cost less accumulated impairment losses,",
            "page_number": 268,
            "pdf_name": "AR_22007_TATAMOTORS_2022_2023_12062023215502.pdf"
        },
        {
            "document": "be adjusted for exceptional expenses pertaining to diligence work for NOVELIC acquisition. Adjusted PAT thus grew by 24% to INR 3,978 million in FY 2022-23. We generated INR 5,347 million as cash from operations, of which INR 3,351 million were deployed in capex. During FY 2022-23, noteworthy order wins from our new products included orders to supply, EDL (Electronically locking differential) for an Electric SUV and Differential Assembly along with intermediate gears and input shaft for a Class 4 Electric CV. For the long-term investors, I believe these should be seen as more than mere order wins since these demonstrate the Company's ability to customise and build new products to the needs of the customers, providing longevity to the Company's growth potential. We also announced a technology licensing agreement with a UK-based company Equipmake for the manufacture and sale of drive motors, inverters and drive trains in the power range",
            "page_number": 13,
            "pdf_name": "AR_22066_SONACOMS_2022_2023_24062023190637.pdf"
        },
        {
            "document": "of medium and heavy commercial vehicles in FY 2022-23 compared to FY 2021-22. We sold 1,22,440 units in FY 2022- 23, compared to 88,191 units in FY 2021-22 in this segment, a growth of 38.8%. The quarter-on-quarter improvement was observed, due to increase in infrastructure projects, housing construction and the mining segments in India. ILCVs in India Our sales in the ILCVs in India increased to 54,636 units in FY 2022-23, compared to the 53,847 units in FY 2021-22, representing an increase of 1.5%. SCVs and Pickups in India Our sales in SCVs and Pickups segment in India increased by 9.6% from 1,65,822 units in FY 2021-22 to 1,81,715 units in FY 2022- 23. Among all segments in commercial vehicles, the SCV and pickup category has experienced increased demand from e-commerce players primarily due to the necessity for last- mile distributions to retail consumers by such companies. CV Passenger Vehicles",
            "page_number": 142,
            "pdf_name": "AR_22007_TATAMOTORS_2022_2023_12062023215502.pdf"
        },
        {
            "document": "(net) 3,963.25 (2,968.54) Disposal of subsidiaries (net of cash disposed) 19.37 (98.45) Investment in government securities (2,839.87) (1,228.21) Investments - others (50.00) (39.71) Proceeds from sale of investments in other companies 59.33 103.55 Proceeds from sale of investments in government securities 2,872.88 - Proceeds from disposal of defence business - 234.09  Integrated Report / 2022-23 427 142-304 Statutory Reports 305-551 Financial Statements 1-141 Integrated Report Consolidated Cash Flow Statement (` in crores) Particulars Year ended March 31, 2023 Year ended March 31, 2022 Interest received 973.44 652.94 Purchase of other assets with a view to resale (298.20) - Dividend received 46.42 32.01 Dividend received from equity accounted investees 21.69 - Deposit/restricted deposits with financial institution (2,169.57) (600.00) Realisation of deposit with financial institution 1,469.59 1,300.00 Deposits/restricted deposits with banks (17,723.34) (13,203.08) Realisation of deposits/restricted deposits with banks 15,497.79 25,978.60 Net cash used in investing activities (16,804.16) (4,775.12) Cash flows",
            "page_number": 359,
            "pdf_name": "AR_22007_TATAMOTORS_2022_2023_12062023215502.pdf"
        },
        {
            "document": "(0.76) (41.96) 0.63 3.17 (1.19) (2.01) 0.17 1.16 (5) Weathermaker FZE (formerly known as Weathermaker Limited) Dubai, United Arab Emirates (Re- domiciliation from earlier Isle of Man) 100.00 0.53 28.96 (1.06) (5.37) 0.45 0.77 (0.68) (4.60) (6) Voltas Qatar W.L.L. Qatar 97.00 3.09 170.19 5.75 29.11 (0.17) (0.28) 4.27 28.83 (7) Universal MEP Projects Pte Limited (w.e.f. 04 August, 2021) Singapore 100.00 * (0.05) (0.01) (0.05) * * (0.01) (0.05) (c ) Non-controlling interests in all subsidiaries (0.69) (38.08) 0.38 1.91 0.97 1.64 0.53 3.55 50 ADDITIONAL INFORMATION AS REQUIRED BY PARAGRAPH 2 OF THE GENERAL INSTRUCTIONS FOR PREPARATION OF CONSOLIDATED FINANCIAL STATEMENTS TO SCHEDULE III TO THE COMPANIES ACT, 2013 (Contd.)  Voltas Limited 278 Name of the Entity Country of Incorporation Ownership in % Net assets (total assets minus total liabilities) Share of profit or (loss) Share in other comprehensive income Share in total comprehensive income As %",
            "page_number": 281,
            "pdf_name": "AR_21928_VOLTAS_2022_2023_26052023210412.pdf"
        },
        {
            "document": "the Company's interest in equity accounted investees: (` in crores) As at March 31, 2023 As at March 31, 2022 Carrying amount in immaterial associates 1,329.81 1,159.81 Carrying amount in material joint venture 3,335.73 3,179.67 Carrying amount in immaterial joint ventures 10.12 9.91 Total 4,675.66 4,349.39 (d) Summary of Company’s share of profit/(loss) in equity accounted investees: (` in crores) Year ended March 31, 2023 Year ended March 31, 2022 Share of profit/(loss) in immaterial associates 192.03 131.40 Share of profit/(loss) in material joint venture 142.81 (184.80) Share of profit/(loss) on other adjustments in material joint venture 1.54 (20.66) Share of profit/(loss) in immaterial joint ventures - - 336.38 (74.06) (` in crores) Year ended March 31, 2023 Year ended March 31, 2022 Share of other comprehensive income in immaterial associates 6.29 4.77 Currency translation differences-immaterial associates (6.63) 0.37 Currency translation differences-material joint venture 11.71 217.65 Currency translation differences-immaterial joint",
            "page_number": 385,
            "pdf_name": "AR_22007_TATAMOTORS_2022_2023_12062023215502.pdf"
        },
        {
            "document": "Reimagine we will deliver double‑digit EBIT margins by 2026 and be net cash positive by FY 2025. We will achieve our Science Based Target initiative (SBTi) carbon reduction targets in 2030 and carbon net zero goals by 2039, and always strive to exceed our clients’ expectations. As part of our modern luxury vision, we have announced the creation of a House of Brands organisation, to amplify the unique DNA of each of JLR’s celebrated British automotive brands ‑ Range Rover, Defender, Discovery, and Jaguar. This allows each brand to project their individual purpose, desirability, and personality. The House of Brands will also Integrated Report / 2022-23 66 Integrated Report / 2022-23 67 Jaguar Land Rover 142-304 Statutory Reports 305-551 Financial Statements 1-141 Integrated Report  provide clarity and differentiation for our clients, to create emotional connection. Two new product additions to the House this year were New Range Rover Sport",
            "page_number": 37,
            "pdf_name": "AR_22007_TATAMOTORS_2022_2023_12062023215502.pdf"
        },
        {
            "document": "STATEMENTS STATUTORY REPORTS CORPORATE OVERVIEW 209  (Figures in Million `, unless stated otherwise) Notes Summary of significant accounting policies and other explanatory information to the standalone financial statements for the year ended 31st March 2023 28 OTHER EXPENSES For the year ended 31st March 2023 For the year ended 31st March 2022 Consumption of stores, spares and tool 1,269.51 1,012.63 Power and fuel 647.93 479.49 Freight, clearing and forwarding charges 579.19 378.21 Packing material 350.01 309.52 Sub contracting cost 852.39 747.85 Rent (refer note 43) 20.35 31.43 Repairs and maintenance - plant and machinery 365.53 300.63 Repair and maintenance - buildings 27.34 16.01 Repair and maintenance - others 139.16 109.21 Manpower hiring on contract 478.19 388.71 Legal and professional charges (refer note (a) below) 238.55 159.19 Rates and taxes 9.51 7.96 Insurance 56.03 52.96 Travelling, conveyance and vehicle expenses 172.82 117.45 Communication and stationery expenses 26.58 22.63 Security charges",
            "page_number": 182,
            "pdf_name": "AR_22066_SONACOMS_2022_2023_24062023190637.pdf"
        },
        {
            "document": "Furniture and Fixtures Aircraft Vehicles Total Balance as at 1st April, 2021 ........................................ 273.57 3,455.73 16,326.97 193.29 247.28 57.22 468.30 21,022.36 Acquisitions through business combinations [Refer note 44 (B)] .............................................................. 8.36 40.71 207.00 2.75 2.10 — 15.31 276.23 Additions/Transfer from CWIP during the year ..... 59.33 806.66 2,790.61 12.72 11.70 — 27.16 3,708.18 Disposals/Transfer during the year .............................. 3.07 3.08 208.86 4.75 5.70 — 76.74 302.20 Balance as at 31st March, 2022 ................................. 338.19 4,300.02 19,115.72 204.01 255.38 57.22 434.03 24,704.57 Balance as at 1st April, 2022 ........................................ 338.19 4,300.02 19,115.72 204.01 255.38 57.22 434.03 24,704.57 Additions/Transfer from CWIP during the year ..... 5.55 235.30 2,661.78 17.61 8.60 — 24.83 2,953.67 Disposals during the year .................................................... 12.95 35.05 169.64 6.10 10.28 — 89.49 323.51 Reclassified as held for sale ............................................... 6.84 47.18 492.87 0.99 1.22 — 1.14 550.26 Balance as at 31st March, 2023 ................................. 323.95 4,453.09 21,114.99 214.53 252.48",
            "page_number": 306,
            "pdf_name": "AR_22135_M&M_2022_2023_03072023013854.pdf"
        },
        {
            "document": "maintenance modules. Learning and development Skill upgradation Skill upgradation is a priority for us, and we conducted various skill training sessions in the current fiscal year, empowering 90% of the employees across technical, compliance, and behavioural skill sets. Performance review We conduct regular performance and career development reviews for all employees, recommending annual increments and incentives to the Nomination and Remuneration Committee. Permanent employees receive promotions and increments based on business and individual performance, including variable pay. For the permanent workers under the collective bargaining scheme, which is negotiated every 4 years, the salaries and enhanced as per the negotiated norms. 90% of total employees participated in these training sessions in FY 2022-23 Social – People 50 Sona Comstar Annual Report 2022-23 FINANCIAL STATEMENTS STATUTORY REPORTS CORPORATE OVERVIEW 51  Creating a lasting impact on the society On the business front, we are creating a positive impact on the environment",
            "page_number": 29,
            "pdf_name": "AR_22066_SONACOMS_2022_2023_24062023190637.pdf"
        },
        {
            "document": "Up to 1 year 1-2 years 2-3 years More than 3 years Total Projects in progress Project 1 - - - - - Various Projects* 1,431.13 23.42 - - 1,454.55 Projects temporarily suspended 1,431.13 23.42 - - 1,454.55 As at March 31, 2022 Up to 1 year 1-2 years 2-3 years More than 3 years Total Projects in progress Project 1 2,241.40 - - - 2,241.40 Project 2 844.68 - - - 844.68 Project 3 731.03 - - - 731.03 Various Projects* 1,265.03 4.18 - - 1,269.21 Projects temporarily suspended Various Projects* - 6.52 - 270.36 276.88 5,082.14 10.70 - 270.36 5,363.20 *Individual projects less than 10% of total Intangible assets under development have been clubbed together in various projects. Original plan is considered as that plan which is approved and on the basis of which implementation progress is evaluated. Such original plan includes management’s estimates and assumptions w.r.t future",
            "page_number": 380,
            "pdf_name": "AR_22007_TATAMOTORS_2022_2023_12062023215502.pdf"
        },
        {
            "document": "particulars of contracts/ arrangements entered into by the Company with related parties referred to in sub-section (1) of Section 188 of the Companies Act, 2013 including certain arm’s length transactions under third proviso thereto. 1. Details of contracts or arrangements or transactions not at arm’s length basis: The Company has not entered into any contract or arrangement or transaction with its related parties which is not at arm’s length during financial year 2022-23. 2. Details of material contracts or arrangement or transactions at arm’s length basis: (a) Name(s) of the related party and nature of relationship: Universal MEP Projects & Engineering Services Limited (UMPESL), wholly-owned subsidiary of the Company. (b) Nature of contracts/arrangements/transactions: During the year, the Business Transfer Agreement (BTA) earlier executed in March 2021 for transfer of domestic B2B businesses to UMPESL on a slump sale basis, was consummated effective 1 August, 2022. ANNEXURE V FORM NO. AOC-2",
            "page_number": 146,
            "pdf_name": "AR_21928_VOLTAS_2022_2023_26052023210412.pdf"
        },
        {
            "document": "and Components 115.06 161.94 (b) Stock-in-trade 19.66 31.83 Total goods-in-transit 134.72 193.77 Footnote : Provision / (reversal) for write-down on value of inventory recognised in statement of profit and loss (0.61) (9.72) 15 CONTRACT ASSETS (CURRENT) (UNSECURED) ` in crores As at 31 March, 2023 As at 31 March, 2022 Amount due from customers under construction contracts 1,111.62 863.28 Less: Impairment Allowance 133.56 114.96 Contract assets (Current) (Net) 978.06 748.32 Footnotes : (1) Break up of security details (i) Unsecured, considered good 1,048.01 751.56 (ii) Contract assets - credit impaired 63.61 111.72 1,111.62 863.28 Less: Impairment Allowance 133.56 114.96 978.06 748.32  CORPORATE OVERVIEW STATUTORY REPORTS FINANCIAL STATEMENTS Annual Report 2022-23 249 (2) Contract assets are initially recognised for revenue earned from electro mechanical projects contracts as receipt of consideration that is conditional on successful completion of project milestone. Upon completion of milestone and acceptance/certification by the customer, the amounts",
            "page_number": 252,
            "pdf_name": "AR_21928_VOLTAS_2022_2023_26052023210412.pdf"
        },
        {
            "document": "the reporting obligations under the U.S. Securities Exchange Act of 1934 until such time the Company terminates its registration under the Exchange Act. The Company expects to satisfy the conditions for deregistration and file Form 15F with the Securities and Exchange Commission on or around January 24, 2024 to deregister its Securities and to terminate its reporting obligations under the Exchange Act. Plant Locations Location Range of Products Produced Pimpri, Pune – 411 018; Chikhali, Pune – 410 501; Chinchwad, Pune – 411 033 Medium and Heavy Commercial Vehicles (M&HCVs), Intermediate & Light Commercial Vehicles (ILCVs), Small Commercial Vehicles – Pickups (SCVs), Winger (Vans) Jamshedpur – 831 010 Intermediate Commercial Vehicles (ICVs) and M&HCVs Chinhat Industrial Area, Dewa Road, Chinhat, Lucknow – 226 019 ICVs, M&HCVs, LCVs, Electric Vehicles and Buses Plot No. 1, Sector 11 and Plot No. 14, Sector 12, I.I.E., Pantnagar, District, Udhamsingh Nagar, Uttarakhand – 263",
            "page_number": 227,
            "pdf_name": "AR_22007_TATAMOTORS_2022_2023_12062023215502.pdf"
        },
        {
            "document": "products and operations by 2039. Jaguar Land Rover’s annual total product and other investment spending was GBP 2.0 billion in FY 2021-22 and GBP 2.4 billion in FY 2022-23. Total product and other investment expenditure guidance for FY 2023-24 is approximately GBP 3.0 billion, with the Refocus program announced under the Reimagine strategy expected to continue to maintain the financial discipline successfully deployed previously under Project Charge+ and other initiatives. Our total product and other investment spending for domestic business was ` 6,812 crores for FY 2022-23. We have plans to significantly step up our capital expenditure for our domestic business, and it is expected to be around ` 8,000 crores in FY 2023-24. TML continues to monitor the external challenges of dynamically managing capital expenditure and implementation of further cash improvement measures. For FY 2023-24, on a consolidated basis, we expect to invest around `38,000 crores in property, plants",
            "page_number": 187,
            "pdf_name": "AR_22007_TATAMOTORS_2022_2023_12062023215502.pdf"
        },
        {
            "document": "the company/ Fellow Subsidiaries Associates Subsidiaries Others Total (vii) Contribution to Post retirement employee benefit trust - - - 8 8 (viii) (Purchase)/ Sale of fixed assets (18) - 14 - (4) (ix) Dividend paid - To Holding companies 26,170 - - 0 26,170 - To key management personnel and their relatives - - - 2 2 - To Non executive directors and their relatives - - - 0 0 (x) Commission/ Sitting Fees - To Non executive directors - - - 5 5 - To other key management personnel - - - 0 0 - To relatives of key management personnel - - - 0 0 (xi) Interest and guarantee commission expense Q 157 - 46 - 203 (xii) Miscellaneous expenses - - 9 - 9 Transactions during the year : (i) Financial guarantees given - - 1,174 - 1,174 (ii) Financial guarantees relinquished - - (3,298) - (3,298)",
            "page_number": 466,
            "pdf_name": "AR_22033_VEDL_2022_2023_19062023161652.pdf"
        },
        {
            "document": "trainings. To build a robust and dynamic service support infrastructure we are also ensuring proper inventory, usage analysis, replenishment and fulfilment of our spares. This supplements our efforts to build a collaborative ecosystem whereby the Mobility as a Service value proposition makes service and downtime easy for the customer. This is particularly in reference to our efforts towards daily preventive and corrective maintenance activities. We also offer on-site dedicated container workshops that are equipped with the necessary tools, fast moving parts/lubes storage space, small office spaces so that repair and support operations can be carried out smoothly. Apart from this, we also provide many other value-added services under: → Tata Kavach: For quick accident repair → Tata Zippy: For quick vehicle repair → Tata Alert: Roadside assistance programme with 24-hour problem resolution assurance for all CV models under warranty. Re.Wi.Re: Responsibly managing the end-of-product life phase Scrapping and recycling of",
            "page_number": 56,
            "pdf_name": "AR_22007_TATAMOTORS_2022_2023_12062023215502.pdf"
        },
        {
            "document": "83.86 54.23 Nil 0.04 83.86 54.19 Revenue from Continued Operations (A + B + C +D +E) 59,509.78 46,130.98 1,925.27 694.15 61,435.04 46,825.13 5,401.90 4,248.93 56,033.13 42,576.20 32. Revenue from Operations (Contd.) Notes to the Consolidated Financial Statements Integrated Annual Report 2022-23 Leading Transition. Powering Transformation #SustainableIsAttainable 477 Corporate Overview Decarbonising for Tomorrow Creating Value for Impact Delivering Value Statutory and Financial Statements  Reconciliation of Revenue For the year ended March 31, 2023 For the year ended March 31, 2022 ` crore ` crore Revenue from Continued Operations as per above 56,033.13 42,576.20 Net movement in Regulatory Deferral Balances (924.05) 239.47 Total Revenue from Operations 55,109.08 42,815.67 Contract Balances As at March 31, 2023 As at March 31, 2022 ` crore ` crore Contract Assets Recoverable from Consumers Non-Current 1,639.02 1,408.30 Unbilled Revenue other than passage of time 9.44 27.81 Total Contract Assets 1,648.46 1,436.11 Contract Liabilities Deferred Revenue",
            "page_number": 481,
            "pdf_name": "AR_2022_2023.pdf"
        },
        {
            "document": "- - - - - 100.00 48 Jaguar Land Rover Pension Trustees Limited (subsidiary w.e.f June 2, 2008) (dormant) UK GBP 101.64 - - - - - - - - - - - 100.00  Integrated Report / 2022-23 549 142-304 Statutory Reports 305-551 Financial Statements 1-141 Integrated Report (` in crores) Sr. No Subsidiary Country Reporting currency Exchange Rate Share capital (incl. advances towards capital where applicable) Reserves and Surplus Total Assets Total Liabilities Turnover Profit/ (Loss) Before Tax Tax Expense/ (Credit) Profit/(Loss) after tax Profit/ (Loss) for the period/ year * Proposed dividend and tax thereon Investments (except in case of investment in the subsidiaries) % of shareholding 49 Jaguar Cars (South Africa) (Pty) Ltd (subsidiary w.e.f June 2, 2008) (dormant) South Africa ZAR 4.62 - - - - - - - - - - - 100.00 50 Jaguar Land Rover Slovakia s.r.o. (JLRHL 0.01% and JLRL 99.99%)",
            "page_number": 481,
            "pdf_name": "AR_22007_TATAMOTORS_2022_2023_12062023215502.pdf"
        },
        {
            "document": "` 7.11 (3.63) (B) ‘A’ Ordinary shares (face value of ` 2 each) : (i) Basic ` 7.21 (3.63) (ii) Diluted ` 7.21 (3.63)  Integrated Report / 2022-23 320 Cash Flow Statement (` in crores) Year ended March 31, 2023 Year ended March 31, 2022 Cash flows from operating activities: Profit/(Loss) for the year from continuing operations 2,728.13 (1,739.23) Profit for the year from discontinued operations - 348.37 Adjustments for: Depreciation and amortisation expense 1,766.86 2,724.93 Allowances for trade and other receivables 105.12 42.71 Discounting of warranty and other provisions (128.53) - Inventory write down (net) 32.21 25.25 Provision for Intangible assets under development 276.91 - Provision/(reversal) for loan given to/investment and cost of closure in subsidiary companies/joint venture (net) 4.55 (699.15) Accrual for share-based payments 20.46 18.04 Profit on sale of assets (net) (including assets scrapped / written off) (88.47) (70.95) Profit on sale of investments at FVTPL",
            "page_number": 252,
            "pdf_name": "AR_22007_TATAMOTORS_2022_2023_12062023215502.pdf"
        },
        {
            "document": "to improve safety, quality, cost erosion and enhance productivity across all locations. Technicians and unions have supported business continuity to achieve productivity levels during challenging times caused by COVID-19 and the semi-conductor supply chain crisis. Employee wages are paid in accordance with the wage settlements signed that have varying terms (typically three to five years) at different locations. The expiration dates of the wage agreements for various locations/subsidiaries are as below: Location/subsidiaries Wage Agreement valid until Jaguar Land Rover – UK Plants 31-Oct -23 Mumbai 31-Dec-25 Pune – Passenger Vehicles 31-Aug-25 Pantnagar – Commercial Vehicles 31-Mar-26 Lucknow – Commercial Vehicles 31-Mar-24 Sanand – Passenger Vehicles 30-Sep-24 Pune – Commercial Vehicles 31-Aug-25 Jamshedpur – Commercial Vehicles 31-Mar-26 Sanand – TPEM 31-Mar-24 LONG-TERM WAGE SETTLEMENTS (LTS) We have successfully and amicably signed the long-term wage settlement (LTS) for our Pune PV and Pantnagar CV Units with complete support and cooperation from the",
            "page_number": 169,
            "pdf_name": "AR_22007_TATAMOTORS_2022_2023_12062023215502.pdf"
        },
        {
            "document": "vehicles in FY 2022-23, down 6% y-o-y as a result of destocking of inventory during FY 2021-22 creating a timing difference vs wholesales. Retail sales have been improving during FY 2022-23. Please refer to the paragraph on JLR in the Management Discussion & Analysis section for detailed analysis. Some of the key highlights of FY 2022-23 were: y Order book at ~200,000 units remained strong but as expected was down from the peak of around 215,000 units. y Ramp up of the new Range Rover and Range Rover Sport approaching target production levels. y Demand for Defender remained well ahead of the expectations at launch and was the best-selling model in FY 2022-23. A third shift has been added in Nitra to meet customer demand. y Strong engagement with chip suppliers continued to secure in calender year 2023 and 2024 supplies. y Pricing and mix have been managed throughout the",
            "page_number": 77,
            "pdf_name": "AR_22007_TATAMOTORS_2022_2023_12062023215502.pdf"
        },
        {
            "document": "(28.1) China 2,374 2,887 (17.8) 22,370 21,858 2.3 Overseas 4,827 6,154 (21.6) 4,488 6,881 (34.8) Land Rover 278,642 244,672 13.9 292,141 299,000 (2.3) UK 50,903 43,371 17.4 51,935 46,422 11.9 North America 69,699 67,881 2.7 66,771 77,520 (13.9) Europe 61,999 49,983 24.0 58,874 54,227 8.6 China 42,544 38,529 10.4 68,628 73,927 (7.2) Overseas 53,497 44,908 19.1 45,933 46,904 (2.1) Jaguar Land Rover 321,362 294,182 9.2 354,662 376,381 (5.8) UK 62,142 57,193 8.7 64,011 63,438 0.9 North America 81,629 79,350 2.9 77,526 91,305 (15.1) Europe 74,349 65,161 14.1 71,706 72,068 (0.5) China 44,918 41,416 8.5 90,998 95,785 (5.0) Overseas 58,324 51,062 14.2 50,421 53,785 (6.3) CJLR 50,855 53,468 (4.9) 50,904 54,035 (5.8)  Integrated Report / 2022-23 213 142-304 Statutory Reports 305-551 Financial Statements 1-141 Integrated Report Jaguar Land Rover’s performance on a wholesale basis: Wholesales (excluding our China Joint Venture) for the FY 2022-23 were 3,21,362 up 9.2%, compared to",
            "page_number": 145,
            "pdf_name": "AR_22007_TATAMOTORS_2022_2023_12062023215502.pdf"
        },
        {
            "document": "Note 8 907.28 412.56 107.27 Nil 23 LTH Milcom Private Ltd. $ August 17, 2015 March 31, 2017 Indian Rupee 1.00 66,660 * 33.33% Note 8 Not material to the group * * * * Integrated Annual Report 2022-23 Leading Transition. Powering Transformation #SustainableIsAttainable 537 Corporate Overview Decarbonising for Tomorrow Creating Value for Impact Delivering Value Statutory and Financial Statements  FORM AOC-I Statement containing salient features of the financial statement of Subsidiaries/ Associate Companies (Contd.) Part \"B\": Associates and Joint Ventures SN Name of the Associate Date of acquiring Associate Reporting period for the Associate concerned Reporting currency Exchange Rate as at March 31, 2023 Shares of Associate company held by the company on the year end Amount of Investment in Associate Extent of Holding % Description of how there is significant influence Reason why Associate is not consolidated Net worth attributable to Shareholding as per latest audited Balance",
            "page_number": 541,
            "pdf_name": "AR_2022_2023.pdf"
        },
        {
            "document": "Rover Italia SpA (subsidiary w.e.f June 2, 2008) Italy EUR 89.47 369.22 591.57 3,842.24 2,881.45 8,624.25 169.10 31.24 137.86 137.86 (1.32) - 100.00 67 Land Rover Ireland Limited - (no longer a trading NSC) (subsidiary w.e.f June 2, 2008) Ireland EUR 89.47 0.00 5.13 20.14 15.01 - - - - - (4.81) - 100.00 68 Jaguar Land Rover Korea Co. Ltd.(subsidiary w.e.f June 2, 2008) South Korea KRW 0.06 0.32 133.78 2,024.56 1,890.47 4,344.16 133.82 37.64 96.18 96.18 - - 100.00 69 Jaguar Land Rover Deutschland GmbH (subsidiary w.e.fJune 2, 2008) Germany EUR 89.47 119.17 424.32 3,853.49 3,309.99 9,993.19 (92.50) 58.61 (151.11) (151.11) 42.52 - 100.00 70 Jaguar Land Rover Austria GmbH (subsidiary w.e.f June 2, 2008) Austria EUR 89.47 1.30 121.29 645.98 523.39 1,857.03 23.54 8.52 15.02 15.02 - - 100.00 71 Jaguar Land Rover Australia Pty Limited (subsidiary w.e.f June 2, 2008) Australia AUD 55.03 3.85 572.25 2,954.58",
            "page_number": 481,
            "pdf_name": "AR_22007_TATAMOTORS_2022_2023_12062023215502.pdf"
        },
        {
            "document": "of pending litigations as at 31 March 2023 on the consolidated financial position of the Group, its associates and joint ventures and joint operations. Refer Note 39 to the consolidated financial statements. b. Provision has been made in the consolidated financial statements, as required under the applicable law or Ind AS, for material foreseeable losses, on long-term contracts including derivative contracts. Refer Note 31 to the consolidated financial statements in respect of such items as it relates to the Group, its associates and joint ventures and joint operations. c. There has been no delay in transferring amounts to the Investor Education and Protection Fund by the Holding Company or its subsidiary companies, associate companies, joint venture companies and joint operation companies incorporated in India during the year ended 31 March 2023. d (i) The respective management of the Holding Company and its subsidiary companies, associate companies, joint venture companies and",
            "page_number": 350,
            "pdf_name": "AR_22007_TATAMOTORS_2022_2023_12062023215502.pdf"
        },
        {
            "document": "the audit period. a. The Board of Directors in its meeting held on January 09, 2023 had approved the acquisition of 54% stake in Novelic d.o.o. Beograd – Zvezdara, a Serbia based Company which is a self-sustaining provider of mmWave radar sensors, perception solutions, and full-stack embedded systems. For PI & Associates, Company Secretaries Nitesh Latwal Partner ACS No.: 32109 CP No.: 16276 Place: New Delhi Peer Review No.: 1498/2021 Date: May 03, 2023 UDIN: A032109E000272461 Disclaimer This report is to be read with our letter of even date which is annexed as “Annexure A” and forms an integral part of this report. 114 Sona Comstar Annual Report 2022-23  Annexure-A To, The Members, SONA BLW Precision Forgings Limited Our Secretarial Audit Report of even date is to be read along with this letter: (i) Maintenance of secretarial records is the responsibility of the management of the Company. Our Responsibility",
            "page_number": 87,
            "pdf_name": "AR_22066_SONACOMS_2022_2023_24062023190637.pdf"
        },
        {
            "document": "0.11 (ii) The Company has a process whereby periodically all long term contracts (including derivative contracts) are assessed for material foreseeable losses. At the year end, the Company has reviewed and ensured that adequate provision as required under any law/accounting standards for material foreseeable losses on such long term contracts (including derivative contracts) has been made in books of account. (iii) In April 2021, the Company has completed the sale of certain assets related to defence business to Tata Advanced Systems Limited (TASL) for sale consideration of `234.09 crores againts the Net Assets of `231.57 crores resulting in a gain of `2.52 crores recorded as an exceptional item in Statement of Profit and Loss. In terms of our report attached For and on behalf of the Board For B S R & Co. LLP N CHANDRASEKARAN [DIN: 00121863] P B BALAJI Chartered Accountants Chairman Group Chief Financial Officer Firm's Registration",
            "page_number": 340,
            "pdf_name": "AR_22007_TATAMOTORS_2022_2023_12062023215502.pdf"
        },
        {
            "document": "four reporting segments: → Tata and other brand vehicles - Commercial Vehicles; → Tata and other brand vehicles – Passenger Vehicles; → Jaguar Land Rover; and → Vehicle Financing. Overview of Automotive Operations The total vehicle sales (excluding China joint venture) for FY 2022-23 and FY 2021-22 are set forth in the table below: FY 2022-23 FY 2021-22 Units % Units % Passenger cars 2,24,450 17.5% 1,94,185 18.8% Utility vehicles 6,37,877 49.6% 4,72,154 45.7% Intermediate and Light Commercial Vehicles 68,606 5.3% 63,097 6.1% SCV & Pick Up 1,99,769 15.5% 1,80,222 17.4% CV Passenger Vehicle 28,374 2.2% 17,699 1.7% Medium and Heavy Commercial Vehicles 1,25,888 9.8% 1,06,547 10.3% Total 12,84,964 100.0% 10,33,904 100.0% We sold 9,31,602 units of Tata Commercial Vehicles and Tata Passenger Vehicles and 3,21,362 units (excluding wholesales from the China Joint Venture) of Jaguar Land Rover vehicles in FY 2022-23. In India, we sold 9,31,429 and 6,93,036 units,",
            "page_number": 140,
            "pdf_name": "AR_22007_TATAMOTORS_2022_2023_12062023215502.pdf"
        },
        {
            "document": "crores for FY 2022-23, compared to `1,308 crores in FY 2021-22. The increase is mainly due to higher provisions for restructured portfolio. The allowances for trade and other receivables were `81 crores in FY 2022-23, compared to `151 crores in FY 2021-22. 5. Warranty and product liability expenses represented 3.0% and 3.2% of our total revenues in FY 2022-23 and FY 2021-22, respectively. The warranty expenses at Jaguar Land Rover increased to GBP 885 million (3.9% of the revenue) in FY 2022-23, compared to GBP 748 million (4.1% of revenue) in FY 2021-22, mainly due to increased retailer guidance, guided diagnostics enhancement, proactive issue detection, prioritisation and resolution coming from charge initiatives, quality improvements in vehicles and the implementation of other business enhancement activities. For Tata Motors’ Indian operations, Commercial Vehicles remains at 1.5% in FY 2022-23 and FY 2021-2022, Passenger Vehicles partially decreased from 0.7% in FY 2021-22 to",
            "page_number": 152,
            "pdf_name": "AR_22007_TATAMOTORS_2022_2023_12062023215502.pdf"
        },
        {
            "document": "among other things, undertaking new projects, issuing new securities, changes in management, mergers, sales of undertakings and investments in subsidiaries. In addition, certain negative covenants may limit our ability to borrow additional funds or to incur additional liens, and/or provide for increased costs in case of breach. Certain financing arrangements also include financial covenants to maintain certain debt-to-equity ratios, debt-to-earnings ratios, liquidity ratios, capital expenditure ratios and debt coverage ratios. We monitor compliance with our financial covenants on an ongoing basis. We also review our refinancing strategy and continue to plan for deployment of long-term funds to address any potential non-compliance. We monitor compliance with our financial covenants on an ongoing basis. We also review our refinancing strategy and continue to plan for deployment of long-term funds to address any potential non-compliance. For FY 2022-23, the Company is in compliance with all the covenants. In one of our subsidiaries, we",
            "page_number": 163,
            "pdf_name": "AR_22007_TATAMOTORS_2022_2023_12062023215502.pdf"
        },
        {
            "document": "into individually or taken together with previous transactions during a financial year, exceeds `1,000 crore or 10% of the annual consolidated turnover of the listed entity as per the last audited financial statements of the listed entity, whichever is lower (“Materiality Threshold”). Accordingly, the threshold for determination of material RPTs under Regulation 23(1) of the Listing Regulations has been reduced with effect from 01 April 2022. Given the nature of the industry, the Company works closely with its related parties (including holding companies, subsidiaries, fellow subsidiaries and joint ventures) to achieve its business objectives and enters into various operational transactions with its related parties, from time to time, in the ordinary course of business and on arm’s-length basis. Amongst the transactions that the Company executes with its related parties, the estimated value of Agreements entered into/to be entered into during FY 2024 and in each financial year(s) until FY 2026",
            "page_number": 21,
            "pdf_name": "AR_22033_VEDL_2022_2023_19062023161652.pdf"
        },
        {
            "document": "five‑star safety scores, including ratings of over 80% for Occupant Protection and in the Safety Assist category, recognising their suite of Advanced Driver Assistance Systems. The FY 2022‑23 also saw us add to our Defender collection, with the introduction of the Defender 130 model. Echoing the name of the original long‑wheelbase model, the Defender 130 adds another dimension to our all‑conquering, all‑terrain brand, providing space and comfort for up to eight adults, across three rows of full‑size seating. With the new Range Rover Velar, we are providing a calm sanctuary to our customers, promoting comfort and well‑being. The cabin includes active technologies that help cleanse the air and minimise road noise, to be both cleaner and quieter, on any journey. With an upgraded battery pack on the F‑PACE P400e plug‑in electric hybrid, we offer an increase of 20% to our customers on their electric‑only range. Jaguar I‑PACE continues to reinforce",
            "page_number": 33,
            "pdf_name": "AR_22007_TATAMOTORS_2022_2023_12062023215502.pdf"
        },
        {
            "document": "2022-23 from `39,999 crores in FY 2021-22, due to increased volumes. The material costs as  Integrated Report / 2022-23 218 Management Discussion and Analysis a percentage of total revenue decreased to 74.6% in FY 2022- 23, compared to 76.5% in FY 2021-22, primarily due to a improved product mix. Material costs for ILCVs category increased by 32.6% to `7,166 crores in FY 2022-23, compared to `5,404 crores in FY 2021- 22 and for SCVs and Pickups increased by 16.4% to `6,339 crores in FY 2022-23, compared to `5,444 crores in FY 2021-22 mainly due to increase in volumes. Material costs for MHCVs category increased by 37.0% to `24,624 crores in FY 2022- 23, compared to `17,978 crores in FY 2021-22 and for CV Passenger Vehicles category substantially increased to `3,974 crores in FY 2022-23, compared to `1,707 crores in FY 2021- 22 mainly due to increase in volumes. The",
            "page_number": 150,
            "pdf_name": "AR_22007_TATAMOTORS_2022_2023_12062023215502.pdf"
        },
        {
            "document": "Integral foreign operations. (49.80) (3.83) - interest and other expenses relating to borrowings for investment 72.20 63.86 - Others (88.33) 160.76 Undistributed earnings of subsidiaries, joint operations and equity accounted investees 602.29 407.25 Deferred tax assets not recognised because realisation is not probable 692.17 3,528.19 Deferred tax assets recognized on unabsorbed depreciation and others (refer note 3 below) (1,977.01) - Deferred tax assets recognized on Long term capital loss (150.48) - Previously recognised deferred tax assets written down - (6.34) Utilization/credit of unrecognised tax losses, unabsorbed depreciation and other tax benefits (547.45) (725.34) Effect of change in statutory tax rates 19.32 2.04 Profit on sale of passenger vehicle undertaking (Common control transaction) - 1,282.92 Impact of change in rates on moving to new tax regime (refer note 2 below) 522.36 - Profit on sale of Defence Business - (0.88) Others 492.24 470.34 Income tax expense reported in consolidated statement of",
            "page_number": 392,
            "pdf_name": "AR_22007_TATAMOTORS_2022_2023_12062023215502.pdf"
        },
        {
            "document": "(B) Designated and carried at FVTPL In Other Companies SsangYong Motor Company ## ........................................................... KRW 5,000 1,25,36,341 172.14 11,18,55,108 — (C) Designated and carried at FVTOCI In Other Companies Equity shares ................................................................................................. 1.29 1.22 1.29 1.22 5,205.18 5,525.84 Unquoted (A) At Cost (i) In Subsidiary Companies Equity shares Gromax Agri Equipment Limited ........................................... 10 59,73,218 4.29 59,73,218 4.29 Kota Farm Services Limited ..................................................... 10 2,73,420 — 2,73,420 — Mahindra & Mahindra Contech Limited ............................ 10 35,000 0.04 35,000 0.04 Mahindra Agri Solutions Limited ........................................... 10 9,30,32,599 367.33 9,30,32,599 367.33 Mahindra and Mahindra South Africa (Proprietary) Limited ..................................................................................................... ZAR 1 5,20,00,000 28.54 5,20,00,000 28.54 Mahindra Automotive Australia Pty. Limited ................ AUD 1 45,75,000 21.16 45,75,000 21.16 Mahindra Automotive Mauritius Limited – Ordinary shares ............................................................................. EUR 1 13,30,05,001 1,075.42 13,30,05,001 1,075.42 – Ordinary shares ............................................................................. NA 1,10,50,23,98,69,39,88,000 735.54 3,65,36,06,54,761 474.36 Mahindra Aerospace Private Limited # ............................ 10 91,23,89,607 1,106.96 — — Mahindra",
            "page_number": 310,
            "pdf_name": "AR_22135_M&M_2022_2023_03072023013854.pdf"
        },
        {
            "document": "during FY 2022-23 and FY 2021-22, respectively (constituting 72.5% and 67.0% of total sales in FY 2022-23 and FY 2021-22, respectively). In North America, we sold 81,629 units and 79,360 units in FY 2022-23 and FY 2021-22, respectively (constituting 6.4% and 7.7% of total sales in FY 2022-23 and FY 2021-22, respectively). 1.7% Share of volumes (FY 2021-22) PV SCV & Pick Up CV Passenger Vehicle MHCV UV ILCV 1.7% 45.7% 18.8% 6.1% 17.4% 10.3% 2.2% Share of volumes (FY 2022-23) PV SCV & Pick Up CV Passenger Vehicle MHCV UV ILCV 2.2% 49.6% 17.5% 5.3% 15.5% 9.8%  Integrated Report / 2022-23 209 142-304 Statutory Reports 305-551 Financial Statements 1-141 Integrated Report Tata and other brand vehicles The following table sets forth our total wholesale sales worldwide of Tata Commercial Vehicles and Tata Passenger Vehicles: FY 2022-23 FY 2021-22 Units % Units % Tata Passenger Vehicles 5,40,965 56.1% 3,72,157",
            "page_number": 141,
            "pdf_name": "AR_22007_TATAMOTORS_2022_2023_12062023215502.pdf"
        },
        {
            "document": "of share options for the year ended 31 March 2022 is presented below: Financial Year of Grant Exercise Period Options outstanding 01 April 2021 Options granted during the year Options transferred (to)/ from Parent/ fellow subsidiaries Options forfeited/ lapsed during the year Options exercised during the year Options outstanding 31 March 2022 Options exercisable 31 March 2022 2017-18 01 September 2020 - 28 February 2021 3,76,940 - - 23,457 3,53,483 - - 2018-19 01 November 2021 - 30 April 2022 99,12,240 - - 69,06,444 26,82,781 3,23,015 3,23,015 2018-19 Cash settled 99,086 - - - 99,086 - - 2019-20 29 November 2022 - 28 May 2023 1,35,72,278 - - 20,90,560 - 1,14,81,718 - 2019-20 Cash settled 80,050 - - 61,700 - 18,350 - 2020-21 06 November 2023 - 05 May 2024 1,27,11,112 - - 19,03,591 - 1,08,07,521 - 2020-21 Cash settled 87,609 - - 68,445 - 19,164 - 2021-22 01 November",
            "page_number": 450,
            "pdf_name": "AR_22033_VEDL_2022_2023_19062023161652.pdf"
        },
        {
            "document": "out with a 69% response rate, of the 11,500 employees who took the survey, to gauge their engagement and their response to the movements made on the desired culture. To qualitatively measure the delta change made, questions were designed to focus on the dimensions of Engagement, Culture Pillars and Change Management. The Engagement Score increased from 59% in 2020 to 70% in 2022 and further increased to 71% in 2023.. Cascade and co-creation: Over 40 workshops, covering over 1,750 staff employees, were conducted across all business units with leadership participation. Action plans co-evolved. 165+ projects were finalised across eight themes at the organisation and BU level for action sponsored by unit leadership. Culture Connect workshops Skill development In today's highly competitive business environment, investing in the employees' skill development is of paramount importance. We provide educational programmes to assist in the skill development of our technician-grade employees. In FY 2022-23,",
            "page_number": 62,
            "pdf_name": "AR_22007_TATAMOTORS_2022_2023_12062023215502.pdf"
        },
        {
            "document": "0.5% in FY 2022-23, thereby on overall level represent 1.2% and 1.1% of the revenue for FY 2022-23 and FY 2021-22, respectively, due to quality improvements and product mix. 6. Engineering expenses increased by 45.2% to `4,401 crores in FY 2022-23, compared to `3,031 crores in FY 2021- 22. These expenses represent 1.3% and 1.1% of our total revenues in FY 2022-23 and FY 2021-22, respectively and are attributable mainly to increased expenditure at Jaguar Land Rover. 7. There was loss of `1,415 crores in FY 2022-23 for commodity derivative as compared to gain of `1,371 crores in FY 2021-22. Expenditure capitalized This represents employee costs, stores and other manufacturing supplies and other work expenses incurred mainly toward product development projects. Considering the nature of our industry, we continually invest in the development of new products to address safety, emission, and other regulatory standards. The expenditure capitalized increased by 28.0%",
            "page_number": 152,
            "pdf_name": "AR_22007_TATAMOTORS_2022_2023_12062023215502.pdf"
        },
        {
            "document": ": Share of loss of joint ventures and associates 120.65 110.31 Depreciation and amortisation expenses 39.62 37.26 Allowance for doubtful debts and advances 360.04 93.49 Unrealised foreign exchange (gain) / loss (net) (3.34) 3.88 Interest income (44.59) (4.01) Dividend income (6.91) (5.02) Gain arising on financial assets measured at Fair Value through Profit or Loss (FVTPL) (net) (63.24) (81.09) Finance costs 29.59 25.87 Unclaimed credit balances written back (7.66) (9.79) (Gain) / loss on disposal of property, plant and equipment 1.90 1.14 Rental income (24.60) (24.40) 401.46 147.64 Operating profit before working capital changes 708.60 844.94 Changes in Working Capital: Adjustments for (increase) / decrease in operating assets: Inventories 69.42 (381.79) Trade receivables (287.48) (386.81) Contract assets (248.34) 300.20 Other financial assets (211.19) (5.93) Other non-financial assets (33.50) (46.53) Adjustments for increase / (decrease) in operating liabilities: Trade payables 80.76 485.27 Contract liabilities 168.73 (64.50) Other financial liabilities (17.76) 7.66",
            "page_number": 219,
            "pdf_name": "AR_21928_VOLTAS_2022_2023_26052023210412.pdf"
        },
        {
            "document": "Jaguar Land Rover Taiwan Company Pte. Ltd Taiwan TWD 2.69 10.36 117.63 1,017.23 889.25 2,397.00 133.94 26.67 107.27 107.27 - - 100.00 81 Jaguar Land Rover Classic Deutschland GmbH (Incorporated w.e.f. August 10,2018) Germany GBP 101.64 25.41 (27.02) 15.04 16.65 38.70 0.96 - 0.96 0.96 - - 100.00 82 Jaguar Land Rover Hungary KFT Budapest HUF 0.24 0.07 14.91 92.47 77.49 191.91 7.67 4.75 2.93 2.93 - - 100.00 83 Jaguar Land Rover Classic USA LLC ( Incorporated w.e.f June 1, 2018) (dormant) USA USD 82.18 - - - - - - - - - - - 100.00 84 Bowler Motors Limited (Name changed from Jaguar Land Rover Auto Ventures Limited on 28 January 2020) UK GBP 101.64 30.49 (63.24) 64.93 97.68 4.41 (15.99) - (15.99) (15.99) - - 100.00 85 Jaguar Land Rover Ventures Limited UK GBP 101.64 - - - - - - - - - - -",
            "page_number": 482,
            "pdf_name": "AR_22007_TATAMOTORS_2022_2023_12062023215502.pdf"
        },
        {
            "document": "AS 115 in applying the percentage of completion on its long-term projects, the Group is required to recognise any anticipated losses on it contracts. Impairment of financial assets and contract assets The Group’s Management reviews periodically items classified as receivables to assess whether a provision for impairment should be recorded in the statement of profit and loss. Management estimates the amount and timing of future cash flows when determining the level of provisions required. Such estimates are necessarily based on assumptions about several factors involving varying degrees of judgement and uncertainty. Details of impairment provision on contract assets and trade receivable are given in Note 15 and Note 16. The Group reviews it’s carrying value of investments annually, or more frequently when there is indication for impairment. If the recoverable amount is less than it’s carrying amount, the impairment loss is accounted for. Fair value measurement of financial instruments Some",
            "page_number": 235,
            "pdf_name": "AR_21928_VOLTAS_2022_2023_26052023210412.pdf"
        },
        {
            "document": "bold look. Harrier and Safari are further enhanced with a desirable larger infotainment screen and new ADAS features. Commercial Vehicles in India Industry sales of commercial vehicles rose by 34.0% to total 962,347 units in FY 2022-23 compared to the sales of 718,155 units in FY 2021-22. The following table sets forth the breakup of the wholesale sales in various categories. Category Industry Sales Tata Commercial Vehicles Sales FY 2022-23 (In Units) FY 2021-22 (In Units) % Change FY 2022-23 (In Units) FY 2021-22 (In Units) % Change Medium and Heavy Commercial Vehicles (MHCV) 2,30,720 1,51,546 52.2% 1,22,440 88,191 38.8% Intermediate and Light Commercial Vehicles (ILCV) 1,24,388 1,09,997 13.1% 54,636 53,847 1.5% SCVs and Pickups 5,23,923 4,23,560 23.7% 1,81,715 1,65,822 9.6% CV Passenger Vehicles 83,316 33,052 152.1% 34,120 14,822 130.2% Total 9,62,347 7,18,155 34.0% 3,92,911 3,22,682 21.8% MHCVs in India Industry saw a significant increase of 52.2% in the sale",
            "page_number": 142,
            "pdf_name": "AR_22007_TATAMOTORS_2022_2023_12062023215502.pdf"
        }
    ],
    "keywords": {
        "keywords": [
            "defense",
            "Military Contracts",
            "Defense Contracts",
            "Government Contracts",
            "Force Modernization",
            "Military Upgrades",
            "Defense Revitalization",
            "Defense Budget",
            "Military Spending",
            "Defense Expenditure",
            "Weapons Systems",
            "Armament Development",
            "Defense Platforms",
            "Strategic Partnerships",
            "Military Alliances",
            "Defense Collaboration",
            "Unmanned Vehicles",
            "Autonomous Systems",
            "Drone Technology",
            "Threat Assessment",
            "Risk Analysis",
            "Security Evaluation"
        ]
    }
}
```