import streamlit as st
from langchain.callbacks.base import BaseCallbackHandler

class StreamHandler(BaseCallbackHandler):
  def __init__(self, container: st.markdown, initial_text=""):
    self.container = container
    self.text = initial_text
    self.final_answer = False
    
    self.ignore_list = ['{','}','"','{\n','",\n','}\n','\n}']
    self.replace_list = ['"','action_input',':']
    
  def on_llm_new_token(self, token: str, **kwargs) -> None:
    if token not in self.ignore_list:
      self.text += token
    
    if "Final Answer" in self.text:
      self.final_answer = True
      self.text = ""
      
    if self.final_answer:
      if '"action_input"' in self.text:
        self.text = ""
        
      if token not in self.ignore_list:
        for string_to_replace in self.replace_list:
          self.text = self.text.replace(string_to_replace, '')
          final = self._convert_newlines(self.text)

          self.container.markdown(final, unsafe_allow_html=True)
          
  def _convert_newlines(self, text: str) -> str:
    return text.replace("\n", "  \n")