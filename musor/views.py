# update user profile
@login_required
def update_user(request):
    form = ProfileForm()
    form2 = UserProfileForm()
    print(request.user.id, request.user)
    print(request)
    if request.method == 'POST':
        print('method is post')
        # request.POST = request.POST.copy()
        # request.POST['user'] = request.user.id
        print()
        print(request)
        print()
        form = ProfileForm(request.POST)
        formUser = User.objects.get(username=request.user.username)[0]
        print(formUser)
        form2 = UserProfileForm({'username': request.user.username})
        # form.errors['user'] = form['user'].errors_class()
        # form.errors.pop('user')
        if form.is_valid() and form2.is_valid():
            form.user = form2.username
            form.save()
            return redirect('home')
        else:
            print(request.POST)
            print(form.is_valid())
            print('error data not valid')
            return render(request, 'emarket/profile.html', {'form': form, 'form2': form2, })
    else:
        return render(request, 'emarket/profile.html', {'form': form, 'form2': form2, })

def profile(request):
    form = ProfileForm
    print(request.user.id)
    if request.method == 'POST':
        form = ProfileForm(data=request.POST)
        if form.is_valid():
            old_user = Profile.objects.filter(id=request.user.id)
            if old_user:
                print(old_user)
                old_user.delete()
            profile_user = Profile()
            profile_user.user = request.user
            profile_user.bio = request.POST['bio']
            profile_user.location = request.POST['location']
            profile_user.birth_date = request.POST['birth_date']
            profile_user.save()
            # user_profile = form.save(commit=False)
            # user_profile.user = request.user
            # Profile.objects.filter(id=request.user.id).delete()
            # user_profile.save()
            return redirect('home')
        else:
            print("form not valid", form.errors)
    else:
        return render(request, 'emarket/profile.html', {'form': form})

@login_required
def profile(request):
    form = ProfileForm
    print(request.user.id)
    if request.method == 'POST':
        form = ProfileForm(data=request.POST)
        if form.is_valid():
            Profile.objects.filter(id=request.user.id).delete()
            user_profile = form.save(commit=False)
            # user_profile.user = User.objects.filter(username=request.user.username)
            user_profile.user = request.user
            user_profile.save()
            return redirect('home')
        else:
            print("form not valid", form.errors)
    else:
        return render(request, 'emarket/profile.html', {'form': form})




@login_required
def add_item_img(request, it_id):
    if request.method == 'POST':
        item_img = Item_Image(item_id=it_id)
        form = Item_ImageForm(request.POST, request.FILES, instance=item_img)
        if form.is_valid():
            form.save()
            return redirect('show_item', it_id)
    else:
        form = Item_ImageForm()
        return render(request, 'emarket/item_add_image.html', {'form':form, })



@login_required
def add_item_img(request, it_id):
    if request.method == 'POST':
        item_img = Item_Image(item_id=it_id)
        form = Item_ImageForm(request.POST, request.FILES, instance=item_img)
        if form.is_valid():
            photo = form.save()
            data = {'is_valid': True, 'name': photo.file.name, 'url': photo.file.url}
        else:
            data = {'is_valid': False}
        return JsonResponse(data)
    else:
        photos_list = Item_Image.objects.all()
        print(photos_list)
        return render(request, 'emarket/item_img_add.html', {'photos': photos_list})
