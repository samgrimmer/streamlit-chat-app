from datetime import datetime
import streamlit as st
from dto.user_info_dto import UserInfoDto

class Session:
  def __init__(self) -> None:
    pass
    
  @property
  def user_info(self) -> UserInfoDto:
    return st.session_state.user_info

  @user_info.setter
  def user_info(self, new_value) :
    st.session_state.user_info = new_value  
    
  @property
  def chat_id(self) -> str:
    if 'key' not in st.session_state:
      st.session_state.steps = {}
      st.session_state.key = self.__create_unique_user_session_id()
      
    return st.session_state.key

  @chat_id.setter
  def chat_id(self, new_value) :
    st.session_state.key = new_value

  def init_chat(self, link_id = None):
    st.session_state.steps = {}
    
    if (link_id is None):
      link_id = self.__create_unique_user_session_id()
    
    self.chat_id = link_id
    
  def __create_unique_user_session_id(self) -> str:
    return datetime.now().strftime("%Y%m%d%H%M%S%f")