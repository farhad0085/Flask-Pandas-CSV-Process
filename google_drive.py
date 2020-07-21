from apiclient import discovery
from httplib2 import Http
from oauth2client import client, tools
import os

def upload_file(files):
    from oauth2client import file
    SCOPES = 'https://www.googleapis.com/auth/drive'
    store = file.Storage(os.path.dirname(os.path.realpath(__file__))+'/token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets(os.path.dirname(os.path.realpath(__file__))+'/client_secrets.json', SCOPES)
        creds = tools.run_flow(flow, store)
    DRIVE = discovery.build('drive', 'v3', http=creds.authorize(Http()))

    folder_id = "1KOH4_ddjwtWJcNDO8HXtxyrjXuOMgI4U"  # change this id

    result_ids = []

    for file in files:
        path, filename = os.path.split(file)
        metadata = {'name': filename,
                    'parents': [folder_id]}

        res = DRIVE.files().create(body=metadata,
                                   media_body=file,
                                   fields='parents,id').execute()

        result_ids.append(res.get('id'))

    return result_ids

if __name__ == "__main__":
    upload_file(['NLG.py']) # you don't need to follow this.