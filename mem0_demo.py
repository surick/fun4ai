from mem0 import MemoryClient
client = MemoryClient(api_key="m0-ng9qq33dKoUkNnc413sgpee8JPUwSfgKnzIDrFPx")
messages = [
    {"role": "user", "content": "Hi, I'm Alex. I'm a vegetarian and I'm allergic to nuts."},
    {"role": "assistant", "content": "Hello Alex! I've noted that you're a vegetarian and have a nut allergy. I'll keep this in mind for any food-related recommendations or discussions."}
]
client.add(messages, user_id="alex")

