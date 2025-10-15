from django.shortcuts import render,redirect
from .models import Tag
from .forms import TagForm

def tag_list(request):
    tags = Tag.objects.all()
    return render(request, 'tags/tag_list.html', {'tags': tags})

def tag_create(request):
    form = TagForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('tag_list')
    return render(request, 'tags/tag_form.html', {'form': form})

def tag_update(request, pk):
    tag = Tag.objects.filter(pk=pk).first()
    form = TagForm(request.POST or None, instance=tag)
    if form.is_valid():
        form.save()
        return redirect('tag_list')
    return render(request, 'tags/tag_form.html', {'form': form})

def tag_delete(request, pk):
    tag = Tag.objects.filter(pk=pk).first()
    if request.method == 'POST':
        tag.delete()
        return redirect('tag_list')
    return render(request, 'tags/tag_delete.html', {'tag': tag})
