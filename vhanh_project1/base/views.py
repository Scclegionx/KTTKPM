from django.core.paginator import Paginator
from django.shortcuts import render
from pymongo import MongoClient
from django.conf import settings
from bson import ObjectId
from django.http import Http404


client = MongoClient(settings.DATABASES['ecommercedb']['CLIENT']['host'])
db = client.ecommercedb
# print(db.list_collection_names())
# print(list(db.product_book.find()))  # Xem tất cả sách
# print(list(db.product_clothes.find()))  # Xem tất cả quần áo
# print(settings.DATABASES['ecommercedb']['NAME'])  # Tên DB
# print(db.book.count_documents({}))  # Đếm số lượng tài liệu


def shop(request):
    product_type = request.GET.get('type', 'all')

    query = {}
    if product_type != 'all':
        query['category'] = product_type

    products = list(db.product_product.find(query))

    # Chuyển _id thành string để dùng được trong template
    for product in products:
        product['id_str'] = str(product['_id'])

    paginator = Paginator(products, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'base/shop.html', {'page_obj': page_obj, 'product_type': product_type})



from bson import ObjectId

def book_detail(request, book_id):
    try:
        product = db.product_product.find_one({'_id': ObjectId(book_id), 'category': 'book'})
    except Exception:
        raise Http404("Invalid book ID")

    if not product:
        raise Http404("Book not found")

    book_details = db.product_book.find_one({'product_ptr_id': product['id']})
    if not book_details:
        raise Http404("Book details not found")

    book = {**product, **book_details}

    # Thêm id_str cho MongoDB ObjectId để dùng trong template
    book['id_str'] = str(book['_id'])
    book['price'] = float(book['price'].to_decimal()) 

    return render(request, 'book/book_detail.html', {'book': book})


def clothes_detail(request, clothes_id):
    try:
        product = db.product_product.find_one({'_id': ObjectId(clothes_id), 'category': 'clothes'})
    except Exception:
        raise Http404("Invalid clothes ID")

    if not product:
        raise Http404("Clothes not found")

    clothes_details = db.product_clothes.find_one({'product_ptr_id': product['id']})
    if not clothes_details:
        raise Http404("Clothes details not found")

    clothes = {**product, **clothes_details}

    # Thêm id_str cho MongoDB ObjectId để dùng trong template
    clothes['id_str'] = str(clothes['_id'])
    clothes['price'] = float(clothes['price'].to_decimal())

    return render(request, 'clothes/clothes_detail.html', {'clothes': clothes})


def shoes_detail(request, shoes_id):
    try:
        product = db.product_product.find_one({'_id': ObjectId(shoes_id), 'category': 'shoes'})
    except Exception:
        raise Http404("Invalid shoes ID")

    if not product:
        raise Http404("shoes not found")

    shoes_details = db.product_shoes.find_one({'product_ptr_id': product['id']})
    if not shoes_details:
        raise Http404("Clothes details not found")

    shoes = {**product, **shoes_details}

    # Thêm id_str cho MongoDB ObjectId để dùng trong template
    shoes['id_str'] = str(shoes['_id'])
    shoes['price'] = float(shoes['price'].to_decimal())

    return render(request, 'shoes/shoes_detail.html', {'shoes': shoes})


def electronics_detail(request, electronics_id):
    try:
        product = db.product_product.find_one({'_id': ObjectId(electronics_id), 'category': 'electronics'})
    except Exception:
        raise Http404("Invalid electronics ID")

    if not product:
        raise Http404("electronics not found")

    electronics_details = db.product_electronics.find_one({'product_ptr_id': product['id']})
    if not electronics_details:
        raise Http404("Clothes details not found")

    electronics = {**product, **electronics_details}

    # Thêm id_str cho MongoDB ObjectId để dùng trong template
    electronics['id_str'] = str(electronics['_id'])
    electronics['price'] = float(electronics['price'].to_decimal())

    return render(request, 'electronics/electronics_detail.html', {'electronics': electronics})

