#!/home/talen/python2.7/bin/python
#coding=UTF8

from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from ChaDianFei.models import ChaDianFei
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader,Context,RequestContext

from ChaDianFei.models import *
from django.shortcuts import render_to_response

#import sys
#if not "/mypython/" in sys.path:
#    sys.path.append("/mypython/") 
from insertdb import Insertdb 
#import mypython.insertdb.Insertdb as Insertdb
    
def remark(request):
    if request.method == 'POST': # 如果表单被提交
        form = ContactForm(request.POST) # 获取Post表单数据
        if form.is_valid(): # 验证表单
            #向数据库插入数据
            dorm = form.cleaned_data['dorm']
            mail = form.cleaned_data['mail']
            newmessage=Insertdb(dorm, mail)
            try:
                newmessage.save()
            except Exception as e:
                return HttpResponseRedirect('/error/') # 错误跳转
            return HttpResponseRedirect('/remark/') # 跳转
    else:
        form = ContactForm() #获得表单对象
        variables = RequestContext(request, {'form': form})
    return render_to_response('message.html', variables) 
   
#def error(request):
#    return render_to_response('errorPage.html',{'error': 'error'},context_instance=RequestContext(request))

   
def test(request):
    dorm=request.GET.get('dorm')
    mail=request.GET.get('mail')
    newmessage=Insertdb(dorm,mail)
    ret=newmessage.save()
    if(ret==1):
        return HttpResponse('succeed!')
    else: 
        return HttpResponse('unknow error!')

    

















