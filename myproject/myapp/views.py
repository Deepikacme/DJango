from django. http import HttpResponse

from myapp.models import Student

# Create your views here.
def index(request):
    students = Student.objects.all()
    return HttpResponse(students)