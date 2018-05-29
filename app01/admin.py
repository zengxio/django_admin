from django.contrib import admin
from django.http import HttpResponse
# Register your models here.
from app01 import models
from django.utils.safestring import mark_safe
from django.forms import widgets
from django.utils.html import format_html


class MyTextarea(widgets.Widget):
    def __init__(self, attrs=None):
        # Use slightly better defaults than HTML's 20x2 box
        default_attrs = {'cols': '40', 'rows': '10'}
        if attrs:
            default_attrs.update(attrs)
        super(MyTextarea, self).__init__(default_attrs)

    def render(self, name, value, attrs=None):
        if value is None:
            value = ''
        final_attrs = self.build_attrs(attrs, name=name)
        return format_html('<textarea {}>\r\n{}</textarea>', final_attrs, value)

from app01 import models
from django.forms import ModelForm
from django.forms import fields
from django.forms import widgets

class MyForm(ModelForm):
    others = fields.CharField(widget=widgets.TextInput())  #加字段
    user = fields.CharField(widget=widgets.TextInput(),error_messages={'required':'用户名不能为空'}) #默认优先使用

    class Meta:
        model = models = models.UserInfo
        fields = "__all__"


class UserInfoModelAdmin(admin.ModelAdmin):

    def yuhao(obj):
        return mark_safe("<a href='http://www.baidu.com'>%s</a>"%(obj.user))

    list_display = ('user', 'email',yuhao) #用于定制页面具体显示哪一列数据
    list_display_links =('email',) #定制email可点击进入修改
    list_filter = ('user','email') #右边筛选框
    # list_select_related，列表时，连表查询是否自动select_related 跟ForeignKey 有关
    """
    分页相关
    # 分页，每页显示条数
        list_per_page = 100
    # 分页，显示全部（真实数据<该值时，才会有显示全部）
        list_max_show_all = 200  
    # 分页插件
        paginator = Paginator
    """

    # #设置为可编辑框
    # list_editable=('user',)

    #模糊搜索
    search_fields=('user',)
    # def changelist_view(self, request, extra_context=None):
    #     return HttpResponse("余浩不玩了")

    #date_hierarchy，列表时，对Date和DateTime类型进行搜索
    preserve_filters=False #详细页面，删除、修改，更新后跳转回列表后，是否保留原搜索条件.在url上可见

    #save_as = False，详细页面，按钮为“Sava as new” 或 “Sava and add another”是否显示按钮
    #save_as_continue = True，点击保存并继续编辑
    #save_on_top = False，详细页面，在页面上方是否也显示保存删除等按钮
    #action，列表时，定制action中的操作,批量操作数据

    def func(self, request, queryset):
        print(self, request, queryset)
        print(request.POST.getlist('_selected_action'))

    func.short_description = "中文显示自定义Actions"
    actions=[func,]

    #定制HTML模板
    # change_list_template ="my_change_list.html" #显示自定制页面
    """
    add_form_template = None
    change_form_template = None
    change_list_template = None
    delete_confirmation_template = None
    delete_selected_confirmation_template = None
    object_history_template = None
    """

    # raw_id_fields=('ug',) #详细页面，针对FK和M2M字段变成以Input框形式
    # fields，详细页面时，显示字段的字段
    # exclude=('user',)#详细页面时，排除的字段
    #readonly_fields，详细页面时，只读字段
    # fieldsets = (
    #     ('基本数据', {
    #         'fields': ('user',)
    #     }),
    #     ('其他', {
    #         'classes': ('collapse', 'wide', 'extrapretty'),  # 'collapse','wide', 'extrapretty'样式
    #         'fields': ( 'email',),
    #     }),
    # ) #详细页面时，使用fieldsets标签对数据进行分割显示

    #详细页面时，M2M显示时，数据移动选择（方向：上下和左右）
    # filter_vertical = ('m2m',)#上下
    filter_horizontal=('m2m',)#左右
    #ordering = ('-id') #列表时，数据排序规则

    def view_on_site(self, obj): #编辑时，是否在页面上显示view on set
        return 'https://www.baidu.com'

    #详细页面时，使用radio显示选项（FK默认使用select）
    radio_fields = {"ug": admin.VERTICAL}  # 或admin.HORIZONTAL 水平的
    show_full_result_count = True #列表时，模糊搜索后面显示的数据个数样式

    #详细页面时，指定实现插件
    # formfield_overrides = {
    #     models.models.CharField: {'widget': MyTextarea},
    # }

    # prepopulated_fields = {"email": ("user", "email",)} #添加页面，当在某字段填入值后，自动会将值填充到指定字段。

    empty_value_display = "列数据为空时，显示默认值"
    form = MyForm #使用自定制的myform

#inlines详细页面，如果有其他表和当前表做FK，那么详细页面可以进行动态增加和删除
class UserInfoInline(admin.StackedInline):  # TabularInline 水平展示
    extra = 0
    model = models.UserInfo

class UserGroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    inlines = [UserInfoInline, ]



admin.site.register(models.UserInfo, UserInfoModelAdmin)
admin.site.register(models.UserGroup,UserGroupAdmin)
admin.site.register(models.Role,admin.ModelAdmin)


# @admin.register(models.UserInfo)                # 第一个参数可以是列表
# @admin.register(models.UserGroup)                # 第一个参数可以是列表
# class UserAdmin(admin.ModelAdmin):
#     # list_display = ('user', 'pwd',)
#     pass

# admin.site.register([models.UserInfo,models.UserGroup])
