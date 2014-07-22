from django.shortcuts import render

from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.context_processors import csrf
from recaptcha.client import captcha
from utils import *

def getthoughts(request):
    response_data = fetch_thoughts()
    return HttpResponse(json.dumps(response_data), content_type="application/json")

def home(request):
    contents = retrieve_data()
    for content in contents:
        content.tags = content.tags.split(',')
    return render_to_response('home.html',{'share':True,'contents':contents},context_instance=RequestContext(request))

def article(request):
    if request.method == "GET":
        article_id = request.GET.get('id','')
        content = get_thoughts_by_id(article_id)
        tags = content.tags.split(',')
        title = content.title
        return render_to_response('article.html',{'share':True,'content':content,'tags':tags,'title':title},context_instance=RequestContext(request))

def search(request):
    if request.method == "GET":
        tag_name = request.GET.get('search-tag','')
        contents = search_tag(tag_name)
        for content in contents:
            tags = content.tags.split(',')
        return render_to_response('search.html',{'share':True,'contents':contents,'tags':tags},context_instance=RequestContext(request))

def toshare(request):
    remote_address =  get_client_ip(request)
    context_dict = {}
    if request.method=='POST':
        title = request.POST.get('title','')
        content = request.POST.get('content','')
        tags = request.POST.get('tags','')
        category_selected = request.POST.get('category_selected','')
        #response = captcha.submit(request.POST.get('recaptcha_challenge_field',''),
        #                          request.POST.get('recaptcha_response_field',''),
        #                          '6LctCPMSAAAAAEW17EABD3SDTgvCclUnT058mwxN',
        #                          remote_address)
        context_dict['errors'] = validate_data(title, content, tags, category_selected)
        #if not response.is_valid:
        #    context_dict['captcha_error'] = True
        #else:
        if len(context_dict['errors']) == 0:
            save_text_for_review(title,content,tags,category_selected)
            return HttpResponseRedirect(reverse("thanks_page"))
    context_dict['options'] = get_category()
    context_dict.update(csrf(request))
    return render_to_response('share.html',context_dict,context_instance=RequestContext(request))

def thanks(request):
    return render_to_response('thanks.html',{'share':True},context_instance=RequestContext(request))

def about(request):
    return render_to_response('about.html',{'share':True},context_instance=RequestContext(request))

def feedback(request):
    return render_to_response('feedback.html',{'share':True},context_instance=RequestContext(request))

def feedback_thanks(request):
    if request.method=='POST':
        ip_address = get_client_ip(request)
        comment = request.POST.get('feedback','')
        save_feedback(comment, ip_address)
    return render_to_response('feedback_thanks.html',{'share':True},context_instance=RequestContext(request))
                                
