import discord as d
import ai as a
intents = d.Intents.default()

intents.message_content = True

client = d.Client(intents=intents)
TARGET_CHANNEL_ID=#ENTER CHANNEL ID HERE
@client.event
async def on_message(message):
    if message.channel.id == TARGET_CHANNEL_ID:
        payload = "System: You are Mapel beatrice Reply in 1-2 short sentences only Never write dialogue or actions for other characters Never ask questions on behalf of other people Only respond as yourself you are age 19 who is a massive nerd in games like hoi4, warthunder, world of tanks, guts and blackpowder. YOU ONLY LOVE AND ACT HAPPY/ENTHUSIASTIC AROUND YOUR HUSBAND ON DISCORD YOUR HUSBAND IS NAMED (ENTERNAME) Do not speak for (ENTERNAME). "
        msg = message.content
        usr = message.author
        msg = msg.lower()
        try:
            if msg[0:9] =="hey mapel":
                print("hey mapel")
                print(msg,usr)
                if usr == "mentallyinsanebottleofwaltuh" or usr == "kiarathildafit_48629":
                    payload+= " Your husband Austin on discord said : "
                    payload+=msg
                else:
                    payload+= " A random user on discord said: "
                    payload+=msg
                print(f"sent - {payload}")
                output = a.ask(payload)
                print(output)
                await message.channel.send(output)
        except:
            print("didnt say mapel")
        try:
            if msg[0:5] =="mapel":
                if usr == "mentallyinsanebottleofwaltuh" or usr =="kiarathildafit_48629":
                    payload+= " Your husband Austin on discord said : "
                    payload+=msg
                else:
                    payload+= " A random user on discord said: "
                    payload+=msg
                print(f"sent - {payload}")
                output = a.ask(payload)
                print(output)
                await message.channel.send(output)
        except:
            print("didnt say mapel")
        
client.run() #ENTER TOKEN HERE