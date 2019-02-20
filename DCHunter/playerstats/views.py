from django.shortcuts import render
from .forms import PlayerForm
from .models import Player
# Create your views here.

def stats(request):

    form = PlayerForm()

    if request.method == 'POST':
        form = PlayerForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
        else:
            print("Invalid entry")
    else:
        form = PlayerForm()
    return render(request, 'playerstats/details.html',{'form': form})


def home(request):
    playerList = Player.objects.all()
    playerDict = {'playerDict' : playerList}
    return render(request,'playerstats/home.html',context=playerDict)

def wins(request):
    playerwinsList = Player.objects.order_by('-TotalWins')
    playerwinsDict = {'playerwinsDict': playerwinsList}
    return render(request, 'playerstats/totalwins.html', context=playerwinsDict)

def match(request):
    playermatchList = Player.objects.order_by('-TotalMatches')
    playermatchDict = {'playermatchDict': playermatchList}
    return render(request, 'playerstats/totalmatches.html', context=playermatchDict)

def kills(request):
    playerkilllist = Player.objects.order_by('-Killratio')
    playerkillDict = {'playerkillDict': playerkilllist}
    return render(request,'playerstats/totalkills.html', context=playerkillDict)

def headshot(request):
    playerheadshotlist = Player.objects.order_by('-Headshotratio')
    playerheadshotDict = {'playerheadshotDict': playerheadshotlist}
    return render(request,'playerstats/totalheadshot.html', context=playerheadshotDict)

def mostkills(request):
    playermostkillList = Player.objects.order_by('-Mostkills')
    playermostkillDict = {"playermostkillDict":playermostkillList}
    return render(request,'playerstats/mostkills.html',context=playermostkillDict)

def topseason05(request):
    topseason05List = Player.objects.order_by('-Topseason')
    topseason05Dict = {"topseason05Dict":topseason05List}
    return render(request,'playerstats/topseason05.html',context=topseason05Dict)
