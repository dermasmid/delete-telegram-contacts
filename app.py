from pyrogram import Client


api_id = int()
api_hash = str()

app = Client('delete', api_id, api_hash)



with app:
    contacts = list(map(lambda user: user.id, app.get_contacts()))
    app.delete_contacts(contacts)