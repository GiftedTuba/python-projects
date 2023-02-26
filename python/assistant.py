# Initial message used by assistant

name = input("Hello! My name is Acadia, your all in one personal assistant? What is your name? ")
print(name)

# Assistant takes name

print(f"\nNice to meet you, {name}. I hope we can grow as friends.")

# Starts intial question
firstcommand = input("What would you like to do? ")

def functions():
	try:
		if firstcommand == 'Help' or 'help':
			help_command = """I can do many things, like: 
			Weather: Check the weather 
			Quit: Quit the current session
			Open: Open an application that you have installed"""
			print(help_command)
		return

		if firstcommand == 'quit' or 'Quit':
			quit_command = "I am now shutting down. See you soon!"
			print(quit_command)
		return

	except:
		print(f"I'm sorry, {name.title()}, but I don't understand.")