from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

def item_list(request):
    return HttpResponse('Balle Balle')
    # items = Item.objects.all()
    # return render(request, 'item_list.html', {'items': items})

# def item_detail(request, pk):
#     item = get_object_or_404(Item, pk=pk)
#     return render(request, 'item_detail.html', {'item': item})

# def item_create(request):
#     if request.method == "POST":
#         form = ItemForm(request.POST)
#         if form.is_valid():
#             item = form.save()
#             return redirect('item_detail', pk=item.pk)
#     else:
#         form = ItemForm()
#     return render(request, 'item_form.html', {'form': form})

# def item_update(request, pk):
#     item = get_object_or_404(Item, pk=pk)
#     if request.method == "POST":
#         form = ItemForm(request.POST, instance=item)
#         if form.is_valid():
#             item = form.save()
#             return redirect('item_detail', pk=item.pk)
#     else:
#         form = ItemForm(instance=item)
#     return render(request, 'item_form.html', {'form': form})

# def item_delete(request, pk):
#     item = get_object_or_404(Item, pk=pk)
#     if request.method == "POST":
#         item.delete()
#         return redirect('item_list')
#     return render(request, 'item_confirm_delete.html', {'item': item})
