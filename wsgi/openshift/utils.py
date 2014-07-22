import datetime
from django.forms.models import model_to_dict
import json
from core.models import *

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def validate_data(title, content, tags, category_selected):
    errors = {}
    if category_selected == "Choose Category":
        errors['category_error'] = True
    if title == "" or len(title) < 5:
        errors['title_error'] = True
    if content == "" or len(content) < 20:
        errors['content_error'] = True
    if tags == "" or len (tags) < 5:
        errors['tags_error'] = True
    return errors

def  get_thoughts_by_id(article_id):
    thought = TextTable.objects.filter(id=article_id)
    if thought:
      return thought[0]
    else:
      return None

def save_text_for_review(title, text, tags, category):
    time = str(datetime.datetime.now())
    ReviewTable.objects.create(title=title,text=text,tags=tags,timestamp=time,category=category)


def save_text(title,text,tags,category):
    time = str(datetime.datetime.now())
    TextTable.objects.create(title=title,text=text,tags=tags,timestamp=time,category=category)

def save_feedback(comment, ip_address):
    time = str(datetime.datetime.now())
    VisitorFeedback.objects.create(ip = ip_address, comments = comment,timestamp = time)

def retrieve_data():
    return TextTable.objects.all().order_by('-timestamp')[0:10]

def fetch_thoughts():
    thoughts = TextTable.objects.all().order_by('-timestamp')[0:10]
    thought_list = []
    for thought in thoughts:
      thought_dict = {}
      thought_dict['id'] = thought.id
      thought_dict['title'] = thought.title
      thought_dict['content'] = thought.text
      thought_list.append(thought_dict)
    return thought_list
      

def search_tag(tag):
    #return TextTable.objects.filter(tags=tag).order_by('-timestamp')
    return TextTable.objects.raw("select * from core_texttable WHERE MATCH(title,text,tags) AGAINST ('%s') limit 10"%tag)

def get_category():
    return Category.objects.all().order_by('name')

def save_media(title,text,tags,url):
    time =  str(datetime.datetime.now())
    TextTable.objects.create(title=title,text=text,tags=tags,url=url,timestamp=time)
