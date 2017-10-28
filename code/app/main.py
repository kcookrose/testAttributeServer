from arguments import set_up_arguments
import os
import subprocess

import classifiers

args = set_up_arguments()

print(classifiers.modules)
#with open(args.portrait) as portrait:
for module in classifiers.modules:
	print(dir(module))
	module.classify(os.path.abspath(args.portrait))
#    for root, dirs, files in os.walk("./classifiers/"):
#        for file in files:
#            subprocess.check_output("python {0} --image {1}".format(os.path.abspath(os.path.join(root, file)), os.path.abspath("./{0}".format(args.portrait))))
