
from smtplib import SMTP

class mail:
	# mail sender

	def __init__(self, host, port, sender, pwd, receiver):
		self.host = host # host
		self.port = port # port
		self.sender = sender # sender
		self.pwd = pwd # password
		self.receiver = receiver # reciever address
		self.header = 'From: Notification Service\nTo: ' + receiver + '\nSubject: '
		self.subject = self.msg = ''

	def set_subject(self, subject):
		self.subject = subject + '\n'

	def set_msg(self, msg):
		# set text of notification
		self.msg = msg

	def get_msg(self):
		# get the full text of message
		return self.header + self.subject + self.msg

	def send(self):
		server = SMTP(self.host, self.port)
		#server.connect(self.host, self.port) # connect to SMTP server
		#print("host:\t" + self.host + "\nport:\t" + self.port)
		server.starttls()
		server.login(self.sender, self.pwd) # login to SMTP server
		server.sendmail(self.sender, self.receiver, self.get_msg()) # send mail
		server.close()

def print_help():
	# help message
	hlp = "\n'mail_sender' sends a mail notification to specified address\n"
	hlp += "\ncommands:\n  --help\t\t\tshow this help message\n"
	hlp += "  --synopsis\t\t\tshow a short description\n"
	hlp += "  --bat={STRING}\t\tauthentication token, where STRING is in format 'username.hash\n"
	hlp += "  --send={user@mail.com}\tsend a mail notification to user@mail.com; the text of the\n"
	hlp += 4*"\t" + "notification message should be typed on the following lines"
	hlp += "\nVersion: 1.0"
	print (hlp)

def print_synopsis():
	# synopsis message
	print ("\nNotification mail sender.(v1.0)")

def send_mail(reciever, msg):
	host = 'smtp.gmail.com' # define host
	port = '587' # define port
	sender = 'e-mail@gmail.com' # define sender mail account
	pwd = 'password' # define sender password
	note = mail(host, port, sender, pwd, reciever) # create mail object
	note.set_subject('NOTIFICATION')
	note.set_msg(msg)
	#print(note.get_msg())
	note.send()
	print ('\nNotification sent to ' + note.receiver)


if __name__ == "__main__":
	cmd = input() # read command
	lines = [] # buffer for the next lines
	cur_line = '' # current line
	while cur_line != ".eot":
		if cur_line:
			lines.append(cur_line) # store previous line
		cur_line = input() # read current line

	if cmd == '--help': # process --help command
		print_help()
	elif cmd == '--synopsis': # process --synopsis command
		print_synopsis()
	elif cmd[:5] == '--bat': # process --bat command
		# extract username and hash from command line and print
		[username, hashtag] = cmd.split('=')[1].strip().split('.') # extract
		print('\nusername:\t' + username + '\nhash:\t\t' + hashtag) # print
	elif cmd[:6] == '--send': # process --send command
		# extract mail address from command line
		send_mail(cmd.split('=')[1].strip(), '\n'.join(lines))
	else: # incorrect input
		print('ERROR: Incorrect command.\nSee help:')
		print_help()


