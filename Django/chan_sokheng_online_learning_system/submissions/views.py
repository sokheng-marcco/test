from django.shortcuts import render, redirect
from submissions.models import Submission
from submissions.forms import SubmissionForm

def submission_list(request):
    submissions = Submission.objects.all()
    return render(request, 'submissions/submission_list.html', {'submissions': submissions})

def submission_create(request):
    form = SubmissionForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('submission_list')
    return render(request, 'submissions/submission_form.html', {'form': form})

def submission_update(request, pk): 
    submission = Submission.objects.filter(pk=pk).first()
    form = SubmissionForm(request.POST or None, request.FILES or None, instance=submission)
    if form.is_valid():
        form.save()
        return redirect('submission_list')
    return render(request, 'submissions/submission_form.html', {'form': form})

def submission_delete(request, pk):
    submission = Submission.objects.filter(pk=pk).first()
    if request.method == 'POST':
        submission.delete()
        return redirect('submission_list')
    return render(request, 'submissions/submission_delete.html', {'submission': submission})