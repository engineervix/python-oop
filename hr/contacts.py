from faker import Faker
from typing import List

fake = Faker(["en_US", "en_GB", "en_IE"])


class AddressBook:
    def __init__(self) -> None:
        self._employee_addresses = {
            1: Address(
                fake.street_address(),
                fake.city(),
                fake.state(),
                fake.postcode(),
                # fake.secondary_address()
            ),
            2: Address(
                fake.street_address(),
                fake.city(),
                fake.state(),
                fake.postcode(),
                # fake.secondary_address()
            ),
            3: Address(
                fake.street_address(),
                fake.city(),
                fake.state(),
                fake.postcode(),
                fake.secondary_address(),
            ),
            4: Address(
                fake.street_address(),
                fake.city(),
                fake.state(),
                fake.postcode(),
                # fake.secondary_address()
            ),
            5: Address(
                fake.street_address(),
                fake.city(),
                fake.state(),
                fake.postcode(),
                # fake.secondary_address()
            ),
        }

    def get_employee_address(self, employee_id):
        address = self._employee_addresses.get(employee_id)
        if not address:
            raise ValueError(employee_id)
        return address


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
