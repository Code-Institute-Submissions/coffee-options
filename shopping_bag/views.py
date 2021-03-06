from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages

"""
Code adapted from from CI's Boutique Ado project,
Shopping Bag section
"""


def view_shopping_bag(request):
    """ A view that renders the bag contents page """
    return render(request, 'shopping_bag/shopping_bag.html')


def add_to_shopping_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    shopping_bag = request.session.get('shopping_bag', {})
    if item_id in list(shopping_bag.keys()):
        shopping_bag[item_id] += quantity
    else:
        shopping_bag[item_id] = quantity
        messages.success(request, 'Successfully added to your bag!')

    request.session['shopping_bag'] = shopping_bag
    return redirect(redirect_url)


def remove_from_shopping_bag(request, item_id):
    """Remove the item from the shopping bag"""
    shopping_bag = request.session.get('shopping_bag', {})
    shopping_bag.pop(item_id)

    request.session['shopping_bag'] = shopping_bag
    return HttpResponse(status=200)
