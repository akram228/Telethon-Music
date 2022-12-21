import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "15039244"))
    API_HASH = os.environ.get("API_HASH", "7ad462f23bd323421339cbcb7b10d893")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5810602588:AAFee7uWE65y5EwbtyzrNMV_MfJoQtj_INc")
    STRING_SESSION = os.environ.get("STRING_SESSION", "BQDlewwAmNsavr-pD1Phjto9KZXxiTjMnLsi64kkXu5jl2YecOYQ7XqSEp2okYCwjIbElH8QCbH5qdmHxj8S9Dw205JMLaj3Bqo0K0XcKyB7ANUSbTf4bni52mExLqnoFQwtg0VFUFxjXfgNO5FaQCeJe3BvVqOY9BodUXVCpE6z16cAfZhHhQIChK4Poan6OaND2pHRNm-zurLLmfSAULClr5GzLzLe3_9mWPQUhGZU0t4eEkjTCuCvVa_qrjcewd_ksccmoNgq_iakN9opxSwQ9qTNtlEVftKahXVcSRxnMQ-2hHe0JrV9b8_1T2A2mPwKbCpjJe21VK27zViwk3ZzeibSAgAAAAEqyqCjAA")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "music782_bot")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5012889763")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', True) # Change it to "True"
