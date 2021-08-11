from typing import Iterable, Optional, Union


def send_mail(to: Union[Iterable[str],str], subject:str, message: str, bcc: Optional[Union[Iterable[str],str]] = None):
    """Sends email `message` to user or users `to` with specified `subject` and optional hidden email(s) `bcc`."""
    pass
