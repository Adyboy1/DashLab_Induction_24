import google.generativeai as genai
import os
import json
import time

# Configure the Gemini API key using environment variable
genai.configure(api_key=os.environ.get("API_KEY"))

# Specify the model you want to use
model = genai.GenerativeModel('gemini-1.5-flash')

# Prepare the list to store the JSON objects
output_data = []

# Read prompts from the input file
input_file_path = 'input.txt'  # Path to the input file
with open(input_file_path, "r") as infile:
    prompts = infile.readlines()

# Function to call the Gemini API and process each prompt
def get_gemini_response(prompt):
    start_time = time.time()  # TimeSent as UNIX Timestamp

    # Make API call to Gemini
    response = model.generate_content(prompt.strip())
    
    end_time = time.time()  # TimeRecvd as UNIX Timestamp
    
    # Parse the response
    message = response.text  # Extract the response text

    # Create a dictionary for the JSON object
    result = {
        "Prompt": prompt.strip(),
        "Message": message,
        "TimeSent": int(start_time),
        "TimeRecvd": int(end_time),
        "Source": "Gemini"
    }

    return result

# Iterate over prompts and collect responses
for prompt in prompts:
    if prompt.strip():  # Ensure there are no empty lines
        response_data = get_gemini_response(prompt)
        output_data.append(response_data)

# Write output to a JSON file
output_file_path = 'output.json'  # Path to the output file
with open(output_file_path, "w") as outfile:
    json.dump(output_data, outfile, indent=4)

print(f"Responses saved to {output_file_path}")
