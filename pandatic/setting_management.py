from enum import Enum
from datetime import datetime
from pydantic import (
    BaseModel,
    BaseSettings,
    PyObject,
    RedisDsn,
    PostgresDsn,
    AmqpDsn,
    Field,
    validator
)

class TestEnum(Enum):
    opt1 = "OPT1"
    opt2 = "OPT2"

class SubModel(BaseModel):
    foo = "bar"
    apple = 1


class Settings(BaseSettings):
    case_enum : TestEnum = Field(default=TestEnum.opt1, env="TEST_ENUM2")
    dep_case:AmqpDsn = Field(default="amqp://user:pass@localhost:5672/", env= "DEP_CASE")
    created_at = Field(default="09:00", env="CREATED_AT")

    # auth_key: str
    api_key: str = Field(default="tt001", env="my_api_key2")

    redis_dsn: RedisDsn = "redis://user:pass@localhost:6379/1"
    pg_dsn: PostgresDsn = "postgres://user:pass@localhost:5432/foobar"
    amqp_dsn: AmqpDsn = "amqp://user:pass@localhost:5672/"

    special_function: PyObject = "math.cos"

    # to override domains:
    # export my_prefix_domains='["foo.com", "bar.com"]'
    domains: set[str] = set()

    # to override more_settings:
    # export my_prefix_more_settings='{"foo": "x", "apple": 1}'
    more_settings: SubModel = SubModel()

    class Config:
        env_prefix = "my_prefix_"  # defaults to no prefix, i.e. ""
        fields = {
            # "auth_key": {
            #     "env": "my_auth_key",
            #     "default": "etddssa"
            # },
            "redis_dsn": {"env": ["service_redis_dsn", "redis_url"]},
        }
    
    @validator('created_at')
    def validate_case_enum(cls, time_in):
        print("time_in : ", time_in)
        return datetime.now()

    # def check_value(self):
    #     if self.case_enum == TestEnum.opt1:
    #         print("...")
    #         self.test = Field(default="...")
    #     else:
    #         print(";;")

setting = Settings()
print(setting)

