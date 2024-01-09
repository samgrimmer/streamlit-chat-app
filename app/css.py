class Css:
  @staticmethod
  def header():
    # hide deploy button and menu and custom
    return """
      <style>
        .reportview-container { margin-top: -2em; } 
        .block-container { padding-top: 0; }
        header, footer, #MainMenu { visibility: hidden; }
      </style>
      """
       
  @staticmethod
  def ui_section():
    return """
      <style>
        div[data-testid="column"]:nth-of-type(1) { padding: 5px 0 0 0 } 
        div[data-testid="column"]:nth-of-type(2) { text-align: right; } 
      </style>
      """