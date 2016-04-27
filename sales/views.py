from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import *
from django.contrib.auth.decorators import login_required
from wkhtmltopdf.views import PDFTemplateView

@login_required(login_url="/singin")
def add_sale(request):
	if request.method == "POST":
		form = SalesForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/')
	else:
		form = SalesForm()
	return render(request, 'add_sale.html', {'form': form })



class Invoice(PDFTemplateView):
    filename = 'my_pdf.pdf'
    template_name = 'invoice.html'
    cmd_options = {
        'margin-top': 3,
        'orientation': 'Landscape',
    }