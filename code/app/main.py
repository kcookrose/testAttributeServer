import classifiers
from arguments import set_up_arguments
import os

args = set_up_arguments()

for module in classifiers.modules:
	prediction = module.classify(os.path.abspath(args.portrait))
	print(prediction)