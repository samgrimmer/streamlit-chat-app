from dataclasses import dataclass

@dataclass
class HomePageParamsDto:
  title: str
  openai_deployment_name: str
  openai_temperature: str
  openai_api_version: str
  openai_api_max_tokens: str
  openai_conversation_memory_number_of_messages: str
  chat_memory_azure_cosmos_endpoint: str
  chat_memory_azure_cosmos_database: str
  chat_memory_azure_cosmos_container_name: str
  chat_memory_azure_cosmos_connectionstring: str