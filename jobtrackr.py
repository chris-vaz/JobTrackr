import os
from serpapi import GoogleSearch
from dotenv import load_dotenv
from datetime import datetime, timedelta

# Load the .env file
load_dotenv()

# Retrieving the API key from environment variables
api_key = os.getenv('API_KEY')

if not api_key:
    raise ValueError("API_KEY not set. Please add it to your .env file.")

users = [
    {"id": 1, "name": "Shehan Silva", "initials": "SS", "position": "Graphic Designer", "uds-filter": "ADvngMjcH0KdF7qGWtwTBrP0nt7dzscMcMwPDcy7a2dsJUesKpFj-gvu5q5BkJiiKct_tYJ3sBwsErSKC5opfhNbP0FwvqgXf5v-jaXTa9G5hvS4NDDTEcA", "location": "Al Farwaniyah Governorate, Kuwait"},
    {"id": 2, "name": "Anmol Deen Cutinha", "initials": "ADC", "position": "Finance", "uds-filter": "ADvngMjcH0KdF7qGWtwTBrP0nt7dzscMcMwPDcy7a2dsJUesKpFj-gvu5q5BkJiiKct_tYJ3sBwsErSKC5opfhNbP0FwvqgXf5v-jaXTa9G5hvS4NDDTEcA", "location": "Al Farwaniyah Governorate, Kuwait"},
    {"id": 3, "name": "Fahad Asif", "initials": "FA", "position": "Software", "uds-filter": "ADvngMjcH0KdF7qGWtwTBrP0nt7diIVohtvdusKCCc-5AJAmrb3GJ4jZ-S1JHBgg2hfmmTTK3l8JzOgMdULLKuhMBxXwpJWGcQVnv9U5quAqw9DWeo7dBNP_0sJeFnVNQSlr5ABdUlvt-K6UStW68K-4vU9E9D8Moq4Rr8y62PhTNzyel2mbFF7WSbxWc3KDu-rD3A_Uv5Z3XNOKVj_D7S17CejC7Iw8Bf8mcNg1EY-DsIpgt_zTlZH3-E4MOcsupcqTF7TvkxbH6ERFRdnS1AJK47Z6ik0iiZ9TGrAHK63cVc5QxKLF8A63OzeWUS-4BE71glvoJoC_V82BR4EKbhwF1QTd_2DS2A", "location": "Al Farwaniyah Governorate, Kuwait"},
    {"id": 4, "name": "Bryan Nazareth", "initials": "BN", "position": "Logistics", "uds-filter": "ADvngMjcH0KdF7qGWtwTBrP0nt7diIVohtvdusKCCc-5AJAmrb3GJ4jZ-S1JHBgg2hfmmTTK3l8JzOgMdULLKuhMBxXwpJWGcQVnv9U5quAqw9DWeo7dBNP_0sJeFnVNQSlr5ABdUlvt-K6UStW68K-4vU9E9D8Moq4Rr8y62PhTNzyel2mbFF7WSbxWc3KDu-rD3A_Uv5Z3XNOKVj_D7S17CejC7Iw8Bf8mcNg1EY-DsIpgt_zTlZH3-E4MOcsupcqTF7TvkxbH6ERFRdnS1AJK47Z6ik0iiZ9TGrAHK63cVc5QxKLF8A63OzeWUS-4BE71glvoJoC_V82BR4EKbhwF1QTd_2DS2A", "location": "Toronto, ON, Canada"},
    {"id": 5, "name": "Francis", "initials": "F", "position": "Senior Accountant", "uds-filter": "ADvngMjcH0KdF7qGWtwTBrP0nt7diIVohtvdusKCCc-5AJAmrb3GJ4jZ-S1JHBgg2hfmmTTK3l8JzOgMdULLKuhMBxXwpJWGcQVnv9U5quAqw9DWeo7dBNP_0sJeFnVNQSlr5ABdUlvt-K6UStW68K-4vU9E9D8Moq4Rr8y62PhTNzyel2mbFF7WSbxWc3KDu-rD3A_Uv5Z3XNOKVj_D7S17CejC7Iw8Bf8mcNg1EY-DsIpgt_zTlZH3-E4MOcsupcqTF7TvkxbH6ERFRdnS1AJK47Z6ik0iiZ9TGrAHK63cVc5QxKLF8A63OzeWUS-4BE71glvoJoC_V82BR4EKbhwF1QTd_2DS2A", "location": "Al Farwaniyah Governorate, Kuwait"},
    {"id": 6, "name": "Sudeep Shetty", "initials": "SS", "position": "HVAC", "uds-filter": "ADvngMjcH0KdF7qGWtwTBrP0nt7diIVohtvdusKCCc-5AJAmrb3GJ4jZ-S1JHBgg2hfmmTTK3l8JzOgMdULLKuhMBxXwpJWGcQVnv9U5quAqw9DWeo7dBNP_0sJeFnVNQSlr5ABdUlvt-K6UStW68K-4vU9E9D8Moq4Rr8y62PhTNzyel2mbFF7WSbxWc3KDu-rD3A_Uv5Z3XNOKVj_D7S17CejC7Iw8Bf8mcNg1EY-DsIpgt_zTlZH3-E4MOcsupcqTF7TvkxbH6ERFRdnS1AJK47Z6ik0iiZ9TGrAHK63cVc5QxKLF8A63OzeWUS-4BE71glvoJoC_V82BR4EKbhwF1QTd_2DS2A", "location": "Al Farwaniyah Governorate, Kuwait"}
]
 
# Helper function to get the start and end of the current week (Sunday to Saturday)
def get_week_range():
    today = datetime.now()
    # Calculate the start of the week (Sunday)
    start_of_week = today - timedelta(days=today.weekday() + 1)
    # Calculate the end of the week (Saturday)
    end_of_week = start_of_week + timedelta(days=6)
    return start_of_week.strftime('%d-%m'), end_of_week.strftime('%d-%m')

# Prompt for the user ID input
try:
    user_id = int(input("Enter the user ID: "))
    # Select the user based on the entered ID
    selected_user = next(user for user in users if user['id'] == user_id)
except (ValueError, StopIteration):
    print("Invalid ID entered. Exiting.")
    exit()  

# Dynamically get the current week's Sunday and Saturday
start_week, end_week = get_week_range()

# Define the search parameters for the Google Jobs API
params = {
    "engine": "google_jobs",
    "ltype": "1",
    "no_cache": "true",
    "q": f"{selected_user['position']} jobs",  
    "google_domain": "google.com.kw",
    "gl": "kw",
    "hl": "en",
    "location": selected_user['location'],
    "uds": selected_user['uds-filter'],  
    "api_key": api_key
}

# Fetch job results
search = GoogleSearch(params)
results = search.get_dict()

# Extract the jobs from the results
jobs = results.get('jobs_results', [])

# Initialize the variable to store the job list message
job_list_message = f"Job List for {selected_user['name']} - ({start_week} To {end_week})\n\n"

# Helper function to clean URLs by removing tracking parameters like ?utm
def clean_url(url):
    if url:
        return url.split('?')[0]  
    return url

# Loop through each job and build the job list message
for idx, job in enumerate(jobs, start=1):
    title = job.get('title', 'N/A')
    company_name = job.get('company_name', 'N/A')
    location = job.get('location', 'N/A')
    
    # Append job details to the job list message
    job_list_message += f"{idx}. \n"
    job_list_message += f"Title: {title}\n"
    job_list_message += f"Company Name: {company_name}\n"
    job_list_message += f"Location: {location}\n"

    # Title and Link cleaning process
    apply_options = job.get('apply_options', [])
    if apply_options: 
        for i, option in enumerate(apply_options, start=1):
            apply_title = option.get('title', 'N/A')
            apply_link = clean_url(option.get('link', 'N/A'))  # Clean the URL
            job_list_message += f"  {i}. {apply_title} - {apply_link}\n"
    else:
        job_list_message += "  No apply options available\n"
    
    job_list_message += "\n"  # Add spacing between job entries

# Save the job list message to a text file
with open("job_list_message.txt", "w", encoding="utf-8") as file:
    file.write(job_list_message)

# Let the user know the message was saved
print(f"The job list message for {selected_user['name']} has been updated and saved to 'job_list_message.txt'. Open the file to copy and paste the message easily.")
