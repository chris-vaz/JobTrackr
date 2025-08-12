import os
from serpapi import GoogleSearch
from dotenv import load_dotenv
from datetime import datetime, timedelta
import json

# Load the .env file
load_dotenv()

# Retrieving the API key from environment variables
api_key = os.getenv('API_KEY')

if not api_key:
    raise ValueError("API_KEY not set. Please add it to your .env file.")

users = [
    {"id":1,"name":"Shehan Silva","initials":"SS","position":"Graphic Designer in the last week","location":"Al Farwaniyah Governorate, Kuwait"},
    {"id":2,"name":"Anmol Deen Cutinha","initials":"ADC","position":"Finance","location":"Al Farwaniyah Governorate, Kuwait"},
    {"id":3,"name":"Fahad Asif","initials":"FA","position":"Developer","location":"Al Farwaniyah Governorate, Kuwait"},
    {"id":4,"name":"Bryan Nazareth","initials":"BN","position":"Logistics","location":"Toronto, ON, Canada"},
    {"id":5,"name":"Francis","initials":"F","position":"Senior Accountant","location":"Al Farwaniyah Governorate, Kuwait"},
    {"id":6,"name":"Sudeep Shetty","initials":"SS","position":"HVAC","location":"Al Farwaniyah Governorate, Kuwait"},
    {"id":7,"name":"Joylet","initials":"J","position":"Senior Merchandiser","location":"Kuwait"},
    {"id":8,"name":"Milford D'souza","initials":"MD1","position":"UI","location":"Kuwait"},
    {"id":9,"name":"Milford D'souza 2 ","initials":"MD2","position":"Product","location":"Kuwait"},
    {"id":10,"name":"Milford D'souza 3","initials":"MD3","position":"Frontend Developer","location":"Kuwait"},
    {"id":11,"name":"Mohit Philipose","initials":"MP","position":"HVAC","location":"Al Farwaniyah Governorate, Kuwait"},
    {"id":12,"name":"Mohit Philipose","initials":"MP2","position":"HVAC sales","location":"Al Farwaniyah Governorate, Kuwait"},
    {"id":13,"name":"Jane","initials":"J2","position":"HR jobs in kuwait in the last month","location":"Al Farwaniyah Governorate, Kuwait"},
    {"id":14,"name":"Jane 2","initials":"J22","position":"HR intern","location":"Mangaluru, Karnataka, India"},
    {"id":15,"name":"George","initials":"GA","position":"Dentist","location":"Al Farwaniyah Governorate, Kuwait"},
    {"id":16,"name":"Darren Dsouza","CDD":"GA","position":"Sales","location":"Al Farwaniyah Governorate, Kuwait"},
    {"id":17,"name":"Darren Dsouza","CDD":"GA","position":"Sales Assistant","location":"Al Farwaniyah Governorate, Kuwait"},
    {"id":18,"name":"Darren Dsouza","CDD2":"GA","position":"Marketing","location":"Al Farwaniyah Governorate, Kuwait"},
    {"id":19,"name":"Darren Dsouza","CDD2":"GA","position":"Marketing Assitant","location":"Al Farwaniyah Governorate, Kuwait"},
    {"id":20,"name":"Darren Dsouza","CDD3":"GA","position":"Sales and Marketing","location":"Al Farwaniyah Governorate, Kuwait"},
    {"id":21,"name":"Deepthi Aloysius","initials":"DA","position":"Computer","location":"Al Farwaniyah Governorate, Kuwait"},
    {"id":22,"name":"Deepthi Aloysius","initials":"DA","position":"Teacher","location":"Al Farwaniyah Governorate, Kuwait"},
    {"id":23,"name":"Sakina","initials":"SA1","position":"Senior Graphic Designer in kuwait in the last week","location":"Al Farwaniyah Governorate, Kuwait"},
    {"id":24,"name":"Sakina","initials":"SA2","position":"Freelance Graphic Designer in kuwait in the last week","location":"Al Farwaniyah Governorate, Kuwait"},
    {"id":25,"name":"Raihan","initials":"R1","position":"Sales","location":"Al Farwaniyah Governorate, Kuwait"},
    {"id":26,"name":"Jayden","initials":"JD1","position":"Admin Jobs","location":"Al Farwaniyah Governorate, Kuwait"},
    {"id":27,"name":"Avlon Avy Rodrigues","initials":"AAR2","position":"HR","location":"Al Farwaniyah Governorate, Kuwait"},
    {"id":28,"name":"Avlon Avy Rodrigues","initials":"AAR3","position":"Marketing","location":"Al Farwaniyah Governorate, Kuwait"},
    {"id":29,"name":"Avlon Avy Rodrigues","initials":"AAR4","position":"Accountant","location":"Al Farwaniyah Governorate, Kuwait"},
    {"id":30,"name":"Sara Abu Atta","initials":"SAA","position":"Senior Marketing Manager","location":"Al Farwaniyah Governorate, Kuwait"},
    {"id":31,"name":"Melroy Lobo","initials":"MLF","position":"Frontend Developer","location":"Al Farwaniyah Governorate, Kuwait"},
    {"id":32,"name":"Melroy Lobo","initials":"MLB","position":"Backend Developer","location":"Al Farwaniyah Governorate, Kuwait"},
    {"id":33,"name":"Melroy Lobo","initials":"MLFS","position":"Full stack developer","location":"Al Farwaniyah Governorate, Kuwait"},
    {"id":34,"name":"Melroy Lobo","initials":"MLDA","position":"Data Analyst","location":"Al Farwaniyah Governorate, Kuwait"},
    {"id":35,"name":"Mark Francis","initials":"MFV","position":"Video Editor","location":"Al Farwaniyah Governorate, Kuwait"},
    {"id":36,"name":"Mark Francis","initials":"MFV2","position":"Content Specialist","location":"Al Farwaniyah Governorate, Kuwait"},
    {"id":37,"name":"Krishna Sai Busamudram","initials":"KSB","position":"Software Developer","location":"Al Farwaniyah Governorate, Kuwait"},
    {"id":38,"name":"Maryam Amin","initials":"MA","position":"Back end Developer jobs in kuwait in the last month","location":"Al Farwaniyah Governorate, Kuwait"},
    {"id":39,"name":"Callie Travasso","initials":"CTA","position":"marketing internship jobs in kuwait in the last month","location":"Al Farwaniyah Governorate, Kuwait"},
    {"id":40,"name":"Janice","initials":"JOYJ","position":"Auditor jobs in kuwait in the last week","location":"Al Farwaniyah Governorate, Kuwait"},
    {"id":41,"name":"Callie Travasso","initials":"CTA2","position":"hr internship jobs in kuwait in the last month","location":"Al Farwaniyah Governorate, Kuwait"},
    {"id":42,"name":"Callie Travasso","initials":"CTA3","position":"sales internship jobs in kuwait in the last month","location":"Al Farwaniyah Governorate, Kuwait"},
    {"id":43,"name":"Sakina","initials":"SA3","position":"Graphic Designer jobs in kuwait in the last week","location":"Al Farwaniyah Governorate, Kuwait"},
    {"id":44,"name":"Reem","initials":"RM","position":"Software Engineer jobs in Cairo in the last month","location":"Cairo, Egypt"},
    {"id":45,"name":"Reem","initials":"RM","position":"Data Science jobs in the last week","location":"Al Farwaniyah Governorate, Kuwait"},
    {"id":46,"name":"Tanisha","initials":"TAN","position":"Logistics jobs in the last week","location":"Dubai, United Arab Emirates"},
    {"id":47,"name":"Samskriti Pai","initials":"SAM1","position":"Marketing jobs in the last week","location":"Dubai, United Arab Emirates"},
    {"id":48,"name":"Samskriti Pai","initials":"SAM2","position":"Accountant jobs in the last week","location":"Dubai, United Arab Emirates"},
    {"id":49,"name":"Samskriti Pai","initials":"SAM3","position":"HR jobs in the last week","location":"Dubai, United Arab Emirates"},
    {"id":50,"name":"Meriska","initials":"MS1","position":"Social Media Marketing jobs in the last week","location":"Al Farwaniyah Governorate, Kuwait"},
    {"id":51,"name":"Meriska","initials":"MS2","position":"Marketing jobs in the last week","location":"Al Farwaniyah Governorate, Kuwait"}
]
 
def get_week_range():

    today = datetime.now()
    start_of_week = today - timedelta(days=today.weekday() + 1)
    end_of_week = start_of_week + timedelta(days=6)
    return start_of_week.strftime('%d-%m'), end_of_week.strftime('%d-%m')

def try_search(params, description):
    """Try a search with given parameters and return results"""
    print(f"Trying: {description}")
    try:
        search = GoogleSearch(params)
        results = search.get_dict()
        

        if 'error' in results:
            print(f"  ❌ Error: {results['error']}")
            return None
        
        jobs = results.get('jobs_results', [])
        print(f"  ✅ Found {len(jobs)} jobs")
        return results
    except Exception as e:
        print(f"  ❌ Exception: {e}")
        return None

# Get user input
try:
    user_id = int(input("Enter the user ID: "))
    selected_user = next(user for user in users if user['id'] == user_id)
    print(f"Selected user: {selected_user['name']}")
except (ValueError, StopIteration):
    print("Invalid ID entered. Exiting.")
    exit()

start_week, end_week = get_week_range()
print(f"Week range: {start_week} to {end_week}\n")

# Use the position as-is (keeping your intentional phrases like "in the last week")
position_for_search = selected_user['position']

print(f"Searching for: '{position_for_search}'")

# Progressive search strategy - NO UDS filter by default
search_attempts = [
    {
        "params": {
            "engine": "google_jobs",
            "q": f"{position_for_search}",
            "google_domain": "google.com.kw",
            "gl": "kw",
            "hl": "en", 
            "location": selected_user['location'],
            "api_key": api_key
        },
        "description": f"Primary search: '{position_for_search}' in {selected_user['location']}"
    },
    {
        "params": {
            "engine": "google_jobs",
            "q": f"{position_for_search} Kuwait",
            "google_domain": "google.com.kw",
            "gl": "kw",
            "hl": "en",
            "api_key": api_key
        },
        "description": f"Broader search: '{position_for_search} Kuwait'"
    },
    {
        "params": {
            "engine": "google_jobs", 
            "q": position_for_search,
            "google_domain": "google.com.kw",
            "gl": "kw",
            "hl": "en",
            "api_key": api_key
        },
        "description": f"Simple search: '{position_for_search}'"
    },
    {
        "params": {
            "engine": "google_jobs",
            "q": f"{position_for_search}",
            "api_key": api_key
        },
        "description": f"Global search: '{position_for_search}'"
    }
]

# Try each search strategy until we find results
results = None
successful_params = None

for attempt in search_attempts:
    results = try_search(attempt["params"], attempt["description"])
    if results and results.get('jobs_results'):
        successful_params = attempt["params"] 
        break
    print()

if not results or not results.get('jobs_results'):
    print("❌ No results found with any search strategy!")
    # Still create the file with no results message
    job_list_message = f"Job List for {selected_user['name']} - ({start_week} To {end_week})\n\n"
    job_list_message += "No jobs found for any search variation.\n"
    job_list_message += f"Tried searching for: {position_for_search}\n"
    job_list_message += f"Location: {selected_user['location']}\n"
    
    with open("job_list_message.txt", "w", encoding="utf-8") as file:
        file.write(job_list_message)
    exit()

# Save debug info
with open("debug_api_response.json", "w", encoding="utf-8") as debug_file:
    json.dump(results, debug_file, indent=2)

print(f"\n🎉 SUCCESS! Using: {successful_params.get('q', 'N/A')}")

# Extract jobs and create the message
jobs = results.get('jobs_results', [])
job_list_message = f"Job List for {selected_user['name']} - ({start_week} To {end_week})\n\n"

def clean_url(url):
    if url:
        return url.split('?')[0]  
    return url

for idx, job in enumerate(jobs, start=1):
    title = job.get('title', 'N/A')
    company_name = job.get('company_name', 'N/A')
    location = job.get('location', 'N/A')
    
    job_list_message += f"{idx}. \n"
    job_list_message += f"Title: {title}\n"
    job_list_message += f"Company Name: {company_name}\n"
    job_list_message += f"Location: {location}\n"

    apply_options = job.get('apply_options', [])
    if apply_options: 
        for i, option in enumerate(apply_options, start=1):
            apply_title = option.get('title', 'N/A')
            apply_link = clean_url(option.get('link', 'N/A'))
            job_list_message += f"  {i}. {apply_title} - {apply_link}\n"
    else:
        job_list_message += "No apply options available\n"
    
    job_list_message += "\n"

# Save the results
with open("job_list_message.txt", "w", encoding="utf-8") as file:
    file.write(job_list_message)

print(f"\n✅ Job list saved! Found {len(jobs)} jobs for {selected_user['name']}")
print("📄 Check 'job_list_message.txt' for the formatted results")
print("🔍 Check 'debug_api_response.json' for full API response details")