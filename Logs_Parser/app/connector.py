'''
Author: Rishabh Sharma

'''

import os
import subprocess

from app.parser import main

CURR_PATH = os.path.dirname(os.path.realpath(__file__))
SCRIPT_PATH = os.path.realpath(os.path.join(CURR_PATH, "script+to_run"))


def run_command(script_name, script_dir, *args, **kwargs):
    p = subprocess.Popen(["python", os.path.join(script_dir, script_name)] + list(args), stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT, cwd=script_dir, shell=True)
    stdout, stderr = p.communicate()
    return_code = p.wait()
    return return_code, stdout.rstrip()


def get_bpm_information(result_dict, target_name):
    if result_dict and result_dict["b"] and result_dict["p"] and result_dict["m"]:
        bid_pid_mid_res_tup = run_command("script1.py", SCRIPT_PATH, target_name, result_dict["b"][0],
                                          result_dict["p"][0], result_dict["m"][0])
    else:
        bid_pid_mid_res_tup = ("unknown", "Unknown=Unknown")

    if bid_pid_mid_res_tup[1].split("=")[-1] == " unknown":
        result_dict["BPM"] = ["unknown", "Not able to decode B/P/M information"]
    elif bid_pid_mid_res_tup[0] == 0:
        result_dict["BPM"] = [bid_pid_mid_res_tup[1].split("=")[-1],"This is the information"]
        if "not supported" not in result_dict["BPM"][0]:
            if result_dict["Access_Type"][1] == "External module is trying to Read a area which is protected":
                result_dict["Access_Type"][1] = str(
                    result_dict["BPM"][0]) + " is trying to Read a area which is protected"
            else:
                result_dict["Access_Type"][1] = str(
                    result_dict["BPM"][0]) + " is trying to Write a area which is protected"
    else:
        result_dict["BPM"] = list(bid_pid_mid_res_tup)


def some_function(log_string):
    result_dict, result_dict1 = main(log_string)
    return result_dict, result_dict1
