import pytest

from data.web_tables_data import build_updated_web_table_record, generate_web_table_record
from pages.web_tables_page import WebTablesPage
from services.web_tables_service import WebTablesService


@pytest.mark.describe("[UI] [Web Tables CRUD] [Regression]")
class TestWebTables:
    @pytest.mark.ui
    @pytest.mark.regression
    def test_create_read_update_delete_record(
        self,
        web_tables_page: WebTablesPage,
        web_tables_service: WebTablesService,
    ) -> None:
        web_tables_page.open()
        created_record = generate_web_table_record()
        updated_record = build_updated_web_table_record(created_record)

        result = web_tables_service.create_read_update_delete(created_record, updated_record)

        assert result.created_row == [
            created_record.first_name,
            created_record.last_name,
            created_record.age,
            created_record.email,
            created_record.salary,
            created_record.department,
        ]
        assert result.updated_row == [
            updated_record.first_name,
            updated_record.last_name,
            updated_record.age,
            updated_record.email,
            updated_record.salary,
            updated_record.department,
        ]
        assert result.deleted, f"Record with email '{updated_record.email}' was not deleted"
