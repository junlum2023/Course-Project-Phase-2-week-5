def getdatesWorked():
    fromDate = input("Please enter start date in the following format MM/DD/YYYY: ")
    endDate = input("Please enter the end date in the following format MM/DD/YYYY: ")
    return fromDate,  endDate

def getEmpname():
    empName = input("Enter employee name: ")
    return empName

def getHoursWorked():
    hours = float(input("Enter hours: "))
    return hours

def getHourlyrate():
    hourlyRate = float(input("Enter hourly rate: "))
    return hourlyRate

def getTaxRate():
    taxRate = float(input("Enter tax rate: "))
    taxRate = taxRate / 100
    return taxRate

def CalcTaxAndNetpay(hours, hourlyrate, taxRate):
    gPay = hours * hourlyRate
    incomeTax = gPay * taxRate
    netPay = gPay - incomeTax
    return gPay, incomeTax, netPay

def printinfo(empDetailList):
    totalEmployees = 0
    totalHours = 0.00
    totalGrossPay = 0.00
    totalTax = 0.00
    totalNetpay = 0.00
    for empList in empDetailList:
        fromDate = empList[0]
        endDate = empList[1]
        empName = empList[2]
        hours = empList[3]
        hourlyRate = empList[4]
        taxRate = empList[5]
        
gPay, incomeTax, netPay = CalcTaxAndNetPay(hours, hourlyRate, taxRate)
print(fromDate, endDate, empName,  f"{hours:,.2f}", f"{hourlyRate:,.2f}", f"{grosspay:,.2f}", f"{taxRate:,.1%}", f"{incometax:,.2f}", f'{netPay:,.2f}")
totalEmployees += 1
totalHours += hoours
totalGrossPay += gPay
totaltax += incometax
totalNetPay += netPay


