import csv


# #EMPLOYEE WAGES Dictionary --------------------------
# hourlyWage = { 'Abby': -1, 'Akeem': 24.00, 'Albina': -1, 'Aukash': 25.00, 'Ben': 24.00, 'Cameron': 30.00, 'Britto': 20.00, 'Carla': 20.00, 'Darian': 16.00, 'Shashi': -2, 'Dawa': 24.00, 'Dor Cheieh': 22.00, 'Jen': 22.00, 'Eliza': 18.00, 'Glenton': 23.00, 'Jeffrey': 18.00, 'Kamala': -2, 'Keepa': 17.00, 'Lily': 17.00, 'Pema': -1, 'Prakash': -2, 'Oli': -2, 'Preetam': 33.00, 'Ruslan': 22.00, 'Sanish': -2, 'Soman': 18.00, 'Shiva': -2, 'Sujal': 19.00, 'Sunil': -2, 'Tanya': -1, 'Tenzin': -3, 'Yangzi': 19.00, 'Youden': 22.00 }
# # overTimeAndSalary = [['Tanya', 16.00],['Abby', 16.00],['Albina', 16],['Pema', 19.60]]
# otWages = { 'Abby': 16.00, 'Tanya': 16.00, 'Albina': 16.00, "Pema":19.50 }
# fixedPHousing = { 'Sanish': 700, 'Shashi': 900, 'Sunil': 900.00, 'Shiva': 900.00, 'Oli': 900.00, 'Kamala': 900.00}
# salaryWages = {'Tenzin': 1500.00}


# #-----------------------------
# #weekly earnings functions

# def scootersWeelky(row):
#     scooters = 0.00
#     tipsIndex = len(row) - 5
#     totalIndex = len(row) - 1

#     tips = row[tipsIndex]
#     tips = tips.rstrip('",-')
#     tips = tips.replace(',','')
#     tips = float(tips)

#     total = row[totalIndex]
#     total = total.replace(',','')
#     total = total.replace('"','')
#     total = float(total)
#     scooters = total - tips
#     print('Scooters Net')
#     print(scooters)
#     print('')

#     return scooters

# def islandCoffeeWeekly(row):
#     islandCofee = 0.00

#     tipsIndex = len(row) - 5
#     totalIndex = len(row) - 1

#     tips = row[tipsIndex]
#     tips = tips.rstrip('",-')
#     tips = tips.replace(',','')
#     tips = float(tips)

#     total = row[totalIndex]
#     total = total.replace(',','')
#     total = total.replace('"','')
#     total = float(total)

#     islandCofee = total - tips

#     print('Island Coffee Net')
#     print(islandCofee)
#     print('')

#     return islandCofee

# def stubbysWeekly(row):
#     stubbys =0.00

#     tipsIndex = len(row) - 5
#     totalIndex = len(row) - 1

#     tips = row[tipsIndex]
#     tips = tips.rstrip('",-')
#     tips = tips.replace(',','')
#     tips = float(tips)

#     total = row[totalIndex]
#     total = total.replace(',','')
#     total = total.replace('"','')
#     total = float(total)
#     stubbys = total - tips

#     print('Stubbys SQUARE ONLY')
#     print(stubbys)

#     stubbys = (10/9)* stubbys

#     print('Stubbys Net (with 10% cash sales)')
#     print(stubbys)
#     print('')

#     return stubbys


# #Read Weekly Earngings ---------------------------

# salesSummaryByLocation = 'sales-summary-2025-08-24-2025-08-31(0500am-0400amEDT).csv'

# islandCoffeeNet = 0.00
# stubbysNet = 0.00
# scootersNet = 0.00

# with open(salesSummaryByLocation, newline='') as csvfile:
#     fileReadIn = csv.reader(csvfile, delimiter=' ', quotechar='|')
#     for unSplitRow in fileReadIn:
#         if unSplitRow:
#             # print(unSplitRow)
#             for item in unSplitRow:
#                 row = item.split('$')
#             # print(row)
#             # print(len(row))

#             if ('Scooter' in row[0]):
#                 scootersNet = scootersWeelky(row)

#             if ('coffee' in row[0]):
#                 islandCoffeeNet = islandCoffeeWeekly(row)

#             if ('Stubbys' in row[0]):
#                 stubbysNet = stubbysWeekly(row)

# dreadlockNet = stubbysNet + islandCoffeeNet + scootersNet
# # print(dreadlockNet)




# # READ IN EMPLOYEE HOURS

# timeCards = 'labor-cost-summary_2025-08-24_2025-08-31.csv'
# laborCostTable = []
# numberOfRenters = 0
# with open(timeCards, newline='') as csvfile:
#     fileReadIn = csv.reader(csvfile, delimiter=' ', quotechar='|')
#     for unSplitRow in fileReadIn:
#         if unSplitRow:
#             # print(unSplitRow)
#             # print('aaaaaaaa')
#             # print(unSplitRow)
#             row = []
#             if ("Employee" not in unSplitRow[0]):

#                 for item in unSplitRow:
#                     row = item.split(',')
#                     # print(row)
#                     # print('bbbbbb')

#                     if (row[0] == '""'):
#                         row = row[1:]
#                     # print(row[0])
#                     # print('c')


#                 # SET UP LIST OF ARRAYS, [EMPLOYEE NAME, EMPLOYEE WEEK LABOR COST]
#                 firstName = row[0].replace('"','',10)
#                 weekPay = 0.0


#                 hoursIndex = len(row) -7
#                 paidHours = float(row[hoursIndex].replace('"',''))
#                 wage = hourlyWage[firstName]

#                 # ot wages
#                 if wage == -1:
#                     otWage = otWages[firstName]
#                     if paidHours > 40.00:
#                         weekPay = (40*otWage)+((paidHours-40)*1.5*otWage)
#                     else:
#                         weekPay = 40*otWage
#                 elif wage == -2:
#                     numberOfRenters += 1
#                     weekPay = fixedPHousing[firstName]
#                 elif wage == -3:
#                     weekPay = salaryWages[firstName]
#                 else:
#                     weekPay = (paidHours*wage)



#                 tableEl = [firstName, weekPay]
#                 laborCostTable.append(tableEl)
#                 # print(paidHours)
#                 # print(laborCostTable)
#                 # print(hours)
#                 # print(firstName)
#                 # print(hourlyWage[firstName])

#             # print(row)
#             # print(row[1:])
#             # print(len(row))


# # print(laborCostTable)

# laborCostTotal = 0.00
# for employee in laborCostTable:
#     laborCostTotal += employee[1]

# laborCostTotal = laborCostTotal + 5000.00

# # print(numberOfRenters)
# laborCostPRent = laborCostTotal + ((numberOfRenters + 2) * 200.00)

# laborCostRation = (laborCostTotal/dreadlockNet)*100
# laborCostPRentRatio = (laborCostPRent/dreadlockNet)*100
# print('dreatlock net total (with stubbys 10% cash sales, no chownow or ack eats)')
# print(dreadlockNet)
# print('')
# print('')
# print('labor cost no rent')
# print(laborCostTotal)
# print('percent of dreadlock net')
# print(laborCostRation)
# print('')

# print('approximate 200 per week rent for fixed plus housing')
# print((len(fixedPHousing)+2) * 200)
# print('')

# print('labor cost with rent')
# print(laborCostPRent)
# print('percent of dreadlock net')
# print(laborCostPRentRatio)
# print('')

class LaborCosts:
    """
     self.strArray = [str(self.dreadlockNet),str(self.laborCostTotal), str(self.laborCostPRent), str(self.laborCostPercent), str(self.laborPlResntPercent)]
    """
    def __init__(self, salesFileName, timeCardsFileName):
        self.salesFileName = salesFileName
        self.timeCardsFileName = timeCardsFileName


        self.dreadlockNet, self.laborCostTotal, self.laborCostPRent, self.laborCostPercent, self.laborPlResntPercent, self.employeesMissing = self.calcLaborCost()
        self.strArray = [str(self.dreadlockNet),str(self.laborCostTotal), str(self.laborCostPRent), str(self.laborCostPercent), str(self.laborPlResntPercent), self.employeesMissing]

    def calcLaborCost(self):
        #EMPLOYEE WAGES Dictionary --------------------------
        hourlyWage = { 'Abby': -1, 'Akeem': 24.00, 'Albina': -1, 'Aukash': 25.00, 'Ben': 24.00, 'Cameron': 30.00, 'Britto': 20.00, 'Carla': 20.00, 'Darian': 16.00, 'Shashi': -2, 'Dawa': 24.00, 'Dor Cheieh': 22.00, 'Jen': 22.00, 'Eliza': 18.00, 'Glenton': 23.00, 'Jeffrey': 18.00,'Kabita': -2, 'Kamala': -2, 'Keepa': 17.00, 'Lily': 17.00, 'Pema': -1, 'Prakash': -2, 'Oli': -2, 'Preetam': 33.00, 'Ruslan': 22.00, 'Sanish': -2, 'Soman': 18.00, 'Shiva': -2, 'Sujal': 19.00, 'Sunil': -2, 'Tanya': -1, 'Tenzin': -3, 'Yangzi': 19.00, 'Youden': 22.00 }
        # overTimeAndSalary = [['Tanya', 16.00],['Abby', 16.00],['Albina', 16],['Pema', 19.60]]
        otWages = { 'Abby': 16.00, 'Tanya': 16.00, 'Albina': 16.00, "Pema":19.50 }
        fixedPHousing = { 'Sanish': 700, 'Shashi': 900, 'Sunil': 900.00, 'Shiva': 900.00, 'Oli': 900.00, 'Kamala': 900.00, 'Kabita': 900.00}
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

        dreadlockNet = stubbysNet + islandCoffeeNet + scootersNet
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

                        for item in unSplitRow:
                            row = item.split(',')
                            # print(row)
                            # print('bbbbbb')

                            if (row[0] == '""'):
                                row = row[1:]
                            # print(row[0])
                            # print('c')


                        # SET UP LIST OF ARRAYS, [EMPLOYEE NAME, EMPLOYEE WEEK LABOR COST]
                        firstName = row[0].replace('"','',10)
                        weekPay = 0.0


                        hoursIndex = len(row) -7
                        paidHours = float(row[hoursIndex].replace('"',''))
                        if firstName in hourlyWage:
                            wage = hourlyWage[firstName]

                            # ot wages
                            if wage == -1:
                                otWage = otWages[firstName]
                                if paidHours > 40.00:
                                    weekPay = (40*otWage)+((paidHours-40)*1.5*otWage)
                                else:
                                    weekPay = 40*otWage
                            elif wage == -2:
                                numberOfRenters += 1
                                weekPay = fixedPHousing[firstName]
                            elif wage == -3:
                                weekPay = salaryWages[firstName]
                            else:
                                weekPay = (paidHours*wage)



                            tableEl = [firstName, weekPay]
                            laborCostTable.append(tableEl)
                        else:
                            # print('EMPLOYEE NOT FOUND')
                            # print(firstName)
                            employeesNotFound = employeesNotFound + ' ' + firstName +','
                        # print(paidHours)
                        # print(laborCostTable)
                        # print(hours)
                        # print(firstName)
                        # print(hourlyWage[firstName])

                    # print(row)
                    # print(row[1:])
                    # print(len(row))


        # print(laborCostTable)

        laborCostTotal = 0.00
        for employee in laborCostTable:
            laborCostTotal += employee[1]

        laborCostTotal = laborCostTotal + 5000.00

        # print(numberOfRenters)
        laborCostPRent = laborCostTotal + ((numberOfRenters + 2) * 200.00)

        laborCostPercent = (laborCostTotal/dreadlockNet)*100
        laborCostPRentPercent = (laborCostPRent/dreadlockNet)*100
        # print('dreatlock net total (with stubbys 10% cash sales, no chownow or ack eats)')
        # print(dreadlockNet)
        # print('')
        # print('')
        # print('labor cost no rent')
        # print(laborCostTotal)
        # print('percent of dreadlock net')
        # print(laborCostRation)
        # print('')

        # print('approximate 200 per week rent for fixed plus housing')
        # print((len(fixedPHousing)+2) * 200)
        # print('')

        # print('labor cost with rent')
        # print(laborCostPRent)
        # print('percent of dreadlock net')
        # print(laborCostPRentPercent)
        # print('')

        return dreadlockNet, laborCostTotal, laborCostPRent, laborCostPercent, laborCostPRentPercent, employeesNotFound





