from .models import Feedback
from ..product.models import Product
from ..user.models import Profile
from django.shortcuts import get_object_or_404
import json
import requests


def get_feedback(request):
    return list(Feedback.objects.values("id","user","product","message","rating", "sentiment","summary", "suggestions"))

def get_feedback_by_id(request,user_id):
    feedbacks = Feedback.objects.filter(user__id = user_id).values("id","user","product","message","rating")
    print(feedbacks)
    if feedbacks:
        return {"feedback":list(feedbacks)}
    else:
        return {"message":f"{user_id} there no feedback from this user"}

def add_feedback (request):
    data = json.loads(request.body)

    user = get_object_or_404(Profile, id=request.user_id)
    product = get_object_or_404(Product, id=data.get("product_id"))
    ai_response = sentiment_analyzer(data.get("message"), data.get("rating"))
    
    Feedback.objects.create(user = user,product=product,message = data.get("message"),rating=data.get("rating"),
                             sentiment=ai_response.get("sentiment"), summary=ai_response.get("summary"), suggestions=ai_response.get("suggestions"))

    return {"message": "feedback added successfully"}

def sentiment_analyzer(message, rating):
    url = "https://sharp-gpt.ai/PostAPIRequest"

    payload = json.dumps({
    "inputPrompt": f"message : {message}, rating  : {rating}",
    "ChatMessage": [
        {
        "role": "system",
        "content": "You are an AI feedback analyzer. You will receive a input like this: message : message, rating : rating "
        "Analyze both the message and rating, and return ONLY a JSON response with these fields: "
        "{ \"sentiment\": \"positive | neutral | negative\", \"summary\": \"A one-sentence summary of the feedback\", \"suggestions\": [\"List of recommended improvements or acknowledgments based on the feedback\"] } "
        "Rules: - Use both the message and rating to infer sentiment. - If rating ≤ 2 → likely negative; if rating = 3 → neutral; if rating ≥ 4 → positive (unless message strongly contradicts it). - Respond ONLY in JSON, with no explanation text. Example Input: { \"message\": \"The app is great but crashes when I try to upload an image.\", \"rating\": 3 } Example Output: { \"sentiment\": \"negative\", \"summary\": \"User experiences crashes during image upload despite overall satisfaction.\", \"suggestions\": [\"Fix image upload crashes\", \"Improve app stability\"] }"
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
    
    return json.loads(content)