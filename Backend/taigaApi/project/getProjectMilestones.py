import os
import requests
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

def get_number_of_milestones(project_id, auth_token):
    taiga_url = os.getenv('TAIGA_URL')
    project_api_url = f"{taiga_url}/milestones?project={project_id}"
    headers = {
        'Authorization': f'Bearer {auth_token}',
        'Content-Type': 'application/json',
    }
    try:
        response = requests.get(project_api_url, headers=headers)
        response.raise_for_status()
        sprints = response.json()
        return len(sprints)
    except requests.exceptions.RequestException as e:
        # Handle errors during the API request and print an error message
        print(f"Error fetching number of sprints: {e}")
        return None
