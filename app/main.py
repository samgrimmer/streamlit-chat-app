# pylint: disable=invalid-name
# pylint: disable=non-ascii-file-name

from dotenv import load_dotenv
from default_page import DefaultPage
from config import Config
from dto.params.home_page_params_dto import HomePageParamsDto

def main():
  load_dotenv()
  
  default_page = DefaultPage(
    home_page_params_dto=HomePageParamsDto(
      title=Config.application_title(),
      openai_deployment_name=Config.openai_deployment_name(),
      openai_temperature=Config.openai_temperature(),
      openai_api_version=Config.openai_api_version(),
      openai_api_max_tokens=Config.openai_api_max_tokens(),
      openai_conversation_memory_number_of_messages=Config.openai_conversation_memory_number_of_messages(),
      chat_memory_azure_cosmos_database=Config.azure_cosmos_database(),
      chat_memory_azure_cosmos_container_name=Config.azure_cosmos_container_name(),
      chat_memory_azure_cosmos_endpoint=Config.azure_cosmos_endpoint(),
      chat_memory_azure_cosmos_connectionstring=Config.azure_cosmos_connectionstring()
    )
  )

if __name__ == '__main__':
  main()