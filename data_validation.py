from pydantic import BaseModel, Field, field_validator
from typing import Literal

class LoanApplication(BaseModel):
    ID: int
    Client_Income: float
    Car_Owned: Literal[0, 1]
    Bike_Owned: Literal[0, 1]
    Active_Loan: Literal[0, 1]
    House_Own: Literal[0, 1]
    Child_Count: int
    Credit_Amount: float
    Loan_Annuity: float
    Accompany_Client: Literal['Alone', 'Relative', 'Others', 'Kids', 'Partner', 'Group']
    Client_Income_Type: Literal['Commercial', 'Service', 'Retired', 'Govt Job', 'Student','Unemployed', 'Maternity leave', 'Businessman']
    Client_Education: Literal['Secondary', 'Graduation', 'Graduation dropout','Junior secondary', 'Post Grad']
    Client_Marital_Status: Literal["D", "S", "M", "W"]
    Client_Gender: Literal["Male", "Female"]
    Loan_Contract_Type: Literal["CL", "RL"]
    Client_Housing_Type: Literal['Home', 'Family', 'Office', 'Municipal', 'Rental', 'Shared']
    Population_Region_Relative: float
    Age_Days: int
    Employed_Days: int
    Registration_Days: int
    ID_Days: int
    Own_House_Age: int | None = None
    Mobile_Tag: Literal[0, 1]
    Homephone_Tag: Literal[0, 1]
    Workphone_Working: Literal[0, 1]
    Client_Occupation: Literal['Sales',  'Realty agents', 'Laborers', 'Core', 'Drivers',
                                'Managers', 'Accountants', 'High skill tech', 'Cleaning', 'HR',
                                'Waiters/barmen', 'Low-skill Laborers', 'Medicine', 'Cooking',
                                'Private service', 'Security', 'IT', 'Secretaries']
    Client_Family_Members: int
    Cleint_City_Rating: Literal[1, 2, 3]
    Application_Process_Day: Literal[0, 1, 2, 3, 4, 5, 6]
    Application_Process_Hour: Literal[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                                11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
    Client_Permanent_Match_Tag: Literal['Yes', 'No']
    Client_Contact_Work_Tag: Literal['Yes', 'No']
    Type_Organization: Literal['Self-employed', 'Government', 'XNA', 'Business Entity Type 3',
                                'Other',  'Industry: type 3', 'Business Entity Type 2',
                                'Business Entity Type 1', 'Transport: type 4', 'Construction',
                                'Kindergarten', 'Trade: type 3', 'Industry: type 2',
                                'Trade: type 7', 'Trade: type 2', 'Agriculture', 'Military',
                                'Medicine', 'Housing', 'Industry: type 1', 'Industry: type 11',
                                'Bank', 'School', 'Industry: type 9', 'Postal', 'University',
                                'Transport: type 2', 'Restaurant', 'Electricity', 'Police',
                                'Industry: type 4', 'Security Ministries', 'Services',
                                'Transport: type 3', 'Mobile', 'Hotel', 'Security',
                                'Industry: type 7', 'Advertising', 'Cleaning', 'Realtor',
                                'Trade: type 6', 'Culture', 'Industry: type 5', 'Telecom',
                                'Trade: type 1', 'Industry: type 12', 'Industry: type 8',
                                'Insurance', 'Emergency', 'Legal Services', 'Industry: type 10',
                                'Trade: type 4', 'Industry: type 6', 'Transport: type 1',
                                'Industry: type 13', 'Religion', 'Trade: type 5']
    Score_Source_1: float
    Score_Source_2: float
    Score_Source_3: float
    Social_Circle_Default: float
    Phone_Change: int
    Credit_Bureau: int

    @field_validator('*', mode='before')
    @classmethod
    def no_nans(cls, v):
        if v is None:
            raise ValueError("Missing value not allowed")
        return v

    model_config = {
        "extra": "forbid"  # Prevent unknown fields
    }
