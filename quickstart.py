from __future__ import print_function

import datetime
import os.path
import pytz

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar']


def main():
    creds = None

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json')

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'E:\\Arquivos de Programas\\Projetos VS Code\\projetos\\SukitoFilms\\credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('calendar', 'v3', credentials=creds)
        now = datetime.datetime.utcnow().isoformat() + 'Z' 

        print('Getting the upcoming 10 events')
        events_result = service.events().list(calendarId='1a7439756e4f899cd615b16694ab5c062b7aa827cb299bb95aac56aec9c8ae52@group.calendar.google.com', timeMin=now,
                                              maxResults=10, singleEvents=True,
                                              orderBy='startTime').execute()
        events = events_result.get('items', [])

        if not events:
            print('No upcoming events found.')
            return


        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            start_datetime = datetime.datetime.fromisoformat(start)
            local_timezone = pytz.timezone('America/Sao_Paulo')
            localized_start = start_datetime.astimezone(local_timezone)
            formatted_start = localized_start.strftime('%d-%m-%Y %H:%M:%S')
            print(formatted_start, event['summary'])
            print('Event ID:', event['id'])
            print('-----------------------')

    except HttpError as error:
        print('An error occurred: %s' % error)

def create_watched(nome, data_add, data, tipo, nota, gen1, gen2, stream, prod):
    creds = None

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json')

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'E:\\Arquivos de Programas\\Projetos VS Code\\projetos\\SukitoFilms\\credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('calendar', 'v3', credentials=creds)
        event = {
            'summary': nome,
            'location': stream,
            'description': f"Nota: {nota} \nTipo: {tipo} \nGenero: {gen1} e {gen2} \nProdução: {prod} \nAno Lançamento: {data}",
            'start': {
                'dateTime': f'{data_add}T09:00:00-03:00',
                'timeZone': 'America/Sao_Paulo',
            },
            'end': {
                'dateTime': f'{data_add}T17:00:00-03:00',
                'timeZone': 'America/Sao_Paulo',
            },
            'recurrence': [
                'RRULE:FREQ=DAILY;COUNT=1'
            ],
            }

        event = service.events().insert(calendarId='6697c707d51f3e6c11b926da14a9f3fbcce366efdef078cc3038c417c0795c58@group.calendar.google.com', body=event).execute()
        print(f"Event created: {event.get('htmlLink')}")
        

        start = event['start'].get('dateTime', event['start'].get('date'))
        start_datetime = datetime.datetime.fromisoformat(start)
        local_timezone = pytz.timezone('America/Sao_Paulo')
        localized_start = start_datetime.astimezone(local_timezone)
        formatted_start = localized_start.strftime('%d-%m-%Y %H:%M:%S')
        print(formatted_start, event['summary'])
        print('Event ID:', event['id'])
        print('-----------------------')

    except HttpError as error:
        print('An error occurred: %s' % error)  
    
    return event['id']  
    
    
def update_watched(id_calendar, nome, data_add, data, tipo, nota, gen1, gen2, stream, prod):
    creds = None

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json')

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'E:\\Arquivos de Programas\\Projetos VS Code\\projetos\\SukitoFilms\\credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('calendar', 'v3', credentials=creds)
        now = datetime.datetime.utcnow().isoformat() + 'Z' 


        event = service.events().get(calendarId='6697c707d51f3e6c11b926da14a9f3fbcce366efdef078cc3038c417c0795c58@group.calendar.google.com', eventId=id_calendar).execute()

        event['summary'] = nome
        event['location'] = stream
        event['description'] = f"Nota: {nota} \nTipo: {tipo} \nGenero: {gen1} e {gen2} \nProdução: {prod} \nAno Lançamento: {data}"
        event['start'] = {
                'dateTime': f'{data_add}T09:00:00-03:00',
                'timeZone': 'America/Sao_Paulo',
            }
        event['end'] = {
                'dateTime': f'{data_add}T17:00:00-03:00',
                'timeZone': 'America/Sao_Paulo',
            }

        update_evento = service.events().update(calendarId='6697c707d51f3e6c11b926da14a9f3fbcce366efdef078cc3038c417c0795c58@group.calendar.google.com', eventId=event['id'], body=event).execute()

        return update_evento['summary']


    except HttpError as error:
        print('An error occurred: %s' % error)

    
    
    

def create_future(nome, data, tipo, gen1, gen2, stream, prod, freque, ep_count):
    creds = None

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json')

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'E:\\Arquivos de Programas\\Projetos VS Code\\projetos\\SukitoFilms\\credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('calendar', 'v3', credentials=creds)
        event = {
            'summary': nome,
            'location': stream,
            'description': f"Tipo: {tipo} \nGenero: {gen1} e {gen2}\nProdução: {prod}",
            'start': {
                'dateTime': f'{data}T09:00:00-03:00',
                'timeZone': 'America/Sao_Paulo',
            },
            'end': {
                'dateTime': f'{data}T17:00:00-03:00',
                'timeZone': 'America/Sao_Paulo',
            },
            'recurrence': [
                f'RRULE:FREQ={freque};COUNT={ep_count}'
            ],
            'reminders': {
                'useDefault': False,
                'overrides': [
                {'method': 'email', 'minutes': 30}
                ],
            },
            }

        event = service.events().insert(calendarId='1a7439756e4f899cd615b16694ab5c062b7aa827cb299bb95aac56aec9c8ae52@group.calendar.google.com', body=event).execute()
        print('===================================')
        print(f" Evento criado: {event.get('htmlLink')}")
        

        start = event['start'].get('dateTime', event['start'].get('date'))
        start_datetime = datetime.datetime.fromisoformat(start)
        local_timezone = pytz.timezone('America/Sao_Paulo')
        localized_start = start_datetime.astimezone(local_timezone)
        formatted_start = localized_start.strftime('%d-%m-%Y %H:%M:%S')
        print(formatted_start, event['summary'])
        print(' Evento ID:', event['id'])
        print('===================================')

    except HttpError as error:
        print('An error occurred: %s' % error)  
    
    return event['id']  



def update(id_calendar, nome, data, tipo, gen1, stream, prod):
    creds = None

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json')

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'E:\\Arquivos de Programas\\Projetos VS Code\\projetos\\SukitoFilms\\credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('calendar', 'v3', credentials=creds)
        now = datetime.datetime.utcnow().isoformat() + 'Z' 


        event = service.events().get(calendarId='1a7439756e4f899cd615b16694ab5c062b7aa827cb299bb95aac56aec9c8ae52@group.calendar.google.com', eventId=id_calendar).execute()

        event['summary'] = nome
        event['location'] = stream
        event['description'] = f"Tipo: {tipo} \nGenero: {gen1} \nProdução: {prod}"
        event['start'] = {
                'dateTime': f'{data}T09:00:00-03:00',
                'timeZone': 'America/Sao_Paulo',
            }
        event['end'] = {
                'dateTime': f'{data}T17:00:00-03:00',
                'timeZone': 'America/Sao_Paulo',
            }

        update_evento = service.events().update(calendarId='1a7439756e4f899cd615b16694ab5c062b7aa827cb299bb95aac56aec9c8ae52@group.calendar.google.com', eventId=event['id'], body=event).execute()

        return update_evento['summary']


    except HttpError as error:
        print('An error occurred: %s' % error)





if __name__ == '__main__':
    main()


# comentar varias linhas = ctrl + ;