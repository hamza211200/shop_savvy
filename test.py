import requests
import json

url = "https://sharp-gpt.ai/PostAPIRequest"

payload = json.dumps({
  "inputPrompt": "message : The food was good, rating  : 4",
  "ChatMessage": [
    {
      "role": "system",
      "content": "You are an AI feedback analyzer. You will receive a input like this: message: {message}, rating: {rating} Analyze both the message and rating, and return ONLY a JSON response with these fields: { \"sentiment\": \"positive | neutral | negative\", \"summary\": \"A one-sentence summary of the feedback\", \"suggestions\": [\"List of recommended improvements or acknowledgments based on the feedback\"] } Rules: - Use both the message and rating to infer sentiment. - If rating ≤ 2 → likely negative; if rating = 3 → neutral; if rating ≥ 4 → positive (unless message strongly contradicts it). - Respond ONLY in JSON, with no explanation text. Example Input: { \"message\": \"The app is great but crashes when I try to upload an image.\", \"rating\": 3 } Example Output: { \"sentiment\": \"negative\", \"summary\": \"User experiences crashes during image upload despite overall satisfaction.\", \"suggestions\": [\"Fix image upload crashes\", \"Improve app stability\"] }"
    }
  ],
  "userResume": None
})

headers = {'Content-Type': 'application/json'}

response = requests.post(url, headers=headers, data=payload)

# Parse the outer JSON
data = json.loads(response.text)

# Parse the nested JSON inside "data"
inner_data = json.loads(data["data"])

# Extract the AI message content
content = inner_data["choices"][0]["message"]["content"]

print(json.loads(content))
