from django.http import HttpResponse,JsonResponse
from . models import Employee,Department

# Create your views here.
def handleEmp(request):
    if request.method=='GET':
        manager = Employee.objects.values()

        return JsonResponse({'employees':list(manager)})
    


    if request.method == 'POST':
        id = request.POST.get('id')
        name = request.POST.get('name')
        salary = request.POST.get('salary')
        address = request.POST.get('address')


        if name is None or salary is None or address is None:
            return JsonResponse({
                'message':'name, salary or address is required'
            })
        
        employee=Employee()
        employee.name=name
        employee.salary=salary
        employee.address=address
        employee.save()


        return JsonResponse({
            'message':'successful'
        })
    

    if request.method=='DELETE':
        id=request.GET.get('id')


        if id is None:
            return JsonResponse({
                'message':'ID is required to delete'
            })
        
        employee = Employee.objects.filter(id=id).first()
        
        if employee is not None:
            employee.delete()

            return JsonResponse({
                'message':'your record is deleted'
            })
        
        return JsonResponse ({
            'message':'Does not exist'
        })


def handleEmpRelationship(request):
    if request.method == 'POST':
        id=request.POST.get('id')
        name=request.POST.get('name')
        salary = request.POST.get('salary')
        address = request.POST.get('address')

        if name is not None or salary is not None or address is not None:

            if id is not None:
                employee=Employee.objects.filter(id=id).first()
                if employee is None:
                    return JsonResponse({
                        'message':'Employee does not exist with id'
                    })
                
                employee.name=name
                employee.salary=salary
                employee.address=address
                employee.save()

                return JsonResponse({
                    'message':'edited successful!!!'

                })

                

            employee = Employee()
            employee.name=name
            employee.salary=salary
            employee.address=address
            employee.save()


            return JsonResponse({
                'message':'Created successful!!!'
            })
        
        return JsonResponse({
            'message':'name, salary, address are required'
        })


    
def handleDept(request):
    if request.method=='GET':
        manager=Department.objects.values()
        return JsonResponse({'departments':list(manager)})
    


    if request.method=='POST':
        id = request.POST.get('id')
        lead = request.POST.get('lead')
        name = request.POST.get('name')
        active = request.POST.get('active')


        if lead is not None or name is not None or active is not None:

            if id:
                department=Department.objects.filter(id=id).first()

                if department is None:
                    return JsonResponse({
                        'message':'department does not exists!!'
                    })  
                
                department.lead=lead
                department.name=name
                department.active=active
                department.save()

                return JsonResponse({
                    'message':'edited successful!!'
                })
            
            employee = Employee.objects.filter(id=lead).first()

            department = Department()
            department.lead=employee
            department.name=name
            department.active=bool(active)
            department.save()



            return JsonResponse({
                'message':'record saved successful!!'
            })

                 




    


