import datetime as dt
import os

import sqlalchemy as sa
from supabase import Client, create_client
from supabase.client import ClientOptions
from dotenv import load_dotenv

load_dotenv()

DB_URL: str = os.environ.get("SUPABASE_URL")
DB_KEY: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(
    DB_URL,
    DB_KEY,
    options=ClientOptions(postgrest_client_timeout=10, storage_client_timeout=10),
)


print(f"Hello {dt.datetime.now()}")

print(f"GITHUB_RUN_ID = {os.environ.get('GITHUB_RUN_ID')}")
print(f"GITHUB_SHA: {os.environ.get('GITHUB_SHA')}")
print(f"GITHUB_EVENT_NAME: {os.environ.get('GITHUB_EVENT_NAME')}")
print(f"GITHUB_JOB: {os.environ.get('GITHUB_JOB')}")

print(f"Message: { os.environ.get('GITHUB_EVENT_INPUTS_MESSAGE1') }")
print(f"Tags: {os.environ.get('INPUT_MESSAGE')}"
