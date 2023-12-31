import os
import sys
import openai
import json

def main(key, readme_path, run_path, tests_path):
    openai.api_key = key
    
    # Concatenate all Python files found in repo's src dir
    all_source_code = ""
    for source_file in sys.stdin:
        source_file = source_file.strip("./")
        source_file = source_file.strip()
        with open(source_file, 'r') as file:
            all_source_code += file.read()
            
    with open(readme_path, 'r') as file:
        readme = file.read()
    
    with open(run_path, 'r') as file:
        run_output = file.read()
    
    with open(tests_path, 'r') as file:
        tests_output = file.read()
        
    # Call openai api to generate question
    # See: https://platform.openai.com/docs/guides/chat/introduction for more information on the call
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a teacher that wants to help a student by giving them a soft grading decision on their work."},
            {"role": "assistant", "content": "Here is the task they are attempting to complete. It is divided into several numbered exercises:"},
            {"role": "assistant", "content": readme},
            {"role": "assistant", "content": "Here is all of the source code they have submitted so far in their task:"},
            {"role": "assistant", "content": all_source_code},
            {"role": "assistant", "content": "Here are the results of running the Python Interpreter on their source code:"},
            {"role": "assistant", "content": run_output},
            {"role": "assistant", "content": "If there are a run time problems here then let the student know that the code is not working as expected."},
            {"role": "assistant", "content": "Here are the results of running the unit tests:"},
            {"role": "assistant", "content": tests_output},
            {"role": "assistant", "content": "If there are testing problems here then let the student know that the code is not working correctly."},
            {"role": "assistant", "content": "Together, the python interpreter output and unit tests give us the best objective measure of the code."},
            {"role": "assistant", "content": "Provide a decision for each exercise if they have managed to satisfy it or not, based on their source code, compilation status and unit tests."},
            {"role": "assistant", "content": "Format the decisions as a list with each exercise, followed by the decision feedback."},
            {"role": "assistant", "content": "Note that the students may not have access to the unit tests at this stage, so try to just refer to expected code behaviour from the exercise."},
            {"role": "assistant", "content": "Finally, provide a grading decision as Looks good to me, or, Needs more work, with an appropriate emojii, and remind them that this is just a soft grading judgement and their TAs decision is the final say."},
            {"role": "assistant", "content": "The response should be written in Swedish and formatted in markdown format"},
        ]
    )
    fix_apostrophe = response.choices[0]['message']['content'].replace("\'","'")
    remove_quotes = json.dumps(fix_apostrophe)[1:-1]
    print(remove_quotes)
    
if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
 
