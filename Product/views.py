from django.contrib import messages
from django.shortcuts import render, HttpResponseRedirect
from Product.models import Comment, CommentForm


def comment_add(request, id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        pos = CommentForm(request.POST)
        if pos.is_valid():
            data = Comment()
            data.subject = pos.cleaned_data['subject']
            data.comment = pos.cleaned_data['comment']
            data.rate = pos.cleaned_data['rate']
            data.ip = request.META.get('REMOTE_ADDR')
            data.product_id = id
            current_user = request.user
            data.user_id = current_user.id
            data.save()
            messages.success(request, 'Your comment has been sent!')
            return HttpResponseRedirect(url)
    return HttpResponseRedirect(url)
