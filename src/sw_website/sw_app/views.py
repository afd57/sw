from django.shortcuts import render
from sw_app.models import Story
# Create your views here.

def index(request):
    all_story = Story.objects.all()
    story_title = all_story.story.name
    story_type = all_story.story.story_type
    story_priority = all_story.card.priority
    time_bound = all_story.card.time_bound
    author = all_story.confirmation.creator
    approver = all_story.confirmation.approver
    note = all_story.confirmation.note
    approve_date = all_story.confirmation.date
    who = all_story.card.who
    why = all_story.card.why
    what = all_story.card.what
    end_point = all_story.detailedappropriately.end_point
    detail_description = all_story.detailedappropriately.description.html
    story_input = all_story.detailedappropriately.story_input
    internal_apis = all_story.detailedappropriately.internal_apis
    formula = all_story.detailedappropriately.formula
    external_apis = all_story.detailedappropriately.external_apis
    authantication = all_story.detailedappropriately.authantication
    max_response_time = all_story.detailedappropriately.max_response_time
    acceptancecriteria = all_story.acceptancecriteria_set
    







    return render(
        request,
        'display.html',
        context={"test":all_story[0].detailedappropriately.description.html},
    )
