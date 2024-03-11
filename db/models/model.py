from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from db.base_class import Base

class token(Base):
    uid = Column(String, primary_key = True)
    jwt = Column(String, unique = True)
    expire = Column(DateTime)
    flag = Column(Integer)
    access_time = Column(DateTime)   # when user access this tool
    visitor_ip_address = Column(String)    # visitors's ip address
    api_callers_ip_address = Column(String)    # api caller's ip address
    country = Column(String)       # user's city which will be get from visitor_ip_address
    city = Column(String)          # user's country which will be get from visitor_ip_address
    tool_id_fk = Column(Integer, ForeignKey("tool.tool_id"))    # this will update upon 
    token_file = relationship("file", back_populates = "file_token")
    token_tool = relationship("tool", back_populates = "tool_token")
    
class file(Base):
    table_id = Column(Integer, primary_key = True, index = True)
    file_name = Column(String)
    file_path = Column(String)
    uid_fk = Column(String, ForeignKey("token.uid"))
    file_token = relationship("token", back_populates = "token_file")

class tool(Base):
    tool_id = Column(Integer, primary_key = True, index = True)
    tool_name = Column(String, unique = True)
    start_date = Column(DateTime)
    tool_token = relationship("token", back_populates = "token_tool")