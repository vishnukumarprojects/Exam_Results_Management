from django.shortcuts import render

from . models import *
# Create your views here.


def index(request):
    return render(request,'index.html')

def eleventh_dash(request):
    return render(request,'eleventh_dash.html')

def admin_side(request):
    if request.method=="POST":
        reg_no=request.POST.get('reg_no')
        internal1=request.POST.get('internal1')
        internal2=request.POST.get('internal2')
        internal3=request.POST.get('internal3')
        internal4=request.POST.get('internal4')
        internal5=request.POST.get('internal5')
        ex1=tenth_internal_table(reg_no=reg_no,internal1=internal1,internal2=internal2,internal3=internal3,internal4=internal4,internal5=internal5)
        ex1.save()
    if request.method=="POST":
        verify=request.POST.get('verify')
        print("verify")
    # if verify==tenth_name_regno_table(reg_no):
    #     print("ok")    
    
    return render(request,'admin_side.html')

def tenth_dash(request):
    return render(request,'tenth_dash.html')

def twelveth_dash(request):
    if request.method=="POST":
        reg_no=request.POST.get('reg_no')
        subject_data=twelveth_subjects_table.objects.get(reg_no=reg_no)
        internal_data=twelveth_internal_table.objects.get(reg_no=reg_no)
        practical_data=twelveth_practical_table.objects.get(reg_no=reg_no)
        theory_data=twelveth_theory_table.objects.get(reg_no=reg_no)
        student_data=twelveth_name_regno_table.objects.get(reg_no=reg_no)
        student_name=student_data.names
        regno=twelveth_name_regno_table.objects.get(reg_no=reg_no)
        total_mark_sub1=int(internal_data.internal1) + int(theory_data.theory1)
        total_mark_sub2=int(internal_data.internal2) + int(theory_data.theory2)
        total_mark_sub3=int(internal_data.internal3) + int(theory_data.theory3) 
        total_mark_sub4=int(internal_data.internal4) + int(theory_data.theory4) + int(practical_data.practical1)
        total_mark_sub5=int(internal_data.internal5) + int(theory_data.theory5) + int(practical_data.practical2)
        total_mark_sub6=int(internal_data.internal6) + int(theory_data.theory6) + int(practical_data.practical3)
        grand_total=total_mark_sub1 + total_mark_sub2 + total_mark_sub3 + total_mark_sub4 + total_mark_sub5 + total_mark_sub6
        if total_mark_sub1 >=35:
            sub1p="P"
        else:
            sub1p="F"
        if total_mark_sub2 >=35:
            sub2p="P"
        else:
            sub2p="F"
        if total_mark_sub3 >=35:
            sub3p="P"
        else:
            sub3p="F"

        if total_mark_sub4 >=35:
            sub4p="P"
        else:
            sub4p="F"
        if total_mark_sub5 >=35:
            sub5p="P"
        else:
            sub5p="F"
        if total_mark_sub6 >=35:
            sub6p="P"
        else:
            sub6p="F"
        
        if sub1p=="P" and sub2p=="P" and sub3p=="P" and sub4p=="P" and sub5p=="P" and sub6p=="P":
            pass_fail="PASS"
        else:
            pass_fail="FAIL"
        
        

        return render(request,'twelveth_result.html',{
            'subject_data':subject_data,
            'internal_data':internal_data,
            'practical_data':practical_data,
            'theory_data':theory_data,
            'total_mark_sub1':total_mark_sub1,
            'total_mark_sub2':total_mark_sub2,
            'total_mark_sub3':total_mark_sub3,
            'total_mark_sub4':total_mark_sub4,
            'total_mark_sub5':total_mark_sub5,
            'total_mark_sub6':total_mark_sub6,
            'grand_total':grand_total,
            'sub1p':sub1p,
            'sub2p':sub2p,
            'sub3p':sub3p,
            'sub4p':sub4p,
            'sub5p':sub5p,
            'sub6p':sub6p,
            'pass_fail':pass_fail,
            'student_name':student_name,
            'reg_no':reg_no,
        
            
            })
    
    return render(request,'twelveth_dash.html')

def eleventh_result(request):
    if request.method=="POST":
        reg_no=request.POST.get('reg_no')
        subject_data=eleventh_subjects_table.objects.get(reg_no=reg_no)
        internal_data=eleventh_internal_table.objects.get(reg_no=reg_no)
        practical_data=eleventh_practical_table.objects.get(reg_no=reg_no)
        theory_data=eleventh_theory_table.objects.get(reg_no=reg_no)
        student_data=eleventh_name_regno_table.objects.get(reg_no=reg_no)
        student_name=student_data.names
        regno=eleventh_name_regno_table.objects.get(reg_no=reg_no)
        total_mark_sub1=int(internal_data.internal1) + int(theory_data.theory1)
        total_mark_sub2=int(internal_data.internal2) + int(theory_data.theory2)
        total_mark_sub3=int(internal_data.internal3) + int(theory_data.theory3) 
        total_mark_sub4=int(internal_data.internal4) + int(theory_data.theory4) + int(practical_data.practical1)
        total_mark_sub5=int(internal_data.internal5) + int(theory_data.theory5) + int(practical_data.practical2)
        total_mark_sub6=int(internal_data.internal6) + int(theory_data.theory6) + int(practical_data.practical3)
        grand_total=total_mark_sub1 + total_mark_sub2 + total_mark_sub3 + total_mark_sub4 + total_mark_sub5 + total_mark_sub6
        if total_mark_sub1 >=35:
            sub1p="P"
        else:
            sub1p="F"
        if total_mark_sub2 >=35:
            sub2p="P"
        else:
            sub2p="F"
        if total_mark_sub3 >=35:
            sub3p="P"
        else:
            sub3p="F"

        if total_mark_sub4 >=35:
            sub4p="P"
        else:
            sub4p="F"
        if total_mark_sub5 >=35:
            sub5p="P"
        else:
            sub5p="F"
        if total_mark_sub6 >=35:
            sub6p="P"
        else:
            sub6p="F"
        
        if sub1p=="P" and sub2p=="P" and sub3p=="P" and sub4p=="P" and sub5p=="P" and sub6p=="P":
            pass_fail="PASS"
        else:
            pass_fail="FAIL"
        
        

        return render(request,'eleventh_result.html',{
            'subject_data':subject_data,
            'internal_data':internal_data,
            'practical_data':practical_data,
            'theory_data':theory_data,
            'total_mark_sub1':total_mark_sub1,
            'total_mark_sub2':total_mark_sub2,
            'total_mark_sub3':total_mark_sub3,
            'total_mark_sub4':total_mark_sub4,
            'total_mark_sub5':total_mark_sub5,
            'total_mark_sub6':total_mark_sub6,
            'grand_total':grand_total,
            'sub1p':sub1p,
            'sub2p':sub2p,
            'sub3p':sub3p,
            'sub4p':sub4p,
            'sub5p':sub5p,
            'sub6p':sub6p,
            'pass_fail':pass_fail,
            'student_name':student_name,
            'reg_no':reg_no,
        
            
            })
    
    return render(request,'eleventh_dash.html')

def tenth_result(request):
    if request.method=="POST":
        reg_no=request.POST.get('reg_no')
        subject_data=tenth_subjects_table.objects.get(reg_no=reg_no)
        internal_data=tenth_internal_table.objects.get(reg_no=reg_no)
        practical_data=tenth_practical_table.objects.get(reg_no=reg_no)
        theory_data=tenth_theory_table.objects.get(reg_no=reg_no)
        student_data=tenth_name_regno_table.objects.get(reg_no=reg_no)
        student_name=student_data.names
        regno=tenth_name_regno_table.objects.get(reg_no=reg_no)
        total_mark_sub1=int(internal_data.internal1) + int(theory_data.theory1)
        total_mark_sub2=int(internal_data.internal2) + int(theory_data.theory2)
        total_mark_sub3=int(internal_data.internal3) + int(theory_data.theory3) 
        total_mark_sub4=int(internal_data.internal4) + int(theory_data.theory4) + int(practical_data.practical1)
        total_mark_sub5=int(internal_data.internal5) + int(theory_data.theory5)
        grand_total=total_mark_sub1 + total_mark_sub2 + total_mark_sub3 + total_mark_sub4 + total_mark_sub5
        if total_mark_sub1 >=35:
            sub1p="P"
        else:
            sub1p="F"
        if total_mark_sub2 >=35:
            sub2p="P"
        else:
            sub2p="F"
        if total_mark_sub3 >=35:
            sub3p="P"
        else:
            sub3p="F"

        if total_mark_sub4 >=35:
            sub4p="P"
        else:
            sub4p="F"
        if total_mark_sub5 >=35:
            sub5p="P"
        else:
            sub5p="F"
        
        if sub1p=="P" and sub2p=="P" and sub3p=="P" and sub4p=="P" and sub5p=="P":
            pass_fail="PASS"
        else:
            pass_fail="FAIL"
        
        

        return render(request,'tenth_result.html',{
            'subject_data':subject_data,
            'internal_data':internal_data,
            'practical_data':practical_data,
            'theory_data':theory_data,
            'total_mark_sub1':total_mark_sub1,
            'total_mark_sub2':total_mark_sub2,
            'total_mark_sub3':total_mark_sub3,
            'total_mark_sub4':total_mark_sub4,
            'total_mark_sub5':total_mark_sub5,
            'grand_total':grand_total,
            'sub1p':sub1p,
            'sub2p':sub2p,
            'sub3p':sub3p,
            'sub4p':sub4p,
            'sub5p':sub5p,
            'pass_fail':pass_fail,
            'student_name':student_name,
            'reg_no':reg_no,
        
            
            })
    
    return render(request,'tenth_dash.html')

def twelveth_result(request):
    return render(request,'twelveth_result.html')
