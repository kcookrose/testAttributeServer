from arguments import set_up_arguments
import os
import subprocess

args = set_up_arguments()

with open(args.portrait) as portrait:
    for root, dirs, files in os.walk("./classifiers/"):
        for file in files:
            subprocess.check_output("python {0} --image {1}".format(os.path.abspath(os.path.join(root, file)), os.path.abspath("./{0}".format(args.portrait))))
