from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import  login_required
from django.views.generic.base import TemplateView


#View inicio club
@method_decorator(login_required, name='dispatch')
class HomePageView(TemplateView):
    template_name = "core/index.html"
    
    def get(self,request,*args,**kwargs):
        return render(request, self.template_name, {"title":"Home | Club"})

#View inicio general
class InicioPageView(TemplateView):
    template_name = "core/inicio.html"
    
    def get(self,request,*args,**kwargs):
        return render(request, self.template_name, {"title":"Home | Medical Weed App"})

