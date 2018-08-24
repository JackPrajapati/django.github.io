from django.shortcuts import render
from cart.models import CartModel

import pdb


def mycart(request):
    pdb.set_trace()
    cart_obj = CartModel.objects.new_or_create(request)
    products = cart_obj.products.all()
    return render(request, "cart/cart.html", {})
# cart_id = request.session.get("cart_id", None)
# qs = CartModel.objects.filter(id=cart_id)
# if qs.count() == 1:
#     cart_obj = qs.first()
#     print("cart exist")
#     if request.user.is_authenticated() and cart_obj.user is None:
#         cart_obj.user = request.user
#         cart_obj.save()
# else:
#     cart_obj = CartModel.objects.new(user=request.user)
#     request.session['cart_id'] = cart_obj.id
#     print("cart created")
