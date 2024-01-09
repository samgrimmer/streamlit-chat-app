import streamlit as st
from agent import Agent
from stream_handler import StreamHandler
from dto.params.agent_params_dto import AgentParamsDto
from dto.params.home_page_params_dto import HomePageParamsDto
from css import Css
from user import User
from session import Session

from memory.custom_cosmos_db import CustomCosmosDBChatMessageHistory

class DefaultPage:
  def __init__(self, home_page_params_dto: HomePageParamsDto) -> None:
    self.home_page_params_dto = home_page_params_dto
    
    self.__render_title()
    self.session = Session()
    self.__render_header()
    self.chat_history_memory = self.__init_chat_history_memory()
    self.__render_body()
    
  def __render_title(self):
    st.set_page_config(page_title=self.home_page_params_dto.title, page_icon="🦜", layout="centered")
    
  def __render_header(self):
    st.markdown(Css.header(), unsafe_allow_html=True)
    
    header = st.container()

    col1, col2 = header.columns(2)
    
    # col1.image("./images/logo.png", width=80)
    col2.title(self.home_page_params_dto.title)
    
    self.session.user_info = User().get_authenticated_user()

    with col2:
      st.write(f"user: {self.session.user_info.username}")
      
  def __render_body(self):
    self.__render_sidebar()
    
    body = st.container()
    
    with body:
      self.__render_section(body)
      
      self.__render_in_chat_history()
      
      if prompt := st.chat_input(placeholder="Type a new question"):
        st.chat_message("user").write(prompt)

        with st.chat_message("assistant"):
          chat_container = st.empty()
          
          with chat_container:
            stream_handler = StreamHandler(chat_container)
            
            agent_executor = Agent(
              chat_memory=self.chat_history_memory,
              agent_params_dto=AgentParamsDto(
                openai_deployment_name=self.home_page_params_dto.openai_deployment_name,
                openai_temperature=self.home_page_params_dto.openai_temperature,
                openai_api_version=self.home_page_params_dto.openai_api_version,
                openai_api_max_tokens=self.home_page_params_dto.openai_api_max_tokens,
                openai_conversation_memory_number_of_messages=self.home_page_params_dto.openai_conversation_memory_number_of_messages
              ),
              stream_handler=stream_handler
            ).executor
            
            response = agent_executor(prompt)
            
          # st.session_state.steps[str(len(self.chat_history_memory.messages) - 1)] = response[
          #   "intermediate_steps"
          # ]
          
  def __render_in_chat_history(self):
    if len(self.chat_history_memory.messages) == 0:
      st.session_state.steps = {}
      
    avatars = {"human": "user", "ai": "assistant"}

    for idx, msg in enumerate(self.chat_history_memory.messages):
        with st.chat_message(avatars[msg.type]):
            # Render intermediate steps if any were saved
            for step in st.session_state.steps.get(str(idx), []):
              if step[0].tool == "_Exception":
                continue

              with st.expander(f"✅ **{step[0].tool}**: {step[0].tool_input}"):
                st.write(step[0].log)
                st.write(f"**{step[1]}**")

            st.write(msg.content)
                    
  def __render_section(self, body):
    st.markdown(Css.ui_section(), unsafe_allow_html=True)
    
    col1, col2 = body.columns(2)  

    with col1:
      st.write("This chatbot is configured to answer questions")

    with col2:
      st.button("New chat", on_click=self.session.init_chat, args=[None])
  
  def __render_sidebar(self):
    user_history = self.chat_history_memory.recent_user_history()
    
    with st.sidebar:
      st.title("Recent History")

      for history in user_history:
        st.button(history.question, on_click=self.session.init_chat, args=[history.session_id])
      
  def __init_chat_history_memory(self):
    chat_history_memory = CustomCosmosDBChatMessageHistory(
      cosmos_endpoint=self.home_page_params_dto.chat_memory_azure_cosmos_endpoint,
      cosmos_database=self.home_page_params_dto.chat_memory_azure_cosmos_database,
      cosmos_container=self.home_page_params_dto.chat_memory_azure_cosmos_container_name,
      connection_string=self.home_page_params_dto.chat_memory_azure_cosmos_connectionstring,
      session_id=self.session.chat_id,
      user_id=self.session.user_info.username
    )
    
    chat_history_memory.prepare_cosmos() 
    
    return chat_history_memory