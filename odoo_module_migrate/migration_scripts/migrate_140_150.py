# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo_module_migrate.base_migration_script import BaseMigrationScript

x2many_operations = {
    r"[\(\[][ \n]*[0-1],[ \n]*[^,]*,[ \n]*{": "[15] It seems there is an old style x2many operations in file (starting from 0 or 1). Please use Command to manipulate with x2many items.",
    r"[\(\[][ \n]*[2-4],": "[15] It seems there is an old style x2many operations in file (starting from 2, 3 or 4). Please use Command to manipulate with x2many items.",
    r"[\(\[][ \n]*5,": "[15] It seems there is an old style x2many operations in file (starting from 5). Please use Command to manipulate with x2many items.",
    r"[\(\[][ \n]*6,[ \n]*[^,]*,[ \n]": "[15] It seems there is an old style x2many operations in file (starting from 6). Please use Command to manipulate with x2many items.",
}
class MigrationScript(BaseMigrationScript):
    """
    Common information can be found here: https://github.com/OCA/maintainer-tools/wiki/Migration-to-version-15.0
    Javascript migration to owl:
    - https://www.odoo.com/documentation/15.0/developer/reference/frontend/framework_overview.html
    - https://codingdodo.com/odoo-15-owl-view-migration-guide/
    """

    _TEXT_WARNINGS = {
        ".py": {
            **x2many_operations,
        },
        ".xml": {
            **x2many_operations,
        },
    }
