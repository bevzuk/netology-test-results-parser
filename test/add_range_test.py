from __future__ import print_function

import pytest
import requests
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SPREADSHEET_ID = '1n-zEOZjuthfiBT9yhw06WrSTzZfcLRVwtjfyL9yFgxk'
CORRECT_RESPONSES_RANGE_NAME = "'Ответы'!B6:V8"

def test_add_range():
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'src/client_secret_811500274556-qnrv0sotc9l4ne140baro3c6nndo187e.apps.googleusercontent.com.json',
                SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('sheets', 'v4', credentials=creds)

    body = {
      "requests": [
          {
              "deleteNamedRange": {
                "namedRangeId": "Answers_01"
              }
          },
        {
          "addNamedRange": {
            "namedRange": {
              "name": "Answers_01",
              "range": {
                "sheetId": 0,
                "startColumnIndex": 0,
                "startRowIndex": 41,
                "endColumnIndex": 2,
                "endRowIndex": 67
              },
              "namedRangeId": "Answers_01"
            }
          }
        }
      ]
    }
    request = service.spreadsheets().batchUpdate(spreadsheetId=SPREADSHEET_ID,
                                                 body=body)
    response = request.execute()

    # TODO: Change code below to process the `response` dict:
    print(response)
