import datetime
from datetime import datetime
import os
import shutil
import db.models.model as db

from db.session import SessionLocal
import asyncio

# purpose of this function is to get expire token, 
# 
def delete_data():

    print("Running Delete Data...")
    DB = SessionLocal()
    # print("\n\n------------ delete_data function start ------------")

    # Get the current date and time
    current_datetime = datetime.now()
    # print("\ncurrent_datetime : ", current_datetime)

    # querying token table to fetch all records whose expire time is less than current time
    expired_users = DB.query(db.token).filter(db.token.expire < current_datetime).all()
    # print("\ntype of expired_users : ", type(expired_users))
    # print("\nvalue inside expired_users : ", expired_users)
    
    no_of_expired_users = len(expired_users)
    print("\nvalue inside no_of_expired_users : ", no_of_expired_users)
    
    for user in expired_users:
        
        uid = user.uid

        if uid:
            # print("\ntype of uid : ", type(uid))
            # print("\nvalue inside uid : ", uid)
            
            # removing specific directory with uid named under storage directory
            dir_path = 'storage/'+ uid
            # print("\ntype of dir_path : ", type(dir_path))
            # print("\nvalue inside dir_path : ", dir_path)
            if os.path.exists(dir_path):
                shutil.rmtree(dir_path)

            # removing specific zip file with uid named under storage directory
            zip_path = f'storage/{uid}.zip'
            # print("\ntype of zip_path : ", type(zip_path))
            # print("\nvalue inside zip_path : ", zip_path)
            if os.path.exists(zip_path):
                os.remove(zip_path)

            # print("\ndeleting all records from file table whose uid is : ", uid)
            DB.query(db.file).filter(db.file.uid_fk == uid).delete()
            
            # print("\nupdating records in token table whose uid is : ", uid)
            DB.query(db.token).filter(db.token.uid == uid).update({
                "jwt": None,
                "expire": None,
                "flag": 0
            })

    DB.commit()
    '''
    print("\nshowing token table data after delete_data")
    tokens = DB.query(db.token).all()
    for token in tokens:
        print("\nvalue inside token : ", token)

    print("\nshowing file table data after delete_data")
    files = DB.query(db.file).all()
    for file in files:
        print("\nvalue inside file : ", file)
    '''
    print("\n------------ delete_data function end ------------")

        # await asyncio.sleep(60)



# import schedule
# import time

# # Schedule the job to run every minute
# schedule.every(1).minutes.do(delete_data)

# while True:
#     schedule.run_pending()
#     time.sleep(60)
    

