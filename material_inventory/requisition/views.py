from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.contrib import messages
from .models import Requisition
from employee.models import Employee
from .forms import RequisitionCreate
from datetime import datetime

# Create your views here.
def index(request):
    requisitions = Requisition.objects.all()
    context = {
        'requisitions': requisitions,
    }
    return render(request, 'requisition/index.html', context)

def add(request):
    newRequisition = RequisitionCreate()
    if request.method == 'POST':
        if request.POST['due_date'] == '':
            context = {
                "newRequisition" : RequisitionCreate(request.POST)
            }
            
            messages.error(request, 'Due Date cannot be empty')
            return render(request, 'requisition/add.html', context)

        try:
            due_date = datetime.strptime(request.POST['due_date'], '%b %d, %Y')
        except:
            due_date = datetime.strptime(request.POST['due_date'], '%B %d, %Y')
        
        modifiedPost = request.POST.copy()
        modifiedPost['due_date'] = due_date

        newRequisition = RequisitionCreate(modifiedPost, request.FILES)
        next = request.POST.get('next', '/')
        if newRequisition.is_valid():
            newRequisition.save()
            messages.success(request, 'Requisition data saved, pending further action.')    
            return HttpResponseRedirect(next)
        else:
            context = {
                "newRequisition" : newRequisition
            }
            
            messages.error(request, 'Invalid form data. Please check form data')
            return render(request, 'requisition/add.html', context)

    context = {
        "newRequisition" : newRequisition
    }
    return render(request, 'requisition/add.html', context)

def show(request, requisition_id):
    requisition = get_object_or_404(Requisition, pk=requisition_id)
    context = {
        'requisition': requisition
    }
    return render(request, 'requisition/show.html', context)

def edit(request, requisition_id):   
    # requisition = get_object_or_404(Requisition, pk=int(requisition_id))
    # messages.error(request, 'Invalid request. Data not found')
    # update_form = RequisitionCreate(request.POST or None, instance = requisition)

    # if update_form.is_valid():
    #    update_form.save()
    #    messages.success(request, 'Requisition data updated')
    #    return redirect('requisitoin/show', {'requisition': requisition})

    # context = {'upload_form':update_form}
    # return render(request, 'requisition/edit.html', context)


    requisition = get_object_or_404(Requisition, pk=int(requisition_id))        
    if request.method == 'POST':
        next = request.POST.get('next', '/')
        
        # Get form values
        if(request.POST['item'] == '' or request.POST['quantity'] == '' or request.POST['unit'] == '' or request.POST['due_date'] == '' or request.POST.get('status') == '' or request.POST.get('originator') == '' or request.POST.get('authorizer') == '' or request.POST.get('approver') == ''):
            print(request.POST)
            messages.error(request, 'Invalid form data. Please check form data. All feilds are compulsory')
            return HttpResponseRedirect(next)
        
        try:
            requisition.item = request.POST['item']
            requisition.quantity = request.POST['quantity']
            requisition.unit = request.POST['unit']
            requisition.description = request.POST['description']
            try:
                requisition.due_date = datetime.strptime(request.POST['due_date'], '%b %d, %Y')
            except:
                requisition.due_date = datetime.strptime(request.POST['due_date'], '%B %d, %Y')
            requisition.status = request.POST.get('status')
            requisition.originator = Employee.objects.get(id =  int(request.POST.get('originator')))
            requisition.authorizer = Employee.objects.get(id =  int(request.POST.get('authorizer')))
            requisition.approver = Employee.objects.get(id =  int(request.POST.get('approver')))
            
        except:
            print(requisition)
            messages.error(request, 'Invalid form data. Please check form data')
            return HttpResponseRedirect(next)
        if requisition:
            try:
                requisition.save()
                messages.success(request, 'Requisition updated')   
                return HttpResponseRedirect(next)
            except:
                messages.error(request, 'Invalid form data. Please check form data')   
                return HttpResponseRedirect(next)
    else:
        status = Requisition._meta.get_field('status').choices
        employee = Employee.objects.all()
        request_status = dict(status)
        context = {
            'requisition': requisition,
            'status': request_status,
            'employee': employee,
        }
        return render(request, 'requisition/edit.html', context)

def delete(request, requisition_id):
    next = request.POST.get('next', '/')    
    requisition_id = int(requisition_id)
    try:
        requisition = Requisition.objects.get(id = requisition_id)
    except requisition.DoesNotExist:
        messages.error(request, 'Invalid requisition data')   
        return HttpResponseRedirect(next)

    if requisition.delete():
        requisitions = Requisition.objects.all()
        context = {
            'requisitions': requisitions,
        }
        messages.success(request, 'Requisition data deleted')   
        return render(request, 'requisition/index.html', context)
    else:
        messages.error(request, 'Unable to delete this request')   
        return HttpResponseRedirect(next)