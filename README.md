# ✈️🧳 AI Travel Agent - Powered by LangGraph: A Practical Use Case 🌍

Welcome to the **AI Travel Agent** repository! This project demonstrates how to build a smart, stateful travel assistant using **LangGraph, LangChain, Groq, SerpAPI, Streamlit, and SendGrid**.

The agent interacts with users in natural language, searches for flights and hotels, processes the results, generates a personalized travel plan, allows the user to review the plan before sending, and can deliver the final travel information through email.

## **Features**

- **Stateful Interactions**: The agent maintains state throughout the workflow and uses previous steps to continue the travel-planning process.
- **Human-in-the-Loop**: Users can review the generated travel plan before the email is sent.
- **Dynamic LLM Usage**: Groq is used for LLM-based reasoning, tool invocation, travel-plan generation, and email-content generation.
- **Flight Search**: Searches flight information using the SerpAPI Google Flights engine.
- **Hotel Search**: Searches hotel information using the SerpAPI Google Hotels engine.
- **Email Automation**: Generates HTML-formatted travel information and sends it using SendGrid.
- **Streamlit Interface**: Provides a simple web interface for interacting with the AI travel agent.
- **LangGraph Workflow**: Uses nodes, edges, state, tool calling, and human approval to manage the agent workflow.

## **Architecture**

```text
                         ┌──────────────────┐
                         │      User        │
                         │ Travel Request   │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │    Streamlit     │
                         │       UI         │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │    LangGraph     │
                         │      Agent       │
                         └────────┬─────────┘
                                  │
                     ┌────────────┴────────────┐
                     │                         │
                     ▼                         ▼
             ┌────────────────┐       ┌────────────────┐
             │  Flight Tool   │       │   Hotel Tool   │
             │    SerpAPI     │       │     SerpAPI    │
             └───────┬────────┘       └───────┬────────┘
                     │                        │
                     └───────────┬────────────┘
                                 │
                                 ▼
                         ┌──────────────────┐
                         │     Groq LLM     │
                         │ Travel Planning  │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │ Human Approval   │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │    SendGrid      │
                         │  Email Service   │
                         └────────┬─────────┘
                                  │
                                  ▼
                         ┌──────────────────┐
                         │  User's Email    │
                         └──────────────────┘
```

## **Technologies Used**

- **Python** - Application development
- **LangGraph** - Stateful agent workflow and orchestration
- **LangChain** - LLM and tool integration
- **Groq** - LLM inference
- **SerpAPI** - Flight and hotel search
- **Google Flights** - Flight information
- **Google Hotels** - Hotel information
- **Streamlit** - Web interface
- **SendGrid** - Email delivery
- **Pydantic** - Input validation
- **python-dotenv** - Environment variable management

## **Getting Started**

### **1. Clone the Repository**

```bash
git clone https://github.com/nirbar1985/ai-travel-agent.git
```

Go to the project directory:

```bash
cd ai-travel-agent-main
```

### **2. Create and Activate the Conda Environment**

Create the environment:

```bash
conda create -n dsml_26_env python=3.11
```

Activate it:

```bash
conda activate dsml_26_env
```

### **3. Install Dependencies**

Install all dependencies:

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not available, install the required packages manually:

```bash
pip install python-dotenv langchain langchain-core langchain-groq langgraph sendgrid google-search-results pydantic streamlit
```

## **Store Your API Keys**

Create a `.env` file in the root directory of the project.

Your project should look like:

```text
ai-travel-agent-main/
├── .env
├── app.py
├── requirements.txt
├── README.md
└── ...
```

Add your API keys and environment variables to the `.env` file:

```env
# Groq LLM
GROQ_API_KEY=your_groq_api_key

# SerpAPI - Flight and Hotel Search
SERPAPI_API_KEY=your_serpapi_api_key

# SendGrid - Email Service
SENDGRID_API_KEY=your_sendgrid_api_key
FROM_EMAIL=your_verified_sender_email
TO_EMAIL=your_receiver_email
EMAIL_SUBJECT=Travel Information

# LangChain / LangSmith Observability
LANGCHAIN_API_KEY=your_langchain_api_key
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=ai_travel_agent
```

Make sure to replace the placeholders:

- `your_groq_api_key`
- `your_serpapi_api_key`
- `your_sendgrid_api_key`
- `your_verified_sender_email`
- `your_receiver_email`
- `your_langchain_api_key`

with your actual API keys and email addresses.

### **Example `.env`**

```env
GROQ_API_KEY=gsk_xxxxxxxxxxxxxxxxx

SERPAPI_API_KEY=xxxxxxxxxxxxxxxxx

SENDGRID_API_KEY=SG.xxxxxxxxxxxxxxxxx

FROM_EMAIL=your_verified_email@gmail.com
TO_EMAIL=your_receiver_email@gmail.com
EMAIL_SUBJECT=Travel Information

LANGCHAIN_API_KEY=lsv2_xxxxxxxxxxxxxxxxx
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=ai_travel_agent
```

> **Important:** Never commit your `.env` file or API keys to GitHub.

Add `.env` to your `.gitignore`:

```text
.env
```

## **API Services**

### **Groq**

Groq provides the LLM inference used by the travel agent.

The application uses:

```python
ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0
)
```

The LLM is used for:

- Understanding travel requests
- Deciding which tools to call
- Processing tool results
- Generating travel recommendations
- Generating HTML email content

### **SerpAPI**

SerpAPI provides the flight and hotel search data.

The application uses:

```python
from serpapi import GoogleSearch
```

and:

```python
search = GoogleSearch(search_params)
results = search.get_dict()
```

The tools use:

- `google_flights` for flight searches
- `google_hotels` for hotel searches

### **SendGrid**

SendGrid is used to send the generated travel plan through email.

The sender email must be verified in SendGrid.

Example:

```env
SENDGRID_API_KEY=your_sendgrid_api_key
FROM_EMAIL=your_verified_sender@gmail.com
TO_EMAIL=your_receiver@gmail.com
EMAIL_SUBJECT=Travel Information
```

### **LangSmith / LangChain Observability**

LangSmith can be used for monitoring and tracing LLM and agent executions.

```env
LANGCHAIN_API_KEY=your_langchain_api_key
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=ai_travel_agent
```

LangSmith tracing is optional.

## **How to Run the Chatbot**

Make sure the Conda environment is activated:

```bash
conda activate dsml_26_env
```

Start the Streamlit application:

```bash
streamlit run app.py
```

After starting the application, Streamlit will display a local URL similar to:

```text
Local URL: http://localhost:8501
```

Open the URL in your browser:

```text
http://localhost:8501
```

## **Using the Chatbot**

Once the application is launched, enter your travel request.

For example:

> I want to travel from Mumbai to Dubai from November 10th to November 15th. Find me the best flights and 4-star hotels.

The chatbot will:

1. Understand the travel request.
2. Identify the required travel information.
3. Search for flights using SerpAPI.
4. Search for hotels using SerpAPI.
5. Process the search results.
6. Generate a personalized travel plan.
7. Allow the user to review the travel plan.
8. Generate an HTML email.
9. Send the approved travel plan through SendGrid.

## **Flight Search**

The flight tool uses SerpAPI Google Flights.

Example parameters:

```python
{
    "engine": "google_flights",
    "departure_id": "BOM",
    "arrival_id": "DXB",
    "outbound_date": "2026-11-10",
    "return_date": "2026-11-15",
    "adults": 1
}
```

The flight results can include:

- Airline
- Flight number
- Departure time
- Arrival time
- Duration
- Stops
- Price
- Booking link

## **Hotel Search**

The hotel tool uses SerpAPI Google Hotels.

Example parameters:

```python
{
    "engine": "google_hotels",
    "q": "Hotels in Dubai",
    "check_in_date": "2026-11-10",
    "check_out_date": "2026-11-15",
    "adults": 1
}
```

The hotel results can include:

- Hotel name
- Location
- Rating
- Price
- Description
- Booking link

## **Human-in-the-Loop**

The email integration uses a human-in-the-loop approach.

The workflow allows the user to review the generated travel information before sending it.

```text
Travel Plan Generated
        │
        ▼
User Reviews Information
        │
        ├── Approve ──► Generate Email ──► SendGrid
        │
        └── Reject ──► Stop / Modify Request
```

This gives the user control over the final information before the email is sent.

## **Email Integration**

Travel data is formatted as HTML and delivered through SendGrid.

The email can contain:

- Flight recommendations
- Hotel recommendations
- Prices
- Travel dates
- Travel details
- Relevant links

The email configuration is stored in `.env`:

```env
FROM_EMAIL=your_verified_sender@gmail.com
TO_EMAIL=your_receiver@gmail.com
EMAIL_SUBJECT=Travel Information
```

## **Test SendGrid Separately**

You can test the SendGrid integration independently before running the complete application.

Run:

```bash
python test_sendgrid.py
```

A successful result should look like:

```text
FROM: your_verified_sender@gmail.com
TO: your_receiver@gmail.com
API KEY: Found
Status Code: 202
✅ SUCCESS - SendGrid accepted the email!
```

A `202` response means SendGrid accepted the email for processing.

## **Troubleshooting**

### **Conda is not recognized**

If you see:

```text
'conda' is not recognized
```

run the project using Anaconda Prompt.

You can also initialize Conda:

```bash
conda init
```

Restart VS Code after running the command.

### **`.env` Variables Return `None`**

Make sure `.env` is located in the project root:

```text
ai-travel-agent-main/.env
```

Check that the variable names are exactly:

```env
GROQ_API_KEY=
SERPAPI_API_KEY=
SENDGRID_API_KEY=
FROM_EMAIL=
TO_EMAIL=
EMAIL_SUBJECT=
```

### **Groq API Error**

If you receive:

```text
401 Unauthorized
```

check that your `GROQ_API_KEY` is valid and correctly loaded.

If you receive a model-not-found error, verify that the configured model is available in your Groq account.

### **Groq Token Limit Error**

If you receive an error similar to:

```text
Request too large
TPM Limit
Requested tokens > allowed tokens
```

the application may be sending too much flight/hotel data or conversation history to the LLM.

To reduce token usage:

- Return only required flight fields.
- Return only required hotel fields.
- Limit the number of flight results.
- Limit the number of hotel results.
- Avoid sending unnecessary conversation history.
- Avoid sending large raw API responses to the LLM.

### **SerpAPI Error**

Make sure your API key is configured correctly:

```env
SERPAPI_API_KEY=your_serpapi_api_key
```

The application uses:

```python
from serpapi import GoogleSearch
```

and:

```python
search = GoogleSearch(search_params)
results = search.get_dict()
```

### **SendGrid Error**

If you receive a `400` or `403` error, check:

1. `SENDGRID_API_KEY`
2. `FROM_EMAIL`
3. `TO_EMAIL`
4. SendGrid sender verification
5. SendGrid Mail Send permission

You can test SendGrid separately:

```bash
python test_sendgrid.py
```

A successful response should be:

```text
Status Code: 202
✅ SUCCESS - SendGrid accepted the email!
```

## **Security**

Never commit API keys to GitHub.

Add the following to `.gitignore`:

```text
.env
__pycache__/
*.pyc
.venv/
```

If an API key is accidentally exposed:

1. Revoke the exposed API key.
2. Generate a new API key.
3. Update your `.env` file.
4. Never commit the new API key to GitHub.

## **Example Output**

### ✈️ Flight Recommendations

The application can display:

```text
Airline: Example Airlines
Departure: Mumbai (BOM)
Arrival: Dubai (DXB)
Duration: 3h 20m
Stops: Non-stop
Price: $XXX
```

### 🏨 Hotel Recommendations

The application can display:

```text
Hotel: Example Hotel
Location: Dubai
Rating: 4.5
Price: $XXX/night
```

The application can also provide relevant links so users can verify availability and complete their booking.

> **Note:** Flight and hotel information is fetched through external search services and may change based on availability, date, and provider.

## **Future Improvements**

- Multi-city trip planning
- Budget-based travel recommendations
- Weather information
- Restaurant recommendations
- Tourist attraction recommendations
- Currency conversion
- Trip cost estimation
- Calendar integration
- WhatsApp integration
- Persistent user preferences
- Multi-agent travel planning
- Travel document/RAG integration
- Personalized itinerary generation

## **Learn More**

This project demonstrates practical concepts including:

- Generative AI
- Large Language Models
- AI Agents
- Tool Calling
- LangChain
- LangGraph
- Stateful Workflows
- Human-in-the-Loop
- API Integration
- Web Search
- Structured Data Processing
- Email Automation
- Streamlit
- Environment Variable Management

For more information about LangGraph and agent workflows, see the LangGraph documentation.

## **Author**

**Riya Teke**

AI/ML Engineer | Generative AI | Agentic AI | LLMs | RAG | Python
