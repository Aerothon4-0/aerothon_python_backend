import subprocess
import sys
import getopt


def create_docker(app,port,env_var,url,token):
	print("--before docker image build--")
	bashCommand = "sudo docker build -t {} .".format(app)
	output = subprocess.check_output(['bash','-c', bashCommand])
	print("--after docker image build--")

	print("--before docker container build--")
	bashCommand = "sudo docker run -d -p {}:3000 -e APP='{}' -e TOKEN='{}' -e APP_PORT='{}' -e URL='{}' --name={}  {}".format(port,env_var,token,port,url,app,app)
	output = subprocess.check_output(['bash','-c', bashCommand])
	print("--after docker container build--")

def delete_docker(app):
	print("--before delete docker container--")
	bashCommand = "sudo docker rm $(sudo docker stop $(sudo docker ps --filter name={} -q) )".format(app)
	output = subprocess.check_output(['bash','-c', bashCommand])
	print("--after delete docker container--")

def get_options(argv):
	option_list = []
	for index in range(1,len(argv),2):
		temp_opt = (argv[index],argv[index+1])
		option_list.append(temp_opt)

	return option_list

def main(argv):
	app_name = ""
	port = ""
	script_type = ""
	env_var = ""
	token = ""
	url=""
	try:
		opts = get_options(argv)
	except Exception as e:
		print(e)
		sys.exit(2)

	for opt, arg in opts:
		if opt in ("-h", "--help"):
			sys.exit(2)
		elif opt in ("-a", "--app_name"):
			app_name = arg
		elif opt in ("-p", "--port"):
			port = arg
		elif opt in ("-t", "--type"):
			script_type = arg
		elif opt in ("-e", "--env"):
			env_var = arg
		elif opt in ("-u", "--url"):
			url = arg
		elif opt in ("--token"):
			token = arg


	print('app_name:', app_name)
	print('user:', port)
	print('script_type:', script_type)
	print('app:', env_var)
	print('token:', token)
	print('url:', url)

	if script_type == 'create' and app_name and port:
		create_docker(app_name,port,env_var,url,token)
	elif script_type == 'delete' and app_name:
		delete_docker(app_name)



if __name__ == "__main__":
    main(sys.argv)

#sudo python start.py -a "python_backend" -p 5001 -e Alans -u "url" --token 40b1abb5db2011ecb95ec809a8853d3d -t create