class Project_Settings:
    project_title : str = "Admin - PDFPack"
    project_version : str = "1.0.0"

class Database_Settings:
    database_url : str = "postgresql://postgres:amia1234@localhost:5432/pdfpack" 

    
project_settings = Project_Settings()
database_settings = Database_Settings()