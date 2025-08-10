from django.shortcuts import render
from django.core.mail import EmailMultiAlternatives, send_mail
from django.conf import settings
from .models import Event
from .forms import ContactForm

def home(request):
    return render(request, 'home.html')

def notes(request):
    return render(request, 'notes.html')

def syllabus(request):
    return render(request, 'syllabus.html')

def carrerplace(request):
    return render(request, 'carrerplace.html')

def events(request):
    events = Event.objects.all()
    if not events:
        events = None
    return render(request, 'events.html', {'events': events})

def syllabus(request):
    return render(request, 'syllabus.html')

def about(request):
    return render(request, 'dummy.html')

def contact(request):
    success = False
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid(): # Save to DB
            contact = form.save()
            # Prepare email details
            name = contact.name
            email = contact.email
            roll = contact.roll_number
            msg = contact.message
           
            # Send email to admin
            send_mail(
                subject=f"New Contact Form Submission - Roll: {roll}",
                message=(
                    f"Name: {name}\n"
                    f"Email: {email}\n"
                    f"Roll Number: {roll}\n\n"
                    f"Message:\n{msg}"
                ),
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=['aceeeeweb@gmail.com'], 
                fail_silently=False,
            )

            # Prepare HTML auto-reply for user
            subject = "Thank you for contacting us!"
            from_email = settings.EMAIL_HOST_USER
            to = [contact.email]

            text_content = (
                f"Hello {contact.name},\n\n"
                "Thank you for reaching out to us. We have received your message "
                "and will get back to you shortly.\n\n"
                "Best regards,\nEEE Students Hub Team"
            )

            html_content = f"""
            <html>
            <body style="font-family: Arial, sans-serif; background-color: #f8f9fa; padding: 20px;">
                <div style="max-width: 600px; margin: auto; background: white; padding: 20px; border-radius: 8px; border: 1px solid #ddd;">
                    <h2 style="color: #0d6efd;">Thank you for contacting us!</h2>
                    <p>Hello <strong>{contact.name}</strong>,</p>
                    <p>We have received your message and our team will respond to you shortly.</p>
                    <hr>
                    <p style="font-size: 14px; color: #6c757d;">
                        Best regards,<br>
                        <strong>Your Website Team</strong>
                    </p>
                </div>
            </body>
            </html>
            """

            msg = EmailMultiAlternatives(subject, text_content, from_email, to)
            msg.attach_alternative(html_content, "text/html")
            msg.send()

            success = True
            form = ContactForm()  # Clear form
    else:
        form = ContactForm()

    return render(request, 'contact.html', {"form": form, "success": success})


