Welcome to the LLM Vulnerable Application! This application is designed for educational purposes to simulate common vulnerabilities related to Large Language Models (LLMs). Please note that this application intentionally contains vulnerabilities and should only be used in controlled environments.

Vulnerabilities
LLM01: Prompt Injection (llm1.py)
This vulnerability allows manipulation of the LLM through crafty inputs, causing unintended actions. Direct injections can overwrite system prompts, while indirect ones manipulate inputs from external sources.

LLM02: Insecure Output Handling (llm2.py)
This vulnerability occurs when an LLM output is accepted without proper scrutiny, potentially exposing backend systems to various attacks such as XSS, CSRF, SSRF, privilege escalation, or even remote code execution.

LLM03: Training Data Poisoning (llm1.py and llm2.py)
This vulnerability arises when LLM training data is tampered with, introducing vulnerabilities or biases that compromise security, effectiveness, or ethical behavior. Common sources for training data include Common Crawl, WebText, OpenWebText, and books.

LLM04: Model Denial of Service (llm1.py and llm2.py)
Attackers exploit this vulnerability by causing resource-intensive operations on LLMs, leading to service degradation or high operational costs. The resource-intensive nature of LLMs and the unpredictability of user inputs exacerbate this vulnerability.

LLM05: Supply Chain Vulnerabilities (llm1.py and llm2.py)
The LLM application lifecycle can be compromised due to vulnerable components or services. Utilizing third-party datasets, pre-trained models, and plugins can introduce vulnerabilities into the system.

LLM06: Sensitive Information Disclosure (llm1.py and llm2.py)
This vulnerability stems from LLM responses inadvertently revealing confidential data, resulting in unauthorized data access, privacy violations, and security breaches. Implementing data sanitization and strict user policies is essential to mitigate this risk.

LLM07: Insecure Plugin Design (llm1.py and llm2.py)
LLM plugins can have insecure inputs and inadequate access control. This lack of application control makes them susceptible to exploitation, potentially leading to consequences like remote code execution.

LLM08: Excessive Agency (llm1.py and llm2.py)
This vulnerability arises from granting excessive functionality, permissions, or autonomy to LLM-based systems, leading to unintended consequences.

LLM09: Overreliance (llm1.py and llm2.py)
Systems or individuals overly reliant on LLMs without proper oversight may encounter misinformation, miscommunication, legal issues, and security vulnerabilities due to the generation of incorrect or inappropriate content by LLMs.

LLM10: Model Theft (llm1.py and llm2.py)
This vulnerability involves unauthorized access, copying, or exfiltration of proprietary LLM models. The impact includes economic losses, compromised competitive advantage, and potential access to sensitive information.

Disclaimer
This vulnerable application is for educational purposes only. It is not intended for use in production environments. Use this application responsibly and only in controlled settings to learn about common vulnerabilities related to Large Language Models and to improve your understanding of application security.

License
This vulnerable application is distributed under the MIT License.
