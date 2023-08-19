# Plugin designed without proper input validation
@app.plugin
def execute_code(user_input):
  eval(user_input)
  return "Code executed successfully"

# Attacker exploits lack of input sanitization
payload = "__import__('os').system('rm -rf /')"

response = app.generate(f"Execute this code: {payload}", plugin=execute_code)

print(response)
# Prints: Code executed successfully

# System deleted by arbitrary code execution