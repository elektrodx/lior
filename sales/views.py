from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from wkhtmltopdf.views import PDFTemplateView, PDFTemplateResponse

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
    template='invoice.html'
    q_sales= Sales.objects.all().last()
    context = { 'pk': q_sales.pk, 'customer': q_sales.customer, 'date': q_sales.date }
    def get(self, request):
        response = PDFTemplateResponse(request=request,
                                       template=self.template,
                                       filename="hello.pdf",
                                       context= self.context,
                                       show_content_in_browser=True,
                                       cmd_options={'margin-top': 5,
                                       'orientation': 'Landscape',
                                       'page-size': 'Letter'},
                                       )
        return response