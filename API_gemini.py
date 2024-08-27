import google.generativeai as genai
import os
import json
import time

genai.configure(api_key=os.environ.get("API_KEY"))

model = genai.GenerativeModel('gemini-1.5-flash')

output_data = []

input_file_path = 'input.txt'  # Path to the input file
with open(input_file_path, "r") as infile:
    prompts = infile.readlines()


def get_gemini_response(prompt):
    start_time = time.time()  
   
    response = model.generate_content(prompt.strip())
    
    end_time = time.time()  
    
    # Parse the response
    message = response.text  

    
    result = {
        "Prompt": prompt.strip(),
        "Message": message,
        "TimeSent": int(start_time),
        "TimeRecvd": int(end_time),
        "Source": "Gemini"
    }

    return result


for prompt in prompts:
    if prompt.strip(): 
        response_data = get_gemini_response(prompt)
        output_data.append(response_data)

# Write output to a JSON file
output_file_path = 'output.json'  # Path to the output file
with open(output_file_path, "w") as outfile:
    json.dump(output_data, outfile, indent=4)

print(f"Responses saved to {output_file_path}")
