


# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import datetime
import os
from zoneinfo import ZoneInfo

import google.auth
from google.adk.agents import Agent

_, project_id = google.auth.default()
os.environ.setdefault("GOOGLE_CLOUD_PROJECT", project_id)
os.environ.setdefault("GOOGLE_CLOUD_LOCATION", "global")
os.environ.setdefault("GOOGLE_GENAI_USE_VERTEXAI", "True")

def get_store_address(store_id: str) -> str:
    """Retrieves the address of a store given its ID.  Also returns 10 fake pharmacy reviews.

    Args:
        store_id: The ID of the store.

    Returns:
        A string containing the store's address and 10 fake pharmacy reviews.
        Returns an error message if the store ID is not found.
    """
    # Replace this with actual store address retrieval logic.
    # This is a placeholder for demonstration purposes.
    if  "123" in store_id:
        address = "123 Main Street, Anytown, USA"
        reviews = [
            "Great service, friendly staff!",
            "Quick prescription refills.",
            "Always helpful and knowledgeable.",
            "Convenient location.",
            "Long wait times sometimes.",
            "Could use more parking.",
            "Excellent customer care.",
            "Pharmacist answered all my questions.",
            "Clean and well-organized.",
            "Highly recommend this pharmacy.",
        ]
        return f"Address: {address}\nReviews:\n" + "\n".join(
            [f"- {review}" for review in reviews]
        )
    elif  "456" in  store_id:
        address = "456 Oak Avenue, Anytown, USA"
        reviews = [
            "Fast and efficient service.",
            "Friendly and approachable staff.",
            "Competitive prices.",
            "Easy to transfer prescriptions.",
            "Sometimes understaffed.",
            "Limited selection of over-the-counter medications.",
            "Overall a good experience.",
            "Helpful with insurance questions.",
            "Drive-thru is very convenient.",
            "Will definitely use again.",
        ]
        return f"Address: {address}\nReviews:\n" + "\n".join(
            [f"- {review}" for review in reviews]
        )
    else:
        return f"Error: Store ID '{store_id}' not found."

def get_store_call_nps_score(store_id: str) -> str:
    """Retrieves the Net Promoter Score (NPS) for customer calls to a store and provides 5 sample call transcripts.

    Args:
        store_id: The ID of the store.

    Returns:
        A string containing the store's call NPS score and 5 sample call transcripts.
        Returns an error message if the store ID is not found.
    """
    # Replace this with actual NPS score and transcript retrieval logic.
    # This is a placeholder for demonstration purposes.
    if "123" in store_id:
        nps_score = "7.5"
        transcripts = [
            "Caller: I need to refill my prescription. Staff: Sure, can I have your name and prescription number?",
            "Caller: What are your hours? Staff: We're open from 9 AM to 7 PM, Monday through Friday.",
            "Caller: Do you have my medication in stock? Staff: Let me check... Yes, we do.",
            "Caller: I have a question about my insurance. Staff: I can help with that, what's your insurance provider?",
            "Caller: Thank you for your help! Staff: You're welcome, have a great day!",
        ]
        return (
            f"Call NPS Score: {nps_score}\nSample Call Transcripts:\n"
            + "\n".join([f"- {transcript}" for transcript in transcripts])
        )
    elif  "456" in store_id:
        nps_score = "8.2"
        transcripts = [
            "Caller: I'm transferring a prescription. Staff: Okay, I'll need some information from your current pharmacy.",
            "Caller: Can you check the price of a medication? Staff: One moment, please... The price is $25.",
            "Caller: I need to speak to the pharmacist. Staff: I'll connect you right away.",
            "Caller: I received a text about my prescription, but I'm not sure what it means. Staff: Let me look into that for you.",
            "Caller: Is my prescription ready for pickup? Staff: Yes, it is. You can pick it up anytime.",
        ]
        return (
            f"Call NPS Score: {nps_score}\nSample Call Transcripts:\n"
            + "\n".join([f"- {transcript}" for transcript in transcripts])
        )
    else:
        return f"Error: Store ID '{store_id}' not found."






root_agent = Agent(
    name="root_agent",
    model="gemini-2.0-flash",
    instruction="You are a helpful AI assistant designed to provide accurate and useful information.",
    tools=[get_store_address, get_store_call_nps_score],
)
