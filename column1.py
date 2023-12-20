# Column 1: Index Hospital Stays (Denominator)
    # Step 1. 
        # Select all acute and nonacute inpatient stays and observation stays
            # SQL Query to  UBREV Lookup table for IPStay and ObStays for Adult Value Sets to Codes

        # Filter out Nonacute INPt Stays
            # Filter by (using where clause) to exclude NonAcute Stays 
            # and exclude any discharges that fall outside of our measurement year (January 1st to December 1st 2022)

            # SQL Query to UBREV Lookup table for ObsStays for Adult Value Sets to Code
            # Filter by (using where clause) to say it equals ObsStays
                # For observation stays (Observation Stay Value Set) that do not have a recorded 
                # admission set the admission date to the earliest date of service on
                # the claim and set the discharge date to the last date of service on the claim (DSCHRG_DT)

        # Group our Patient Stays by MemberID, AdmissionDate, DischargeDate so that we can view all of their stays in a single lookup
            # GROUP BY SQL Query to collect that data

        # Combine consecutive stays within 2 days of each other into one stay
            # Check for any discharge dates + 2 that are <= admission date of another record

    # Step 2.
        # Identify Direct Transfers

        # Filter out Hospital Stay Exclusions

        # Calculate continuous enrollment

        # Remove hospital stays for outlier beneficiaries and report these beneficiaries as outliers.

        # Identify readmision Stay

        # Risk Adjustment Determination