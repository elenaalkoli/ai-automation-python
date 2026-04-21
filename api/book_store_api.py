import requests

from core.config import BASE_URL


class BookStoreApiClient:
    """Repository: isolates all HTTP interactions from the UI layer."""

    def __init__(self) -> None:
        self._base = BASE_URL

    def create_user(self, username: str, password: str) -> str:
        resp = requests.post(
            f"{self._base}/Account/v1/User",
            json={"userName": username, "password": password},
        )
        resp.raise_for_status()
        return resp.json()["userID"]

    def generate_token(self, username: str, password: str) -> str:
        resp = requests.post(
            f"{self._base}/Account/v1/GenerateToken",
            json={"userName": username, "password": password},
        )
        resp.raise_for_status()
        return resp.json()["token"]

    def get_books(self) -> list[dict]:
        resp = requests.get(f"{self._base}/BookStore/v1/Books")
        resp.raise_for_status()
        return resp.json()["books"]

    def add_book(self, user_id: str, isbn: str, token: str) -> None:
        resp = requests.post(
            f"{self._base}/BookStore/v1/Books",
            json={"userId": user_id, "collectionOfIsbns": [{"isbn": isbn}]},
            headers={"Authorization": f"Bearer {token}"},
        )
        resp.raise_for_status()

    def delete_all_books(self, user_id: str, token: str) -> None:
        requests.delete(
            f"{self._base}/BookStore/v1/Books",
            params={"UserId": user_id},
            headers={"Authorization": f"Bearer {token}"},
        )

    def delete_user(self, user_id: str, token: str) -> None:
        requests.delete(
            f"{self._base}/Account/v1/User/{user_id}",
            headers={"Authorization": f"Bearer {token}"},
        )
