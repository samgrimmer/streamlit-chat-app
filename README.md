### My Streamlit Chat App

My Streamlit chat app application is a relatively simple configurable, dockerised python chat application that allows authenticated users to chat with a [generative ai LLM](https://en.wikipedia.org/wiki/Generative_artificial_intelligence), as well as facilitate recent chat history using an Azure Cosmos NoSql database.

The OneNZ Streamlit chat app application utlises the following frameworks and technologies:

- [Streamlit](https://streamlit.io)
- [Langchain](https://www.langchain.com)
- [Azure Open AI Service](https://azure.microsoft.com/en-us/products/ai-services/openai-service)
- [Azure Cosmos DB for Chat History](https://learn.microsoft.com/en-us/azure/cosmos-db/introduction)

Streamlit allows for the simple development of web applications targeted towards data scienctist enginners.

LangChain is an open source framework that lets software developers working with artificial intelligence (AI) and its machine learning subset combine large language models with other external components to develop LLM-powered applications. The goal of LangChain is to link powerful LLMs, such as OpenAI's GPT-3.5 and GPT-4, to an array of external data sources to create and reap the benefits of natural language processing (NLP) applications. 

To run locally and in the cloud, ensure the following environment variables are set:

```

APPLICATION_TITLE = "My Chat App"
OPENAI_API_BASE = "https://{azure_oai_name}-open-ai.openai.azure.com/"
OPENAI_API_KEY = ""
OPENAI_API_TYPE = "azure"
OPENAI_API_VERSION = "2023-05-15"
OPENAI_DEPLOYMENT_NAME = "gpt-35-turbo-16k"
OPENAI_DEPLOYMENT_VERSION = "0613"
OPENAI_MODEL_NAME="gpt-35-turbo-16k"
OPENAI_TEMPERATURE = 0.7
OPENAI_MAXTOKENS = 50
AZURE_COSMOSDB_ENDPOINT = "https://{azure_cosmos_name}.documents.azure.com:443/"
AZURE_COSMOSDB_DATABASE = "conversation_history"
AZURE_COSMOSDB_CONTAINER_NAME = "conversation_history"
AZURE_COSMOSDB_CONNECTIONSTRING = ""

```

To run locally:

If needed to run a python virtual environment
```

1) python -m venv .venv

2) .\.venv\Scripts\activate.ps1

3) Select python interupter (in vscode)

```
Run the actual application:

```

1) pip install -r requirements.txt

2) cd app

3) streamlit run main.py

```

To build the docker image locally and push to your ACR repository, run the following commands:
```
-- login
az login

-- set subscription
az account set --subscription {your_subscription_id}

--build docker container image
docker build . --no-cache -t {docker_image_name}

-- tag docker image
docker tag streamlit-chat-poc {acr_name}.azurecr.io/{docker_image_name}:latest

-- find acr
az acr list -o table

-- login to acr
az acr login -n {acr_name}.azurecr.io 

-- push docker image
docker push {acr_name}.azurecr.io/streamlit-chat-app:latest

-- confirm in container registry
az acr repository list --name {acr name}

```

##Add an identity provider
After deployment, you will need to add an identity provider to provide authentication support in your app. [See this tutorial for more information.](https://learn.microsoft.com/en-us/azure/app-service/scenario-secure-app-authentication-app-service)
