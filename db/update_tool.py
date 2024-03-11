import db.models.model as db
from db.session import SessionLocal

# this function add and update tool table
def update_tool():
    # print("\n\n    ------------ update_tool function start ------------")
    DB = SessionLocal()

    tools = [
		{"tool_id": 11, "tool_name": "pdf-to-docx"},
		{"tool_id": 12, "tool_name": "pdf-to-xlsx"},
		{"tool_id": 13, "tool_name": "pdf-to-jpg"},
		{"tool_id": 14, "tool_name": "pdf-to-png"},
		{"tool_id": 31, "tool_name": "xlsx-to-pdf"},
		{"tool_id": 32, "tool_name": "docx-to-pdf"},
		{"tool_id": 51, "tool_name": "merge-pdf"},
		{"tool_id": 52, "tool_name": "split-pdf"},
		{"tool_id": 53, "tool_name": "organize-pdf"},
		{"tool_id": 61, "tool_name": "rotate-pdf"},
		{"tool_id": 62, "tool_name": "text-watermark-pdf"},
		{"tool_id": 63, "tool_name": "image-watermark-pdf"},
		{"tool_id": 71, "tool_name": "compress-pdf"},
		{"tool_id": 72, "tool_name": "ocr-pdf"}
	]

    # print("\ntype of tools : ", type(tools))
    # print("\nvalue inside tools : ", tools)
    print("Update Tool")
    
    try:
        # Check if each tool_id in tools is already in the database and add it if not
        for tool in tools:
            Tool_ID = tool['tool_id']
            # print("\ntype of Tool_ID : ", type(Tool_ID))
            # print("\nvalue inside Tool_ID : ", Tool_ID)
            
            Tool_Name = tool['tool_name']
            # print("\ntype of Tool_Name : ", type(Tool_Name))
            # print("\nvalue inside Tool_Name : ", Tool_Name)
            
            tool_id_exists = DB.query(db.tool).filter(db.tool.tool_id == Tool_ID).first()
            
            # print("\ntype of tool_id_exists : ", type(tool_id_exists))
            # print("\nvalue inside tool_id_exists : ", tool_id_exists)
            
            if tool_id_exists:  # if tool_id found then updating tool_name if tool_name not matched
                # print("\ntype of tool_id_exists.tool_name : ", type(tool_id_exists.tool_name))
                # print("\nvalue inside tool_id_exists.tool_name : ", tool_id_exists.tool_name)
                # checking weather tool_name matched with existsing record
                if tool_id_exists.tool_name != Tool_Name :
                    # print("\ntool_name not matched")
                    DB.query(db.tool).filter(db.tool.tool_id == Tool_ID).update({"tool_name": Tool_Name})
                    DB.commit()
                    # print("\ntool_name update into tool table successfully")
                # else :
                    # print("\ntool_name matched")
            else: # if tool_id not found
                new_tool = db.tool(tool_id = tool['tool_id'], tool_name = tool['tool_name'])
                DB.add(new_tool)
                DB.commit()
                # print("\nnew tool added into tool table successfully")
        
        return {
            "success": True, 
            "message": "Tool Table updated successfully!"
        }
    
    except Exception as e:
        return {
            "success": False, 
            "error": str(e)
        }
