from objects import ElAppliance, Household, Neighborhood

if __name__ == "__main__":
    #                  0 , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23
    costPerHourToU = [0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5, 1 , 1 , 1 , 1 ,0.5,0.5,0.5]
    myNeighborhood = Neighborhood("Blindern","ToU")

    myHouse = Household("test")
    myHouse.elAppliance.append(ElAppliance("Dishwasher", 1.44, 1.44, 1, 0, 23))
    myHouse.elAppliance.append(ElAppliance("EV", 9.9, 9.9, 3, 0, 23))
    myHouse.elAppliance.append(ElAppliance("WashingMachine", 1.94, 1.94, 1, 0, 23))

    myNeighborhood.houses.append(myHouse)

    for x in range(len(myNeighborhood.houses)):
        myNeighborhood.printInfo(x)

    testHouseRandom =Household("random")
    testHouseRandom.makeElappliances(5)

    myNeighborhood.houses.append(testHouseRandom)

    for x in range(len(myNeighborhood.houses)):
        myNeighborhood.printInfo(x)
