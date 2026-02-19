from django.shortcuts import render,redirect
from django.http import HttpResponse
import pandas as pd
from .forms import UploadFileForm
from django.db import connection
from .models import Users,MCQ,Courses,True_False,LongQues
from datetime import date,datetime

# Create your views here.
def index(request):
    if request.method == 'GET':
        with connection.cursor() as cursor:
            cursor.execute('Select count(*) from Educational_users;')
            users_no = cursor.fetchone()
            cursor.execute('Select count(*) from Educational_mcq;')
            mcq_nos = cursor.fetchone()
    return render(request,'index.html',{'total_users':users_no,'total_ques':mcq_nos})

def newUser(request):

    id_list = ['user_name','user_email','user_phone','user_location','school','religion','board','personal_pc','personal_phn']
    temp_list = []
    if request.method == 'POST':
        name = request.POST.get('user_name')
        email = request.POST.get('user_email')
        phone = request.POST.get('user_phone')
        location = request.POST.get('user_location')
        school = request.POST.get('school')
        religion = request.POST.get('religion')
        board = request.POST.get('board')
        personal_pc = request.POST.get('personal_pc')
        personal_phn = request.POST.get('personal_phn')

        print(name,email,phone,location,school,religion,board,personal_pc,personal_phn)
        users = Users(name=name,email=email,phone=phone,location=location,school=school,religion=religion,board=board,personal_pc=personal_pc,personal_phn=personal_phn)
        users.save()

    return render(request,'newUser.html')

def new_data(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST,request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            df = pd.read_excel(file)
            # print(file)
            print(df.head())
            df_html = df.to_html(classes='table table-striped',index=False)
            context = {'df_table': df_html}
            return render(request,'table.html',context)
    return render(request,'new_data.html')

def oldUsers(request):
    if request.method == 'POST':
        del_id = request.POST.get('delete_id')
        if del_id:
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM Educational_users WHERE id = %s",[del_id])
                cursor.execute("WITH ordered AS ( SELECT id, ROW_NUMBER() OVER (ORDER BY id) AS rn FROM Educational_users ) UPDATE Educational_users SET id = ( SELECT rn FROM ordered WHERE ordered.id = Educational_users.id );")
                cursor.execute("DELETE FROM sqlite_sequence WHERE name='Educational_users';")
    with connection.cursor() as cursor:
        cursor.execute("SELECT * from Educational_users")
        rows = cursor.fetchall()
    return render(request,'oldUser.html',{'rows':rows})

def newQues(request):
    if request.method == 'POST':
        QType = request.POST.get('Qtype')
        if QType == 'mcq':
            ques = request.POST.get('ques')
            ans1 = request.POST.get('ans1')
            ans2 = request.POST.get('ans2')
            ans3 = request.POST.get('ans3')
            ans4 = request.POST.get('ans4')
            crrctAns = request.POST.get('correct')
            marks = request.POST.get('marks')
            subject = request.POST.get('subject')
            print(ques,ans1,ans2,ans3,ans4,crrctAns,marks)
            MCQ_data = MCQ(ques=ques,ans1=ans1,ans2=ans2,ans3=ans3,ans4=ans4,crrctAns=crrctAns,marks=marks,subject = subject)
            MCQ_data.save()
            print('upload to db successfully!!!')
        if QType == 'true-false':
            ques = request.POST.get('ques')
            crrctAns = request.POST.get('correct')
            marks = request.POST.get('marks')
            subject = request.POST.get('subject')
            True_False_data = True_False(ques=ques,crrctAns=crrctAns,marks=marks,subject = subject)
            True_False_data.save()
            print('upload to db successfully!!!')
        if QType == 'question':
            ques = request.POST.get('ques')
            marks = request.POST.get('marks')
            subject = request.POST.get('subject')
            Long_data = LongQues(ques=ques,marks=marks,subject = subject)
            Long_data.save()
            print('upload to db successfully!!!')
    return render(request,'newQues.html')

def mockTest(request):
    today = date.today()
    today = today.strftime("%d/%m/%Y")
    if request.method == 'POST':
        del_id = request.POST.get('delete_id')
        if del_id:
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM Educational_mcq WHERE id = %s",[del_id])
                cursor.execute("WITH ordered AS ( SELECT id, ROW_NUMBER() OVER (ORDER BY id) AS rn FROM Educational_mcq ) UPDATE Educational_mcq SET id = ( SELECT rn FROM ordered WHERE ordered.id = Educational_mcq.id );")
                cursor.execute("DELETE FROM sqlite_sequence WHERE name='Educational_mcq';")
    with connection.cursor() as cursor:
        cursor.execute("SELECT * from Educational_mcq order by random() limit 20;")
        queses = cursor.fetchall()
        cursor.close()
    with connection.cursor() as cursor:
        cursor.execute("SELECT * from Educational_true_false order by random() limit 5;")
        T_F_queses = cursor.fetchall()
        cursor.close()
    with connection.cursor() as cursor:
        cursor.execute("SELECT * from Educational_longques order by random() limit 1;")
        longques = cursor.fetchall()
        cursor.close()
        
    return render(request,'mockTest.html',{'queses' : queses,'stmts':T_F_queses,'longques':longques,'date':today})

def courses(request):
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM Educational_courses;')
        courses = cursor.fetchall()
        cursor.close()
    return render(request,'courses.html',{'courses':courses})

def new_courses(request):
    if request.method == 'POST':
        course_title = request.POST.get('course_name')
        course_time = request.POST.get('course_time')
        course_price = request.POST.get('course_price')

        courses = Courses(Course_title=course_title,duration=course_time,price=course_price)
        courses.save()
    return render(request,'newCourses.html')

def invoice(request):
    return render(request,'invoice.html')

def sales(request):
    return render(request,'sales.html')


def submit_form(request):
    if request.method == "POST":
        user_name = request.POST.get('user_name', '')
        user_email = request.POST.get('user_email', '')
        user_phone = request.POST.get('user_phone', '')
        item_name = request.POST.get('item_name', '')
        Qty = request.POST.get('Qty', '')
        price = request.POST.get('price', '')
        print(user_name)
        # Prepare data for the template
        context = {
            'name': user_name,
            'email': user_email,
            'phone': user_phone,
            'item_name': item_name,
            'Qty': Qty,
            'price': float(price),
            'time': datetime.now().strftime("%H:%M:%S")
        }
        
        # Return ONLY the small partial file
        return render(request, 'results_partial.html', context)
    # Fallback for non-HTMX requests (optional but good practice)

    return render(request, 'invoice.html')
