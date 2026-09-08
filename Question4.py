
# QUESTION 4: CLINIC PATIENT CLASSIFICATION


def classify_patient(systolic, diastolic):
    """
    Classify a patient based on blood pressure readings.
    Returns: "Normal", "Elevated", "Stage 1", or "Urgent"
    """
    
    # Check Urgent first (most serious)
    if systolic >= 160 or diastolic >= 100:
        return "Urgent"
    
    # Check Stage 1
    elif (systolic >= 140 and systolic <= 159) or (diastolic >= 90 and diastolic <= 99):
        return "Stage 1"
    
    # Check Elevated
    elif (systolic >= 120 and systolic <= 139) or (diastolic >= 80 and diastolic <= 89):
        return "Elevated"
    
    # Everything else is Normal
    else:
        return "Normal"


def generate_clinic_report(patients):
    """
    This function takes patient records and prints a report.
    Each record: (patient_name, systolic, diastolic)
    """
    
    # Create lists to store patients by category
    normal_patients = []
    elevated_patients = []  # "At-Risk"
    stage1_patients = []    # Also "At-Risk"
    urgent_patients = []    # "Urgent"
    
    # For calculating averages
    total_systolic = 0
    total_diastolic = 0
    patient_count = 0
    
    # Process each patient
    for name, systolic, diastolic in patients:
        # Add to totals for averages
        total_systolic = total_systolic + systolic
        total_diastolic = total_diastolic + diastolic
        patient_count = patient_count + 1
        
        # Classify the patient
        category = classify_patient(systolic, diastolic)
        
        # Add to appropriate list
        if category == "Normal":
            normal_patients.append((name, systolic, diastolic))
        elif category == "Elevated":
            elevated_patients.append((name, systolic, diastolic))
        elif category == "Stage 1":
            stage1_patients.append((name, systolic, diastolic))
        elif category == "Urgent":
            urgent_patients.append((name, systolic, diastolic))
    
    # Calculate averages
    if patient_count > 0:
        avg_systolic = total_systolic / patient_count
        avg_diastolic = total_diastolic / patient_count
    else:
        avg_systolic = 0
        avg_diastolic = 0
    
    
    # PRINT THE REPORT
   
    print("=" * 60)
    print("         CLINIC PATIENT REPORT")
    print("=" * 60)
    
    print("\n PATIENT CLASSIFICATION:")
    print("-" * 40)
    
    print("\n   NORMAL PATIENTS:")
    if normal_patients:
        for name, sys, dia in normal_patients:
            print("    " + name + " (" + str(sys) + "/" + str(dia) + ")")
    else:
        print("    No normal patients")
    
    print("\n  AT-RISK PATIENTS (Elevated/Stage 1):")
    at_risk = elevated_patients + stage1_patients
    if at_risk:
        for name, sys, dia in at_risk:
            category = classify_patient(sys, dia)
            print("    " + name + " (" + str(sys) + "/" + str(dia) + ") - " + category)
    else:
        print("    No at-risk patients")
    
    print("\n   URGENT PATIENTS:")
    if urgent_patients:
        for name, sys, dia in urgent_patients:
            print("     " + name + " (" + str(sys) + "/" + str(dia) + ") - URGENT!")
    else:
        print("    No urgent patients")
    
    print("\n AVERAGE READINGS:")
    print("-" * 40)
    print("  Average Systolic: " + str(round(avg_systolic, 1)))
    print("  Average Diastolic: " + str(round(avg_diastolic, 1)))
    
    print("\n URGENT PATIENT ALERTS:")
    print("-" * 40)
    if urgent_patients:
        for name, sys, dia in urgent_patients:
            print("  ALERT: " + name + " has URGENT blood pressure (" + str(sys) + "/" + str(dia) + ")")
            print("      -> Requires immediate medical attention!")
    else:
        print("   No urgent alerts - all patients stable")
    
    print("\n FOLLOW-UP RECOMMENDATIONS:")
    print("-" * 40)
    follow_up = at_risk + urgent_patients
    if follow_up:
        for name, sys, dia in follow_up:
            category = classify_patient(sys, dia)
            print("   " + name + " - " + category + " - Schedule follow-up")
    else:
        print("   All patients are normal - no follow-up needed")
    
    print("\n SUMMARY STATISTICS:")
    print("-" * 40)
    print("  Total patients: " + str(patient_count))
    print("  Normal: " + str(len(normal_patients)))
    print("  At-Risk: " + str(len(at_risk)))
    print("  Urgent: " + str(len(urgent_patients)))
    
    print("\n" + "=" * 60)
    print("            END OF REPORT")
    print("=" * 60 + "\n")
    
    return {
        "normal": normal_patients,
        "at_risk": at_risk,
        "urgent": urgent_patients
    }



# TEST 1: Supplied data from assignment

print(" TEST 1: Supplied Dataset")
print("=" * 60)

patients = [
    ("Alice", 115, 75),
    ("Brian", 128, 84),
    ("Carol", 145, 95),
    ("Daniel", 165, 105),
    ("Grace", 118, 78)
]

generate_clinic_report(patients)



# TEST 2: Normal case - Mixed categories

print("\nTEST 2: Normal Case - Mixed categories")
print("=" * 60)

normal_data = [
    ("John", 110, 70),   # Normal
    ("Mary", 125, 82),   # Elevated
    ("Peter", 150, 92),  # Stage 1
    ("Susan", 170, 110), # Urgent
    ("Paul", 118, 76),   # Normal
    ("Jane", 135, 88)    # Elevated
]

generate_clinic_report(normal_data)


# TEST 3: Edge case - All normal

print("\nTEST 3: Edge Case - All normal patients")
print("=" * 60)

all_normal = [
    ("Healthy1", 110, 70),
    ("Healthy2", 115, 75),
    ("Healthy3", 118, 78)
]

generate_clinic_report(all_normal)



# TEST 4: Edge case - All urgent

print("\nTEST 4: Edge Case - All urgent patients")
print("=" * 60)

all_urgent = [
    ("Sick1", 160, 90),
    ("Sick2", 140, 100),
    ("Sick3", 170, 105)
]

generate_clinic_report(all_urgent)



# TEST 5: Edge case - Empty data

print("\n TEST 5: Edge Case - No patients")
print("=" * 60)

empty_data = []
generate_clinic_report(empty_data)


# TEST 6: Edge case - Diastolic alone causes urgent

print("\n TEST 6: Edge Case - Diastolic causes Urgent (systolic normal)")
print("=" * 60)

diastolic_urgent = [
    ("Alice", 118, 78),   # Normal
    ("Bob", 118, 85),     # Elevated (diastolic)
    ("Carol", 118, 95),   # Stage 1 (diastolic)
    ("Dave", 118, 105)    # Urgent (diastolic)
]
# All have normal systolic (118), but diastolic increases

generate_clinic_report(diastolic_urgent)