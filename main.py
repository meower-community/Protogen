from dotenv import dotenv_values
from MeowerBot import Bot
from supporter import message_handler, CommandList

config = dotenv_values(".env")
protogen = Bot(autoreload=1)
protogen.prefixes = ("@gen ", "@Proto ", "@Protogen ")
commands = CommandList()

# Replace the default message handler with our own
protogen.callback(message_handler, cbid="message") 

# ----------------------------------------------------------------

@commands.info("help", "Shows this message")     
@protogen.command("help")
def help(ctx, *args):
    main_prefix = protogen.prefixes[0]

    help_msg = f"Here are the commands: "
    
    for name, desc in commands.as_pairs():
        help_msg += f"\n{main_prefix}{name} - {desc}"
        
    ctx.send_msg(help_msg)

# ----------------------------------------------------------------

protogen.run("Protogen", config["password"])