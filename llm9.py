# LLM-powered medical diagnosis system
diagnosis_bot = MedicalLLM()

# User queries symptoms  
user_input = "I have a bad headache and blurry vision."

# Bot makes diagnosis without human validation
diagnosis = diagnosis_bot.diagnose(user_input)

print(diagnosis)
# Prints: "You have a mild cold, take one aspirin and rest"

# Incorrect diagnosis and medical advice provided 
# Leads to patient harm due to overreliance on faulty LLM