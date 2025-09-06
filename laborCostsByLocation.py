import csv
from collections import defaultdict

class LaborCosts:
    """
    self.strArray = [str(self.dreadlockNet),str(self.laborCostTotal), str(self.laborCostPRent), str(self.laborCostPercent), str(self.laborPlResntPercent)]
    self.laborCostArray =  [Stubbys, Scooters, Island Coffee]
    """
    def __init__(self, salesFileName, timeCardsFileName, locations):
        self.salesFileName = salesFileName
        self.timeCardsFileName = timeCardsFileName
        self.stubbys, self.scooters, self.ic = locations



        self.laborTable = []

        self.laborCostArray =  []
        self.locationNet = []
        self.locationLaborCostPercent = [0,0,0]

        self.dreadlockNet, self.laborCostTotal, self.laborCostPRent, self.laborCostPercent, self.laborPlResntPercent, self.employeesMissing = self.calcLaborCost()
        self.strArray = [str(self.dreadlockNet),str(self.laborCostTotal), str(self.laborCostPRent), str(self.laborCostPercent), str(self.laborPlResntPercent), self.employeesMissing]

    def calcLaborCost(self):
        #EMPLOYEE WAGES Dictionary --------------------------
        hourlyWage = { 'Abby': -1, 'Akeem': 24.00, 'Albina': -1, 'Aukash': 25.00, 'Ben': 24.00, 'Cameron': 30.00, 'Britto': 20.00, 'Carla': 20.00, 'Darian': 16.00, 'Shashi': -2, 'Dawa': 24.00, 'Dor Cheieh': 22.00, 'Jen': 22.00, 'Eliza': 18.00, 'Glenton': 23.00, 'Jeffrey': 18.00,'Kabita': -2, 'Kamala': -2, 'Keepa': 17.00, 'Lily': 17.00, 'Pema': -1, 'Prakash': -2, 'Oli': -2, 'Preetam': 33.00, 'Ruslan': 22.00, 'Saroj': -2, 'Sanish': -2, 'Soman': 18.00, 'Shiva': -2, 'Sujal': 19.00, 'Sunil': -2, 'Tanya': -1, 'Tenzin': -3, 'Yangzi': 19.00, 'Youden': 22.00 }
        # overTimeAndSalary = [['Tanya', 16.00],['Abby', 16.00],['Albina', 16],['Pema', 19.60]]
        otWages = { 'Abby': 16.00, 'Tanya': 16.00, 'Albina': 16.00, "Pema":19.50 }
        fixedPHousing = { 'Saroj': 700, 'Sanish': 700, 'Shashi': 900, 'Sunil': 900.00, 'Shiva': 900.00, 'Prakash': 900.00, 'Kamala': 900.00, 'Kabita': 900.00}
        salaryWages = {'Tenzin': 1500.00}

        def scootersWeelky(row):
            scooters = 0.00
            tipsIndex = len(row) - 5
            totalIndex = len(row) - 1

            tips = row[tipsIndex]
            tips = tips.rstrip('",-')
            tips = tips.replace(',','')
            tips = float(tips)

            total = row[totalIndex]
            total = total.replace(',','')
            total = total.replace('"','')
            total = float(total)
            scooters = total - tips
            # print('Scooters Net')
            # print(scooters)
            # print('')

            return scooters

        def islandCoffeeWeekly(row):
            islandCofee = 0.00

            tipsIndex = len(row) - 5
            totalIndex = len(row) - 1

            tips = row[tipsIndex]
            tips = tips.rstrip('",-')
            tips = tips.replace(',','')
            tips = float(tips)

            total = row[totalIndex]
            total = total.replace(',','')
            total = total.replace('"','')
            total = float(total)

            islandCofee = total - tips

            # print('Island Coffee Net')
            # print(islandCofee)
            # print('')

            return islandCofee

        def stubbysWeekly(row):
            stubbys =0.00

            tipsIndex = len(row) - 5
            totalIndex = len(row) - 1

            tips = row[tipsIndex]
            tips = tips.rstrip('",-')
            tips = tips.replace(',','')
            tips = float(tips)

            total = row[totalIndex]
            total = total.replace(',','')
            total = total.replace('"','')
            total = float(total)
            stubbys = total - tips

            # print('Stubbys SQUARE ONLY')
            # print(stubbys)

            stubbys = (10/9)* stubbys

            # print('Stubbys Net (with 10% cash sales)')
            # print(stubbys)
            # print('')

            return stubbys


        #Read Weekly Earngings ---------------------------


        islandCoffeeNet = 0.00
        stubbysNet = 0.00
        scootersNet = 0.00

        with open(self.salesFileName, newline='') as csvfile:
            fileReadIn = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for unSplitRow in fileReadIn:
                if unSplitRow:
                    # print(unSplitRow)
                    for item in unSplitRow:
                        row = item.split('$')
                    # print(row)
                    # print(len(row))

                    if ('Scooter' in row[0]):
                        scootersNet = scootersWeelky(row)

                    if ('coffee' in row[0]):
                        islandCoffeeNet = islandCoffeeWeekly(row)

                    if ('Stubbys' in row[0]):
                        stubbysNet = stubbysWeekly(row)

        self.locationNet = [stubbysNet, scootersNet, islandCoffeeNet]
        dreadlockNet = stubbysNet + islandCoffeeNet + scootersNet
        print(dreadlockNet)
        # print(dreadlockNet)




        # READ IN EMPLOYEE HOURS

        timeCards = 'labor-cost-summary_2025-08-24_2025-08-31.csv'
        laborCostTable = []
        employeesNotFound = ''
        numberOfRenters = 0
        with open(self.timeCardsFileName, newline='') as csvfile:
            fileReadIn = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for unSplitRow in fileReadIn:
                if unSplitRow:
                    # print(unSplitRow)
                    # print('aaaaaaaa')
                    # print(unSplitRow)
                    row = []
                    if ("Employee" not in unSplitRow[0]):

                        if len(unSplitRow) > 1:
                            # print(unSplitRow)
                            unSplitRow[0] = unSplitRow[0] + unSplitRow[1]
                            # print(unSplitRow[0])
                            del unSplitRow[1]
                        # print(unSplitRow)
                        for item in unSplitRow:
                            # print(item)

                            # if ('"Island', 'coffee"' in unSplitRow):
                            #     print(unSplitRow)
                            #     for el in unSplitRow:
                            #         print(el)
                                # print((unSplitRow))
                            row = item.split(',')
                            # print(row)
                            # print(row)
                            # print('bbbbbb')
                            # print(row[0])
                            if (row[0] == '""'):
                                row = row[1:]
                            # print(row[0])
                            # print('c')


                        # SET UP LIST OF ARRAYS, [EMPLOYEE NAME, EMPLOYEE WEEK LABOR COST]
                        # print(row)
                        firstName = row[0].replace('"','',10)
                        weekPay = 0.0
                        wageStr = ''


                        hoursIndex = len(row) - 7
                        locIndex = len(row) - 11
                        paidHours = float(row[hoursIndex].replace('"',''))
                        location = row[locIndex].replace('"','')

                        # print(firstName)

                        if (location == 'Stubbys'):
                            if firstName in hourlyWage:
                                wage = hourlyWage[firstName]

                                # ot wages
                                if wage == -1:
                                    otWage = otWages[firstName]
                                    otBaseSt = str(otWage)
                                    otTAHWageSt = str(1.5*otWage)
                                    wageStr = otBaseSt + ' / ' + otTAHWageSt + ' OT'
                                    if paidHours > 40.00:
                                        weekPay = (40*otWage)+((paidHours-40)*1.5*otWage)
                                    else:
                                        weekPay = 40*otWage
                                elif wage == -2:
                                    numberOfRenters += 1
                                    weekPay = fixedPHousing[firstName]
                                    weekPayStr = str(weekPay)
                                    wageStr = weekPayStr + ' per week fixed'
                                elif wage == -3:
                                    weekPay = salaryWages[firstName]
                                    weekPayStr = str(weekPay)
                                    wageStr = weekPayStr + ' salary'
                                else:
                                    weekPay = (paidHours*wage)
                                    wageStr = str(wage) + 'hourly'




                                tableEl = [firstName, weekPay, paidHours, wageStr, location]
                                laborCostTable.append(tableEl)
                            else:
                                # print('EMPLOYEE NOT FOUND')
                                # print(firstName)
                                employeesNotFound = employeesNotFound + ' ' + firstName +','


                        if (location == "Scooter's"):
                            if firstName in hourlyWage:
                                wage = hourlyWage[firstName]

                                # ot wages
                                if wage == -1:
                                    otWage = otWages[firstName]
                                    otBaseSt = str(otWage)
                                    otTAHWageSt = str(1.5*otWage)
                                    wageStr = otBaseSt + ' / ' + otTAHWageSt + ' OT'
                                    if paidHours > 40.00:
                                        weekPay = (40*otWage)+((paidHours-40)*1.5*otWage)
                                    else:
                                        weekPay = 40*otWage
                                elif wage == -2:
                                    numberOfRenters += 1
                                    weekPay = fixedPHousing[firstName]
                                    weekPayStr = str(weekPay)
                                    wageStr = weekPayStr + ' per week fixed'
                                elif wage == -3:
                                    weekPay = salaryWages[firstName]
                                    weekPayStr = str(weekPay)
                                    wageStr = weekPayStr + ' salary'
                                else:
                                    weekPay = (paidHours*wage)
                                    wageStr = str(wage) + 'hourly'




                                tableEl = [firstName, weekPay, paidHours, wageStr, location]
                                laborCostTable.append(tableEl)
                            else:
                                # print('EMPLOYEE NOT FOUND')
                                # print(firstName)
                                employeesNotFound = employeesNotFound + ' ' + firstName +','


                        if (location == 'Islandcoffee'):
                            if firstName in hourlyWage:
                                wage = hourlyWage[firstName]

                                # ot wages
                                if wage == -1:
                                    otWage = otWages[firstName]
                                    otBaseSt = str(otWage)
                                    otTAHWageSt = str(1.5*otWage)
                                    wageStr = otBaseSt + ' / ' + otTAHWageSt + ' OT'
                                    if paidHours > 40.00:
                                        weekPay = (40*otWage)+((paidHours-40)*1.5*otWage)
                                    else:
                                        weekPay = 40*otWage
                                elif wage == -2:
                                    numberOfRenters += 1
                                    weekPay = fixedPHousing[firstName]
                                    weekPayStr = str(weekPay)
                                    wageStr = weekPayStr + ' per week fixed'
                                elif wage == -3:
                                    weekPay = salaryWages[firstName]
                                    weekPayStr = str(weekPay)
                                    wageStr = weekPayStr + ' salary'
                                else:
                                    weekPay = (paidHours*wage)
                                    wageStr = str(wage) + 'hourly'




                                tableEl = [firstName, weekPay, paidHours, wageStr, location]
                                laborCostTable.append(tableEl)
                            else:
                                # print('EMPLOYEE NOT FOUND')
                                # print(firstName)
                                employeesNotFound = employeesNotFound + ' ' + firstName +','





        separated_data = defaultdict(list)
        for item in laborCostTable:
            key_value = item[0]  # The value at index 0 is the key
            separated_data[key_value].append(item)

        separated_data = dict(separated_data)

        for emp, els in separated_data.items():
            if len(els) > 1:
                if ('salary' in  els[0][3]) or ('per week fixed' in els[0][3]):
                    weekHours = 0
                    for loc in els:
                        # print(els)
                        weekHours += loc[2]
                    hourlyWage = els[0][1]/weekHours
                    # print(hourlyWage)
                    for loc in els:
                        # print(type(loc[3]))
                        loc[1] = hourlyWage * float(loc[2])
                        # print(loc)

        laborCostTable = []

        stubbysLabor = 0
        scootersLabor = 0
        icLabor = 0

        location = [[self.stubbys, 'Stubbys', stubbysLabor],[self.scooters, "Scooter's", scootersLabor],[self.ic, 'Islandcoffee', icLabor]]

        for loc in location:

            if loc[0]:
                for values in separated_data.values():
                    for el in values:

                        if el[4] == loc[1]:
                            # print(el[4])
                            laborCostTable.append(el)

                            if loc[1] == 'Stubbys':
                                stubbysLabor += el[1]
                                print(el[0])
                            elif loc[1] == "Scooter's":
                                scootersLabor += el[1]
                                print(el[0])
                            elif loc[1] == 'Islandcoffee':
                                icLabor += el[1]
                                print(el[0])
                                # print(loc[2])


        self.laborCostArray = [stubbysLabor, scootersLabor,icLabor]

        i = 0
        for el in self.laborCostArray:
            self.locationLaborCostPercent[i] = (self.laborCostArray[i] / self.locationNet[i]) * 100
            i += 1

        laborCostTotal = stubbysLabor + scootersLabor + icLabor

        self.laborTable = laborCostTable


        # owners
        laborCostTotal = laborCostTotal + 5000.00

        if self.stubbys:
            numberOfRenters =numberOfRenters + 2 # the + 2 is ak and soman
        laborCostPRent = laborCostTotal + ((numberOfRenters ) * 200.00)

        laborCostPercent = (laborCostTotal/dreadlockNet)*100
        laborCostPRentPercent = (laborCostPRent/dreadlockNet)*100


        return dreadlockNet, laborCostTotal, laborCostPRent, laborCostPercent, laborCostPRentPercent, employeesNotFound


# locations = [True, True, True]
# t1 = LaborCosts('sales-summary-2025-08-24-2025-08-31(0500am-0400amEDT).csv','labor-cost-summary_2025-08-24_2025-08-31.csv', locations)
# print(t1.laborCostArray)
# print(t1.locationNet)
