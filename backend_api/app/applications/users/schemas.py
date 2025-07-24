from pydantic import (BaseModel, EmailStr, Field, ValidationInfo,
                      model_validator)


class BaseFields(BaseModel):
    email: EmailStr = Field(
        description="User email", examples=["test_hillel_api_mailing@ukr.net"]
    )
    name: str = Field(description="User nickname", examples=["Casper"])


class PasswordField(BaseModel):
    password: str = Field(min_length=8)

    @model_validator(mode="after")
    def validate_password(
        cls, self: "PasswordField", info: ValidationInfo
    ) -> "PasswordField":
        password = self.password.strip()

        if not password:
            raise ValueError("Password required")

        if len(password) < 8:
            raise ValueError("Too short password")

        if " " in password:
            raise ValueError("No spaces in password, please")

        return self


class RegisterUserFields(BaseFields, PasswordField):
    pass


class BaseUserInfo(BaseFields):
    id: int
