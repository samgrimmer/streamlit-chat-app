from streamlit_javascript import st_javascript
from dacite import from_dict

from dto.user_info_dto import UserInfoDto
from dto.user_dto import UserDto

from constant import DEFAULT_USER

class User:
  def get_authenticated_user(_self) -> UserInfoDto:
    js_code = """(await fetch("/.auth/me")
    .then(function(response) { return response.json(); }).then(function(body) { return body; }))
    """

    json_data = st_javascript(js_code)

    user_info = UserInfoDto(username = DEFAULT_USER, email = None)
    
    if json_data == 0:
      pass
    elif isinstance(json_data, list) and len(json_data) > 0:
      user_data_objects = [from_dict(data_class=UserDto, data=item) for item in json_data]
      
      user_info.username = user_data_objects[0].user_id
      
      for user_claim in user_data_objects[0].user_claims:
        if user_claim.typ == "preferred_username":
          user_info.email = user_claim.val
    
    return user_info
