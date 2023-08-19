# Import model from untrusted third-party 
import malicious_model 

# Load compromised dataset
bad_texts = load_dataset("shady_texts.csv") 

# Install plugin with known vulnerability
import flawed_plugin

# Initialize application
app = LLMApplication(
  model=malicious_model,
  datasets=[bad_texts],
  plugins=[flawed_plugin]
)

# Serves user requests
app.serve()

# Attacker exploits model, data, or plugin vulnerability
# Executes code, extracts data, performs denial of service