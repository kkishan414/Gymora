from pydantic import BaseModel,EmailStr, model_validator

class RegisterRequest(BaseModel):
    username: str
    email: EmailStr
    password: str 
    confirm_password: str

    @model_validator(mode="after")
    def validate_passwords_match(self):
        if self.password != self.confirm_password:
            raise ValueError(
                "Password and confirm password must match"
            )
        
        return self