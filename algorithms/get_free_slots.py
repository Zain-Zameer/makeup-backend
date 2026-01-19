from dotenv import load_dotenv
import os
from supabase import create_client,Client

load_dotenv()

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase : Client =  create_client(url,key)

DAY = "Monday"
LR = "12"

THRESHOLD = 18

data = supabase.table("lr_reserved").select("start_time,end_time").eq("lr",LR).eq("day",DAY).order("start_time").execute()

free_slots = []

if data.data:
    j = 8 
    for i in data.data:
        free_slot = {}
        if j != i['start_time']:
            free_slot = {"start_time":j,"end_time":i['start_time']}
        j = i['end_time']
        free_slots.append(free_slot)
    if j!=18:
        free_slots.append({"start_time":j,"end_time":18})

print(free_slots)
            
