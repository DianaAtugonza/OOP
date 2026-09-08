# QUESTION 2: COMMUNITY LIBRARY BOOK DONATION


def generate_donation_report(donations):
    """
    This function takes donation records and prints a report.
    Each record: (donor_name, genre, number_of_books)
    """
    
    # Create empty dictionaries
    donor_total = {}      # Stores: {"Alice": 6, ...}
    genre_total = {}      # Stores: {"Fiction": 10, ...}
    
    # Process each donation record
    for donor, genre, books in donations:
        # Add to donor's total
        if donor in donor_total:
            donor_total[donor] = donor_total[donor] + books
        else:
            donor_total[donor] = books
        
        # Add to genre's total
        if genre in genre_total:
            genre_total[genre] = genre_total[genre] + books
        else:
            genre_total[genre] = books
    
    # Calculate overall total books
    overall_books = 0
    for books in donor_total.values():
        overall_books = overall_books + books
    
    # Find Gold Donors (donated at least 5 books)
    gold_donors = []
    for donor, total in donor_total.items():
        if total >= 5:
            gold_donors.append(donor + " (" + str(total) + " books)")
    
    # Find most popular genre (most books donated)
    if genre_total:
        most_popular = max(genre_total, key=genre_total.get)
        most_popular_books = genre_total[most_popular]
    else:
        most_popular = "N/A"
        most_popular_books = 0
    
    # Get Top 3 Donors (sort by books donated, highest first)
    # Convert dictionary to list of tuples, then sort
    donor_list = []
    for donor, total in donor_total.items():
        donor_list.append((total, donor))  # (books, name)
    
    donor_list.sort(reverse=True)  # Sort highest to lowest
    top_3_donors = donor_list[:3]  # Take first 3
    
    # PRINT THE REPORT
    
    print("=" * 60)
    print("         LIBRARY DONATION REPORT")
    print("=" * 60)
    
    print("\n DONOR SUMMARY:")
    print("-" * 40)
    for donor, total in donor_total.items():
        print("  " + donor + ": " + str(total) + " book(s)")
    
    print("\n GENRE SUMMARY:")
    print("-" * 40)
    for genre, total in genre_total.items():
        print("  " + genre + ": " + str(total) + " book(s)")
    
    print("\n MOST POPULAR GENRE:")
    print("-" * 40)
    if most_popular == "N/A":
        print("  No donations recorded yet")
    else:
        print("  " + most_popular + " (" + str(most_popular_books) + " books)")
    
    print("\n GOLD DONORS (5+ books):")
    print("-" * 40)
    if gold_donors:
        for donor in gold_donors:
            print("   " + donor)
    else:
        print("  No gold donors yet")
    
    print("\n TOP 3 DONORS:")
    print("-" * 40)
    if top_3_donors:
        rank = 1
        for books, donor in top_3_donors:
            print("  #" + str(rank) + ": " + donor + " - " + str(books) + " books")
            rank = rank + 1
    else:
        print("  No donors yet")
    
    print("\n OVERALL STATISTICS:")
    print("-" * 40)
    print("  Total books donated: " + str(overall_books))
    print("  Total donors: " + str(len(donor_total)))
    print("  Total genres: " + str(len(genre_total)))
    
    print("\n" + "=" * 60)
    print("            END OF REPORT")
    print("=" * 60 + "\n")
    
    return donor_total, genre_total

# TEST 1: Supplied data from assignment

print(" TEST 1: Supplied Dataset")
print("=" * 60)

donations = [
    ("Alice", "Fiction", 3),
    ("Brian", "Technology", 6),
    ("Carol", "History", 2),
    ("Alice", "Technology", 3),
    ("Daniel", "Fiction", 7),
    ("Grace", "Science", 5)
]

generate_donation_report(donations)



# TEST 2: Normal case - More donors

print("\n TEST 2: Normal Case - More donors")
print("=" * 60)

normal_data = [
    ("Alice", "Fiction", 4),
    ("Bob", "Fiction", 3),
    ("Charlie", "Science", 6),
    ("Alice", "History", 2),
    ("Bob", "Science", 1),
    ("Diana", "Technology", 8),
    ("Eve", "Fiction", 5)
]

generate_donation_report(normal_data)


# TEST 3: Edge case - No gold donors

print("\n TEST 3: Edge Case - Everyone donated less than 5")
print("=" * 60)

no_gold_data = [
    ("Tom", "Fiction", 1),
    ("Jerry", "Science", 2),
    ("Spike", "History", 1)
]

generate_donation_report(no_gold_data)



# TEST 4: Edge case - Empty data

print("\n TEST 4: Edge Case - No donations")
print("=" * 60)

empty_data = []
generate_donation_report(empty_data)