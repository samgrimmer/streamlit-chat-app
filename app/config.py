import os

class Config:
  @staticmethod
  def application_title():
    return os.getenv("APPLICATION_TITLE")

  @staticmethod
  def openai_api_base():
    return os.getenv("OPENAI_API_BASE")
  
  @staticmethod
  def openai_api_key():
    return os.getenv("OPENAI_API_KEY")
  
  @staticmethod
  def openai_api_version():
    return os.getenv("OPENAI_API_VERSION")
  
  @staticmethod
  def openai_api_type():
    return os.getenv("OPENAI_API_TYPE")
  
  @staticmethod
  def openai_api_max_tokens():
    return os.getenv("OPENAI_API_MAXTOKENS")
  
  @staticmethod
  def openai_conversation_memory_number_of_messages():
    return os.getenv("OPENAI_CONVERSATION_MEMORY_NUMBER_OF_MESSAGES")
  
  @staticmethod
  def openai_deployment_name():
    return os.getenv("OPENAI_DEPLOYMENT_NAME")
  
  @staticmethod
  def openai_deployment_version():
    return os.getenv("OPENAI_DEPLOYMENT_VERSION")
  
  @staticmethod
  def openai_model_name():
    return os.getenv("OPENAI_MODEL_NAME")
  
  @staticmethod
  def openai_temperature():
    return os.getenv("OPENAI_TEMPERATURE")
  
  @staticmethod
  def azure_cosmos_endpoint():
    return os.getenv("AZURE_COSMOSDB_ENDPOINT")
  
  @staticmethod
  def azure_cosmos_database():
    return os.getenv("AZURE_COSMOSDB_DATABASE")
  
  @staticmethod
  def azure_cosmos_container_name():
    return os.getenv("AZURE_COSMOSDB_CONTAINER_NAME")
  
  @staticmethod
  def azure_cosmos_connectionstring():
    return os.getenv("AZURE_COSMOSDB_CONNECTIONSTRING")
  