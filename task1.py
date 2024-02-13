# Writing financial data to text files
CompanyA_Quarter1 = open("CompanyA_Quarter1.txt", "w+")
CompanyA_Quarter1.write("""Quarter: Q1
Revenue: $1,500,000
Expenses: $900,000
Net Income: $600,000
EPS: $1.20
Assets: $3,000,000
Liabilities: $1,200,000
Equity: $1,800,000\n""")
CompanyA_Quarter1.close()

CompanyA_Quarter2=open("CompanyA_Quarter2.txt","w+")
CompanyA_Quarter2.write(""" 
Company: Company A
Quarter: Q2
Revenue: $1,800,000
Expenses: $1,000,000
Net Income: $800,000
EPS: $1.60
Assets: $3,500,000
Liabilities: $1,400,000
Equity: $2,100,000 \n
""")
CompanyA_Quarter2.close()

CompanyB_Quarter1=open("CompanyB_Quarter1.txt","w+")
CompanyB_Quarter1.write("""
Company: Company B
Quarter: Q1
Revenue: $2,000,000
Expenses: $1,200,000
Net Income: $800,000
EPS: $2.00
Assets: $4,500,000
Liabilities: $2,000,000
Equity: $2,500,000 \n
""")
CompanyB_Quarter1.close()

CompanyB_Quarter2=open("CompanyB_Quarter2.txt","w+")
CompanyB_Quarter2.write("""
Company: Company B
Quarter: Q2
Revenue: $2,300,000
Expenses: $1,300,000
Net Income: $1,000,000
EPS: $2.50
Assets: $5,000,000
Liabilities: $2,200,000
Equity: $2,800,000
\n
""")
CompanyB_Quarter2.close()

# Reading financial data from text files
def read_financial_data(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
    financial_data = {}
    for line in lines:
        if ":" in line:  # Check if the line contains a colon
            key, value = line.strip().split(": ", 1)
            financial_data[key] = value
    return financial_data

# Analyzing the data
def analyze_data(quarter1_data, quarter2_data):
    differences = {}
    for key in quarter1_data:
        if key in quarter2_data:
            try:
                diff = float(quarter2_data[key].replace('$', '').replace(',', '')) - float(quarter1_data[key].replace('$', '').replace(',', ''))
                differences[key] = diff
            except ValueError:
                continue
    return differences

# Read financial data from each file
try:
    companyA_quarter1_data = read_financial_data("CompanyA_Quarter1.txt")
    companyA_quarter2_data = read_financial_data("CompanyA_Quarter2.txt")
    companyB_quarter1_data = read_financial_data("CompanyB_Quarter1.txt")
    companyB_quarter2_data = read_financial_data("CompanyB_Quarter2.txt")

    # Analyze the data for each organization
    companyA_differences = analyze_data(companyA_quarter1_data, companyA_quarter2_data)
    companyB_differences = analyze_data(companyB_quarter1_data, companyB_quarter2_data)

    # Print the differences for each organization
    print("Company A Differences (Q2 - Q1):")
    for key, value in companyA_differences.items():
        print(key + ":", "${:,.2f}".format(value))

    print("\nCompany B Differences (Q2 - Q1):")
    for key, value in companyB_differences.items():
        print(key + ":", "${:,.2f}".format(value))

    # Allow the user to input the organization name and show the difference for the 2nd quarter compared to the 1st quarter
    organization_name = input("\nEnter the name of the organization (Company A or Company B): ").strip().lower()
    if organization_name == "company a":
        print("\nDifferences for Company A (Q2 - Q1):")
        for key, value in companyA_differences.items():
            print(key + ":", "${:,.2f}".format(value))
    elif organization_name == "company b":
        print("\nDifferences for Company B (Q2 - Q1):")
        for key, value in companyB_differences.items():
            print(key + ":", "${:,.2f}".format(value))
    else:
        print("Invalid organization name.")

except FileNotFoundError:
    print("Error: One or more files not found.")
except Exception as e:
    print("An error occurred:", e)
