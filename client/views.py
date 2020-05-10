from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect

from .models import Shop, Client, Dish, Order, DishOrder
from .forms import PhoneForm, CardForm


# Create your views here.
def index(request):
    context = {
        "shops": Shop.objects.all()
    }
    return render(request, "client/index.html", context)


def shop(request, shop_id):
    try:
        shop = Shop.objects.get(pk=shop_id)
    except Shop.DoesNotExist:
        raise Http404("Shop does no exist")
    context = {
        "shop": shop,
        "dishes": shop.dishes.all(),
        "shop_dish_cat": shop.dishes.all().values_list('category', flat=True).distinct(),
        # "dish_categories": Dish.objects.values_list('category', flat=True).distinct(),
    }
    if not request.user.is_anonymous:
        account_context = {
            "email": request.user.username,
            "name": request.user.first_name,
        }
        context.update(account_context)
    return render(request, "client/shop.html", context)


@csrf_protect
def first(request):

    context = {
        "shop_categories": Shop.objects.values_list('category', flat=True).distinct(),
        "dish_categories": Dish.objects.values_list('category', flat=True).distinct(),
        "shops": Shop.objects.all(),
        "asian_shops": Shop.objects.filter(dishes__category="Asian"),
        "burger_shops": Shop.objects.filter(dishes__category="Burger"),
        "pizza_shops": Shop.objects.filter(dishes__category="Pizza"),
        "vegan_shops": Shop.objects.filter(dishes__category="Vegan"),
        "drinks_shops": Shop.objects.filter(dishes__category="Drinks"),

    }

        # user = User.objects.filter(k=username).update(field1='some value')

    if not request.user.is_anonymous:
        if request.method == 'POST':
            # client_id = Client.objects.filter(user_id=request.user.id).first()
            #
            # if Order.objects.filter(client_id=client_id).first() is None:
            #     client = Client.objects.filter(user_id=request.user.id).first()
            #     order = Order.objects.create(client_id=client.id)
            #     order.save()
            # else:
            #     order = Order.objects.filter(client_id=client_id).first()

            phone_form = PhoneForm(request.POST)
            card_form = CardForm(request.POST)
            # dish_id_form = DishIdForm(request.POST)

            if phone_form.is_valid():
                # process the data in form.cleaned_data as required
                phone = phone_form.cleaned_data['phone']
                Client.objects.filter(user_id=request.user.id).update(phone=phone)

                # ...
                # redirect to a new URL:

                # return HttpResponseRedirect('/')
            if card_form.is_valid():
                card = card_form.cleaned_data['card']
                Client.objects.filter(user_id=request.user.id).update(card=card)

                # return HttpResponseRedirect('/')

            # if dish_id_form.is_valid():
            #
            #     dish_id = dish_id_form.cleaned_data['dish_id']
            #     dish_order = DishOrder.objects.create(order_id=order.id, dish_id=dish_id)
            #     dish_order.save()

                # DishOrder.objects.filter(order_id=order.id).update(dish_id=dish_id)

                # Client.objects.filter(user_id=request.user.id).update(card=card)

                # return HttpResponseRedirect('/')

            # if a GET (or any other method) we'll create a blank form

        else:
            phone_form = PhoneForm()
            card_form = CardForm()
            # dish_id_form = DishIdForm()

        account_context = {
            "email": request.user.username,
            "name": request.user.first_name,
            "client": Client.objects.all().filter(user_id=request.user.id).first(),
            "phone_form": phone_form,
            "card_form": card_form,
            # "dish_id_form": dish_id_form,
        }
        context.update(account_context)

    return render(request, "client/first.html", context)


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        # last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        # password2 = request.POST['password2']
        # email = request.POST['email']

        if User.objects.filter(username=username).exists():
            messages.info(request, "Username taken")
            return redirect('/register')
            # elif User.objects.filter(email=email).exists():
            #             #     messages.info(request, "Email taken")
            #             #     return redirect('/register')
        else:
            user = User.objects.create_user(username=username, password=password1,
                                            first_name=first_name)
            client = Client.objects.create(user_id=user.id)
            user.save()
            client.save()
            print("User created")
            return redirect('/login')
        # return redirect("/")
    else:
        return render(request, "client/register.html")


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, "Invalid credentials")
            return redirect('/login')
    else:
        return render(request, 'client/login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def add_user_info(request):
    return render(request, "client/add_user_info.html")


def add_user_info_submit(request):
    if request.method == 'POST':
        phone = request.POST['phone']
        address = request.POST['address']
        card = request.POST['card']
        user = auth.get_user(request)
        client = Client.objects.create(phone=phone, address=address, card=card, user=user)

        client.save()
        print("Client created")
        return redirect('/')
    else:
        return render(request, 'client/add_user_info.html')


def add_phone(request):
    if request.method == 'POST':
        user = auth.get_user(request)
        phone = request.POST['phone']
        client = Client.objects.create(phone=phone, user=user)
        client.save()
        print("Client created")
        return redirect('/')
    else:
        return redirect('/')

# def approve_group(request, pk):
#     group = Group.objects.get(pk=pk)
#     group.status = Status.approved
#     group.save()
#     return redirect(request, 'home')

