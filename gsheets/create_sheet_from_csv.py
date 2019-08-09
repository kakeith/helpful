from pprint import pprint
import pickle, os, argparse 
from googleapiclient import discovery

"""
Goal: create a Google sheets from csv file 

Main helpful reference: 
https://stackoverflow.com/questions/42362702/how-to-import-a-csv-file-using-google-sheets-api-v4
"""
def get_creds():
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    fname = os.getenv("HOME")+'/helpful/gsheets/token.pickle'
    print(fname)
    if not os.path.exists(fname): 
        raise Exception('Create '+fname+ ' first by downloading credentials.json and following https://developers.google.com/sheets/api/quickstart/python')
    with open('token.pickle', 'rb') as token:
        creds = pickle.load(token)
    return creds 

#https://stackoverflow.com/questions/42362702/how-to-import-a-csv-file-using-google-sheets-api-v4
def push_csv_to_gsheet(csv_path, credentials, sheet_title):
    #create spreadsheet 
    properties = {
        'properties': {
            'title': sheet_title 
        }
        
    }
    service = discovery.build('sheets', 'v4', credentials=credentials)
    request = service.spreadsheets().create(body=properties)
    response = request.execute()
    spreadsheetID = response['spreadsheetId']
    spreadsheetUrl = response['spreadsheetUrl']

    #paste the csv into the spreadsheet 
    print('reading in ->', csv_path)
    with open(csv_path, 'r') as csv_file:
        csvContents = csv_file.read()
    body ={
    'requests': [{
            'pasteData': {
                "coordinate": {
                    "rowIndex": "0",  # adapt this if you need different positioning
                    "columnIndex": "0", # adapt this if you need different positioning
                },
                "data": csvContents,
                "type": 'PASTE_NORMAL',
                "delimiter": ',',
            }
        }]
    }
    request = service.spreadsheets().batchUpdate(spreadsheetId=spreadsheetID, body=body)
    response = request.execute()
    print('SUCCESSFULLY UPLOADED CSV')
    print('gsheets_title=', sheet_title)
    print('gsheets_url=', spreadsheetUrl)

def upload_csv_file_to_google_sheets(csv_path, sheet_title): 
    credentials = get_creds()
    #sheet_id = create_new_worksheet()
    push_csv_to_gsheet(csv_path, credentials, sheet_title)

def test_small_csv():
    csv_path = 'small_csv.csv'
    sheet_title = 'test_upload_api'

if __name__ == "__main__": 
    #test_small_csv() 

    #EXAMPLE USAGE: python create_sheet_from_csv.py small_csv.csv blah
    parser = argparse.ArgumentParser()
    parser.add_argument("csv_path", type=str)
    parser.add_argument("sheet_title", type=str)
    args = parser.parse_args()
    upload_csv_file_to_google_sheets(args.csv_path, args.sheet_title)
