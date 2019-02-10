import sys
import subprocess
import datetime
import os
def file_create(script_name, script_text):
    file_create = open(script_name + '.py', 'w')
    file_create.close()

    with open(script_name + '.py', 'r+') as file:
 
        file.write(str(script_text))
        file.close()

def startjob(script_name):
	os.chdir('..')
	os.chdir('..')
	os.chdir('Script_Creator')
	os.chdir('scripts')
	file = open(script_name + '.py', 'r')
	script_text = file.read()
	file.close()
	os.chdir('..')




	os.chdir('..')
	os.chdir('jobs')
	os.chdir(script_name)
	time = str(datetime.datetime.now())[:19].replace(' ', '_')
	time = time.replace('-', '.')
	time = time.replace(':', '.')
	os.mkdir(time) 
	os.chdir(time)
	file_create(script_name, script_text)
	process = subprocess.Popen('python ' + script_name + '.py', stdout=subprocess.PIPE, shell=True)
	data = process.communicate()
	code = process.poll()
	if code == 0:
	    code = "Completed"
	else:
	    code = 'Error'
	history = open(script_name+'_log'+'.txt', 'w')
	history.write('Status - '+ code + '\n')
	history.write(str(data[0]))

	#history = History(host_script=user, active_user=request.user, console_output=str(data[0]), status=code,
	 #                 run_time=str(datetime.datetime.now())[:19])
	#history.save()
	

if '__main__':
	startjob(sys.argv[1])