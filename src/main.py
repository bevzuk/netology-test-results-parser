# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START sheets_quickstart]
from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# If modifying these scopes, delete the file token.json.
from src.results_report import ResultsReport

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# The ID and range of a sample spreadsheet.
SPREADSHEET_ID = '1n-zEOZjuthfiBT9yhw06WrSTzZfcLRVwtjfyL9yFgxk'
RESPONSES_RANGE_NAME = "'Teст Scrum'!B2:V1000"
CORRECT_RESPONSES_RANGE_NAME = "'Ответы'!B6:V8"
SUMMARY_RANGE_NAME = "'Ответы'!A12"
ANSWERS_RANGE_NAME = "'Ответы'!A40"


def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
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

    # Call the Sheets API
    sheet = service.spreadsheets()
    responses = sheet.values() \
        .get(spreadsheetId=SPREADSHEET_ID, range=RESPONSES_RANGE_NAME) \
        .execute() \
        .get('values', [])

    correct_responses = sheet.values() \
        .get(spreadsheetId=SPREADSHEET_ID, range=CORRECT_RESPONSES_RANGE_NAME) \
        .execute() \
        .get('values', [])

    report = ResultsReport(correct_responses[1], correct_responses[2], responses)
    summary = report.summary_sorted_by_count()
    for line in summary:
        print("%s\t%s" % (line[0], line[1]))

    write_to_sheet(service, summary, SUMMARY_RANGE_NAME)

    answers = report.answers()
    for line in answers:
        print(line)

    write_to_sheet(service, answers, ANSWERS_RANGE_NAME)

    add_named_ranges(service, answers)


def write_to_sheet(service, summary, range):
    body = {
        'values': summary
    }
    result = service.spreadsheets().values().update(
        spreadsheetId=SPREADSHEET_ID, range=range,
        valueInputOption="RAW", body=body).execute()
    print('{0} cells updated.'.format(result.get('updatedCells')))


def add_named_ranges(service, answers):
    offset = 40
    index = 0
    number = 1
    while index < len(answers):
        if answers[index] == ['']:
            start_index = index + 1
            end_index = start_index
            while end_index < len(answers) and answers[end_index] != ['']:
                end_index = end_index + 1
            start_row = offset + start_index
            end_row = start_row + (end_index - start_index) - 1
            range_name = "Answers_%02d" % number
            add_named_range(service, range_name, 0, start_row, 2, end_row)
            number = number + 1
            index = end_index
        else:
            index = index + 1


def add_named_range(service, name, start_column_index, start_row_index, end_column_index, end_row_index):
    body = {
        "requests": [
            {
                "deleteNamedRange": {
                    "namedRangeId": name
                }
            },
            {
                "addNamedRange": {
                    "namedRange": {
                        "name": name,
                        "range": {
                            "sheetId": 0,
                            "startColumnIndex": start_column_index,
                            "startRowIndex": start_row_index,
                            "endColumnIndex": end_column_index,
                            "endRowIndex": end_row_index
                        },
                        "namedRangeId": name
                    }
                }
            }
        ]
    }
    request = service.spreadsheets().batchUpdate(spreadsheetId=SPREADSHEET_ID,
                                                 body=body)
    response = request.execute()


if __name__ == '__main__':
    main()
# [END sheets_quickstart]
