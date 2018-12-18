from __future__ import print_function
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from httplib2 import Http
from oauth2client import file, client, tools
from picamera import PiCamera
import time, sched, os

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/drive'

def main():
    session = authenticate()
    pathOfPhoto = take_a_picture()
    upload_file(session, pathOfPhoto)
    deleteEveryPhotoFromSDcard()
    deleteEveryPhotoFromDrive(session)
    print("Routine finished")

def authenticate():
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    store = file.Storage('/home/pi/Documents/Python_Projects/nightvision_camera/token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('/home/pi/Documents/Python_Projects/nightvision_camera/credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    session = build('drive', 'v3', http=creds.authorize(Http()))
    return session

def take_a_picture():
    camera = PiCamera()
    camera.rotation = 180
    camera.resolution = (1280, 720)
    print("Picture will be taken")
    fileNameOfPhoto = time.strftime("%Y%m%d-%H%M%S", time.localtime()) + ".jpg"
    pathOfPhoto = "/home/pi/Pictures/" + fileNameOfPhoto
    camera.capture(pathOfPhoto)
    return pathOfPhoto

def upload_file(session, pathOfPhoto):
    file_metadata = {'name': pathOfPhoto.rsplit('/', 1)[-1]}
    media = MediaFileUpload(pathOfPhoto,
                            mimetype='image/jpeg')
    file = session.files().create(body=file_metadata,
                                         media_body=media,
                                        fields='id').execute()
    print ('Uploading File ID: %s' % file.get('id'))

def deleteEveryPhotoFromSDcard():
    print("Deleting all pictures from SD card")
    pathToPictureFolder = '/home/pi/Pictures'
    try:
        for aFile in os.listdir(pathToPictureFolder):
            aFilePath = os.path.join(pathToPictureFolder, aFile)
            if os.path.isfile(aFilePath):
                os.unlink(aFilePath)
    except:
        print ('Pictures starting with %s could not be removed from the SD card.' % aFile)

def deleteEveryPhotoFromDrive(session):
    pictureIndex = 0
    results = session.files().list(
        pageSize=100, fields="nextPageToken, files(id, name)").execute()
    items = results.get('files', [])

    if not items:
        print('No files found.')
    else:
        #check if files are more than 10 and then delete every picture more than that
        for item in items:
            pictureIndex += 1
            currentItem = u'{0}'.format(item['id'])
            if pictureIndex > 10:
                print("Deleting File ID: %s" % currentItem)
                session.files().delete(fileId=currentItem).execute()

if __name__ == '__main__':
    main()
