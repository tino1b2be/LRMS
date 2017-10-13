from django.conf.urls import url

from prompts.views import PromptsView, PromptDistribution, PromptRejection, PromptDetail
app_name = 'prompts'

urlpatterns = [
    url(r'^$', PromptDetail.as_view(), name='prompt'),
    url(r'^all/$', PromptsView.as_view(), name='all'),
    url(r'^retrieve/$', PromptDistribution.as_view(), name='retrieve'),
    url(r'^reject/(?P<pk>\d+)/$', PromptRejection.as_view(), name='reject'),
]
