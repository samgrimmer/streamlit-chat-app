from dataclasses import dataclass

@dataclass
class AgentParamsDto:
  openai_deployment_name: str
  openai_temperature: float
  openai_api_version: str
  openai_api_version: str
  openai_api_max_tokens: int
  openai_conversation_memory_number_of_messages: str