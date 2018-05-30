from django.shortcuts import render,redirect
from app01 import models
# Create your views here.
from django.forms import Form,ModelForm
from django.forms import fields as ffields
from django.forms import widgets as fwidgests
# from django.template.response import TemplateResponse
"""
class TestForm(Form):
    user=fields.CharField()
    email=fields.EmailField()
    ug_id=fields.ChoiceField(
        widget=widgets.Select,
        choices=[]
    )
    
    #数据实时更新
    def __init__(self,*args,**kwargs):
        super(TestForm, self).__init__(*args,**kwargs)
        self.fields['ug_id'].choices=models.UserGroup.objects.values_list('id','title')

def test(request):
    # django admin原理
    # 默认访问我们自定制的页面，如果没有在访问自带的
    # return TemplateResponse(request,[] or ['xiaohaohao.html','my_change_list.html'],{'k1':'v1'})
    if request.method=="GET":
        form=TestForm()
        context={'form':form}
        return render(request,'test.html',context)
    else:
        form=TestForm(request.POST)
        if form.is_valid():
            models.UserInfo.objects.create(**form.cleaned_data)
            return redirect('http://www.baidu.com')
        context={'form':form}
        return render(request,'test.html',context)
"""
class TestModelForm(ModelForm):
    user=ffields.EmailField(label='用户名') #优先级高于field_classes
    class Meta:
        model=models.UserInfo
        fields="__all__"  #fields=('user','email') 指定显示的字段
        error_messages={
            'user':{'required':'用户名不能为空'},
            'email':{'required':'邮箱不能为空','invalid':'邮箱格式错误'},
            'ug':'',
            'm2m':'',
        }
        labels={  #字段名显示为中文
            'user':'用户名',
            'email':'邮箱'
        }
        help_texts={
            'user':"不区分大小写"
        }
        # widgets={ #定义插件
        #     'user':fwidgests.Textarea(attrs={'class':'c1'})
        # }
        # field_classes={ #为某个字段定义验证规则
        #     'user':ffields.EmailField
        # }

        """
        其他参数
        model,                           # 对应Model的
        fields=None,                     # 字段
        exclude=None,                    # 排除字段
        labels=None,                     # 提示信息
        help_texts=None,                 # 帮助提示信息
        widgets=None,                    # 自定义插件
        error_messages=None,             # 自定义错误信息（整体错误信息from django.core.exceptions import NON_FIELD_ERRORS）
        field_classes=None               # 自定义字段类 （也可以自定义字段）
        localized_fields=('birth_date',) # 本地化，如：根据不同时区显示数据
        如：
            数据库中
                2016-12-27 04:10:57
            setting中的配置
                TIME_ZONE = 'Asia/Shanghai'
                USE_TZ = True
            则显示：
                2016-12-27 12:10:57
        """
        #钩子函数
    def clean_user(self):
        pass
    def clean_email(self):
        pass

def test(request):
    # django admin原理
    # 默认访问我们自定制的页面，如果没有在访问自带的
    # return TemplateResponse(request,[] or ['xiaohaohao.html','my_change_list.html'],{'k1':'v1'})
    if request.method=="GET":
        form=TestModelForm()
        context={'form':form}
        return render(request,'test.html',context)
    else:
        form=TestModelForm(request.POST)
        if form.is_valid():
            # models.UserInfo.objects.create(**form.cleaned_data)
            # print(form.cleaned_data)
            form.save() #保存到数据库
            return redirect('http://www.baidu.com')
        context={'form':form}
        return render(request,'test.html',context)

def edit(request,nid):
    obj=models.UserInfo.objects.filter(id=nid).first()
    if request.method=="GET":
        form=TestModelForm(instance=obj)
        context = {'form': form}
        return render(request, 'edit.html', context)
    else:
        form = TestModelForm(instance=obj,data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('http://www.baidu.com')
        context = {'form': form}
        return render(request, 'edit.html', context)