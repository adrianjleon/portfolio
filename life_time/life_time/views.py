from django.shortcuts import render

def home(request):
    name_contact = request.GET['name_contact']
    email_contact = request.GET['email_contact']
    subject_contact = request.GET['subject_contact']
    text_contact = request.GET['text_contact']

    return render(request, 'index.html', {'name_contact': name_contact,
                                            'email_contact': email_contact,
                                            'subject_contact' : subject_contact,
                                            'text_contact': text_contact})


def contact(request):
    return render(request, 'contact.html')
