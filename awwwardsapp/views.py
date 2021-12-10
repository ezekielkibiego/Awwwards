from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
import cloudinary
import cloudinary.uploader
import cloudinary.api


from awwwardsapp.models import Profile


def index(request):
  
    return render(request, 'index.html')


@login_required(login_url="/accounts/login/")
def profile(request):
    current_user = request.user
    profile = Profile.objects.filter(user_id=current_user.id).first()
    project = Project.objects.filter(user_id=current_user.id).all() 
    return render(request, "profile.html", {"profile": profile, "images": project})


@login_required(login_url="/accounts/login/")
def update_profile(request):
    if request.method == "POST":

        current_user = request.user

        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]

        bio = request.POST["bio"]
        contact = request.POST["contact"]

        profile_image = request.FILES["profile_pic"]
        profile_image = cloudinary.uploader.upload(profile_image)
        profile_url = profile_image["url"]

        user = User.objects.get(id=current_user.id)

        
        if Profile.objects.filter(user_id=current_user.id).exists():

            profile = Profile.objects.get(user_id=current_user.id)
            profile.profile_photo = profile_url
            profile.bio = bio
            profile.contact = contact
            profile.save()
        else:
            profile = Profile(
                user_id=current_user.id,
                profile_photo=profile_url,
                bio=bio,
                contact=contact,
            )
            profile.save_profile()

        user.first_name = first_name
        user.last_name = last_name
        user.username = username
        user.email = email

        user.save()

        return redirect("/profile", {"success": "Profile Updated Successfully"})
    else:
        return render(request, "profile.html", {"danger": "Profile Update Failed"})

@login_required(login_url="/accounts/login/")
def save_project(request):
    if request.method == "POST":

        current_user = request.user

        title = request.POST["title"]
        location = request.POST["location"]
        description = request.POST["description"]
        url = request.POST["url"]
        image = request.FILES["image"]
        image = cloudinary.uploader.upload(image, crop="limit", width=500, height=500)
        image_url = image["url"]

        project = Project(
            user_id=current_user.id,
            title=title,
            location=location,
            description=description,
            url=url,
            image=image_url,
        )
        project.save_project()

        return redirect("/profile", {"success": "Project Saved Successfully"})
    else:
        return render(request, "profile.html", {"danger": "Project Save Failed"})

@login_required(login_url="/accounts/login/")
def delete_project(request, id):
    project = Project.objects.get(id=id)
    project.delete_project()
    return redirect("/profile", {"success": "Deleted Project Successfully"})


