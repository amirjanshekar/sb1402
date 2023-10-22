from django.shortcuts import render
from django.http import HttpResponseRedirect
import json
from maps.pathLib.pathLoc import pathLoc
from maps.models import simulationModel


# Create your views here.


def start_points(request):
    # codes
    lat_lng = []
    loc = [35.79125, 51.35435]
    locations = request.POST.get('lat-lng', False)
    startCounts = request.POST.get('startCount', False)
    if startCounts != 0:
        l = locations.split(',')
        print(l)
        for i in range(0, len(l)):
            l[i] = float(l[i])
        print(l)
        c = int((len(l) / 2))
        for j in range(0, c):
            lat_lng += [[l[j * 2], l[j * 2 + 1]]]
        print(lat_lng)
        # print(json.dumps(lat_lng))
        # send data to models
        sim = simulationModel.objects.create(sratLocs=json.dumps(lat_lng), peopleCount=10,
                                             endLocs=[[0, 0]], endCapacity=10,
                                             emergencyLocs=[[0, 0]], emergencyCapacity=10,
                                             dangerLocs=[[0, 0]], dangerPossibility=0)
        simID = sim.id
        # print(simID)
        request.session['simId'] = simID
        request.session['startcount'] = startCounts
    j_loc = json.dumps(loc)

    if request.method == 'POST':
        return HttpResponseRedirect('emergencyPoints')

    return render(request, 'mapStartLoc.html', {"myloc": j_loc})


def emergency_points(request):  # hospitals
    # codes
    j_path1 = []
    lat_lng = []
    loc = [35.79125, 51.35435]
    locations = request.POST.get('lat-lng', False)
    startCounts = request.POST.get('pointsCount', False)
    if locations:
        l = locations.split(',')
        print(l)
        for i in range(0, len(l)):
            l[i] = float(l[i])
        c = int((len(l) / 2))
        for i in range(0, c):
            lat_lng += [[l[i * 2], l[i * 2 + 1]]]
        print(lat_lng)
        # send data to models
        simID = request.session['simId']
        # print(simID)
        simulationModel.objects.filter(id=simID).update(emergencyLocs=json.dumps(lat_lng))
    j_loc = json.dumps(loc)

    if request.method == 'POST':
        return HttpResponseRedirect('dangerousPoints')

    return render(request, 'mapEmergencyLoc.html', {"myloc": j_loc})


def dangerous_points(request):  # road damages
    # codes
    j_path1 = []
    lat_lng = []
    loc = [35.79125, 51.35435]
    locations = request.POST.get('lat-lng', False)
    satarCount = request.POST.get('pointsCount', False)
    if locations != False:
        l = locations.split(',')
        # print(l)
        for i in range(0, len(l)):
            l[i] = float(l[i])
        c = int((len(l) / 2))
        for i in range(0, c):
            lat_lng += [[l[i * 2], l[i * 2 + 1]]]
        print(lat_lng)
        # send data to models
        simID = request.session['simId']
        # print(simID)
        simulationModel.objects.filter(id=simID).update(dangerLocs=json.dumps(lat_lng))
    j_loc = json.dumps(loc)

    if request.method == 'POST':
        return HttpResponseRedirect('endPoints')

    return render(request, 'mapDangerousLoc.html', {"myloc": j_loc})


def ends_points(request):
    # codes
    j_path1 = []
    lat_lng = []
    loc = [35.79125, 51.35435]
    locations = request.POST.get('lat-lng', False)
    satarCount = request.POST.get('pointsCount', False)
    if locations != False:
        l = locations.split(',')
        # print(l)
        for i in range(0, len(l)):
            l[i] = float(l[i])
        c = int((len(l) / 2))
        for i in range(0, c):
            lat_lng += [[l[i * 2], l[i * 2 + 1]]]
        print(lat_lng)
        # send data to models
        simID = request.session['simId']
        # print(simID)
        simulationModel.objects.filter(id=simID).update(endLocs=json.dumps(lat_lng))
    j_loc = json.dumps(loc)

    if request.method == 'POST':
        return HttpResponseRedirect('simulation')

    return render(request, 'mapEndtLoc.html', {"myloc": j_loc})


def simul(request):
    # codes
    loc = [35.79125, 51.35435]
    # get data from DB(models) send it to
    simID = request.session['simId']
    startP = simulationModel.objects.filter(id=simID).values_list('sratLocs')
    endP = simulationModel.objects.filter(id=simID).values_list('endLocs')
    danP = simulationModel.objects.filter(id=simID).values_list('dangerLocs')
    emrP = simulationModel.objects.filter(id=simID).values_list('emergencyLocs')
    # print(startP[0][0])#str 
    # print(type(startP[0][0]))
    pathL, trafficPath, trafficNodes, startCount = pathLoc.pathArr(startP[0][0], endP[0][0], emrP[0][0], danP[0][0])
    pathJson = json.dumps(pathL)
    trafficPathJ = json.dumps(trafficPath)
    trafficNodesJ = json.dumps(trafficNodes)
    startCountJ = json.dumps(startCount)
    # startCount = request.session['startcount']

    j_loc = json.dumps(loc)

    return render(request, 'mapSimul.html',
                  {"myloc": j_loc, "mypath": pathJson, "startCount": startCountJ, "trafficPath": trafficPathJ,
                   "trafficNodes": trafficNodesJ})


def traffic_path(request):
    return render(request, 'mapTraffic.html')
