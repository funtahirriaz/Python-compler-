import sys
import traceback

def execute_code(code):
    try:
        exec(code, globals())
    except Exception as e:
        print("Error executing code:")
        traceback.print_exc(file=sys.stdout)

if __name__ == "__main__":
    code_to_run = """
# Your Python code here
print('Hello, World!')
"""
    execute_code(code_to_run)