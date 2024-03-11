import asyncio
from fastapi import APIRouter, Depends, HTTPException, Request, security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials


from db.session import SessionLocal, get_db
from db.update_tool import update_tool

tool_table_update = APIRouter()

security = HTTPBearer()

# endpoint for check_tool table
@tool_table_update.post("/update_tool_table", tags = ["Update Tool Table"])
async def update_tool_table(request: Request):
    
    print("\n\n\n ---------- /update tool table route start ------------")

    print("\ntype of request : ", type(request))
    print("\nvalue inside request : ", request)
    


    print("\ntype of request.header : ", type(request.headers))
    print("\nvalue inside request.header : ", request.headers)
    
    # get origin from request.header
    origin = request.headers.get('origin')
    print("\ntype of origin : ", type(origin))
    print("\nvalue inside origin : ", origin)
    
    # get ip from request.header to check users ip
    visitorsIP = request.headers.get('request-ip')
    print("\ntype of visitorsIP : ", type(visitorsIP))
    print("\nvalue inside visitorsIP : ", visitorsIP)
    
    print("\ntype of request.client : ", type(request.client))
    print("\nvalue inside request.client : ", request.client)
    
    # server ip that is sending api request in our case contabo's ip
    api_callers_ip_address = request.client.host
    print("\ntype of api_callers_ip_address : ", type(api_callers_ip_address))
    print("\nvalue inside api_callers_ip_address : ", api_callers_ip_address)




    loop = asyncio.get_event_loop()

    try:
        print("\n------- Calling update_tool function with thread --------")
        response = await loop.run_in_executor(None, update_tool)
        print("\nupdate_tool thread end")
        return response
    except Exception as e:
        return {
            "success": False, 
            "error": str(e)
        }
