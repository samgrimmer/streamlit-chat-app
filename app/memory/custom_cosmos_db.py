"""Custom Azure CosmosDB Memory History."""
from __future__ import annotations

import logging

from typing import TYPE_CHECKING, Any, Optional, List, Type
from langchain.memory import CosmosDBChatMessageHistory
# import streamlit as st
from dto.recent_history_dto import RecentHistoryDto

logger = logging.getLogger(__name__)

if TYPE_CHECKING:
    from azure.cosmos import ContainerProxy
    
class CustomCosmosDBChatMessageHistory(CosmosDBChatMessageHistory):
    def __init__(
      self,
      cosmos_endpoint: str,
      cosmos_database: str,
      cosmos_container: str,
      session_id: str,
      user_id: str,
      credential: Any = None,
      connection_string: Optional[str] = None,
      ttl: Optional[int] = None,
      cosmos_client_kwargs: Optional[dict] = None,
    ):
      super().__init__(
        cosmos_endpoint,
        cosmos_database,
        cosmos_container,
        session_id,
        user_id,
        credential,
        connection_string,
        ttl,
        cosmos_client_kwargs
      )

    # @st.cache_data
    def recent_user_history(_self) -> List[RecentHistoryDto]:
        """Retrieve user messages from Cosmos"""
        if not _self._container:
            raise ValueError("Container not initialized")
        try:
            from azure.cosmos.exceptions import (  # pylint: disable=import-outside-toplevel # noqa: E501
                CosmosHttpResponseError,
            )
        except ImportError as exc:
            raise ImportError(
                "You must install the azure-cosmos package to use the CosmosDBChatMessageHistory."  # noqa: E501
                "Please install it with `pip install azure-cosmos`."
            ) from exc
        try:
            user_sessions = list(_self._container.query_items(
              query="SELECT c.id, c.messages[0].data.content as question FROM conversation_history c WHERE c.user_id=@user_id",
              parameters=[
                { "name" : "@user_id", "value": _self.user_id }
              ],
              enable_cross_partition_query=True
            ))
            
            recent_history = []
            
            for user_session in user_sessions:
              recent_history.append(
                RecentHistoryDto(session_id=user_session["id"], question=user_session["question"])
              )

            return recent_history
        except CosmosHttpResponseError:
            logger.info("no session found")
            return