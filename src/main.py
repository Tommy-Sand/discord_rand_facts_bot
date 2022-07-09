import discord, requests, json
from continuous_hosting import keep_alive

def random_facts():
    header = {"X-Api-Key": "Enter your ninja-api key"}
    html_response = requests.get("https://api.api-ninjas.com/v1/facts?limit=1", headers=header)
    if html_response.status_code != 200:
        return "Something went wrong: We were unable to fetch a fact for you" 
    return json.loads(html_response.text)

if(__name__ == '__main__'):
    client = discord.Client()

    @client.event
    async def on_ready():
        print("We have logged in as {0.user}".format(client))

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        
        if message.content == 'gib fact':
            content = random_facts()
            await message.channel.send(content[0]['fact'])
    keep_alive()
    client.run('Enter your token id')