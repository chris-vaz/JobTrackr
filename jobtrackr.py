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
    {"id": 1, "name": "Shehan Silva", "initials": "SS", "position": "Graphic Designer in the last week", "uds-filter": "ABqPDvztZD_Nu18FR6tNPw2cK_RRnGWYudk6uw8uavw97RLFuZ-vdnMOZ8F89Z49lFobhrXs9lhsZvewNqcuymAyVtNF_zkNkaj9gNEwXRSAzmD1AnjwS45NIW8GQhR4WYfv38jtPyEYq61AAA3gSe1BH1-dnymHaMvyeIBtVwHnlHiFed5pmX9a9fBgmmfASUD9h6aBQs4OK8zMBbGX7DUIaer1RetkoaU9IKd_Nz32cB8RpzxKmUCvYVWQtyyPYUwf1WB9cr66mHE6SVJJbvyyLOFreaamccVN69UK3giEmJGkkWJowZzqgxjG-R6d0aLGsBHU06qn99_wr8HTt-QIeMMf6ZuCgg", "location": "Al Farwaniyah Governorate, Kuwait"},
    {"id": 2, "name": "Anmol Deen Cutinha", "initials": "ADC", "position": "Finance", "uds-filter": "ADvngMjcH0KdF7qGWtwTBrP0nt7dzscMcMwPDcy7a2dsJUesKpFj-gvu5q5BkJiiKct_tYJ3sBwsErSKC5opfhNbP0FwvqgXf5v-jaXTa9G5hvS4NDDTEcA", "location": "Al Farwaniyah Governorate, Kuwait"},
    {"id": 3, "name": "Fahad Asif", "initials": "FA", "position": "Developer", "uds-filter": "ADvngMjcH0KdF7qGWtwTBrP0nt7diIVohtvdusKCCc-5AJAmrb3GJ4jZ-S1JHBgg2hfmmTTK3l8JzOgMdULLKuhMBxXwpJWGcQVnv9U5quAqw9DWeo7dBNP_0sJeFnVNQSlr5ABdUlvt-K6UStW68K-4vU9E9D8Moq4Rr8y62PhTNzyel2mbFF7WSbxWc3KDu-rD3A_Uv5Z3XNOKVj_D7S17CejC7Iw8Bf8mcNg1EY-DsIpgt_zTlZH3-E4MOcsupcqTF7TvkxbH6ERFRdnS1AJK47Z6ik0iiZ9TGrAHK63cVc5QxKLF8A63OzeWUS-4BE71glvoJoC_V82BR4EKbhwF1QTd_2DS2A", "location": "Al Farwaniyah Governorate, Kuwait"},
    {"id": 4, "name": "Bryan Nazareth", "initials": "BN", "position": "Logistics", "uds-filter": "ADvngMjcH0KdF7qGWtwTBrP0nt7diIVohtvdusKCCc-5AJAmrb3GJ4jZ-S1JHBgg2hfmmTTK3l8JzOgMdULLKuhMBxXwpJWGcQVnv9U5quAqw9DWeo7dBNP_0sJeFnVNQSlr5ABdUlvt-K6UStW68K-4vU9E9D8Moq4Rr8y62PhTNzyel2mbFF7WSbxWc3KDu-rD3A_Uv5Z3XNOKVj_D7S17CejC7Iw8Bf8mcNg1EY-DsIpgt_zTlZH3-E4MOcsupcqTF7TvkxbH6ERFRdnS1AJK47Z6ik0iiZ9TGrAHK63cVc5QxKLF8A63OzeWUS-4BE71glvoJoC_V82BR4EKbhwF1QTd_2DS2A", "location": "Toronto, ON, Canada"},
    {"id": 5, "name": "Francis", "initials": "F", "position": "Senior Accountant", "uds-filter": "ADvngMjcH0KdF7qGWtwTBrP0nt7diIVohtvdusKCCc-5AJAmrb3GJ4jZ-S1JHBgg2hfmmTTK3l8JzOgMdULLKuhMBxXwpJWGcQVnv9U5quAqw9DWeo7dBNP_0sJeFnVNQSlr5ABdUlvt-K6UStW68K-4vU9E9D8Moq4Rr8y62PhTNzyel2mbFF7WSbxWc3KDu-rD3A_Uv5Z3XNOKVj_D7S17CejC7Iw8Bf8mcNg1EY-DsIpgt_zTlZH3-E4MOcsupcqTF7TvkxbH6ERFRdnS1AJK47Z6ik0iiZ9TGrAHK63cVc5QxKLF8A63OzeWUS-4BE71glvoJoC_V82BR4EKbhwF1QTd_2DS2A", "location": "Al Farwaniyah Governorate, Kuwait"},
    {"id": 6, "name": "Sudeep Shetty", "initials": "SS", "position": "HVAC", "uds-filter": "ADvngMjcH0KdF7qGWtwTBrP0nt7diIVohtvdusKCCc-5AJAmrb3GJ4jZ-S1JHBgg2hfmmTTK3l8JzOgMdULLKuhMBxXwpJWGcQVnv9U5quAqw9DWeo7dBNP_0sJeFnVNQSlr5ABdUlvt-K6UStW68K-4vU9E9D8Moq4Rr8y62PhTNzyel2mbFF7WSbxWc3KDu-rD3A_Uv5Z3XNOKVj_D7S17CejC7Iw8Bf8mcNg1EY-DsIpgt_zTlZH3-E4MOcsupcqTF7TvkxbH6ERFRdnS1AJK47Z6ik0iiZ9TGrAHK63cVc5QxKLF8A63OzeWUS-4BE71glvoJoC_V82BR4EKbhwF1QTd_2DS2A", "location": "Al Farwaniyah Governorate, Kuwait"},
    {"id": 7, "name": "Joylet", "initials": "J", "position": "Senior Merchandiser", "uds-filter": "ADvngMjcH0KdF7qGWtwTBrP0nt7diIVohtvdusKCCc-5AJAmrb3GJ4jZ-S1JHBgg2hfmmTTK3l8JzOgMdULLKuhMBxXwpJWGcQVnv9U5quAqw9DWeo7dBNP_0sJeFnVNQSlr5ABdUlvt-K6UStW68K-4vU9E9D8Moq4Rr8y62PhTNzyel2mbFF7WSbxWc3KDu-rD3A_Uv5Z3XNOKVj_D7S17CejC7Iw8Bf8mcNg1EY-DsIpgt_zTlZH3-E4MOcsupcqTF7TvkxbH6ERFRdnS1AJK47Z6ik0iiZ9TGrAHK63cVc5QxKLF8A63OzeWUS-4BE71glvoJoC_V82BR4EKbhwF1QTd_2DS2A", "location": "Kuwait"},
    {"id": 8, "name": "Milford D'souza", "initials": "MD1", "position": "UI", "uds-filter": "ADvngMjcH0KdF7qGWtwTBrP0nt7diIVohtvdusKCCc-5AJAmrb3GJ4jZ-S1JHBgg2hfmmTTK3l8JzOgMdULLKuhMBxXwpJWGcQVnv9U5quAqw9DWeo7dBNP_0sJeFnVNQSlr5ABdUlvt-K6UStW68K-4vU9E9D8Moq4Rr8y62PhTNzyel2mbFF7WSbxWc3KDu-rD3A_Uv5Z3XNOKVj_D7S17CejC7Iw8Bf8mcNg1EY-DsIpgt_zTlZH3-E4MOcsupcqTF7TvkxbH6ERFRdnS1AJK47Z6ik0iiZ9TGrAHK63cVc5QxKLF8A63OzeWUS-4BE71glvoJoC_V82BR4EKbhwF1QTd_2DS2A", "location": "Kuwait"},
    {"id": 9, "name": "Milford D'souza 2 ", "initials": "MD2", "position": "Product", "uds-filter": "ADvngMjcH0KdF7qGWtwTBrP0nt7diIVohtvdusKCCc-5AJAmrb3GJ4jZ-S1JHBgg2hfmmTTK3l8JzOgMdULLKuhMBxXwpJWGcQVnv9U5quAqw9DWeo7dBNP_0sJeFnVNQSlr5ABdUlvt-K6UStW68K-4vU9E9D8Moq4Rr8y62PhTNzyel2mbFF7WSbxWc3KDu-rD3A_Uv5Z3XNOKVj_D7S17CejC7Iw8Bf8mcNg1EY-DsIpgt_zTlZH3-E4MOcsupcqTF7TvkxbH6ERFRdnS1AJK47Z6ik0iiZ9TGrAHK63cVc5QxKLF8A63OzeWUS-4BE71glvoJoC_V82BR4EKbhwF1QTd_2DS2A", "location": "Kuwait"},
    {"id": 10, "name": "Milford D'souza 3", "initials": "MD3", "position": "Frontend Developer", "uds-filter": "ADvngMjcH0KdF7qGWtwTBrP0nt7diIVohtvdusKCCc-5AJAmrb3GJ4jZ-S1JHBgg2hfmmTTK3l8JzOgMdULLKuhMBxXwpJWGcQVnv9U5quAqw9DWeo7dBNP_0sJeFnVNQSlr5ABdUlvt-K6UStW68K-4vU9E9D8Moq4Rr8y62PhTNzyel2mbFF7WSbxWc3KDu-rD3A_Uv5Z3XNOKVj_D7S17CejC7Iw8Bf8mcNg1EY-DsIpgt_zTlZH3-E4MOcsupcqTF7TvkxbH6ERFRdnS1AJK47Z6ik0iiZ9TGrAHK63cVc5QxKLF8A63OzeWUS-4BE71glvoJoC_V82BR4EKbhwF1QTd_2DS2A", "location": "Kuwait"},
    {"id": 11, "name": "Mohit Philipose", "initials": "MP", "position": "HVAC", "uds-filter": "ADvngMjcH0KdF7qGWtwTBrP0nt7diIVohtvdusKCCc-5AJAmrb3GJ4jZ-S1JHBgg2hfmmTTK3l8JzOgMdULLKuhMBxXwpJWGcQVnv9U5quAqw9DWeo7dBNP_0sJeFnVNQSlr5ABdUlvt-K6UStW68K-4vU9E9D8Moq4Rr8y62PhTNzyel2mbFF7WSbxWc3KDu-rD3A_Uv5Z3XNOKVj_D7S17CejC7Iw8Bf8mcNg1EY-DsIpgt_zTlZH3-E4MOcsupcqTF7TvkxbH6ERFRdnS1AJK47Z6ik0iiZ9TGrAHK63cVc5QxKLF8A63OzeWUS-4BE71glvoJoC_V82BR4EKbhwF1QTd_2DS2A", "location": "Al Farwaniyah Governorate, Kuwait"},
    {"id": 12, "name": "Mohit Philipose", "initials": "MP2", "position": "HVAC sales", "uds-filter": "ADvngMjcH0KdF7qGWtwTBrP0nt7diIVohtvdusKCCc-5AJAmrb3GJ4jZ-S1JHBgg2hfmmTTK3l8JzOgMdULLKuhMBxXwpJWGcQVnv9U5quAqw9DWeo7dBNP_0sJeFnVNQSlr5ABdUlvt-K6UStW68K-4vU9E9D8Moq4Rr8y62PhTNzyel2mbFF7WSbxWc3KDu-rD3A_Uv5Z3XNOKVj_D7S17CejC7Iw8Bf8mcNg1EY-DsIpgt_zTlZH3-E4MOcsupcqTF7TvkxbH6ERFRdnS1AJK47Z6ik0iiZ9TGrAHK63cVc5QxKLF8A63OzeWUS-4BE71glvoJoC_V82BR4EKbhwF1QTd_2DS2A", "location": "Al Farwaniyah Governorate, Kuwait"},
    {"id": 13, "name": "Jane", "initials": "J2", "position": "HR jobs in kuwait in the last month", "uds-filter": "ADvngMjcH0KdF7qGWtwTBrP0nt7diIVohtvdusKCCc-5AJAmrb3GJ4jZ-S1JHBgg2hfmmTTK3l8JzOgMdULLKuhMBxXwpJWGcQVnv9U5quAqw9DWeo7dBNP_0sJeFnVNQSlr5ABdUlvt-K6UStW68K-4vU9E9D8Moq4Rr8y62PhTNzyel2mbFF7WSbxWc3KDu-rD3A_Uv5Z3XNOKVj_D7S17CejC7Iw8Bf8mcNg1EY-DsIpgt_zTlZH3-E4MOcsupcqTF7TvkxbH6ERFRdnS1AJK47Z6ik0iiZ9TGrAHK63cVc5QxKLF8A63OzeWUS-4BE71glvoJoC_V82BR4EKbhwF1QTd_2DS2A", "location": "Al Farwaniyah Governorate, Kuwait"},
    {"id": 14, "name": "Jane 2", "initials": "J22", "position": "HR intern", "uds-filter": "ADvngMjcH0KdF7qGWtwTBrP0nt7diIVohtvdusKCCc-5AJAmrb3GJ4jZ-S1JHBgg2hfmmTTK3l8JzOgMdULLKuhMBxXwpJWGcQVnv9U5quAqw9DWeo7dBNP_0sJeFnVNQSlr5ABdUlvt-K6UStW68K-4vU9E9D8Moq4Rr8y62PhTNzyel2mbFF7WSbxWc3KDu-rD3A_Uv5Z3XNOKVj_D7S17CejC7Iw8Bf8mcNg1EY-DsIpgt_zTlZH3-E4MOcsupcqTF7TvkxbH6ERFRdnS1AJK47Z6ik0iiZ9TGrAHK63cVc5QxKLF8A63OzeWUS-4BE71glvoJoC_V82BR4EKbhwF1QTd_2DS2A", "location": "Mangaluru, Karnataka, India"},
    {"id": 15, "name": "George", "initials": "GA", "position": "Dentist", "uds-filter": "ADvngMjcH0KdF7qGWtwTBrP0nt7diIVohtvdusKCCc-5AJAmrb3GJ4jZ-S1JHBgg2hfmmTTK3l8JzOgMdULLKuhMBxXwpJWGcQVnv9U5quAqw9DWeo7dBNP_0sJeFnVNQSlr5ABdUlvt-K6UStW68K-4vU9E9D8Moq4Rr8y62PhTNzyel2mbFF7WSbxWc3KDu-rD3A_Uv5Z3XNOKVj_D7S17CejC7Iw8Bf8mcNg1EY-DsIpgt_zTlZH3-E4MOcsupcqTF7TvkxbH6ERFRdnS1AJK47Z6ik0iiZ9TGrAHK63cVc5QxKLF8A63OzeWUS-4BE71glvoJoC_V82BR4EKbhwF1QTd_2DS2A", "location": "Al Farwaniyah Governorate, Kuwait"},
    {"id": 16, "name": "Darren Dsouza", "CDD": "GA", "position": "Sales", "uds-filter": "ADvngMjcH0KdF7qGWtwTBrP0nt7diIVohtvdusKCCc-5AJAmrb3GJ4jZ-S1JHBgg2hfmmTTK3l8JzOgMdULLKuhMBxXwpJWGcQVnv9U5quAqw9DWeo7dBNP_0sJeFnVNQSlr5ABdUlvt-K6UStW68K-4vU9E9D8Moq4Rr8y62PhTNzyel2mbFF7WSbxWc3KDu-rD3A_Uv5Z3XNOKVj_D7S17CejC7Iw8Bf8mcNg1EY-DsIpgt_zTlZH3-E4MOcsupcqTF7TvkxbH6ERFRdnS1AJK47Z6ik0iiZ9TGrAHK63cVc5QxKLF8A63OzeWUS-4BE71glvoJoC_V82BR4EKbhwF1QTd_2DS2A", "location": "Al Farwaniyah Governorate, Kuwait"},
    {"id": 17, "name": "Darren Dsouza", "CDD": "GA", "position": "Sales Assistant", "uds-filter": "ADvngMjcH0KdF7qGWtwTBrP0nt7diIVohtvdusKCCc-5AJAmrb3GJ4jZ-S1JHBgg2hfmmTTK3l8JzOgMdULLKuhMBxXwpJWGcQVnv9U5quAqw9DWeo7dBNP_0sJeFnVNQSlr5ABdUlvt-K6UStW68K-4vU9E9D8Moq4Rr8y62PhTNzyel2mbFF7WSbxWc3KDu-rD3A_Uv5Z3XNOKVj_D7S17CejC7Iw8Bf8mcNg1EY-DsIpgt_zTlZH3-E4MOcsupcqTF7TvkxbH6ERFRdnS1AJK47Z6ik0iiZ9TGrAHK63cVc5QxKLF8A63OzeWUS-4BE71glvoJoC_V82BR4EKbhwF1QTd_2DS2A", "location": "Al Farwaniyah Governorate, Kuwait"},
    {"id": 18, "name": "Darren Dsouza", "CDD2": "GA", "position": "Marketing", "uds-filter": "ADvngMjcH0KdF7qGWtwTBrP0nt7diIVohtvdusKCCc-5AJAmrb3GJ4jZ-S1JHBgg2hfmmTTK3l8JzOgMdULLKuhMBxXwpJWGcQVnv9U5quAqw9DWeo7dBNP_0sJeFnVNQSlr5ABdUlvt-K6UStW68K-4vU9E9D8Moq4Rr8y62PhTNzyel2mbFF7WSbxWc3KDu-rD3A_Uv5Z3XNOKVj_D7S17CejC7Iw8Bf8mcNg1EY-DsIpgt_zTlZH3-E4MOcsupcqTF7TvkxbH6ERFRdnS1AJK47Z6ik0iiZ9TGrAHK63cVc5QxKLF8A63OzeWUS-4BE71glvoJoC_V82BR4EKbhwF1QTd_2DS2A", "location": "Al Farwaniyah Governorate, Kuwait"},
    {"id": 19, "name": "Darren Dsouza", "CDD2": "GA", "position": "Marketing Assitant", "uds-filter": "ADvngMjcH0KdF7qGWtwTBrP0nt7diIVohtvdusKCCc-5AJAmrb3GJ4jZ-S1JHBgg2hfmmTTK3l8JzOgMdULLKuhMBxXwpJWGcQVnv9U5quAqw9DWeo7dBNP_0sJeFnVNQSlr5ABdUlvt-K6UStW68K-4vU9E9D8Moq4Rr8y62PhTNzyel2mbFF7WSbxWc3KDu-rD3A_Uv5Z3XNOKVj_D7S17CejC7Iw8Bf8mcNg1EY-DsIpgt_zTlZH3-E4MOcsupcqTF7TvkxbH6ERFRdnS1AJK47Z6ik0iiZ9TGrAHK63cVc5QxKLF8A63OzeWUS-4BE71glvoJoC_V82BR4EKbhwF1QTd_2DS2A", "location": "Al Farwaniyah Governorate, Kuwait"},
    {"id": 20, "name": "Darren Dsouza", "CDD3": "GA", "position": "Sales and Marketing", "uds-filter": "ADvngMjcH0KdF7qGWtwTBrP0nt7diIVohtvdusKCCc-5AJAmrb3GJ4jZ-S1JHBgg2hfmmTTK3l8JzOgMdULLKuhMBxXwpJWGcQVnv9U5quAqw9DWeo7dBNP_0sJeFnVNQSlr5ABdUlvt-K6UStW68K-4vU9E9D8Moq4Rr8y62PhTNzyel2mbFF7WSbxWc3KDu-rD3A_Uv5Z3XNOKVj_D7S17CejC7Iw8Bf8mcNg1EY-DsIpgt_zTlZH3-E4MOcsupcqTF7TvkxbH6ERFRdnS1AJK47Z6ik0iiZ9TGrAHK63cVc5QxKLF8A63OzeWUS-4BE71glvoJoC_V82BR4EKbhwF1QTd_2DS2A", "location": "Al Farwaniyah Governorate, Kuwait"},
    {"id": 21, "name": "Deepthi Aloysius", "initials": "DA", "position": "Computer", "uds-filter": "ADvngMjcH0KdF7qGWtwTBrP0nt7diIVohtvdusKCCc-5AJAmrb3GJ4jZ-S1JHBgg2hfmmTTK3l8JzOgMdULLKuhMBxXwpJWGcQVnv9U5quAqw9DWeo7dBNP_0sJeFnVNQSlr5ABdUlvt-K6UStW68K-4vU9E9D8Moq4Rr8y62PhTNzyel2mbFF7WSbxWc3KDu-rD3A_Uv5Z3XNOKVj_D7S17CejC7Iw8Bf8mcNg1EY-DsIpgt_zTlZH3-E4MOcsupcqTF7TvkxbH6ERFRdnS1AJK47Z6ik0iiZ9TGrAHK63cVc5QxKLF8A63OzeWUS-4BE71glvoJoC_V82BR4EKbhwF1QTd_2DS2A", "location": "Al Farwaniyah Governorate, Kuwait"},
    {"id": 22, "name": "Deepthi Aloysius", "initials": "DA", "position": "Teacher", "uds-filter": "ADvngMjcH0KdF7qGWtwTBrP0nt7diIVohtvdusKCCc-5AJAmrb3GJ4jZ-S1JHBgg2hfmmTTK3l8JzOgMdULLKuhMBxXwpJWGcQVnv9U5quAqw9DWeo7dBNP_0sJeFnVNQSlr5ABdUlvt-K6UStW68K-4vU9E9D8Moq4Rr8y62PhTNzyel2mbFF7WSbxWc3KDu-rD3A_Uv5Z3XNOKVj_D7S17CejC7Iw8Bf8mcNg1EY-DsIpgt_zTlZH3-E4MOcsupcqTF7TvkxbH6ERFRdnS1AJK47Z6ik0iiZ9TGrAHK63cVc5QxKLF8A63OzeWUS-4BE71glvoJoC_V82BR4EKbhwF1QTd_2DS2A", "location": "Al Farwaniyah Governorate, Kuwait"},
    {"id": 23, "name": "Sakina", "initials": "SA1", "position": "Senior Graphic Designer in kuwait in the last week", "uds-filter": "ABqPDvztZD_Nu18FR6tNPw2cK_RRnGWYudk6uw8uavw97RLFuZ-vdnMOZ8F89Z49lFobhrXs9lhsZvewNqcuymAyVtNF_zkNkaj9gNEwXRSAzmD1AnjwS45NIW8GQhR4WYfv38jtPyEYq61AAA3gSe1BH1-dnymHaMvyeIBtVwHnlHiFed5pmX9a9fBgmmfASUD9h6aBQs4OK8zMBbGX7DUIaer1RetkoaU9IKd_Nz32cB8RpzxKmUCvYVWQtyyPYUwf1WB9cr66mHE6SVJJbvyyLOFreaamccVN69UK3giEmJGkkWJowZzqgxjG-R6d0aLGsBHU06qn99_wr8HTt-QIeMMf6ZuCgg", "location": "Al Farwaniyah Governorate, Kuwait"},
    {"id": 24, "name": "Sakina", "initials": "SA2", "position": "Freelance Graphic Designer in kuwait in the last week", "uds-filter": "ADvngMjcH0KdF7qGWtwTBrP0nt7diIVohtvdusKCCc-5AJAmrb3GJ4jZ-S1JHBgg2hfmmTTK3l8JzOgMdULLKuhMBxXwpJWGcQVnv9U5quAqw9DWeo7dBNP_0sJeFnVNQSlr5ABdUlvt-K6UStW68K-4vU9E9D8Moq4Rr8y62PhTNzyel2mbFF7WSbxWc3KDu-rD3A_Uv5Z3XNOKVj_D7S17CejC7Iw8Bf8mcNg1EY-DsIpgt_zTlZH3-E4MOcsupcqTF7TvkxbH6ERFRdnS1AJK47Z6ik0iiZ9TGrAHK63cVc5QxKLF8A63OzeWUS-4BE71glvoJoC_V82BR4EKbhwF1QTd_2DS2A", "location": "Al Farwaniyah Governorate, Kuwait"},
    {"id": 25, "name": "Raihan", "initials": "R1", "position": "Sales", "uds-filter": "ADvngMjcH0KdF7qGWtwTBrP0nt7diIVohtvdusKCCc-5AJAmrb3GJ4jZ-S1JHBgg2hfmmTTK3l8JzOgMdULLKuhMBxXwpJWGcQVnv9U5quAqw9DWeo7dBNP_0sJeFnVNQSlr5ABdUlvt-K6UStW68K-4vU9E9D8Moq4Rr8y62PhTNzyel2mbFF7WSbxWc3KDu-rD3A_Uv5Z3XNOKVj_D7S17CejC7Iw8Bf8mcNg1EY-DsIpgt_zTlZH3-E4MOcsupcqTF7TvkxbH6ERFRdnS1AJK47Z6ik0iiZ9TGrAHK63cVc5QxKLF8A63OzeWUS-4BE71glvoJoC_V82BR4EKbhwF1QTd_2DS2A", "location": "Al Farwaniyah Governorate, Kuwait"},
    {"id": 26, "name": "Jayden", "initials": "JD1", "position": "Admin Jobs", "uds-filter": "ABqPDvztZD_Nu18FR6tNPw2cK_RRJiRBL9ABNrFVh2IjjZXXrjK_XLuWhkHfzFfu1abFLqUK9-nbgOCVtbtXDSxxrQ96Un3O4NMbBo3KETMgl8R9_2pOQIPKvAg6MJ78IOKyWsSiajRFJlJku9mE5Hv_rlpG3u1f4oDg8apYnSdr7DLEmzFFZvmYsVp4etYb9tLAySEO2t-Kahl8YBYJRKDv20B9PfLU8FS5VV4ofmUg3fH3faTCaKm7djsPpwrjX3g8nDNpnehbcXzVLt4aDSYBYR0E01B0Wdx26M6xUqBtbjyW5WFXIKcZ8X4XpYP3EfeC4gIfURgdNbzZ5r9jJ-i6SjAquQ2f8A", "location": "Al Farwaniyah Governorate, Kuwait"},
    {"id": 27, "name": "Avlon Avy Rodrigues", "initials": "AAR2", "position": "HR", "uds-filter": "ABqPDvztZD_Nu18FR6tNPw2cK_RRJiRBL9ABNrFVh2IjjZXXrjK_XLuWhkHfzFfu1abFLqUK9-nbgOCVtbtXDSxxrQ96Un3O4NMbBo3KETMgl8R9_2pOQIPKvAg6MJ78IOKyWsSiajRFJlJku9mE5Hv_rlpG3u1f4oDg8apYnSdr7DLEmzFFZvmYsVp4etYb9tLAySEO2t-Kahl8YBYJRKDv20B9PfLU8FS5VV4ofmUg3fH3faTCaKm7djsPpwrjX3g8nDNpnehbcXzVLt4aDSYBYR0E01B0Wdx26M6xUqBtbjyW5WFXIKcZ8X4XpYP3EfeC4gIfURgdNbzZ5r9jJ-i6SjAquQ2f8A", "location": "Al Farwaniyah Governorate, Kuwait"},
    {"id": 28, "name": "Avlon Avy Rodrigues", "initials": "AAR3", "position": "Marketing", "uds-filter": "ABqPDvztZD_Nu18FR6tNPw2cK_RRJiRBL9ABNrFVh2IjjZXXrjK_XLuWhkHfzFfu1abFLqUK9-nbgOCVtbtXDSxxrQ96Un3O4NMbBo3KETMgl8R9_2pOQIPKvAg6MJ78IOKyWsSiajRFJlJku9mE5Hv_rlpG3u1f4oDg8apYnSdr7DLEmzFFZvmYsVp4etYb9tLAySEO2t-Kahl8YBYJRKDv20B9PfLU8FS5VV4ofmUg3fH3faTCaKm7djsPpwrjX3g8nDNpnehbcXzVLt4aDSYBYR0E01B0Wdx26M6xUqBtbjyW5WFXIKcZ8X4XpYP3EfeC4gIfURgdNbzZ5r9jJ-i6SjAquQ2f8A", "location": "Al Farwaniyah Governorate, Kuwait"},
    {"id": 29, "name": "Avlon Avy Rodrigues", "initials": "AAR4", "position": "Accountant", "uds-filter": "ABqPDvztZD_Nu18FR6tNPw2cK_RRJiRBL9ABNrFVh2IjjZXXrjK_XLuWhkHfzFfu1abFLqUK9-nbgOCVtbtXDSxxrQ96Un3O4NMbBo3KETMgl8R9_2pOQIPKvAg6MJ78IOKyWsSiajRFJlJku9mE5Hv_rlpG3u1f4oDg8apYnSdr7DLEmzFFZvmYsVp4etYb9tLAySEO2t-Kahl8YBYJRKDv20B9PfLU8FS5VV4ofmUg3fH3faTCaKm7djsPpwrjX3g8nDNpnehbcXzVLt4aDSYBYR0E01B0Wdx26M6xUqBtbjyW5WFXIKcZ8X4XpYP3EfeC4gIfURgdNbzZ5r9jJ-i6SjAquQ2f8A", "location": "Al Farwaniyah Governorate, Kuwait"},
    {"id": 30, "name": "Sara Abu Atta", "initials": "SAA", "position": "Senior Marketing Manager", "uds-filter": "ABqPDvztZD_Nu18FR6tNPw2cK_RRJiRBL9ABNrFVh2IjjZXXrjK_XLuWhkHfzFfu1abFLqUK9-nbgOCVtbtXDSxxrQ96Un3O4NMbBo3KETMgl8R9_2pOQIPKvAg6MJ78IOKyWsSiajRFJlJku9mE5Hv_rlpG3u1f4oDg8apYnSdr7DLEmzFFZvmYsVp4etYb9tLAySEO2t-Kahl8YBYJRKDv20B9PfLU8FS5VV4ofmUg3fH3faTCaKm7djsPpwrjX3g8nDNpnehbcXzVLt4aDSYBYR0E01B0Wdx26M6xUqBtbjyW5WFXIKcZ8X4XpYP3EfeC4gIfURgdNbzZ5r9jJ-i6SjAquQ2f8A", "location": "Al Farwaniyah Governorate, Kuwait"},
    {"id": 31, "name": "Melroy Lobo", "initials": "MLF", "position": "Frontend Developer", "uds-filter": "ABqPDvztZD_Nu18FR6tNPw2cK_RRJiRBL9ABNrFVh2IjjZXXrjK_XLuWhkHfzFfu1abFLqUK9-nbgOCVtbtXDSxxrQ96Un3O4NMbBo3KETMgl8R9_2pOQIPKvAg6MJ78IOKyWsSiajRFJlJku9mE5Hv_rlpG3u1f4oDg8apYnSdr7DLEmzFFZvmYsVp4etYb9tLAySEO2t-Kahl8YBYJRKDv20B9PfLU8FS5VV4ofmUg3fH3faTCaKm7djsPpwrjX3g8nDNpnehbcXzVLt4aDSYBYR0E01B0Wdx26M6xUqBtbjyW5WFXIKcZ8X4XpYP3EfeC4gIfURgdNbzZ5r9jJ-i6SjAquQ2f8A", "location": "Al Farwaniyah Governorate, Kuwait"},
    {"id": 32, "name": "Melroy Lobo", "initials": "MLB", "position": "Backend Developer", "uds-filter": "ABqPDvztZD_Nu18FR6tNPw2cK_RRJiRBL9ABNrFVh2IjjZXXrjK_XLuWhkHfzFfu1abFLqUK9-nbgOCVtbtXDSxxrQ96Un3O4NMbBo3KETMgl8R9_2pOQIPKvAg6MJ78IOKyWsSiajRFJlJku9mE5Hv_rlpG3u1f4oDg8apYnSdr7DLEmzFFZvmYsVp4etYb9tLAySEO2t-Kahl8YBYJRKDv20B9PfLU8FS5VV4ofmUg3fH3faTCaKm7djsPpwrjX3g8nDNpnehbcXzVLt4aDSYBYR0E01B0Wdx26M6xUqBtbjyW5WFXIKcZ8X4XpYP3EfeC4gIfURgdNbzZ5r9jJ-i6SjAquQ2f8A", "location": "Al Farwaniyah Governorate, Kuwait"},
    {"id": 33, "name": "Melroy Lobo", "initials": "MLFS", "position": "Full stack developer", "uds-filter": "ABqPDvztZD_Nu18FR6tNPw2cK_RRJiRBL9ABNrFVh2IjjZXXrjK_XLuWhkHfzFfu1abFLqUK9-nbgOCVtbtXDSxxrQ96Un3O4NMbBo3KETMgl8R9_2pOQIPKvAg6MJ78IOKyWsSiajRFJlJku9mE5Hv_rlpG3u1f4oDg8apYnSdr7DLEmzFFZvmYsVp4etYb9tLAySEO2t-Kahl8YBYJRKDv20B9PfLU8FS5VV4ofmUg3fH3faTCaKm7djsPpwrjX3g8nDNpnehbcXzVLt4aDSYBYR0E01B0Wdx26M6xUqBtbjyW5WFXIKcZ8X4XpYP3EfeC4gIfURgdNbzZ5r9jJ-i6SjAquQ2f8A", "location": "Al Farwaniyah Governorate, Kuwait"},
    {"id": 34, "name": "Melroy Lobo", "initials": "MLDA", "position": "Data Analyst", "uds-filter": "ABqPDvztZD_Nu18FR6tNPw2cK_RRJiRBL9ABNrFVh2IjjZXXrjK_XLuWhkHfzFfu1abFLqUK9-nbgOCVtbtXDSxxrQ96Un3O4NMbBo3KETMgl8R9_2pOQIPKvAg6MJ78IOKyWsSiajRFJlJku9mE5Hv_rlpG3u1f4oDg8apYnSdr7DLEmzFFZvmYsVp4etYb9tLAySEO2t-Kahl8YBYJRKDv20B9PfLU8FS5VV4ofmUg3fH3faTCaKm7djsPpwrjX3g8nDNpnehbcXzVLt4aDSYBYR0E01B0Wdx26M6xUqBtbjyW5WFXIKcZ8X4XpYP3EfeC4gIfURgdNbzZ5r9jJ-i6SjAquQ2f8A", "location": "Al Farwaniyah Governorate, Kuwait"},
    {"id": 35, "name": "Mark Francis", "initials": "MFV", "position": "Video Editor", "uds-filter": "ABqPDvztZD_Nu18FR6tNPw2cK_RRJiRBL9ABNrFVh2IjjZXXrjK_XLuWhkHfzFfu1abFLqUK9-nbgOCVtbtXDSxxrQ96Un3O4NMbBo3KETMgl8R9_2pOQIPKvAg6MJ78IOKyWsSiajRFJlJku9mE5Hv_rlpG3u1f4oDg8apYnSdr7DLEmzFFZvmYsVp4etYb9tLAySEO2t-Kahl8YBYJRKDv20B9PfLU8FS5VV4ofmUg3fH3faTCaKm7djsPpwrjX3g8nDNpnehbcXzVLt4aDSYBYR0E01B0Wdx26M6xUqBtbjyW5WFXIKcZ8X4XpYP3EfeC4gIfURgdNbzZ5r9jJ-i6SjAquQ2f8A", "location": "Al Farwaniyah Governorate, Kuwait"},
    {"id": 36, "name": "Mark Francis", "initials": "MFV2", "position": "Content Specialist", "uds-filter": "ABqPDvztZD_Nu18FR6tNPw2cK_RRJiRBL9ABNrFVh2IjjZXXrjK_XLuWhkHfzFfu1abFLqUK9-nbgOCVtbtXDSxxrQ96Un3O4NMbBo3KETMgl8R9_2pOQIPKvAg6MJ78IOKyWsSiajRFJlJku9mE5Hv_rlpG3u1f4oDg8apYnSdr7DLEmzFFZvmYsVp4etYb9tLAySEO2t-Kahl8YBYJRKDv20B9PfLU8FS5VV4ofmUg3fH3faTCaKm7djsPpwrjX3g8nDNpnehbcXzVLt4aDSYBYR0E01B0Wdx26M6xUqBtbjyW5WFXIKcZ8X4XpYP3EfeC4gIfURgdNbzZ5r9jJ-i6SjAquQ2f8A", "location": "Al Farwaniyah Governorate, Kuwait"},
    {"id": 37, "name": "Krishna Sai Busamudram", "initials": "KSB", "position": "Software Developer", "uds-filter": "ABqPDvztZD_Nu18FR6tNPw2cK_RRJiRBL9ABNrFVh2IjjZXXrjK_XLuWhkHfzFfu1abFLqUK9-nbgOCVtbtXDSxxrQ96Un3O4NMbBo3KETMgl8R9_2pOQIPKvAg6MJ78IOKyWsSiajRFJlJku9mE5Hv_rlpG3u1f4oDg8apYnSdr7DLEmzFFZvmYsVp4etYb9tLAySEO2t-Kahl8YBYJRKDv20B9PfLU8FS5VV4ofmUg3fH3faTCaKm7djsPpwrjX3g8nDNpnehbcXzVLt4aDSYBYR0E01B0Wdx26M6xUqBtbjyW5WFXIKcZ8X4XpYP3EfeC4gIfURgdNbzZ5r9jJ-i6SjAquQ2f8A", "location": "Al Farwaniyah Governorate, Kuwait"},
    {"id": 38, "name": "Maryam Amin", "initials": "MA", "position": "Back end Developer jobs in kuwait in the last month", "uds-filter": "ABqPDvztZD_Nu18FR6tNPw2cK_RRJiRBL9ABNrFVh2IjjZXXrjK_XLuWhkHfzFfu1abFLqUK9-nbgOCVtbtXDSxxrQ96Un3O4NMbBo3KETMgl8R9_2pOQIPKvAg6MJ78IOKyWsSiajRFJlJku9mE5Hv_rlpG3u1f4oDg8apYnSdr7DLEmzFFZvmYsVp4etYb9tLAySEO2t-Kahl8YBYJRKDv20B9PfLU8FS5VV4ofmUg3fH3faTCaKm7djsPpwrjX3g8nDNpnehbcXzVLt4aDSYBYR0E01B0Wdx26M6xUqBtbjyW5WFXIKcZ8X4XpYP3EfeC4gIfURgdNbzZ5r9jJ-i6SjAquQ2f8A", "location": "Al Farwaniyah Governorate, Kuwait"},
    {"id": 39, "name": "Callie Travasso", "initials": "CTA", "position": "marketing internship jobs in kuwait in the last month", "uds-filter": "ABqPDvztZD_Nu18FR6tNPw2cK_RRJiRBL9ABNrFVh2IjjZXXrjK_XLuWhkHfzFfu1abFLqUK9-nbgOCVtbtXDSxxrQ96Un3O4NMbBo3KETMgl8R9_2pOQIPKvAg6MJ78IOKyWsSiajRFJlJku9mE5Hv_rlpG3u1f4oDg8apYnSdr7DLEmzFFZvmYsVp4etYb9tLAySEO2t-Kahl8YBYJRKDv20B9PfLU8FS5VV4ofmUg3fH3faTCaKm7djsPpwrjX3g8nDNpnehbcXzVLt4aDSYBYR0E01B0Wdx26M6xUqBtbjyW5WFXIKcZ8X4XpYP3EfeC4gIfURgdNbzZ5r9jJ-i6SjAquQ2f8A", "location": "Al Farwaniyah Governorate, Kuwait"},
    {"id": 40, "name": "Janice", "initials": "JOYJ", "position": "Auditor jobs in kuwait in the last week", "uds-filter": "ABqPDvztZD_Nu18FR6tNPw2cK_RRJiRBL9ABNrFVh2IjjZXXrjK_XLuWhkHfzFfu1abFLqUK9-nbgOCVtbtXDSxxrQ96Un3O4NMbBo3KETMgl8R9_2pOQIPKvAg6MJ78IOKyWsSiajRFJlJku9mE5Hv_rlpG3u1f4oDg8apYnSdr7DLEmzFFZvmYsVp4etYb9tLAySEO2t-Kahl8YBYJRKDv20B9PfLU8FS5VV4ofmUg3fH3faTCaKm7djsPpwrjX3g8nDNpnehbcXzVLt4aDSYBYR0E01B0Wdx26M6xUqBtbjyW5WFXIKcZ8X4XpYP3EfeC4gIfURgdNbzZ5r9jJ-i6SjAquQ2f8A", "location": "Al Farwaniyah Governorate, Kuwait"},
    {"id": 41, "name": "Callie Travasso", "initials": "CTA2", "position": "hr internship jobs in kuwait in the last month", "uds-filter": "ABqPDvztZD_Nu18FR6tNPw2cK_RRJiRBL9ABNrFVh2IjjZXXrjK_XLuWhkHfzFfu1abFLqUK9-nbgOCVtbtXDSxxrQ96Un3O4NMbBo3KETMgl8R9_2pOQIPKvAg6MJ78IOKyWsSiajRFJlJku9mE5Hv_rlpG3u1f4oDg8apYnSdr7DLEmzFFZvmYsVp4etYb9tLAySEO2t-Kahl8YBYJRKDv20B9PfLU8FS5VV4ofmUg3fH3faTCaKm7djsPpwrjX3g8nDNpnehbcXzVLt4aDSYBYR0E01B0Wdx26M6xUqBtbjyW5WFXIKcZ8X4XpYP3EfeC4gIfURgdNbzZ5r9jJ-i6SjAquQ2f8A", "location": "Al Farwaniyah Governorate, Kuwait"},
    {"id": 42, "name": "Callie Travasso", "initials": "CTA3", "position": "sales internship jobs in kuwait in the last month", "uds-filter": "ABqPDvztZD_Nu18FR6tNPw2cK_RRJiRBL9ABNrFVh2IjjZXXrjK_XLuWhkHfzFfu1abFLqUK9-nbgOCVtbtXDSxxrQ96Un3O4NMbBo3KETMgl8R9_2pOQIPKvAg6MJ78IOKyWsSiajRFJlJku9mE5Hv_rlpG3u1f4oDg8apYnSdr7DLEmzFFZvmYsVp4etYb9tLAySEO2t-Kahl8YBYJRKDv20B9PfLU8FS5VV4ofmUg3fH3faTCaKm7djsPpwrjX3g8nDNpnehbcXzVLt4aDSYBYR0E01B0Wdx26M6xUqBtbjyW5WFXIKcZ8X4XpYP3EfeC4gIfURgdNbzZ5r9jJ-i6SjAquQ2f8A", "location": "Al Farwaniyah Governorate, Kuwait"},
    {"id": 43, "name": "Sakina", "initials": "SA3", "position": "Graphic Designer jobs in kuwait in the last week", "uds-filter": "ABqPDvztZD_Nu18FR6tNPw2cK_RRnGWYudk6uw8uavw97RLFuZ-vdnMOZ8F89Z49lFobhrXs9lhsZvewNqcuymAyVtNF_zkNkaj9gNEwXRSAzmD1AnjwS45NIW8GQhR4WYfv38jtPyEYq61AAA3gSe1BH1-dnymHaMvyeIBtVwHnlHiFed5pmX9a9fBgmmfASUD9h6aBQs4OK8zMBbGX7DUIaer1RetkoaU9IKd_Nz32cB8RpzxKmUCvYVWQtyyPYUwf1WB9cr66mHE6SVJJbvyyLOFreaamccVN69UK3giEmJGkkWJowZzqgxjG-R6d0aLGsBHU06qn99_wr8HTt-QIeMMf6ZuCgg", "location": "Al Farwaniyah Governorate, Kuwait"},
    {"id": 44, "name": "Reem", "initials": "RM", "position": "Software Engineer jobs in Cairo in the last month", "uds-filter": "ABqPDvztZD_Nu18FR6tNPw2cK_RRnGWYudk6uw8uavw97RLFuZ-vdnMOZ8F89Z49lFobhrXs9lhsZvewNqcuymAyVtNF_zkNkaj9gNEwXRSAzmD1AnjwS45NIW8GQhR4WYfv38jtPyEYq61AAA3gSe1BH1-dnymHaMvyeIBtVwHnlHiFed5pmX9a9fBgmmfASUD9h6aBQs4OK8zMBbGX7DUIaer1RetkoaU9IKd_Nz32cB8RpzxKmUCvYVWQtyyPYUwf1WB9cr66mHE6SVJJbvyyLOFreaamccVN69UK3giEmJGkkWJowZzqgxjG-R6d0aLGsBHU06qn99_wr8HTt-QIeMMf6ZuCgg", "location": "Cairo, Egypt"},
    {"id": 45, "name": "Reem", "initials": "RM", "position": "Data Science jobs in the last week", "uds-filter": "ABqPDvztZD_Nu18FR6tNPw2cK_RRnGWYudk6uw8uavw97RLFuZ-vdnMOZ8F89Z49lFobhrXs9lhsZvewNqcuymAyVtNF_zkNkaj9gNEwXRSAzmD1AnjwS45NIW8GQhR4WYfv38jtPyEYq61AAA3gSe1BH1-dnymHaMvyeIBtVwHnlHiFed5pmX9a9fBgmmfASUD9h6aBQs4OK8zMBbGX7DUIaer1RetkoaU9IKd_Nz32cB8RpzxKmUCvYVWQtyyPYUwf1WB9cr66mHE6SVJJbvyyLOFreaamccVN69UK3giEmJGkkWJowZzqgxjG-R6d0aLGsBHU06qn99_wr8HTt-QIeMMf6ZuCgg", "location": "Al Farwaniyah Governorate, Kuwait"},
    {"id": 46, "name": "Tanisha", "initials": "TAN", "position": "Logistics jobs in the last week", "uds-filter": "ABqPDvztZD_Nu18FR6tNPw2cK_RRnGWYudk6uw8uavw97RLFuZ-vdnMOZ8F89Z49lFobhrXs9lhsZvewNqcuymAyVtNF_zkNkaj9gNEwXRSAzmD1AnjwS45NIW8GQhR4WYfv38jtPyEYq61AAA3gSe1BH1-dnymHaMvyeIBtVwHnlHiFed5pmX9a9fBgmmfASUD9h6aBQs4OK8zMBbGX7DUIaer1RetkoaU9IKd_Nz32cB8RpzxKmUCvYVWQtyyPYUwf1WB9cr66mHE6SVJJbvyyLOFreaamccVN69UK3giEmJGkkWJowZzqgxjG-R6d0aLGsBHU06qn99_wr8HTt-QIeMMf6ZuCgg", "location": "Dubai, United Arab Emirates"},
    {"id": 47, "name": "Samskriti Pai", "initials": "SAM1", "position": "Marketing jobs in the last week", "uds-filter": "ABqPDvztZD_Nu18FR6tNPw2cK_RRnGWYudk6uw8uavw97RLFuZ-vdnMOZ8F89Z49lFobhrXs9lhsZvewNqcuymAyVtNF_zkNkaj9gNEwXRSAzmD1AnjwS45NIW8GQhR4WYfv38jtPyEYq61AAA3gSe1BH1-dnymHaMvyeIBtVwHnlHiFed5pmX9a9fBgmmfASUD9h6aBQs4OK8zMBbGX7DUIaer1RetkoaU9IKd_Nz32cB8RpzxKmUCvYVWQtyyPYUwf1WB9cr66mHE6SVJJbvyyLOFreaamccVN69UK3giEmJGkkWJowZzqgxjG-R6d0aLGsBHU06qn99_wr8HTt-QIeMMf6ZuCgg", "location": "Dubai, United Arab Emirates"},
    {"id": 48, "name": "Samskriti Pai", "initials": "SAM2", "position": "Accountant jobs in the last week", "uds-filter": "ABqPDvztZD_Nu18FR6tNPw2cK_RRnGWYudk6uw8uavw97RLFuZ-vdnMOZ8F89Z49lFobhrXs9lhsZvewNqcuymAyVtNF_zkNkaj9gNEwXRSAzmD1AnjwS45NIW8GQhR4WYfv38jtPyEYq61AAA3gSe1BH1-dnymHaMvyeIBtVwHnlHiFed5pmX9a9fBgmmfASUD9h6aBQs4OK8zMBbGX7DUIaer1RetkoaU9IKd_Nz32cB8RpzxKmUCvYVWQtyyPYUwf1WB9cr66mHE6SVJJbvyyLOFreaamccVN69UK3giEmJGkkWJowZzqgxjG-R6d0aLGsBHU06qn99_wr8HTt-QIeMMf6ZuCgg", "location": "Dubai, United Arab Emirates"},
    {"id": 49, "name": "Samskriti Pai", "initials": "SAM3", "position": "HR jobs in the last week", "uds-filter": "ABqPDvztZD_Nu18FR6tNPw2cK_RRnGWYudk6uw8uavw97RLFuZ-vdnMOZ8F89Z49lFobhrXs9lhsZvewNqcuymAyVtNF_zkNkaj9gNEwXRSAzmD1AnjwS45NIW8GQhR4WYfv38jtPyEYq61AAA3gSe1BH1-dnymHaMvyeIBtVwHnlHiFed5pmX9a9fBgmmfASUD9h6aBQs4OK8zMBbGX7DUIaer1RetkoaU9IKd_Nz32cB8RpzxKmUCvYVWQtyyPYUwf1WB9cr66mHE6SVJJbvyyLOFreaamccVN69UK3giEmJGkkWJowZzqgxjG-R6d0aLGsBHU06qn99_wr8HTt-QIeMMf6ZuCgg", "location": "Dubai, United Arab Emirates"},
    {"id": 50, "name": "Meriska", "initials": "MS1", "position": "Social Media Marketing jobs in the last week", "uds-filter": "ABqPDvztZD_Nu18FR6tNPw2cK_RRnGWYudk6uw8uavw97RLFuZ-vdnMOZ8F89Z49lFobhrXs9lhsZvewNqcuymAyVtNF_zkNkaj9gNEwXRSAzmD1AnjwS45NIW8GQhR4WYfv38jtPyEYq61AAA3gSe1BH1-dnymHaMvyeIBtVwHnlHiFed5pmX9a9fBgmmfASUD9h6aBQs4OK8zMBbGX7DUIaer1RetkoaU9IKd_Nz32cB8RpzxKmUCvYVWQtyyPYUwf1WB9cr66mHE6SVJJbvyyLOFreaamccVN69UK3giEmJGkkWJowZzqgxjG-R6d0aLGsBHU06qn99_wr8HTt-QIeMMf6ZuCgg", "location": "Al Farwaniyah Governorate, Kuwait"},
    {"id": 51, "name": "Meriska", "initials": "MS2", "position": "Marketing jobs in the last week", "uds-filter": "ABqPDvztZD_Nu18FR6tNPw2cK_RRnGWYudk6uw8uavw97RLFuZ-vdnMOZ8F89Z49lFobhrXs9lhsZvewNqcuymAyVtNF_zkNkaj9gNEwXRSAzmD1AnjwS45NIW8GQhR4WYfv38jtPyEYq61AAA3gSe1BH1-dnymHaMvyeIBtVwHnlHiFed5pmX9a9fBgmmfASUD9h6aBQs4OK8zMBbGX7DUIaer1RetkoaU9IKd_Nz32cB8RpzxKmUCvYVWQtyyPYUwf1WB9cr66mHE6SVJJbvyyLOFreaamccVN69UK3giEmJGkkWJowZzqgxjG-R6d0aLGsBHU06qn99_wr8HTt-QIeMMf6ZuCgg", "location": "Al Farwaniyah Governorate, Kuwait"},
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
        job_list_message += "No apply options available\n"
    
    job_list_message += "\n"  # Add spacing between job entries

# Save the job list message to a text file
with open("job_list_message.txt", "w", encoding="utf-8") as file:
    file.write(job_list_message)

# Let the user know the message was saved
print(f"The job list message for {selected_user['name']} has been updated and saved to 'job_list_message.txt'. Open the file to copy and paste the message easily.")
