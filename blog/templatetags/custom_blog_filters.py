from django import template
from ..models import Blog

register = template.Library() 

# @register.filter(group_name='blogger') 
# def has_group(user, group_name):
#     print(group_name)
#     print(user)
#     print(user.groups)
#     return user.groups.filter(name=group_name).exists()