from django.contrib.auth.forms import UserCreationForm


class AccountCreationForm(UserCreationForm):  # update할 때 ID는 변경불가하도록 설정.
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # 모든 입력을 그대로 상위 명령에 넣어준다.

        self.fields['username'].disabled = True
