import mechanize, time
class vars:
	browser = mechanize.Browser()
	browser.set_handle_robots(False)
	browser.set_handle_equiv(True)
	browser.set_handle_redirect(True)
class ViewBot:
	def __init__(self, link):
		#Initalize our ViewBot Object
		pass
	@classmethod
	def view(self):
		for i in range(3):
			vars.browser.open("https://www.youtube.com/watch?v=6Dh-RL__uN4")
			time.sleep(3)
def run():
	ViewBot.view()
	print("Viewed 'Bitch Lasagna' 3 times.")
run()
