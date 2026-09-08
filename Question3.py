
# QUESTION 3: SMALL BUSINESS SALES PERFORMANCE


def generate_sales_report(sales):
    """
    This function takes sales records and prints a report.
    Each record: (day, salesperson, phone_brand, amount)
    """
    
    # Create dictionaries
    salesperson_total = {}    # Stores: {"Alice": 5300000, ...}
    brand_revenue = {}        # Stores: {"Samsung": 5100000, ...}
    daily_sales = {}          # Stores: {"Monday": 2050000, ...}
    
    # Process each sales record
    for day, salesperson, brand, amount in sales:
        # Add to salesperson's total
        if salesperson in salesperson_total:
            salesperson_total[salesperson] = salesperson_total[salesperson] + amount
        else:
            salesperson_total[salesperson] = amount
        
        # Add to brand revenue
        if brand in brand_revenue:
            brand_revenue[brand] = brand_revenue[brand] + amount
        else:
            brand_revenue[brand] = amount
        
        # Add to daily sales
        if day in daily_sales:
            daily_sales[day] = daily_sales[day] + amount
        else:
            daily_sales[day] = amount
    
    # Find top performing salesperson(s)
   
    max_sales = 0
    for salesperson, total in salesperson_total.items():
        if total > max_sales:
            max_sales = total
    
    # Find all salespeople with max sales (for ties)
    top_performers = []
    for salesperson, total in salesperson_total.items():
        if total == max_sales:
            top_performers.append(salesperson)
    
    # Award bonuses
 
    bonuses = {}
    for salesperson, total in salesperson_total.items():
        if salesperson in top_performers:
            bonuses[salesperson] = 50000  # Top performer bonus
        else:
            bonuses[salesperson] = 20000  # Regular bonus
    
   
    # Find highest revenue brand
   
    top_brand = max(brand_revenue, key=brand_revenue.get)
    top_brand_revenue = brand_revenue[top_brand]
    
   
    # Find slow days (below 2,000,000 UGX)
    
    slow_days = []
    for day, total in daily_sales.items():
        if total < 2000000:
            slow_days.append(day + " (" + str(total) + " UGX)")
    
   
    # PRINT THE REPORT
  
    print("=" * 60)
    print("         WEEKLY SALES PERFORMANCE REPORT")
    print("=" * 60)
    
    print("\n SALESPERSON PERFORMANCE:")
    print("-" * 40)
    # Sort salespeople by total (highest first)
    sales_list = []
    for salesperson, total in salesperson_total.items():
        sales_list.append((total, salesperson))
    sales_list.sort(reverse=True)
    
    rank = 1
    for total, salesperson in sales_list:
        bonus = bonuses[salesperson]
        # Add star for top performers
        star = " " if salesperson in top_performers else ""
        print("  #" + str(rank) + ": " + salesperson + star + " - " + str(total) + " UGX (Bonus: " + str(bonus) + " UGX)")
        rank = rank + 1
    
    print("\n REVENUE BY PHONE BRAND:")
    print("-" * 40)
    for brand, revenue in brand_revenue.items():
        print("  " + brand + ": " + str(revenue) + " UGX")
    
    print("\n TOP PERFORMING SALESPERSON:")
    print("-" * 40)
    if len(top_performers) == 1:
        print("  " + top_performers[0] + " with " + str(max_sales) + " UGX")
    else:
        print("  TIE between: " + ", ".join(top_performers) + " (each with " + str(max_sales) + " UGX)")
    
    print("\n TOP SELLING BRAND:")
    print("-" * 40)
    print("  " + top_brand + " with " + str(top_brand_revenue) + " UGX")
    
    print("\n DAILY SALES:")
    print("-" * 40)
    for day, total in daily_sales.items():
        if total < 2000000:
            print("  " + day + ": " + str(total) + " UGX (SLOW DAY!)")
        else:
            print("   " + day + ": " + str(total) + " UGX")
    
    print("\n SLOW DAYS (below 2,000,000 UGX):")
    print("-" * 40)
    if slow_days:
        for day in slow_days:
            print("   " + day)
    else:
        print("   No slow days - all days are good!")
    
    print("\n" + "=" * 60)
    print("            END OF REPORT")
    print("=" * 60 + "\n")
    
    return salesperson_total, brand_revenue, daily_sales



# TEST 1: Supplied data from assignment

print("TEST 1: Supplied Dataset")
print("=" * 60)

sales = [
    ("Monday", "Alice", "Samsung", 1200000),
    ("Monday", "Brian", "Tecno", 850000),
    ("Tuesday", "Alice", "iPhone", 2500000),
    ("Tuesday", "Charles", "Samsung", 1100000),
    ("Wednesday", "Brian", "Infinix", 900000),
    ("Wednesday", "Alice", "Samsung", 1600000),
    ("Thursday", "Charles", "Tecno", 700000),
    ("Friday", "Brian", "Samsung", 2300000)
]

generate_sales_report(sales)


# TEST 2: Normal case - More salespeople

print("\nTEST 2: Normal Case - More salespeople")
print("=" * 60)

normal_data = [
    ("Monday", "Alice", "Samsung", 1000000),
    ("Monday", "Bob", "iPhone", 1500000),
    ("Tuesday", "Alice", "Tecno", 2000000),
    ("Tuesday", "Charlie", "Samsung", 800000),
    ("Wednesday", "Bob", "iPhone", 1200000),
    ("Wednesday", "Alice", "Samsung", 900000),
    ("Thursday", "Charlie", "Tecno", 600000),
    ("Friday", "Bob", "Samsung", 1800000)
]

generate_sales_report(normal_data)



# TEST 3: Edge case - Tie for top performer

print("\n TEST 3: Edge Case - Tie for top performer")
print("=" * 60)

tie_data = [
    ("Monday", "Alice", "Samsung", 1000000),
    ("Monday", "Bob", "iPhone", 1000000),
    ("Tuesday", "Alice", "Tecno", 1000000),
    ("Tuesday", "Bob", "Samsung", 1000000),
    ("Wednesday", "Alice", "iPhone", 1000000),
    ("Wednesday", "Bob", "Tecno", 1000000)
]
# Alice and Bob both have 3,000,000 UGX - TIE!

generate_sales_report(tie_data)


# TEST 4: Edge case - All days are slow

print("\nTEST 4: Edge Case - All days are slow (below 2,000,000)")
print("=" * 60)

slow_data = [
    ("Monday", "Alice", "Samsung", 500000),
    ("Tuesday", "Bob", "iPhone", 600000),
    ("Wednesday", "Alice", "Tecno", 400000)
]
# All days under 2,000,000

generate_sales_report(slow_data)



# TEST 5: Edge case - Empty data

print("\n TEST 5: Edge Case - No sales data")
print("=" * 60)

empty_data = []
generate_sales_report(empty_data)
        