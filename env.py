import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
apiKeyName = ''
apiKey = os.getenv('TicketMasterAPIKey')
