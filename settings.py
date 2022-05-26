import os


ROOT_DIR = os.path.abspath(os.curdir)
print(ROOT_DIR , "ROOT_DIR")

PYTHON_USER_BACKEND_END_POINT = '/user/get_data'

USER_BACKEND_PROJECT_DIR = ROOT_DIR + "/user_projects/aerothon_python_user_backend"

FRONT_END_PROJECT_DIR = {
	"blog" : ROOT_DIR + "/user_projects/airothon_blog_web",
	"org" : "",
}

SERVER_IP_ADDRESS = "http://frontendmain-env.eba-9qrg8xzc.us-west-2.elasticbeanstalk.com"