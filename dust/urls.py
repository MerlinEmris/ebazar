url(r'^item-image-upload/$', views.BasicUploadView.as_view(), name='basic_upload'),
url(r'^rest-category/$', views.rest_category, name='rest_category'),
url(r'^rest-item/$', views.ItemList.as_view(), name='rest_item'),