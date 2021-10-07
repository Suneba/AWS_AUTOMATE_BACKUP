import boto3
import logging
from datetime import datetime
import socket
import time
import os

now = datetime.now()
logging.basicConfig(filename='logs.log', level=logging.INFO)

global the_file
the_file = None

LOCAL_PATH = 'C:/Users/deepankar/Desktop/stats'



def current_file_upload_status(the_file,current_file_number,total_files):
    print("uploaded {}, file {}/{}".format(the_file,current_file_number,total_files))



def upload(LOCAL_PATH,FOLDER):
    count = 0
    entries = os.listdir(LOCAL_PATH)

    for the_file in entries:
        # calling s3 bucket
        s3 = boto3.client('s3')
        # uploading
        try:
            s3.upload_file('{}/{}'.format(str(LOCAL_PATH),the_file), 'siddhantayush','{}/{}'.format(FOLDER,the_file))
        except:
            print(" file >{}< upload error".format(the_file))

        # creating logs
        logging.info('{}:->uploaded {} to {}/ from {}'.format(now.strftime("%d/%m/%Y %H:%M:%S"),the_file,FOLDER,LOCAL_PATH))
        # uploading logs
        s3.upload_file('logs.log', 'siddhantayush', 'logs.log')

        count = count +1
        current_file_upload_status(the_file,count,len(entries))


    global uploaded
    uploaded = True

def if_connected():
    try:
        socket.create_connection(("1.1.1.1", 53))
        return True
    except OSError:
        pass



def start():
    if if_connected() == True:
        print("\nConnection estabelished \nuploading")
        upload(LOCAL_PATH, "ORIGINAL")
        print("CREATING BACKUP")
        upload(LOCAL_PATH, "BACKUP")
        if uploaded == True:
            print("process finished")
        else:
            print("upload unsuccessfull due to some other error")
    else:
        print("no connection\nupload unsuccessful")
        logging.error('{} no connection, upload uncuccessful '.format(now.strftime("%d/%m/%Y %H:%M:%S")))




