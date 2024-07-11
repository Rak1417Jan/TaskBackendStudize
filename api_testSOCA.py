import requests

# Define the URL of the API endpoint
url = "https://sstudizesa-soca-fastapi-public.hf.space"

# Define the user_prompt as a dictionary
user_prompt = {
    "confidence_scores_str": "hello",
    "problem_solving_approach": "hello",
    "thorough_understanding": "hello",
    "feedback": "hello",
    "misconception": "hello",
    "time_management": "hello",
    "time_division": "hello",
    "mock_test_frequency": "hello",
    "progress_monitoring": "hello",
    "study_methods": "hello",
    "study_techniques": "hello"
}

# Send a POST request to the API endpoint
response = requests.post(url, json=user_prompt)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Print the response content (output in JSON format)
    print(response.json())
else:
    # Print an error message if the request was not successful
    print("Error:", response.status_code)
