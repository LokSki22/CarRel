from django.urls import path
from main.views import show_main, create_item, show_xml, show_json, show_xml_by_id, show_json_by_id
from main.views import register #sesuaikan dengan nama fungsi yang dibuat
from main.views import login_user #sesuaikan dengan nama fungsi yang dibuat
from main.views import logout_user
from main.views import edit_item
from main.views import get_product_json, add_product_ajax
from main.views import delete_item_ajax, decrement_item_ajax,increment_item_ajax,create_product_flutter
app_name = 'main'


urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-item', create_item, name='create_item'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('edit-item/<int:id>', edit_item, name='edit_item'),
    path('delete-item-ajax/<int:id>/', delete_item_ajax, name='delete_item_ajax'),
    path('get-product/', get_product_json, name='get_product_json'),
    path('create-product-ajax/', add_product_ajax, name='add_product_ajax'),
    path('increment-item-ajax/<int:id>/', increment_item_ajax, name='increment_item_ajax'),
    path('decrement-item-ajax/<int:id>/', decrement_item_ajax, name='decrement_item_ajax'),
    path('create-flutter/', create_product_flutter, name='create_product_flutter'),
]