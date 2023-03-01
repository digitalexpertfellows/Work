from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

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
    "december": "Meet with Santa!"
}

# Create your views here.
def monthly_challenge_by_number(request, month):
   months = list(monthly_challenges.keys())

   if month > len(months):
       return HttpResponseNotFound("Invalid month!")
   redirect_month = months[month-1]
   return HttpResponseRedirect(redirect_month)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported")



