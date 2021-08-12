from typing import List


class Address:
    def __init__(
        self, street: str, city: str, state: str, zip_code: str, street2: int = ""
    ) -> None:
        self.street = street
        self.street2 = street2
        self.city = city
        self.state = state
        self.zip_code = zip_code

    def __str__(self):
        lines: List = [self.street]
        if self.street2:
            lines.append(self.street2)
        lines.append(f"{self.city}, {self.state}, {self.zip_code}")

        return "\n".join(lines)
