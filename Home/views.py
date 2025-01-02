from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponse, render
from django.urls import reverse

from gallery.models import gallery_image
from payments import models as pay
from users.models import User

from .models import *
from .utils import Generate_id_card


# Create your views here.
def Home(request):
    anounce = announcement.objects.all()
    nav_link = Navigation_link.objects.all()
    nav_link2 = Navigation_link2.objects.all()
    team_members = Team_member.objects.all()[:5]
    socialMedia_and_HelpLine = SocialMedia_and_HelpLine.objects.first()
    last_gallery_images = gallery_image.objects.all()

    data = footer_and_home_page_data.objects.first()
    context = {
        "announcement": anounce,
        "Navigation_link": nav_link,
        "Navigation_link2": nav_link2,
        "Team_members": team_members,
        "SocialMedia_and_HelpLine": socialMedia_and_HelpLine,
        "carousel_images": last_gallery_images,
        "data": data,
    }
    return render(request=request, template_name="index.html", context=context)


def team_members(request):
    nav_link = Navigation_link.objects.all()
    context = {"Navigation_link": nav_link, "team_members": Team_member.objects.all()}
    return render(request, "team_members.html", context=context)


@login_required(login_url="/login/")
def id_card_page(request):
    if request.POST:
        if pay.payment.objects.filter(user=request.user).exists() == False:
            return redirect("create_order/order2")
        elif (
            int(pay.payment.objects.filter(user=request.user).first().amount)
            >= int(pay.full_premium.objects.first().cost_of_id_and_volunteer)
        ) == False:
            return redirect("create_order/order2")
        else:
            id = request.user.id
            user = User.objects.get(pk=id)
            relative_url = reverse("profile", kwargs={"username": str(user.username)})
            URL = str(request.build_absolute_uri(relative_url))
            FULL_NAME = str(user.first_name) + " " + str(user.last_name)
            STATUS = str(user.status)
            DATE = str(user.date_joined).split()[0]
            PIC = user.profile_picture
            buffer = Generate_id_card(URL, FULL_NAME, STATUS, DATE, PIC)

            response = HttpResponse(buffer, content_type="image/png")
            response["Content-Disposition"] = 'attachment; filename="{}.png"'.format(
                str(user.username)
            )
            return response

    if request.user:
        if pay.payment.objects.filter(user=request.user).exists() == False:
            return redirect("create_order/order2")
        elif (
            int(pay.payment.objects.filter(user=request.user).first().amount)
            >= int(pay.full_premium.objects.first().cost_of_id_and_volunteer)
        ) == False:
            return redirect("create_order/order2")
        else:
            user = User.objects.get(pk=request.user.id)
            if str(user.profile_picture) == "https://drive.google.com/thumbnail?id=1eS5nP8cMj8eJ-Nq_PHTgLa7rJkj5UCPh&sz=s4000":
                messages.error(request, "PLEASE UPDATE YOUR PROFILE PICTURE")
                return redirect(reverse("update_profile"))
            else:
                return render(
                    request,
                    "id_card.html",
                    context={
                        "Navigation_link": Navigation_link.objects.all(),
                        "SocialMedia_and_HelpLine": SocialMedia_and_HelpLine.objects.all(),
                    },
                )


from forms.models import Volunteer_form


def volunters(request):
    approved_volunteers = Volunteer_form.objects.filter(status="Approved")
    nav_link = Navigation_link.objects.all()
    context = {"volunteers": approved_volunteers, "Navigation_link": nav_link}
    return render(request, "volunters.html", context=context)


@login_required(login_url="/login/")
def joining_page(request):

    if pay.payment.objects.filter(user=request.user).exists() == False:
        return redirect("create_order/order2")
    elif (
        int(pay.payment.objects.filter(user=request.user).first().amount)
        >= int(pay.full_premium.objects.first().cost_of_id_and_volunteer)
    ) == False:
        return redirect("create_order/order2")
    else:
        from datetime import date
        from io import BytesIO

        from reportlab.lib.pagesizes import A4
        from reportlab.pdfgen import canvas

        id = request.user.id
        user = User.objects.get(pk=id)
        buffer = BytesIO()
        # Create a canvas for the PDF
        p = canvas.Canvas(buffer, pagesize=A4)
        width, height = A4

        # Add some content to the PDF
        p.setFont("Helvetica-Bold", 14)
        p.drawString(100, height - 100, "Emerging India Foundation")
        p.setFont("Helvetica", 12)
        p.drawString(100, height - 140, f"Date: {user.date_joined}")
        full_name = user.first_name + " " + user.last_name
        p.drawString(100, height - 180, f"Dear {full_name}(id: {user.user_id}),")

        p.drawString(
            100,
            height - 220,
            "Congratulations! We are pleased to offer you the position of Volunteer",
        )
        p.drawString(100, height - 240, "with the Emerging India Foundation.")

        p.drawString(
            100,
            height - 280,
            "We are excited to have you on board and look forward to your contribution.",
        )
        p.drawString(
            100, height - 300, "Thank you for your interest in supporting our cause."
        )

        p.drawString(100, height - 340, "Sincerely,")
        p.drawString(100, height - 360, "Emerging India Foundation")

        # Save the PDF to the buffer
        p.showPage()
        p.save()

        # Get the PDF value from the buffer
        buffer.seek(0)

        # Create the HttpResponse to return the PDF
        response = HttpResponse(buffer, content_type="application/pdf")
        response["Content-Disposition"] = (
            f'attachment; filename="Joining_Letter_{full_name}.pdf"'
        )

        return response

