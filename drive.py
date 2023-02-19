from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


def get_drive():
	gauth = GoogleAuth()
	gauth.LocalWebserverAuth()
	drive = GoogleDrive(gauth)
	return drive


def upload_to_drive(drive, upload_file_list, parent_id):

	for upload_file in upload_file_list:
		gfile = drive.CreateFile({'parents': [{'id': parent_id}]})
		gfile.SetContentFile(upload_file)
		gfile['title'] = upload_file.split('/')[-1]
		gfile.Upload()
