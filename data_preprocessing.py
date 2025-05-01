import re
import math
import pandas as pd
import numpy as np

class FullLoanPreprocessor:
    @staticmethod
    def clean_and_floor(value):
        if pd.isna(value):
            return value
        cleaned_value = re.sub(r'[^\d.]', '', str(value))
        if cleaned_value:
            return math.floor(float(cleaned_value))
        return None

    @staticmethod
    def family_categorize(x):
        return (
            'upto_1_member' if x <= 1 else
            '2_members' if x == 2 else
            '3_members' if x == 3 else
            'more_than_3_members'
        )

    @staticmethod
    def annuity_categorize(x):
        return (
            'upto_2_percent' if x <= 2 else
            'upto_4_percent' if x <= 4 else
            'upto_6_percent' if x <= 6 else
            'upto_8_percent' if x <= 8 else
            'more_than_8_percent'
        )

    @staticmethod
    def income_category(x):
        return (
            'income_band1' if x <= 6000 else
            'income_band2' if x <= 10000 else
            'income_band3' if x <= 15000 else
            'income_band4' if x <= 20000 else
            'income_band5' if x <= 50000 else
            'income_band6'
        )

    @staticmethod
    def credit_category(x):
        return (
            'credit_band1' if x <= 20000 else
            'credit_band2' if x <= 30000 else
            'credit_band3' if x <= 40000 else
            'credit_band4' if x <= 50000 else
            'credit_band5' if x <= 60000 else
            'credit_band6'
        )

    @staticmethod
    def credit_income_category(x):
        return (
            'Upto_2_times' if x <= 2 else
            'Upto_3_times' if x <= 3 else
            'Upto_4_times' if x <= 4 else
            'Upto_5_times' if x <= 5 else
            'Upto_10_times' if x <= 10 else
            'more_than_10_times'
        )

    @staticmethod
    def registration_category(x):
        return (
            'upto_5_years' if x <= 5 else
            'upto_10_years' if x <= 10 else
            'upto_15_years' if x <= 15 else
            'upto_20_years' if x <= 20 else
            'upto_30_years' if x <= 30 else
            'more_than_30_years'
        )

    @staticmethod
    def id_years_category(x):
        return 'upto_5_years' if x <= 5 else 'upto_10_years' if x <= 10 else 'more_than_10_years'

    @staticmethod
    def convert_employment_days(x):
        if x == 0:
            return 'no_employment'
        return (
            'upto_2_years' if x <= 2 else
            'upto_5_years' if x <= 5 else
            'upto_10_years' if x <= 10 else
            'more_than_10_years'
        )

    @staticmethod
    def convert_age_days(x):
        return (
            'upto_30_years' if x <= 30 else
            'upto_40_years' if x <= 40 else
            'upto_50_years' if x <= 50 else
            'more_than_50_years'
        )

    @staticmethod
    def year_categorize(x):
        return (
            'same_year' if x == 0 else
            'one_year' if x == 1 else
            'two_year' if x == 2 else
            'three_year' if x == 3 else
            'four_year' if x == 4 else
            'more_than_four'
        )

    @staticmethod
    def bureau_categorize(x):
        return (
            'no_search' if x == 0 else
            'one_search' if x == 1 else
            'two_search' if x == 2 else
            'more_than_two_search'
        )

    @staticmethod
    def application_hour_category(x):
        return (
            'upto_6_hours' if x <= 6 else
            'upto_12_hours' if x <= 12 else
            'upto_18_hours' if x <= 18 else
            'more_than_18_hours'
        )

    @staticmethod
    def group_type_organization(org):
        group_mapping = {
            'Self-employed': 'Self-employed',
            'Business Entity Type 1': 'Business',
            'Government': 'Public Sector',
            'Medicine': 'Healthcare',
            'IT': 'Technology',
            'Trade: type 1': 'Trade',
            'Industry: type 1': 'Industry',
            'Other': 'Other'
        }
        return group_mapping.get(org, 'Other')
    
    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
    # Clean and convert income-related columns
        df['Client_Income'] = df['Client_Income'].apply(self.clean_and_floor)
        df['Client_Income'] = pd.to_numeric(df['Client_Income'], errors='coerce')
        df['Client_Income_category'] = df['Client_Income'].apply(self.income_category)

        df['Credit_Amount'] = df['Credit_Amount'].apply(self.clean_and_floor)
        df['Credit_Amount'] = pd.to_numeric(df['Credit_Amount'], errors='coerce')
        df['Credit_Amount_category'] = df['Credit_Amount'].apply(self.credit_category)

        df['Credit_to_Income_Ratio'] = (df['Credit_Amount'] / df['Client_Income']).round(2)
        df['Credit_to_Income_Category'] = df['Credit_to_Income_Ratio'].apply(self.credit_income_category)

        df['Loan_Annuity'] = df['Loan_Annuity'].apply(self.clean_and_floor)
        df['Loan_Annuity'] = pd.to_numeric(df['Loan_Annuity'], errors='coerce')
        df['Loan_Annuity_percent'] = ((df['Loan_Annuity'] / df['Credit_Amount']) * 100).round(2)
        df['Loan_Annuity_category'] = df['Loan_Annuity_percent'].apply(self.annuity_categorize)

        df['Client_Family_Members_Category'] = df['Client_Family_Members'].apply(self.family_categorize)

        df['House_Own'] = df['Own_House_Age'].notnull().astype(int)
        df = df.drop(columns='Own_House_Age')

        df['Registration_Years'] = (pd.to_numeric(df['Registration_Days'], errors='coerce') / 365).round(0)
        df['Registration_Years_Category'] = df['Registration_Years'].apply(self.registration_category)

        df['ID_Years'] = (pd.to_numeric(df['ID_Days'], errors='coerce') / 365).round(0)
        df['ID_Years_Category'] = df['ID_Years'].apply(self.id_years_category)

        df['Employed_Days'] = df['Employed_Days'].replace(365243, 0)
        df['Employed_Days'] = (pd.to_numeric(df['Employed_Days'], errors='coerce') / 365).round(0)
        df['Employed_Days_Category'] = df['Employed_Days'].apply(self.convert_employment_days)

        df['Age_Days'] = (pd.to_numeric(df['Age_Days'], errors='coerce') / 365).round(0)
        df['Age_Days_Category'] = df['Age_Days'].apply(self.convert_age_days)

        # Clean: convert to numeric
        df['Phone_Change'] = pd.to_numeric(df['Phone_Change'], errors='coerce')

        # Impute or handle missing values (optional: fill with median or -1)
        df['Phone_Change'] = df['Phone_Change'].fillna(0)  # or use df['Phone_Change'].median()

        # Then divide and categorize
        df['Phone_Change_years'] = (df['Phone_Change'] / 365).round(0)
        df['Phone_Change_category'] = df['Phone_Change_years'].apply(self.year_categorize)

        # Clean
        df['Credit_Bureau'] = pd.to_numeric(df['Credit_Bureau'], errors='coerce')

        # Impute NaNs
        df['Credit_Bureau'] = df['Credit_Bureau'].fillna(0)

        # Categorize
        df['Credit_Bureau_Category'] = df['Credit_Bureau'].astype(int).apply(self.bureau_categorize)


        #df['Phone_Change_category'] = (pd.to_numeric(df['Phone_Change'], errors='coerce') / 365).astype(int).apply(self.year_categorize)
        #df['Credit_Bureau_Category'] = pd.to_numeric(df['Credit_Bureau'], errors='coerce').astype('Int64').apply(self.bureau_categorize)

        df['Application_Hour_Category'] = pd.to_numeric(df['Application_Process_Hour'], errors='coerce').apply(self.application_hour_category)
        df['Type_Organization_Grouped'] = df['Type_Organization'].apply(self.group_type_organization)

        selected_columns = [
            'Client_Income_category', 'Credit_Amount_category', 'Credit_to_Income_Category',
            'Loan_Annuity_category', 'Client_Family_Members_Category', 'Car_Owned', 'Bike_Owned',
            'Active_Loan', 'Accompany_Client', 'Client_Income_Type', 'Client_Education',
            'Client_Marital_Status', 'Loan_Contract_Type', 'Client_Housing_Type',
            'Registration_Years_Category', 'ID_Years_Category', 'Employed_Days_Category',
            'Age_Days_Category', 'House_Own', 'Client_Occupation', 'Client_City_Rating',
            'Application_Process_Day', 'Application_Hour_Category', 'Type_Organization_Grouped',
            'Score_Source_2', 'Score_Source_3', 'Social_Circle_Default', 'Phone_Change_category',
            'Credit_Bureau_Category'
        ]

        return df[selected_columns]


    
