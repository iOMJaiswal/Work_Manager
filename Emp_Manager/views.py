from django.shortcuts import render, HttpResponse
from .models import Employees


def index(request):
    return render(request, 'index.html')


def list_emp(request):

    # Generating context and posting it to html
    emps = Employees.objects.all()
    context = {
        'emps': emps
    }
    return render(request, 'list_emp.html', context)


def add_emp(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        dept = request.POST['dept']
        role = request.POST['role']
        phone = int(request.POST['phone'])
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])

        # new_emp is object of Employee and saving it into database
        new_emp = Employees(first_name=first_name, last_name=last_name,
                            department=dept, role=role, phone=phone, salary=salary, bonus=bonus)
        new_emp.save()

        return list_emp(request)

    elif request.method == "GET":
        return render(request, 'add_emp.html')

    else:
        return HttpResponse("Unexpected Error Occured!!! Please Try again")


def remove_emp(request):
    # Implementing remove query from database
    if request.method == 'POST':
        emp_id_to_remove = request.POST['emp']
        emp = Employees(id=emp_id_to_remove)
        emp.delete()

        # Update and return new list
        return list_emp(request)

    elif request.method == 'GET':
        emps = Employees.objects.all()
        context = {
            'emps': emps
        }
        return render(request, 'remove_emp.html', context)

    else:
        return HttpResponse("Unexpected Error Occured!!! Please Try again")


def fetch_emp(request):
    # Here Details of employees are fetching according to match with fname, lname, role, dept
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        dept = request.POST['dept']
        role = request.POST['role']

        emps = Employees.objects.all()

        if first_name:
            emps = emps.filter(first_name=first_name)

        if last_name:
            emps = emps.filter(last_name=last_name)

        if dept and dept != "Select Department":
            emps = emps.filter(department=dept)

        if role and role != "Select Role":
            emps = emps.filter(role=role)

        # Overrighted file getting as context
        context = {
            'emps': emps
        }

        return render(request, 'list_emp.html', context)

    elif request.method == 'GET':
        return render(request, 'fetch_emp.html')

    else:
        return HttpResponse("Unexpected Error Occured!!! Please Try again")


def select_update_emp(request):

    # Creating logic for updating employee
    if request.method == 'POST':
        emp_id_to_update = request.POST['emp']

        emps = Employees.objects.all()

        if emp_id_to_update:
            emps = emps.filter(id=emp_id_to_update)

        context = {
            'emps': emps
        }

        # Update and return new list
        return render(request, 'update_emp.html', context)

    elif request.method == 'GET':
        emps = Employees.objects.all()
        context = {
            'emps': emps
        }
        return render(request, 'select_update_emp.html', context)

    else:
        return HttpResponse("Unexpected Error Occured!!! Please Try again")


# Just to update an employee called by select_update_emp
def update_emp(request, id):

    # Creating logic for updating employee
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        dept = request.POST['dept']
        role = request.POST['role']
        phone = int(request.POST['phone'])
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])

        # new_emp is object of Employee and saving it into database
        up_emp = Employees(id=id, first_name=first_name, last_name=last_name,
                           department=dept, role=role, phone=phone, salary=salary, bonus=bonus)
        up_emp.save()

        # Update and return new list
        return list_emp(request)

    elif request.method == 'GET':
        emps = Employees.objects.all()
        context = {
            'emps': emps
        }
        return render(request, 'select_update_emp.html', context)

    else:
        return HttpResponse("Unexpected Error Occured!!! Please Try again")
