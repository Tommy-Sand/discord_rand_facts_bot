import discord, requests
from continuous_hosting import keep_alive

def random_facts():
    header = {"X-Api-Key": "Add-Your-API-key"}
    html_response = requests.get("https://api.api-ninjas.com/v1/facts?limit=1", headers=header)
    if html_response.status_code != 200:
        return "Something went wrong: We were unable to fetch a fact for you" 
    else:
        print(html_response.text)
    return html_response.content

if(__name__ != '__main__'):
    facts = []
    client = discord.Client()

    @client.event
    async def on_ready():
        print("We have logged in as {0.user}".format(client))

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        
        if message.content == 'gib fact':
            if facts == []:
                content = random_facts()
            await message.channel.send(content[0]["fact"])
    keep_alive()
    client.run('Add bot token')