# This function parses messages for commands
from rich import print, markup

def message_handler(msg, bot):
    # Return if message is not of someone using the bot
    if msg.user.username == bot.username \
      or not msg.data.startswith(bot.prefixes):
        return
    
    # Just logs the command used
    print(f"[bold turquoise4]\[{msg.chat}][/bold turquoise4] [cyan3]{msg.user.username}[/cyan3]: {markup.escape(msg.data)}")

    # Remove all the prefixes so that just the command and arguments remain
    for i in bot.prefixes:
        msg.data = msg.data.removeprefix(i)
    
    bot.run_command(msg)

class CommandList:
    def __init__(self):
        self.commands = {}
    def as_pairs(self):
        return self.commands.items()
    def info(self, name, desc):
        def inner(*args, **kwargs):
            self.commands.update({name: desc})
        return inner
