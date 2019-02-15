from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Room, Reservation


def go_home(request):
    '''
    for ease of testing redirects to the tested app url
    :param request:
    :return: redirect to url
    '''
    return redirect('/reservation/address/')


def show_rooms(request):
    '''
    Render page with rooms available
    :param request: request object
    :return: render room page
    '''
    action = request.POST.get('action')

    # list all rooms available
    rooms = Room.objects.all()

    if action == "book" or action == "check":
        id = request.POST.get('id')
        try:
            request_date = datetime.strptime(request.POST.get('date'), '%Y-%m-%d').date()
        except Exception as e:
            messages.warning(request, e)
            return redirect('roomreservation-show_rooms')
        today = datetime.now().date()
        reservation = Reservation.objects.filter(room_id=id).filter(date=request_date)

        if request_date < today:
            messages.info(request, "Invalid date.")
            return redirect('roomreservation-show_rooms')
        elif reservation.count() != 0:
            messages.warning(request, "This date is already taken.")
            return redirect('roomreservation-show_rooms')
        else:
            if action == "check":
                messages.success(request, "This date is available for booking.")
                return render(request, 'rooms.html', {'rooms': rooms, 'date': request.POST.get('date')})
            else:
                return redirect('roomreseration-room_reservation', id=id, date=request.POST.get('date'))

    if action == "delete":
        id = request.POST.get('id')
        r = Room.objects.get(pk=id)
        r.delete()
        messages.info(request, "Room deleted")
        return redirect('roomreservation-show_rooms')

    if action == "add":
        return render(request, 'room_manage.html')

    return render(request, 'rooms.html', {'rooms': rooms})


def room_details(request, id):
    '''
    Render room details
    :param request: request object
    :param id: room id
    :return: render room details page
    '''
    room = Room.objects.get(pk=id)

    return render(request, 'room_details.html', {'room': room})


def add_room(request):
    '''
    Enable adding new rooms to database
    :param request:
    :return: Render add room page
    '''
    action = request.POST.get('action')

    if action == "commit":
        name = request.POST.get('name')
        capacity = request.POST.get('capacity')
        is_projector = request.POST.get('is_projector')

        r = Room.objects.create(name=name,
                                capacity=capacity,
                                is_projector=bool(is_projector))
        r.save()
        return redirect('roomreservation-show_rooms')

    return render(request, 'room_manage.html')


def edit_room(request, id):
    '''
    Render room edit page - enable CRUD operations
    :param request: request object
    :param id: room id
    :return: render room edit page
    '''
    action = request.POST.get('action')
    if action == "commit":
        r = Room.objects.get(pk=id)
        r.save()
        return redirect('roomreservation-show_rooms')

    room = Room.objects.get(pk=id)
    return render(request, 'room_manage.html', {'room': room})


def make_reservation(request, id, date):
    '''
    Render confirm reservation page
    :param request: request object
    :param id: room id
    :param date: search date
    :return: render confirm reservation page
    '''
    action = request.POST.get('action')
    room = Room.objects.get(pk=id)

    try:
        request_date = datetime.strptime(date, '%Y-%m-%d').date()
    except Exception as e:
        messages.warning(request, e)
        return redirect('roomreservation-show_rooms')

    if action == "commit":
        today = datetime.now().date()
        reservation = Reservation.objects.filter(room_id=id).filter(date=request_date)

        if request_date < today:
            messages.info(request, "Invalid date.")
            return redirect('roomreservation-show_rooms')
        elif reservation.count() != 0:
            messages.warning(request, "This date is already taken.")
            return redirect('roomreservation-show_rooms')
        else:
            comment = request.POST.get('comment')
            res = Reservation.objects.create(date=date,
                                             comment=comment,
                                             room=room)
            res.save()
            messages.success(request,
                             f"Your booking is placed for {room.name} on {date}")
            return redirect('roomreservation-show_rooms')

    reservations = room.reservation_set.all()

    return render(request, 'reservation.html', {'room': room,
                                                'date': date,
                                                'reservations': reservations})


def search_room(request):
    '''
    find queryset which matches given serch criteria
    :param request: request
    :return: render search page
    '''
    name = request.GET.get('name')
    capacity = request.GET.get('capacity')
    is_projector = request.GET.get('is_projector')
    date = request.GET.get('date')

    rooms = Room.objects.all()

    if name:
        rooms = rooms.filter(name=name)

    if capacity:
        rooms = rooms.filter(capacity__gte=int(capacity))

    if is_projector:
        rooms = rooms.filter(is_projector=bool(is_projector))

    # todo: modify filter to work properly with dates. DONE
    if date:
        for room in rooms:
            if room.reservation_set.filter(date=date).count() != 0:
                rooms = rooms.exclude(pk=room.id)
    else:
        messages.warning(request, "Please select date.")
        return redirect('roomreservation-show_rooms')

    return render(request, 'search.html', {"rooms": rooms, 'date': date})
