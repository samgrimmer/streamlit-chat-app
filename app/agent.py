from langchain.agents import AgentExecutor, ConversationalChatAgent
from langchain.memory import ConversationBufferMemory, ConversationBufferWindowMemory
from langchain.chat_models import AzureChatOpenAI
from stream_handler import StreamHandler
from dto.params.agent_params_dto import AgentParamsDto

from constant import AGENT_DEFAULT_PARSING_ERROR

class Agent:
  def __init__(self, chat_memory, agent_params_dto: AgentParamsDto, stream_handler: StreamHandler) -> None:
    self.agent_params_dto = agent_params_dto
    self.stream_handler = stream_handler
    
    self.executor = self.__init_agent_executor(chat_memory)
  
  def __init_agent_executor(self, chat_memory):
    # memory = ConversationBufferWindowMemory(
    #   chat_memory=chat_memory,
    #   k=self.agent_params_dto.openai_conversation_memory_number_of_messages,
    #   return_messages=True,
    #   memory_key="chat_history",
    #   output_key="output",
    # )
    
    memory = ConversationBufferMemory(
      chat_memory=chat_memory,
      return_messages=True,
      memory_key="chat_history",
      output_key="output",
    )
    
    llm = AzureChatOpenAI(
      deployment_name=self.agent_params_dto.openai_deployment_name,
      temperature=self.agent_params_dto.openai_temperature,
      openai_api_version=self.agent_params_dto.openai_api_version,
      #max_tokens=self.agent_params_dto.openai_api_max_tokens,
      streaming=True,
      verbose=False,
      callbacks=[self.stream_handler]
    )
    
    tools = []

    chat_agent = ConversationalChatAgent.from_llm_and_tools(
      llm=llm, 
      tools=tools,
      return_only_outputs=True
    )

    executor = AgentExecutor.from_agent_and_tools(
      agent=chat_agent,
      tools=tools,
      memory=memory,
      return_intermediate_steps=True,
      handle_parsing_errors=True,
      #max_execution_time=1200
    )
    
    return executor