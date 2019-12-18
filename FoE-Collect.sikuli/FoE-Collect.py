print "start"

def startGame():
    App.open("chrome")
    wait(1.25)
    paste("https://de.forgeofempires.com/")
    type(Key.ENTER)
    wait(1)
    
    #login
    if exists("1527601417125.png"):
        click("1527601417125")
        wait(1)
        click("1527601615780.png")
        wait(3)

def collectResources(event):
    print "collect"
    for x in findAll(Pattern("1527582458451.png").similar(0.57)):
        click(x.below(40))
	for y in findAll(Pattern("1527581487161.png").similar(0.57)):
		click(y.below(40))

def collectMoney(event):
    print "money"
    for x in findAll(Pattern("1527582458451.png").similar(0.57)):
        click(x.below(40))

def collectTools(event):
    print "tools"
    for x in findAll(Pattern("1527581487161.png").similar(0.57)):
        click(x.below(40))

def collectArmy(event):
    print "army"
    for x in findAll(Pattern("1527601979700.png").similar(0.57)):
        click(x.below(40))

def collectGoods(event):
    print "goods"
    for x in findAll(Pattern("1527605472635.png").similar(0.57)):
        click(x.below(40))

def showChangedInRegion(event):
    print "something changed in ", event.region
    for ch in event.changes:
        ch.highlight() # highlight all changes
    sleep(1)
    for ch in event.changes:
        ch.highlight() # turn off the highlights

def onScreenChange():
    collectResources()

def isLoggedIn():
    # check if already open
    if exists("1576677990119.png"):
        return True
    return False

# main
if not isLoggedIn():
    startGame()

onAppear(Pattern("1527582458451.png").similar(0.57), collectMoney)
onAppear(Pattern("1527581487161.png").similar(0.57), collectTools)
onAppear(Pattern("1527601979700.png").similar(0.57), collectArmy)
onAppear(Pattern("1527605472635.png").similar(0.57), collectGoods)

observe(100, False)