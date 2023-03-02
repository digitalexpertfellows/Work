from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


monthly_challenges = {
    "january": "Eat no meat this month!",
    "february":  "Walk for at least 20 minutes a day!",
    "march": "Learn django at least 20 minutes at day",
    "april": "Learn to be fooled!",
    "may":" Say no more!",
    "june": "Get enough sunshine",
    "july": "Get hotter",
    "august": "Go to the beach",
    "september": "Eat no more crap!",
    "october": "Drink more beer",
    "november": "Buy new shoes!",
    "december": None
}

# Create your views here.


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", {
        "months": months
    })


    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

def monthly_challenge_by_number(request, month):
   months = list(monthly_challenges.keys())

   if month > len(months):
       return HttpResponseNotFound("Invalid month!")
   redirect_month = months[month-1]
   redirect_path = reverse("month-challenge", args=[redirect_month]) #/challenge/january
   return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request , "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month
        })
    except:
        return HttpResponseNotFound("<h1>Invalid data for month!</h1>")



