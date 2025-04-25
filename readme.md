# Discord Server Nuker

A powerful Discord bot for server destruction. This tool is designed for educational purposes only to demonstrate Discord server security vulnerabilities.

⚠️ **DISCLAIMER: Use at your own risk. Using this tool on servers without explicit permission is against Discord's Terms of Service and may result in your account being banned. The author takes NO responsibility for any damages caused by this tool.**

## Features

- Complete server takeover
- Deletes all channels and creates spam channels
- Deletes all emojis
- Creates mass spam roles
- Bans all members (except owner and protected users)
- Deletes all invites
- Spams messages in all created channels
- Configurable through a simple JSON file

## Setup

1. Clone the repository
   ```
   git clone https://github.com/yourusername/discord-server-nuker.git
   cd discord-server-nuker
   ```

2. Install the required dependencies
   ```
   pip install discord.py
   ```

3. Configure the bot by editing `config.json`
   - The file will be automatically created on first run
   - Or create it manually using the template below

4. Run the bot
   ```
   python main.py
   ```

## Configuration

The bot uses a `config.json` file with the following structure:

```json
{
    "bot_token": "YOUR_BOT_TOKEN_HERE",
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
```

### Configuration Options

- `bot_token`: Your Discord bot token
- `guild_name`: Name to rename the server to
- `channel_name`: Name for all created spam channels
- `spam_message`: Message to spam in all channels
- `targeted_user_id`: User ID that can activate the nuke (0 = anyone)
- `target_server_ids`: List of server IDs that can be nuked (empty = any server)
- `protected_user_id`: User ID that cannot be banned
- `channel_topics`: List of random topics for created channels
- `nuke_command`: Command to trigger the nuke (default is "!test")

## Usage

1. Invite the bot to a server with administrator permissions
2. Type the configured command (default: `!test`) in any channel
3. Watch the destruction

## Security Features

- Server targeting: Only works on specified server IDs if configured
- User targeting: Only activates for specified user IDs if configured
- Protected users: Specified users won't be banned

## License

This project is released under the MIT License. See the LICENSE file for details.

## Contributions

Contributions are welcome! Please feel free to submit a Pull Request.

## Contact

For questions or concerns, please open an issue on this repository.

---

Remember: With great power comes great responsibility. Use this tool ethically and legally.