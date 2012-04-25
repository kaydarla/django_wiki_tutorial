from wiki.models import Page
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
import markdown

def view_page(request, page_name):
    try:
        page = Page.objects.get(pk=page_name)
    except Page.DoesNotExist:
        return render_to_response("create.html", { "pagename": page_name, })
    
    content = page.contents
    return render_to_response("view.html", { "pagename": page_name, 
                                             "content": markdown.markdown(content) })

def edit_page(request, page_name):
    try:
        page = Page.objects.get(pk=page_name)
        content = page.contents
    except Page.DoesNotExist:
        content = ""

    return render_to_response("edit.html", { "pagename": page_name, 
                                             "content": content, },
                              context_instance=RequestContext(request))


def save_page(request, page_name):
    content = request.POST["content"]
    try:
        page = Page.objects.get(pk=page_name)
        page.contents = content
    except Page.DoesNotExist:
        page = Page(name=page_name, contents=content)

    page.save()

    return HttpResponseRedirect(reverse("view_page", args=(page_name,)))
    
