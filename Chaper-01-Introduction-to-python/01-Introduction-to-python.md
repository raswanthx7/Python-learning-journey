# Chapter 1 – Introduction to Python

## Topics Covered
1. Introduction to Python
2. Key Features of Python
3. Python in Cloud Computing
4. Execution of Python Programs  
   - Interactive Mode  
   - Script Mode  
   - Using Python Command-Line Window  
   - Using Python IDE (Graphical Window)  
5. Bytecode & Python Virtual Machine (PVM)  
6. Shebang (`#!`) in Python Scripts  

---

## 1. Introduction to Python
- Python is a **high-level, interpreted** programming language.  
- Known for **simplicity, readability, and versatility**.  
- Widely used in **automation, data processing, cloud computing, AI/ML, web development**, and more.  

## 2. Key Features of Python
1. **Easy to Learn and Read** – Uses simple English-like syntax.
2. **Interpreted Language** – No need to compile; executes line by line.
3. **Cross-platform** – Works on Windows, macOS, Linux, etc.
4. **Extensive Libraries** – Huge collection of built-in and third-party libraries.
5. **Dynamic Typing** – No need to declare variable types explicitly.
6. **Versatile** – Supports multiple programming paradigms: procedural, object-oriented, functional.

---

## 3. Python in Cloud Computing
- Used for **automation scripts**, **serverless functions (AWS Lambda, Azure Functions)**, and **API integrations**.  
- Ideal for **DevOps pipelines** and **Infrastructure as Code (IaC)**.  
- Works well with **AWS SDK (Boto3)**, **Azure SDK**, and **GCP APIs**.  

---

## 4. Execution of Python Programs

### 4.1 Interactive Mode
- Run Python directly in the terminal.  
- Example:  
```bash
python3
>>> print("Hello from Interactive Mode!")
```

### 4.2 Script Mode

- Write code in a .py file and execute it.

- Example:
```bash
python3 my_script.py
```

### 4.3 Using Python Command-Line Window

- Open Python interpreter in the terminal (Linux/Windows) and execute commands.

### 4.4 Using Python IDE (Graphical Window)

- Examples: PyCharm, VS Code, IDLE.
- Provides GUI-based editing and debugging tools.

## 5. Bytecode & Python Virtual Machine (PVM)

**Basic Flow of Python Execution:**

```text
Python Source Code (.py)
        ↓
    Bytecode (.pyc)
        ↓
Python Virtual Machine (PVM)
        ↓
Machine Code (CPU Executes)
```

- Bytecode: Intermediate code Python creates before execution.
- PVM: Executes the bytecode line-by-line.

## 6. Shebang in Python Scripts
### What is Shebang?

A special line at the start of a script that tells the system which interpreter to use.

Example:
```bash
#!/usr/bin/env python3
print("Hello World")
```
**Why use `#!/usr/bin/env python3`?**

- Ensures the script uses the Python version in your environment.

- Works across different systems without hardcoding /usr/bin/python3.
