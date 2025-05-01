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
    Accompany_Client: str
    Client_Income_Type: str
    Client_Education: str
    Client_Marital_Status: Literal["D", "S", "M", "W"]
    Client_Gender: Literal["M", "F"]
    Loan_Contract_Type: Literal["CL", "RL"]
    Client_Housing_Type: str
    Population_Region_Relative: float
    Age_Days: int
    Employed_Days: int
    Registration_Days: int
    ID_Days: int
    Own_House_Age: int | None = None
    Mobile_Tag: Literal[0, 1]
    Homephone_Tag: Literal[0, 1]
    Workphone_Working: Literal[0, 1]
    Client_Occupation: str
    Client_Family_Members: int
    Cleint_City_Rating: Literal[1, 2, 3]
    Application_Process_Day: Literal[0, 1, 2, 3, 4, 5, 6]
    Application_Process_Hour: int
    Client_Permanent_Match_Tag: Literal[0, 1]
    Client_Contact_Work_Tag: Literal[0, 1]
    Type_Organization: str
    Score_Source_1: float
    Score_Source_2: float
    Score_Source_3: float
    Social_Circle_Default: int
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
