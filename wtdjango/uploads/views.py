from django.shortcuts import render
from .models import Document
from .forms import DocumentForm
from django.shortcuts import redirect
from django.views.generic.list import ListView

# Create your views here.
def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('uploads')
    else:
        form = DocumentForm()
    return render(request, 'uploads/model_form_upload.html', {'form': form})

class DocumentListView(ListView):
    model = Document
    
