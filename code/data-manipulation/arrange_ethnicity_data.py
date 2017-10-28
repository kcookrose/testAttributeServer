import argparse, os, shutil, warnings, glob

classes = ["Caucasian", "Asian", "Black", "Hispanic", "Multiracial"]

package_directory                           = os.path.dirname(os.path.abspath(__file__))
data_directory                              = os.path.join(package_directory, "../../datasets/")
ethnicity_directory                         = os.path.join(data_directory, "ethnicity/")
ethnicity_data_directory                    = os.path.join(data_directory, "ethnicity-data")
ethnicity_data_train_directory              = os.path.join(data_directory, "ethnicity-data/train")

ethnicity_data_train_caucasian_directory    = os.path.join(data_directory, "ethnicity-data/train/Caucasian")
ethnicity_data_train_asian_directory        = os.path.join(data_directory, "ethnicity-data/train/Asian")
ethnicity_data_train_black_directory        = os.path.join(data_directory, "ethnicity-data/train/Black")
ethnicity_data_train_hispanic_directory     = os.path.join(data_directory, "ethnicity-data/train/Hispanic")
ethnicity_data_train_multi_directory        = os.path.join(data_directory, "ethnicity-data/train/Multiracial")

ethnicity_data_val_directory                = os.path.join(data_directory, "ethnicity-data/val")
ethnicity_data_val_caucasian_directory      = os.path.join(data_directory, "ethnicity-data/val/Caucasian")
ethnicity_data_val_asian_directory          = os.path.join(data_directory, "ethnicity-data/val/Asian")
ethnicity_data_val_black_directory          = os.path.join(data_directory, "ethnicity-data/val/Black")
ethnicity_data_val_hispanic_directory       = os.path.join(data_directory, "ethnicity-data/val/Hispanic")
ethnicity_data_val_multi_directory          = os.path.join(data_directory, "ethnicity-data/val/Multiracial")

parser = argparse.ArgumentParser()
parser.add_argument("num_training_images", help="The number of per class images you want to train on.", type=int)
parser.add_argument("num_validation_images", help="The number of per class images you want to validate on.", type=int)
args = parser.parse_args()

num_training_images = args.num_training_images
num_validation_images = args.num_validation_images

def create_ethnicity_dirs():
    shutil.rmtree(ethnicity_data_directory, ignore_errors=True)
    try:
        os.mkdir(ethnicity_data_directory)

        os.mkdir(ethnicity_data_train_directory)          
        os.mkdir(ethnicity_data_train_caucasian_directory)
        os.mkdir(ethnicity_data_train_asian_directory)    
        os.mkdir(ethnicity_data_train_black_directory)    
        os.mkdir(ethnicity_data_train_hispanic_directory) 
        os.mkdir(ethnicity_data_train_multi_directory)    

        os.mkdir(ethnicity_data_val_directory)            
        os.mkdir(ethnicity_data_val_caucasian_directory)  
        os.mkdir(ethnicity_data_val_asian_directory)      
        os.mkdir(ethnicity_data_val_black_directory)      
        os.mkdir(ethnicity_data_val_hispanic_directory)   
        os.mkdir(ethnicity_data_val_multi_directory)      
    except:
        print("Error while creating ethnicity-data directories.")

create_ethnicity_dirs()

# We enumerate the image paths to get the corresponding index.
# Because the data is ordered, the gender can be found at that same index in the gender list.
# Depending on which gender we find, we copy the image over the corresponding folder.  
num_train_caucasian = 0
num_train_asian = 0
num_train_black = 0
num_train_hispanic = 0
num_train_multi = 0

num_val_caucasian = 0
num_val_asian = 0
num_val_black = 0
num_val_hispanic = 0
num_val_multi = 0

for file in glob.glob(os.path.join(ethnicity_directory, "Caucasian") +  "/*.jpg"):
    if num_train_caucasian < num_training_images:
        shutil.copy2(file, ethnicity_data_train_caucasian_directory)
        num_train_caucasian += 1
    elif num_val_caucasian < num_validation_images:
        shutil.copy2(file, ethnicity_data_val_caucasian_directory)
        num_val_caucasian += 1
    else:
        break

for file in glob.glob(os.path.join(ethnicity_directory, "Black") +  "/*.jpg"):
    if num_train_black < num_training_images:
        shutil.copy2(file, ethnicity_data_train_black_directory)
        num_train_black += 1
    elif num_val_black  < num_validation_images:
        shutil.copy2(file, ethnicity_data_val_black_directory)
        num_val_black += 1
    else:
        break

for file in glob.glob(os.path.join(ethnicity_directory, "Hispanic") +  "/*.jpg"):
    if num_train_hispanic < num_training_images:
        shutil.copy2(file, ethnicity_data_train_hispanic_directory)
        num_train_hispanic += 1
    elif num_val_hispanic  < num_validation_images:
        shutil.copy2(file, ethnicity_data_val_hispanic_directory)
        num_val_hispanic += 1
    else:
        break

for file in glob.glob(os.path.join(ethnicity_directory, "Asian") +  "/*.jpg"):
    if num_train_asian < num_training_images:
        shutil.copy2(file, ethnicity_data_train_asian_directory)
        num_train_asian += 1
    elif num_val_asian  < num_validation_images:
        shutil.copy2(file, ethnicity_data_val_asian_directory)
        num_val_asian += 1
    else:
        break

for file in glob.glob(os.path.join(ethnicity_directory, "Multiracial") +  "/*.jpg"):
    if num_train_multi < num_training_images:
        shutil.copy2(file, ethnicity_data_train_multi_directory)
        num_train_multi += 1
    elif num_val_multi  < num_validation_images:
        shutil.copy2(file, ethnicity_data_val_multi_directory)
        num_val_multi += 1
    else:
        break