import os
import shutil
import datetime
import argparse
from distutils.dir_util import copy_tree

def create_timestamp_result_dir():
    if not DEBUG:
        if not os.path.exists(RESULTS_DIR):
            os.mkdir(RESULTS_DIR)

        timestamp = str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S_"))
        latest_RESULTS_DIR_name = timestamp + TEST_SUITE_NAME
        latest_RESULTS_DIR_path = os.path.join(ROOT_DIR, RESULTS_DIR, latest_RESULTS_DIR_name)
        os.mkdir(latest_RESULTS_DIR_path)
        return latest_RESULTS_DIR_path

def copy_results(destinations):
    # HTML
    if os.path.exists(REPORT_HTML_FOLDER):
        copy_tree(REPORT_HTML_FOLDER, destinations)

    # XML
    if os.path.exists(REPORT_XML_FILE):
        shutil.copy(REPORT_XML_FILE, destinations)

    # VIDEO
    if os.path.exists(VIDEO_FILE):
        shutil.copy(VIDEO_FILE, destinations)

def delete_html_folder():
    # HTML
    if os.path.exists(REPORT_HTML_FOLDER):
        shutil.rmtree(REPORT_HTML_FOLDER)

####################################################################################
# Get the argument about the test from command line 
# 'python runner.py smoke_tests' - smoke_tests is the 1st Argument sys.argv[1]
####################################################################################
parser = argparse.ArgumentParser()
parser.add_argument("--set", help="echo the string you use here")
parser.add_argument("--debug", action="store_true", default=False)
args = parser.parse_args()
print(args)

TEST_SUITE_NAME = args.set
DEBUG = args.debug # default is False

####################################################################################
# Asign paths to constants
# Get Current Working Dir - The folder where Python is operating at the moment - C:\framework
####################################################################################
ROOT_DIR = os.getcwd() 
TOOLS_DIR = os.path.join(ROOT_DIR, 'tools')
CONTENT_DIR = os.path.join(ROOT_DIR, 'content')
RESULTS_DIR = os.path.join(ROOT_DIR, 'results')
JENKINS_DIR = os.path.join(RESULTS_DIR, 'jenkins')
CURRENT_TESTS = os.path.join(ROOT_DIR, 'tests', TEST_SUITE_NAME + '.py')
LATEST_RESULTS_DIR = create_timestamp_result_dir()

REPORT_HTML_FOLDER = os.path.join(ROOT_DIR, "Report_html")
REPORT_XML_FILE = os.path.join(ROOT_DIR, "Report.xml")
VIDEO_FILE = os.path.join(ROOT_DIR, "Video.avi")


# Tools paths
FFMPEG_EXE = os.path.join(TOOLS_DIR, 'video_recorder', 'ffmpeg.exe')
TEXTBOX_EXE = os.path.join(TOOLS_DIR, 'textbox', 'Textbox.exe')
TEXTBOX_TXT = os.path.join(TOOLS_DIR, 'textbox', 'textbox.txt')


delete_html_folder()

####################################################################################
# PRECONDITIONS - Start Video Recording and Textbox
####################################################################################
if not DEBUG:
    os.system("taskkill /im ffmpeg.exe")
    os.system("taskkill /im Textbox.exe")
    os.system(r'start ' + TEXTBOX_EXE + ' ' + TEXTBOX_TXT)
    os.system(r'start ' + FFMPEG_EXE + ' -f gdigrab -framerate 15 -i desktop -q:v 5 Video.avi -y')

####################################################################################
# Assemble the command used to run the set
# call C:\ui-automation\Sikuli\runsikulix.cmd -r C:\ui-automation\Tests\smoke_tests.sikuli
####################################################################################
command ="python " + CURRENT_TESTS
print(command)

####################################################################################
####################################################################################
# RUN TESTS
####################################################################################
os.system("fake cmd") # workaround for colorization
os.system(command)

####################################################################################
# POSTCONDITIONS - Kill all leftovers - Video Recording + Textbox
####################################################################################
if not DEBUG:
    copy_results(LATEST_RESULTS_DIR)
    copy_tree(LATEST_RESULTS_DIR, JENKINS_DIR)
    delete_html_folder()
    os.system("taskkill /im ffmpeg.exe")
    os.system("taskkill /im Textbox.exe")

